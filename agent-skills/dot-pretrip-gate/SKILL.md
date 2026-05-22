---
name: dot-pretrip-gate
description: Apply DVIR gate before truck dispatch.
when_to_use: 'Pipeline kind: review.'
---

# DOT pre-trip inspection gate (DVIR / 49 CFR 396)

Apply driver vehicle inspection report gate — out-of-service criteria block dispatch.

## Task

Apply DVIR gate before truck dispatch.

## Steps

1. **structured_to_prose** — `processor` → `processor/structured-to-prose`
2. **checklist_gate** — `processor` → `processor/checklist-evaluator`
3. **audit** — `processor` → `processor/audit-trace-emitter`

## Defaults

- **knowledge_packs**: `knowledge-pack/technician-checklists`

## Success criteria

- deterministic `$.steps.checklist_gate.output.verdict` == `go`

## Provenance

- Hub artifact: `pipeline/dot-pretrip-gate` v0.1.0
- License: `MIT`
- Industry: transportation, compliance
- Full source manifest: see `references/manifest.yaml`
