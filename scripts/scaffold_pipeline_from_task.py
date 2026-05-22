#!/usr/bin/env python3
"""Search the catalog for components matching a free-text task description
and emit a draft pipeline manifest. Designed for two audiences:

1. A human developer who knows roughly what they want to build.
2. An LLM agent that is asked to assemble a pipeline from the catalog.

Usage:
    python3 scripts/scaffold_pipeline_from_task.py "Review a vendor invoice for fraud signals + extract line items"
    python3 scripts/scaffold_pipeline_from_task.py "Moderate user image upload for unsafe content"
    python3 scripts/scaffold_pipeline_from_task.py --json "..."   # JSON output for agent consumption

The script does NOT call an LLM; it grep-searches catalog manifests for token
overlap against the task. The output is intended to be a starting draft a
human (or agent) refines.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Iterable

import yaml


REPO = Path(__file__).resolve().parent.parent
CATALOG = REPO / "catalog"

STOP = {"with", "from", "this", "that", "have", "been", "will", "must", "shall", "into", "than", "then", "each", "such", "their", "would", "could", "should", "above", "below", "over", "more", "less", "very", "many", "some", "what", "when", "where", "which", "while", "until", "after", "before", "every", "etc", "the", "and", "for", "are", "any", "you", "your"}


def tokenize(text: str) -> set[str]:
    toks = set()
    for raw in text.lower().split():
        t = "".join(c for c in raw if c.isalnum())
        if len(t) >= 3 and t not in STOP:
            toks.add(t)
    return toks


def load_artifacts() -> list[dict]:
    out = []
    for p in CATALOG.rglob("*.yaml"):
        try:
            doc = yaml.safe_load(p.read_text())
        except Exception:
            continue
        if not isinstance(doc, dict) or not doc.get("id") or not doc.get("type"):
            continue
        searchable = " ".join([
            doc.get("name", ""),
            doc.get("description", "") if isinstance(doc.get("description"), str) else "",
            " ".join(doc.get("tags", []) if isinstance(doc.get("tags"), list) else []),
            " ".join(doc.get("industry", []) if isinstance(doc.get("industry"), list) else []),
            " ".join(doc.get("capability", []) if isinstance(doc.get("capability"), list) else []),
        ])
        out.append({
            "id": doc["id"],
            "type": doc["type"],
            "name": doc.get("name", ""),
            "description": (doc.get("description") or "")[:200] if isinstance(doc.get("description"), str) else "",
            "tokens": tokenize(searchable),
            "path": str(p.relative_to(REPO)),
        })
    return out


def score(task_tokens: set[str], artifact: dict) -> float:
    if not task_tokens:
        return 0.0
    overlap = task_tokens & artifact["tokens"]
    return len(overlap) / max(1, len(task_tokens) ** 0.7)


def search(task: str, artifacts: list[dict], top_k: int = 25) -> list[tuple[dict, float, set[str]]]:
    tt = tokenize(task)
    ranked = []
    for art in artifacts:
        s = score(tt, art)
        if s > 0:
            ranked.append((art, s, tt & art["tokens"]))
    ranked.sort(key=lambda x: -x[1])
    return ranked[:top_k]


def group_by_type(hits: list[tuple[dict, float, set[str]]]) -> dict[str, list[tuple[dict, float, set[str]]]]:
    out: dict[str, list] = {}
    for h in hits:
        out.setdefault(h[0]["type"], []).append(h)
    return out


def first_of(grouped: dict, t: str) -> dict | None:
    return grouped[t][0][0] if grouped.get(t) else None


def make_draft_pipeline(task: str, grouped: dict) -> dict:
    persona = first_of(grouped, "persona")
    rule_pack = first_of(grouped, "rule-pack")
    knowledge_pack = first_of(grouped, "knowledge-pack")
    rubric = first_of(grouped, "rubric")
    adapter = first_of(grouped, "adapter")

    steps: list[dict] = []
    steps.append({"id": "structured_to_prose", "kind": "processor", "ref": "processor/structured-to-prose", "inputs": {"data": "$.inputs.input_packet"}})
    steps.append({"id": "redact_pii", "kind": "processor", "ref": "processor/redact-pii-text", "inputs": {"text": "$.steps.structured_to_prose.output.prose"}})
    if rule_pack:
        steps.append({"id": "grep_red_flags", "kind": "rule_pack", "ref": rule_pack["id"], "inputs": {"text": "$.steps.redact_pii.output.text"}})
    if knowledge_pack:
        steps.append({"id": "rag", "kind": "rule_pack", "ref": "rule-pack/hybrid-retrieval-policy", "inputs": {"query": "$.steps.grep_red_flags.output.fired" if rule_pack else "$.steps.redact_pii.output.text", "corpus": knowledge_pack["id"], "top_k": 6}})
    if rubric:
        steps.append({"id": "grade", "kind": "processor", "ref": "processor/llm-judge", "inputs": {"candidate": "$.steps.redact_pii.output.text", "rubric_ref": rubric["id"]}})
    steps.append({"id": "audit", "kind": "processor", "ref": "processor/audit-trace-emitter", "inputs": {"step_id": "draft-pipeline", "applied_layers": ["persona", "pii_redact"] + (["grep"] if rule_pack else []) + (["rag"] if knowledge_pack else []) + (["judge"] if rubric else [])}})

    defaults = {}
    if persona:
        defaults["persona"] = persona["id"]
    if adapter:
        defaults["model_adapter"] = adapter["id"]
    else:
        defaults["model_adapter"] = "adapter/ollama-default"
    if rule_pack:
        defaults["rule_packs"] = [rule_pack["id"]]
    if knowledge_pack:
        defaults["knowledge_packs"] = [knowledge_pack["id"]]

    pipeline = {
        "id": "pipeline/DRAFT-rename-me",
        "type": "pipeline",
        "version": "0.1.0",
        "name": f"DRAFT: {task[:60]}",
        "description": f"Auto-scaffolded by scripts/scaffold_pipeline_from_task.py from task: {task!r}",
        "authors": [{"name": "Open Harness Hub contributors"}],
        "license": "MIT",
        "industry": ["compliance"],
        "capability": ["evaluation", "extraction"],
        "modality": ["text"],
        "lifecycle": "experimental",
        "trust_boundary": "local",
        "pipeline_kind": "review",
        "inputs": [{"name": "input_packet", "type": "string|object"}],
        "outputs": [{"name": "grade", "type": "number"}, {"name": "findings", "type": "object[]"}],
        "defaults": defaults,
        "steps": steps,
        "success_criteria": [{"rubric": rubric["id"], "threshold": 0.6}] if rubric else [],
    }
    return pipeline


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("task", help="Free-text task description")
    parser.add_argument("--top-k", type=int, default=25)
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON (for LLM agent consumption)")
    parser.add_argument("--draft-yaml", action="store_true", help="Emit a draft pipeline YAML manifest")
    args = parser.parse_args()

    artifacts = load_artifacts()
    hits = search(args.task, artifacts, top_k=args.top_k)
    grouped = group_by_type(hits)

    if args.json:
        payload = {
            "task": args.task,
            "hits_by_type": {t: [{"id": a["id"], "score": round(s, 3), "matched_tokens": sorted(m), "name": a["name"], "description": a["description"], "path": a["path"]} for a, s, m in lst[:10]] for t, lst in grouped.items()},
            "draft_pipeline": make_draft_pipeline(args.task, grouped),
        }
        print(json.dumps(payload, indent=2))
        return 0

    if args.draft_yaml:
        draft = make_draft_pipeline(args.task, grouped)
        print(yaml.safe_dump(draft, sort_keys=False))
        return 0

    print(f"Task: {args.task!r}")
    print()
    print(f"Found {len(hits)} relevant artifacts across {len(grouped)} types.")
    print()
    for t in ["persona", "rule-pack", "knowledge-pack", "rubric", "tool", "processor", "pattern", "adapter", "pipeline", "dataset"]:
        if t not in grouped:
            continue
        print(f"== {t} ({len(grouped[t])} hits) ==")
        for a, s, m in grouped[t][:5]:
            print(f"  [{s:.2f}] {a['id']}")
            print(f"         {a['name']}")
            print(f"         matched: {', '.join(sorted(m))}")
        print()

    print("== Draft pipeline (use --draft-yaml to emit YAML) ==")
    draft = make_draft_pipeline(args.task, grouped)
    print(f"Steps: {len(draft['steps'])}")
    for s in draft["steps"]:
        print(f"  - {s['id']:25s} {s['ref']}")
    print()
    print("To get a full YAML draft:")
    print(f"  python3 scripts/scaffold_pipeline_from_task.py {args.task!r} --draft-yaml > /tmp/draft.yaml")
    print("To get JSON for agent consumption:")
    print(f"  python3 scripts/scaffold_pipeline_from_task.py {args.task!r} --json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
