#!/usr/bin/env python3
"""Minimal pipeline runner — load a pipeline manifest, walk its steps,
call a model adapter for harness steps, and emit a sample-run JSON.

This is the runtime that the playground (hf-space/app.py) uses. It is
intentionally small: each step kind has one handler, and unknown step
kinds become a stub with `simulated: true`.

Usage:
  python scripts/run_pipeline.py pipeline/research-entity --inputs inputs.json
  python scripts/run_pipeline.py pipeline/brand-safe-product-photo --simulate
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    sys.stderr.write("pyyaml is required: pip install pyyaml\n")
    sys.exit(2)

ROOT = Path(__file__).resolve().parent.parent
CATALOG = ROOT / "catalog"


def load_catalog() -> dict[str, dict]:
    out: dict[str, dict] = {}
    for path in CATALOG.rglob("*.yaml"):
        if "_inbox" in path.parts or any(p == "data" for p in path.parts):
            continue
        try:
            data = yaml.safe_load(path.read_text())
        except yaml.YAMLError:
            continue
        if isinstance(data, dict) and "id" in data:
            out[data["id"]] = data
    return out


PATH_RE = re.compile(r"\$\.([A-Za-z_]+)(?:\.([A-Za-z0-9_\.]+))?")


def resolve(value: Any, ctx: dict) -> Any:
    """Resolve `$.steps.<id>.output...`-style references against ctx."""
    if not isinstance(value, str):
        return value
    match = PATH_RE.fullmatch(value)
    if not match:
        return value
    head, tail = match.group(1), match.group(2) or ""
    obj: Any = ctx.get(head)
    if tail:
        for part in tail.split("."):
            if isinstance(obj, dict) and part in obj:
                obj = obj[part]
            else:
                return None
    return obj


# ------------------------------------------------------------------
# Processor implementations — small, deterministic, no external calls.
# Open vocabulary: add new ones by id.
# ------------------------------------------------------------------

_PII_PATTERNS = [
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "EMAIL"),
    (re.compile(r"\b(\+?\d{1,3}[ -]?)?\(?\d{2,4}\)?[ -]?\d{2,4}[ -]?\d{2,4}\b"), "PHONE"),
    (re.compile(r"\b\d{3}-\d{2}-\d{4}\b"), "US_SSN"),
    (re.compile(r"\b[A-Z]{2}\d{2}[A-Z0-9]{1,30}\b"), "IBAN"),
    (re.compile(r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13})\b"), "CREDIT_CARD"),
]

def _redact_pii(text: str) -> tuple[str, list[dict]]:
    found: list[dict] = []
    for pat, kind in _PII_PATTERNS:
        for m in pat.finditer(text):
            found.append({"type": kind, "start": m.start(), "end": m.end(), "value": m.group()[:32]})
        text = pat.sub(f"[REDACTED:{kind}]", text)
    return text, found


def _structured_to_prose(data, prefix: str = "") -> list[str]:
    out: list[str] = []
    if isinstance(data, dict):
        for k, v in data.items():
            label = k.replace("_", " ")
            if isinstance(v, (str, int, float, bool)) and v not in (None, "", 0):
                out.append(f"{label}: {v}")
            else:
                out.extend(_structured_to_prose(v, label))
    elif isinstance(data, list):
        for item in data:
            if isinstance(item, str):
                if item.strip():
                    out.append(f"{prefix}: {item}" if prefix else item)
            elif isinstance(item, dict):
                out.extend(_structured_to_prose(item, prefix))
    elif isinstance(data, str) and data.strip():
        out.append(f"{prefix}: {data}" if prefix else data)
    return out


def _run_processor(ref_id: str, inputs: dict, artifact: dict | None) -> dict:
    """Dispatch on processor id. Falls back to structured echo if unknown."""
    if ref_id == "processor/structured-to-prose":
        lines = _structured_to_prose(inputs.get("data", {}))
        return {"prose": "\n".join(lines), "lines": lines, "line_count": len(lines)}

    if ref_id == "processor/redact-pii-text":
        text = inputs.get("text", "")
        if not isinstance(text, str):
            text = json.dumps(text) if text else ""
        redacted, found = _redact_pii(text)
        counts: dict[str, int] = {}
        for f in found:
            counts[f["type"]] = counts.get(f["type"], 0) + 1
        return {"text": redacted, "detected_entities": found, "entity_counts_by_type": counts}

    if ref_id == "processor/audit-trace-emitter":
        return {
            "step_id":        inputs.get("step_id", "unknown"),
            "applied_layers": inputs.get("applied_layers", []),
            "trace_ts":       time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }

    if ref_id == "processor/llm-judge":
        # Deterministic stub: emit a fixed score so the pipeline returns
        # a complete trace. Real implementation routes to an adapter.
        return {
            "_simulated": True,
            "score":       0.0,
            "rationale":   "Replace with real adapter call; this is a stub.",
            "rubric_ref":  inputs.get("rubric_ref"),
        }

    return {"_simulated": True, "echo": inputs, "processor": ref_id}


def run_step(step: dict, catalog: dict[str, dict], ctx: dict, *, simulate: bool) -> dict:
    """Run one pipeline step. Returns a step-result record."""
    started = time.monotonic()
    ref_id = step["ref"]
    artifact = catalog.get(ref_id) if not ref_id.startswith("$.") else catalog.get(resolve(ref_id, ctx))
    inputs = {k: resolve(v, ctx) for k, v in (step.get("inputs") or {}).items()}

    output: dict = {}
    simulated = simulate or artifact is None

    if simulated:
        # Stub: echo a structured response so the trace is meaningful.
        output = {
            "_simulated": True,
            "echo": inputs,
            "note": f"simulated run of step {step['id']!r} → {ref_id!r}",
        }
    elif step["kind"] == "rule_pack":
        # Deterministic: report which rules would fire over the input text.
        text = inputs.get("text", "")
        if isinstance(text, (dict, list)):
            text = json.dumps(text)
        elif not isinstance(text, str):
            text = str(text)
        fired = []
        for rule in artifact.get("rules", []) or []:
            pattern = rule.get("pattern")
            if pattern:
                try:
                    matches = re.findall(pattern, text, re.IGNORECASE)
                    if matches:
                        fired.append({
                            "rule_id":     rule["id"],
                            "category":    rule.get("category"),
                            "severity":    rule.get("severity"),
                            "match_count": len(matches),
                            "first_match": str(matches[0])[:120] if matches else None,
                        })
                except re.error:
                    pass
        output = {"fired": fired, "pack": ref_id, "hit_count": len(fired)}
    elif step["kind"] == "processor":
        output = _run_processor(ref_id, inputs, artifact)
    elif step["kind"] == "harness":
        # Deferred to the playground app; here we stub.
        output = {"_simulated": True, "echo": inputs, "harness": ref_id}
    elif step["kind"] == "tool":
        output = {"_simulated": True, "echo": inputs, "tool": ref_id}
    elif step["kind"] == "knowledge_pack":
        output = {"_simulated": True, "echo": inputs, "pack": ref_id}

    return {
        "step_id":   step["id"],
        "kind":      step["kind"],
        "ref":       ref_id,
        "input":     inputs,
        "output":    output,
        "ms":        round((time.monotonic() - started) * 1000, 2),
        "simulated": simulated,
    }


def run_pipeline(pipeline: dict, inputs: dict, *, simulate: bool) -> dict:
    catalog = load_catalog()
    ctx: dict[str, Any] = {"inputs": inputs, "steps": {}}
    trace: list[dict] = []
    for step in pipeline.get("steps", []) or []:
        if "when" in step:
            cond = resolve(step["when"], ctx)
            if not cond:
                continue
        result = run_step(step, catalog, ctx, simulate=simulate)
        trace.append(result)
        ctx["steps"][step["id"]] = result

    last_output = trace[-1]["output"] if trace else {}
    return {
        "pipeline":  pipeline["id"],
        "inputs":    inputs,
        "trace":     trace,
        "output":    last_output,
        "model":     os.environ.get("OH_MODEL", "simulated"),
        "frozen_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="Run a pipeline manifest from the catalog.")
    ap.add_argument("pipeline_id", help="e.g. pipeline/research-entity")
    ap.add_argument("--inputs", default=None, help="Path to a JSON file with inputs.")
    ap.add_argument("--simulate", action="store_true", help="Force all steps to simulate.")
    args = ap.parse_args()

    catalog = load_catalog()
    pipeline = catalog.get(args.pipeline_id)
    if pipeline is None:
        sys.stderr.write(f"unknown pipeline {args.pipeline_id!r}\n")
        return 1
    if pipeline.get("type") != "pipeline":
        sys.stderr.write(f"{args.pipeline_id!r} is not a pipeline\n")
        return 1

    inputs = json.loads(Path(args.inputs).read_text()) if args.inputs else {}
    result = run_pipeline(pipeline, inputs, simulate=args.simulate)
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
