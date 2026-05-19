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
        fired = []
        for rule in artifact.get("rules", []) or []:
            pattern = rule.get("pattern")
            if pattern and isinstance(text, str):
                try:
                    if re.search(pattern, text):
                        fired.append({"rule_id": rule["id"], "severity": rule.get("severity")})
                except re.error:
                    pass
        output = {"fired": fired, "pack": ref_id}
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
