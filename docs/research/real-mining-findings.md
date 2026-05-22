# Real mining findings - Meta Kaggle + GitHub

> This time the mining ACTUALLY ran. Meta Kaggle parsed, 9 top-voted
> LLM-competition kernels pulled, 10 production agentic-AI repos
> cloned and pattern-searched.

## Methodology

1. **Meta Kaggle**: downloaded the official `kaggle/meta-kaggle` dataset
   (~1.5 GB CSV metadata) via authenticated Kaggle CLI. Parsed
   `Competitions.csv` (with NUL-byte stripping) for LLM-relevant titles
   and slugs. Found **97 competitions** matching keywords like
   `llm`, `language model`, `gemma`, `chatbot`, `prompt`, `lmsys`,
   `detect-ai`, `retrieval`, etc.

2. **Top kernel pulls**: for the 5 highest-signal competitions
   (`llm-detect-ai-generated-text`, `wsdm-cup-multilingual-chatbot-arena`,
   `llm-classification-finetuning`, `h2oai-predict-the-llm`,
   `llms-you-cant-please-them-all`) ran `kaggle kernels list --sort-by
   voteCount --page-size 5` and pulled the top kernels via
   `kaggle kernels pull <ref> -m`.

3. **Detector run**: extracted code cells from each pulled `.ipynb`
   and ran the existing `scripts/mine_kaggle_harnesses.py` regex
   detector pack PLUS a library-presence check (transformers, peft,
   unsloth, bitsandbytes, langchain, llama_index, haystack, dspy,
   sentence_transformers, datasets, trl, vllm, litellm).

4. **GitHub clones**: shallow-cloned 10 production agentic-AI repos
   (langgraph, autogen, crewAI, open_deep_research, self-rag,
   SWE-agent, reflexion, graphrag, semantic-router, open-interpreter)
   into `/tmp/oh-mining/github`. 688 MB total.

5. **Pattern grep**: ran `grep -rl` for known pipeline-pattern markers
   across all cloned repos.

## Concrete findings

### Kaggle - WSDM Chatbot Arena harness pattern (CONFIRMED with real code)

Three of nine pulled kernels - all from WSDM Cup Multilingual Chatbot
Arena - confirmed the same harness shape:

| Kernel | Pattern hit | Libraries |
|---|---|---|
| `mbmmurad/gemma-2-9b-4-bit-qlora-lb-0-63` (453 votes) | `harness_wrapper_call_model` | transformers + peft + bitsandbytes |
| `takaito/wsdm-cup-lb-0-684-only-gemma-2-9b-4-bit` (428 votes) | `harness_wrapper_call_model` | transformers + peft + bitsandbytes |
| `takamichitoda/wsdm-apply-previous-lmsys-solution` (329 votes) | `harness_wrapper_call_model` | transformers + peft + bitsandbytes |

**Canonical shape (verified)**:

1. Load Gemma-2 9B with 4-bit QLoRA quantization (bitsandbytes).
2. Wrap with PEFT LoRA adapter for fine-tuning.
3. Fine-tune on the (prompt, response_A, response_B) → pref triples.
4. Inference: run the same model on the test set with a classifier head
   over A / B / tie.

This is now a confirmed `pipeline/*` shape for the hub:
`pipeline/judge-pairwise-lora-qlora`. Adding to the next batch.

### Kaggle - kernels NOT matching the harness detector

The other six kernels (top-voted in detect-ai-generated-text,
llm-classification-finetuning, h2oai-predict-the-llm,
llms-you-cant-please-them-all) used **classical ML** approaches:
TF-IDF + LightGBM / XGBoost / DeBERTa fine-tune. No
"wrap-an-LLM-with-pre/post-processing" pattern in the top kernels for
those competitions.

This is itself a useful finding: **for closed-vocabulary
classification competitions, the winning shape is small-model
fine-tuning, not LLM-harness orchestration.** The hub should reflect
this - `pipeline/classify-with-tfidf-lightgbm` and
`pipeline/classify-with-deberta-finetune` are real-world-validated
shapes that should join the catalog.

### GitHub - pattern markers found

| Pattern marker | Repos that contain it |
|---|---|
| ReAct (`Thought:` / `Observation:` / `Action:`) | crewAI (extensive - both code + tests) |
| MCP tool definitions | crewAI (`lib/crewai/src/crewai/tools/mcp_tool_wrapper.py`, `mcp/config.py`, `mcp/tool_resolver.py`, `mcp/filters.py`) |
| Reflexion / self-critique | langgraph (errors, pregel/_algo, stream/_mux, graph/state, retry) |
| Plan-and-execute / state-graph | semantic-router (encoders), langgraph (checkpoint, store, state machine) |
| Subagent / multi-agent / supervisor | langgraph (sdk-py async client, prebuilt/tool_node, CLI), crewAI (flow tests) |

Tree-of-Thoughts (`tree.of.thought` / `BFS`) - **no direct hits in
the cloned set**. ToT is more academic than production today; the
production frameworks use Self-Refine + Reflexion + Plan-Execute
instead. The hub's `pattern/tree-of-thoughts` should stay
`lifecycle: beta` reflecting that.

### Specific high-value files for direct adoption

Files worth porting code/shape from into hub `processor/*` or
`pipeline/*` manifests:

| File | What it gives the hub |
|---|---|
| `crewAI/lib/crewai/src/crewai/tools/mcp_tool_wrapper.py` | Reference impl for `tool/mcp-*` wrappers |
| `crewAI/lib/crewai/src/crewai/mcp/tool_resolver.py` | MCP tool selection from large catalog (Toolformer-style) |
| `langgraph/libs/langgraph/langgraph/graph/state.py` | State-machine semantics for `pipeline/*` runs |
| `langgraph/libs/prebuilt/langgraph/prebuilt/tool_node.py` | Reference impl for the `step.kind: tool` pipeline step |
| `langgraph/libs/langgraph/langgraph/pregel/_algo.py` | Pregel scheduling for parallel `processor/parallel.fan_out` |
| `semantic-router/semantic_router/encoders/*.py` | Reference impls for `adapter/openai-embeddings`, `adapter/bge-embeddings-local` |

## Disk + bandwidth used

- Meta Kaggle: ~1.5 GB (1×).
- 9 kernels pulled: 1.8 MB.
- 10 GitHub repos shallow-cloned: 688 MB.
- Total: ~2.2 GB. Negligible vs the 12 GB Meta Kaggle Code dataset
  that I deliberately did NOT pull (would have given me kernel
  source for every public kernel but at 7× the disk cost).

## What this enables next batch

Concrete artifacts to add (next push):

- `pipeline/judge-pairwise-lora-qlora` - verified WSDM Cup shape
- `pipeline/classify-with-tfidf-lightgbm` - verified classical-ML shape
- `pipeline/classify-with-deberta-finetune` - verified classical-NLP shape
- `tool/mcp-crewai-resolver` - port shape from crewAI's tool_resolver
- Update `processor/iterative-revise-loop` impl notes with langgraph's pregel scheduling pattern
- Add `pattern/langgraph-state-machine` - formalize the StateGraph shape as a named pattern

## Honest limitations

- Only 9 kernels pulled (more would land more shapes). At ~1 minute/kernel
  for 50 kernels, that's 50 minutes of mining; ROI worth it for a
  weekend pass but not this session.
- Detector regex pack is conservative; would miss kernels where the
  harness pattern uses non-standard naming. Worth a second pass with
  AST-based detection later.
- GitHub clone depth=1 means no commit-history mining; can add later
  if useful.
- WebFetch denied for some sources; relied on Playwright + gh CLI
  + Kaggle CLI directly.
