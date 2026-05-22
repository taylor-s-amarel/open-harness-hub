# Agent Skills bundle

# Open Harness Hub — Agent Skills bundle

This directory is the **Agent Skills export** of every harness and
pipeline in the hub. Agent Skills is an open standard (agentskills.io)
adopted by 40+ tools including Claude Code, OpenAI Codex, GitHub
Copilot, Gemini CLI, Cursor, VS Code, OpenHands, Roo Code, Goose,
Letta, Amp, Junie, Workshop, Tabnine, OpenCode, Factory, and more.

## Use as Claude Code skills

Copy any `<slug>/` directory under `~/.claude/skills/` or your
project's `.claude/skills/`:

```bash
cp -r dist/agent-skills/text-safety-review ~/.claude/skills/
```

Restart Claude Code; the skill is now available as
`/text-safety-review`.

## Use as a Claude Code plugin marketplace

The `.claude-plugin/marketplace.json` in this directory makes the
whole bundle a Claude Code plugin marketplace. Users can add it
with:

```
/plugin marketplace add <git-url-of-this-repo>
```

## Use in other Agent Skills-compatible tools

Every other tool that implements Agent Skills (Cursor, OpenHands,
Gemini CLI, Roo Code, etc.) accepts the same SKILL.md folder
layout. Check each tool's docs for the exact install path — the
contents are identical.

## Skills in this bundle

- `text-safety-review/SKILL.md` — harness (`harness/text-safety-review`)
- `esg-disclosure-grading/SKILL.md` — harness (`harness/esg-disclosure-grading`)
- `clinical-decision-support/SKILL.md` — harness (`harness/clinical-decision-support`)
- `personal-corpus-search/SKILL.md` — harness (`harness/personal-corpus-search`)
- `code-act-jupyter/SKILL.md` — harness (`harness/code-act-jupyter`)
- `appsec-code-audit/SKILL.md` — harness (`harness/appsec-code-audit`)
- `chat-with-memory/SKILL.md` — harness (`harness/chat-with-memory`)
- `contract-redline/SKILL.md` — harness (`harness/contract-redline`)
- `redact-pii-text/SKILL.md` — harness (`harness/redact-pii-text`)
- `data-cleaning-and-enrichment/SKILL.md` — harness (`harness/data-cleaning-and-enrichment`)
- `email-triage-and-draft/SKILL.md` — harness (`harness/email-triage-and-draft`)
- `radiology-report-review/SKILL.md` — harness (`harness/radiology-report-review`)
- `aml-investigation/SKILL.md` — harness (`harness/aml-investigation`)
- `radiology-report-grading/SKILL.md` — pipeline (`pipeline/radiology-report-grading`)
- `ma-dd-review/SKILL.md` — pipeline (`pipeline/ma-dd-review`)
- `medlabel-photo-to-warning/SKILL.md` — pipeline (`pipeline/medlabel-photo-to-warning`)
- `quantized-llm-inference/SKILL.md` — pipeline (`pipeline/quantized-llm-inference`)
- `telco-compliance-review/SKILL.md` — pipeline (`pipeline/telco-compliance-review`)
- `climate-disclosure-review/SKILL.md` — pipeline (`pipeline/climate-disclosure-review`)
- `bidirectional-lstm-sequence-prediction/SKILL.md` — pipeline (`pipeline/bidirectional-lstm-sequence-prediction`)
- `platform-content-triage/SKILL.md` — pipeline (`pipeline/platform-content-triage`)
- `space-launch-review/SKILL.md` — pipeline (`pipeline/space-launch-review`)
- `anonymized-illicit-recruitment-pattern-sharing/SKILL.md` — pipeline (`pipeline/anonymized-illicit-recruitment-pattern-sharing`)
- `lgb-xgb-catboost-ensemble/SKILL.md` — pipeline (`pipeline/lgb-xgb-catboost-ensemble`)
- `code-act-jupyter-loop/SKILL.md` — pipeline (`pipeline/code-act-jupyter-loop`)
- `dicom-medical-image-preprocessing/SKILL.md` — pipeline (`pipeline/dicom-medical-image-preprocessing`)
- `chat-with-pdf-citations/SKILL.md` — pipeline (`pipeline/chat-with-pdf-citations`)
- `customs-broker-review/SKILL.md` — pipeline (`pipeline/customs-broker-review`)
- `hr-hiring-compliance-review/SKILL.md` — pipeline (`pipeline/hr-hiring-compliance-review`)
- `brand-safe-product-photo/SKILL.md` — pipeline (`pipeline/brand-safe-product-photo`)
- `rcra-waste-review/SKILL.md` — pipeline (`pipeline/rcra-waste-review`)
- `threat-intel-ioc-review/SKILL.md` — pipeline (`pipeline/threat-intel-ioc-review`)
- `gaming-integrity-review/SKILL.md` — pipeline (`pipeline/gaming-integrity-review`)
- `real-estate-dd-review/SKILL.md` — pipeline (`pipeline/real-estate-dd-review`)
- `vllm-batch-llm-inference/SKILL.md` — pipeline (`pipeline/vllm-batch-llm-inference`)
- `code-security-review/SKILL.md` — pipeline (`pipeline/code-security-review`)
- `sentence-transformer-finetune-retrieval/SKILL.md` — pipeline (`pipeline/sentence-transformer-finetune-retrieval`)
- `suspicious-transaction-review/SKILL.md` — pipeline (`pipeline/suspicious-transaction-review`)
- `food-safety-review/SKILL.md` — pipeline (`pipeline/food-safety-review`)
- `academic-integrity-review/SKILL.md` — pipeline (`pipeline/academic-integrity-review`)
- `construction-safety-review/SKILL.md` — pipeline (`pipeline/construction-safety-review`)
- `code-review-with-risk-score/SKILL.md` — pipeline (`pipeline/code-review-with-risk-score`)
- `perplexity-baseline-scoring/SKILL.md` — pipeline (`pipeline/perplexity-baseline-scoring`)
- `deepseek-r1-code-interpreter-math/SKILL.md` — pipeline (`pipeline/deepseek-r1-code-interpreter-math`)
- `deep-research-supervisor-workers/SKILL.md` — pipeline (`pipeline/deep-research-supervisor-workers`)
- `deep-research-with-citations/SKILL.md` — pipeline (`pipeline/deep-research-with-citations`)
- `ai-governance-audit/SKILL.md` — pipeline (`pipeline/ai-governance-audit`)
- `insurance-claim-review/SKILL.md` — pipeline (`pipeline/insurance-claim-review`)
- `deep-tier-supplier-audit/SKILL.md` — pipeline (`pipeline/deep-tier-supplier-audit`)
- `maritime-safety-review/SKILL.md` — pipeline (`pipeline/maritime-safety-review`)
- `efficientnet-medical-imaging/SKILL.md` — pipeline (`pipeline/efficientnet-medical-imaging`)
- `research-entity/SKILL.md` — pipeline (`pipeline/research-entity`)
- `bill-info-extract-fraud-detect-recommend/SKILL.md` — pipeline (`pipeline/bill-info-extract-fraud-detect-recommend`)
- `synthetic-data-gen-with-teacher-llm/SKILL.md` — pipeline (`pipeline/synthetic-data-gen-with-teacher-llm`)
- `qwen-vllm-rerank-eedi/SKILL.md` — pipeline (`pipeline/qwen-vllm-rerank-eedi`)
- `email-triage-pipeline/SKILL.md` — pipeline (`pipeline/email-triage-pipeline`)
- `personal-chat-pipeline/SKILL.md` — pipeline (`pipeline/personal-chat-pipeline`)
- `personal-search-pipeline/SKILL.md` — pipeline (`pipeline/personal-search-pipeline`)
- `everything-research-pipeline/SKILL.md` — pipeline (`pipeline/everything-research-pipeline`)
- `sd-prompt-embedding-cosine/SKILL.md` — pipeline (`pipeline/sd-prompt-embedding-cosine`)
- `trade-compliance-review/SKILL.md` — pipeline (`pipeline/trade-compliance-review`)
- `aviation-safety-review/SKILL.md` — pipeline (`pipeline/aviation-safety-review`)
- `dfars-cmmc-compliance-review/SKILL.md` — pipeline (`pipeline/dfars-cmmc-compliance-review`)
- `contract-clause-review/SKILL.md` — pipeline (`pipeline/contract-clause-review`)
- `personal-code-review-with-preferences/SKILL.md` — pipeline (`pipeline/personal-code-review-with-preferences`)
- `gxp-validation-review/SKILL.md` — pipeline (`pipeline/gxp-validation-review`)
- `llm-judge-essay-grading/SKILL.md` — pipeline (`pipeline/llm-judge-essay-grading`)
- `transfer-pricing-review/SKILL.md` — pipeline (`pipeline/transfer-pricing-review`)
- `gdpr-dsar-review/SKILL.md` — pipeline (`pipeline/gdpr-dsar-review`)
- `biosecurity-review/SKILL.md` — pipeline (`pipeline/biosecurity-review`)
- `email-triage-and-draft/SKILL.md` — pipeline (`pipeline/email-triage-and-draft`)
- `water-utility-compliance-review/SKILL.md` — pipeline (`pipeline/water-utility-compliance-review`)
- `mixed-criteria-demo/SKILL.md` — pipeline (`pipeline/mixed-criteria-demo`)
- `unet-segmentation-tta/SKILL.md` — pipeline (`pipeline/unet-segmentation-tta`)
- `trid-loan-gate/SKILL.md` — pipeline (`pipeline/trid-loan-gate`)
- `esi-triage-gate/SKILL.md` — pipeline (`pipeline/esi-triage-gate`)
- `faa-preflight-gate/SKILL.md` — pipeline (`pipeline/faa-preflight-gate`)
- `nfpa-70e-loto-gate/SKILL.md` — pipeline (`pipeline/nfpa-70e-loto-gate`)
- `msha-preshift-exam/SKILL.md` — pipeline (`pipeline/msha-preshift-exam`)
- `who-surgical-safety-gate/SKILL.md` — pipeline (`pipeline/who-surgical-safety-gate`)
- `kyc-cip-gate/SKILL.md` — pipeline (`pipeline/kyc-cip-gate`)
- `itil-change-gate/SKILL.md` — pipeline (`pipeline/itil-change-gate`)
- `haccp-ccp-gate/SKILL.md` — pipeline (`pipeline/haccp-ccp-gate`)
- `dot-pretrip-gate/SKILL.md` — pipeline (`pipeline/dot-pretrip-gate`)
- `nist-800-61-ir-gate/SKILL.md` — pipeline (`pipeline/nist-800-61-ir-gate`)
- `pssr-startup-gate/SKILL.md` — pipeline (`pipeline/pssr-startup-gate`)
- `aorn-surgical-count-gate/SKILL.md` — pipeline (`pipeline/aorn-surgical-count-gate`)
- `storm-persona-curation-article/SKILL.md` — pipeline (`pipeline/storm-persona-curation-article`)
- `plan-execute-critic-loop/SKILL.md` — pipeline (`pipeline/plan-execute-critic-loop`)
- `verify-claim-against-corpus/SKILL.md` — pipeline (`pipeline/verify-claim-against-corpus`)
- `self-rag-grade-and-revise/SKILL.md` — pipeline (`pipeline/self-rag-grade-and-revise`)
- `nuclear-safety-review/SKILL.md` — pipeline (`pipeline/nuclear-safety-review`)
- `multi-model-judging-ensemble/SKILL.md` — pipeline (`pipeline/multi-model-judging-ensemble`)
- `two-time-retrieve-rerank/SKILL.md` — pipeline (`pipeline/two-time-retrieve-rerank`)
- `nerc-cip-compliance-review/SKILL.md` — pipeline (`pipeline/nerc-cip-compliance-review`)
- `sensor-fusion-imu-blending/SKILL.md` — pipeline (`pipeline/sensor-fusion-imu-blending`)
- `benefits-adjudication-review/SKILL.md` — pipeline (`pipeline/benefits-adjudication-review`)
- `document-to-knowledge-graph/SKILL.md` — pipeline (`pipeline/document-to-knowledge-graph`)
- `optuna-tabular-tuning/SKILL.md` — pipeline (`pipeline/optuna-tabular-tuning`)
- `multi-doc-qa-subquestion/SKILL.md` — pipeline (`pipeline/multi-doc-qa-subquestion`)
- `awq-quantized-inference/SKILL.md` — pipeline (`pipeline/awq-quantized-inference`)
- `large-model-faiss-rag/SKILL.md` — pipeline (`pipeline/large-model-faiss-rag`)
- `mask-rcnn-coco-transfer/SKILL.md` — pipeline (`pipeline/mask-rcnn-coco-transfer`)
- `audio-mel-spec-cnn-classifier/SKILL.md` — pipeline (`pipeline/audio-mel-spec-cnn-classifier`)
- `swe-patch-sample-and-review/SKILL.md` — pipeline (`pipeline/swe-patch-sample-and-review`)
- `blip-clip-image-to-prompt/SKILL.md` — pipeline (`pipeline/blip-clip-image-to-prompt`)
- `full-vendor-due-diligence/SKILL.md` — pipeline (`pipeline/full-vendor-due-diligence`)
- `knowledge-graph-from-corpus/SKILL.md` — pipeline (`pipeline/knowledge-graph-from-corpus`)
- `sustainability-report-full-review/SKILL.md` — pipeline (`pipeline/sustainability-report-full-review`)
- `supplier-policy-grading/SKILL.md` — pipeline (`pipeline/supplier-policy-grading`)
- `longformer-bigbird-ner/SKILL.md` — pipeline (`pipeline/longformer-bigbird-ner`)
- `customer-record-enrichment/SKILL.md` — pipeline (`pipeline/customer-record-enrichment`)
- `security-incident-grading/SKILL.md` — pipeline (`pipeline/security-incident-grading`)
- `multi-agent-debate-with-judge/SKILL.md` — pipeline (`pipeline/multi-agent-debate-with-judge`)
- `twenty-questions-agent/SKILL.md` — pipeline (`pipeline/twenty-questions-agent`)
- `cannabis-compliance-review/SKILL.md` — pipeline (`pipeline/cannabis-compliance-review`)
- `election-misinformation-review/SKILL.md` — pipeline (`pipeline/election-misinformation-review`)
- `agriculture-compliance-review/SKILL.md` — pipeline (`pipeline/agriculture-compliance-review`)
- `citemind-pdf-to-research-wiki/SKILL.md` — pipeline (`pipeline/citemind-pdf-to-research-wiki`)
- `deberta-lgbm-hybrid-scorer/SKILL.md` — pipeline (`pipeline/deberta-lgbm-hybrid-scorer`)
- `differential-diagnosis/SKILL.md` — pipeline (`pipeline/differential-diagnosis`)
