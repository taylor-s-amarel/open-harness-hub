# Mine Kaggle for harnesses

LLM-relevant Kaggle competition notebooks are a goldmine for harness,
RAG, GREP, and pipeline patterns. The hub ships a mining script
(`scripts/mine_kaggle_harnesses.py`) that ingests competition kernels,
detects harness-shaped code, and emits draft manifests for curator
review.

## What gets mined

The script targets LLM-relevant competitions and their kernels:

- Gemma family competitions (the source of `_reference/gemma4_comp`).
- LMSYS / Chatbot Arena evaluation challenges.
- Retrieval-augmented-generation and document-QA challenges.
- Agent / tool-use hackathons.
- Image-generation competitions (Stable Diffusion variants, ControlNet).
- Reasoning challenges that ship public eval notebooks.

The competition filter and detector pack live in
`catalog/rule-packs/online-search/kaggle-mining-policy.yaml` (TBA) so
the mining is itself a hub artifact.

## What gets detected

The detector applies a small pack of `grep` + `classifier` rules to
each kernel file. The detectors look for:

- a function that wraps an LLM call with **preprocessing** (PII redact,
  query rewrite, query expansion);
- a function that wraps an LLM call with **retrieval** (BM25, dense,
  hybrid, citation graph);
- a function that wraps an LLM call with **tool-calling** (function
  schemas, tool registries, MCP servers);
- a function that wraps an LLM call with **output post-processing**
  (citation extraction, refusal post-edit, schema-coercion);
- a notebook cell that defines a **rubric** (graded examples,
  weighted dimensions);
- a notebook cell that defines a **pipeline** as a sequence of those
  primitives.

When the detector fires, the script extracts the primitive into a
draft manifest under `catalog/_inbox/{date}-{kernel_id}/` with
`attribution.source_url`, `attribution.author`, `attribution.license`
filled in.

## License safety

The mining script SKIPS any kernel whose license is incompatible with
redistribution (no license, "CC BY-NC", or explicit "All rights
reserved"). The default policy accepts `Apache-2.0`, `MIT`,
`CC0-1.0`, `BSD-3-Clause`, `CC-BY-4.0`, `CC-BY-SA-4.0`.

The license-decision logic is itself a rule pack:
`catalog/rule-packs/online-search/kaggle-license-policy.yaml` (TBA).

## Running it

```bash
# 1. Install Kaggle CLI and authenticate (kaggle.json).
pip install kaggle
mkdir -p ~/.kaggle && cp ~/Downloads/kaggle.json ~/.kaggle/

# 2. Run the miner. Defaults to a 7-day window.
python scripts/mine_kaggle_harnesses.py \
    --competitions gemma-4-good-hackathon lmsys-chatbot-arena \
    --since 2026-04-01 --until 2026-05-31

# 3. Review the inbox.
ls catalog/_inbox/
$EDITOR catalog/_inbox/2026-05-19-<kernel-id>/

# 4. Promote a draft to the catalog.
mv catalog/_inbox/2026-05-19-<kernel-id>/harness.yaml \
   catalog/harnesses/<slug>.yaml
python scripts/validate.py
```

## Curator workflow

Curators should:

1. **Read the original kernel.** The detector finds the shape, but the
   intent and constraints live in the prose around the code.
2. **Strip industry-specific assumptions.** A competition's `corridor_profile`
   may be a `corridor_profile` only when applied to migrant safety;
   for a generic catalog entry, model it as a generic `entity_signal`.
3. **Anonymize sample data.** Real worker chats, real patient records,
   real customer messages are NEVER published — replace with
   synthetic composites.
4. **Cite the source.** Every promoted manifest must retain its
   `attribution.source_url` and `attribution.author`.
