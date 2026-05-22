# Getting started: assemble a pipeline from a task description

A common ask: "I have a task. The catalog has 493 artifacts. Which ones do I need?"

The catalog ships a scaffolding script that takes a free-text task description, searches the catalog for relevant components, and emits a draft pipeline manifest. The script is meant for two audiences:

1. A developer poking around for the right components.
2. An LLM agent asked to assemble a pipeline from the catalog (give the agent the JSON output).

## Quick start

```bash
python3 scripts/scaffold_pipeline_from_task.py "Review a vendor invoice for fraud signals + extract line items"
```

Output (abridged):

```
Task: 'Review a vendor invoice for fraud signals + extract line items'

Found 24 relevant artifacts across 8 types.

== persona (3 hits) ==
  [0.61] persona/bureaucracy-translator-cite-first
         Bureaucracy translator (cite-first)
         matched: bill, document, extract, fraud

== rule-pack (4 hits) ==
  [0.72] rule-pack/grep-fake-inkasso-fraud-flags
         Fake-Inkasso fraud flags
         matched: extract, fraud, invoice, signals

== knowledge-pack (2 hits) ==
  [0.55] knowledge-pack/verbraucherzentrale-fake-inkasso-indicators
         Verbraucherzentrale fake-Inkasso 10-indicator taxonomy
         matched: fraud, signals

== rubric (2 hits) ==
  [0.49] rubric/bureaucracy-translation-quality-v1

== Draft pipeline (use --draft-yaml to emit YAML) ==
Steps: 6
  - structured_to_prose       processor/structured-to-prose
  - redact_pii                processor/redact-pii-text
  - grep_red_flags            rule-pack/grep-fake-inkasso-fraud-flags
  - rag                       rule-pack/hybrid-retrieval-policy
  - grade                     processor/llm-judge
  - audit                     processor/audit-trace-emitter
```

## Get the draft YAML

```bash
python3 scripts/scaffold_pipeline_from_task.py \
  "Triage user-generated content for illicit signals on a social platform" \
  --draft-yaml > /tmp/my-pipeline.yaml
```

Then refine the draft, validate it, and you have a working pipeline.

## Use it from an LLM agent

```bash
python3 scripts/scaffold_pipeline_from_task.py "..." --json > /tmp/catalog-hits.json
```

The JSON has the shape:

```json
{
  "task": "...",
  "hits_by_type": {
    "persona": [{ "id": "...", "score": 0.61, "matched_tokens": [...], "name": "...", "description": "...", "path": "..." }],
    "rule-pack": [...],
    "knowledge-pack": [...],
    "rubric": [...]
  },
  "draft_pipeline": { ... full pipeline manifest ... }
}
```

Feed it to your agent with a prompt like:

> Here is a task and a set of catalog hits. Compose a working pipeline.yaml using only artifacts that exist in `hits_by_type`. Refine the `draft_pipeline` if needed; never invent artifact IDs.

The "never invent artifact IDs" constraint is important. The script gives the agent a closed set of real IDs to compose from, which prevents fabricated references that would fail validation.

## Validation loop

```bash
# 1. Get the draft.
python3 scripts/scaffold_pipeline_from_task.py "..." --draft-yaml > catalog/pipelines/mine/draft.yaml

# 2. Edit it (rename, add real inputs/outputs, tag).
$EDITOR catalog/pipelines/mine/draft.yaml

# 3. Validate against schemas.
python3 scripts/validate.py

# 4. If it has clean+flagged samples, add them to scripts/bench_pipelines.py.
```

## When the script is not enough

The script does lexical search (token overlap, no embeddings). For larger catalogs or where semantic search matters, build the derived SQLite + embeddings DB:

```bash
OH_BUILD_EMBEDDINGS=1 python3 scripts/build_catalog_db.py
```

Then query the DB directly or write your own ranker. YAML stays the source of truth; the DB is a derived build artifact, regenerated from the YAML on every push.
