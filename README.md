# Open Harness Hub

> A host-agnostic, industry-agnostic catalog of **harnesses**, **knowledge
> objects**, **logic packs**, **rule packs** (GREP / RAG / classifier /
> heuristic), **tools**, **pipelines**, **benchmarks**, and **rubrics** for
> building, evaluating, and shipping AI-assisted systems.

The hub is a **specification + content catalog + static site**. You can run
it from a clone, browse it on GitHub Pages, embed it as a Hugging Face Space,
or deploy it to Vercel / Netlify / Cloudflare Pages without changes.

## What this is

The Open Harness Hub gives you a standard way to describe and combine the
modular pieces of a real AI pipeline:

| Layer | Primitive | What it is |
|---|---|---|
| **Knowledge** | knowledge pack | A typed bundle of *facts* — RAG corpus, fact tables, contact directories, citation graphs. |
| **Logic** | logic pack | A typed bundle of *behavior* — prompt templates, tool registries, schemas, rubrics, response policies. |
| **Rules** | rule pack | A modular bundle of one rule family — GREP regex, glob patterns, classifier rules, heuristic rules, RAG retrieval rules. |
| **Tools** | tool | A function-call definition with example payloads and a backing implementation contract. |
| **Models** | model adapter | A provider-neutral transport (local Gemma, Ollama, OpenAI-compatible, Anthropic, Gemini, HF endpoint, frontier API, callable, none). |
| **Personas** | persona | A character or role frame the model adopts at the start of a workflow. |
| **Harnesses** | harness | A named, repeatable workflow around a model or trust boundary. Declares applied layers, packs consumed/emitted, model targets, input/output verification, and privacy boundaries. |
| **Pipelines** | pipeline | A DAG of harnesses + rule packs + tools that completes a specific task. |
| **Benchmarks** | benchmark | A pipeline run against a labeled test set with a rubric and a judge, producing a comparable score. |
| **Rubrics** | rubric | An evaluation contract — dimensions, weights, scoring scale, and the evidence each grade requires. |
| **Datasets** | dataset | A typed collection of inputs, outputs, and labels with provenance. |
| **Schemas** | schema | A typed I/O contract shared across artifacts. |

Every artifact is described by a small YAML manifest validated against a
JSON Schema in `schemas/`. The static site reads the catalog and renders a
browsable, searchable index.

## The two big goals

1. **Help people work out a benchmark for any task.** Pick a pipeline,
   plug in a dataset, declare a rubric, choose a judge — get a comparable
   score across models, harness configurations, and rule packs.
2. **Help people work out a tool for any task.** Pick the right modular
   primitives — a harness, a few rule packs, a tool registry, a knowledge
   pack — and compose them into a pipeline that solves a real problem.

Both goals share the same primitives. The catalog is the substrate.

## What lives in the catalog

The hub hosts every shape of pipeline that can be built by composing the
primitives above:

- **Research an entity** — sourced one-page profile of a company / person / place.
- **Verify data** — claim + corpus → supports / contradicts / no-evidence.
- **Format response** — coerce model output into a strict typed envelope.
- **Classify / extract / summarize / translate / redact / route.**
- **Agent loops** — plan + tool-call + verify + reflect.
- **Generate text** — free-form text generation with a defined harness.
- **Generate image** — prompt-shaping + style RAG + guard GREP rules + output-safety review.
- **Generate audio and video** — same primitive stack, different tools.
- **System-prompt / persona library** — reusable role frames.
- **RAG / GREP / classifier / heuristic libraries** — curated rule packs ready to plug in.
- **Tool library** — function-call schemas, MCP servers, OpenAPI ops.

The full list and the `pipeline_kind` vocabulary live in
`taxonomy/SPEC.md §11`.

## Where new content comes from

Three ingest paths feed the catalog (see `taxonomy/SPEC.md §12`):

1. **Direct PRs** — a contributor writes a manifest and opens a PR.
2. **Reference repos** — curators hand-port patterns from established
   harness/safety repos (e.g. DueCare, llm-safety-framework).
3. **Kaggle harness mining** — a scheduled crawler reads Kaggle competition
   notebooks (Gemma hackathon, LMSYS, retrieval challenges, agent
   competitions, image-gen competitions), detects harness-shaped patterns
   in the kernel code, and emits draft manifests under
   `catalog/_inbox/` for curator review. The crawler is itself a
   pipeline in this catalog — see `scripts/mine_kaggle_harnesses.py` and
   `docs/howto/mine-kaggle-harnesses.md`.

## Quick tour

- **`taxonomy/SPEC.md`** — the controlled vocabulary and field definitions.
  Start here.
- **`schemas/`** — JSON Schemas that every manifest must validate against.
- **`vocabularies/`** — controlled lists (industries, capabilities,
  modalities, trust boundaries, lifecycle stages).
- **`catalog/`** — the actual content. One YAML per artifact, organized by
  type (`catalog/harnesses/`, `catalog/rule-packs/`, etc.).
- **`examples/`** — worked end-to-end examples. `examples/migrant-worker-safety/`
  is a generic instance of the reference DueCare safety harness ecosystem.
- **`docs/`** — MkDocs source for the published site.
- **`scripts/`** — `validate.py` (run schemas across the catalog),
  `build_catalog_pages.py` (turn manifests into doc pages), `new.py`
  (scaffold a new artifact).

## Run the site locally

```bash
pip install mkdocs-material mkdocs-awesome-pages-plugin jsonschema pyyaml
python scripts/validate.py        # validate every manifest
python scripts/build_catalog_pages.py   # generate docs/catalog/*.md
mkdocs serve                      # http://127.0.0.1:8000
```

## Deploy targets (host-agnostic)

The same `mkdocs build` output deploys unchanged to:

- **GitHub Pages** — `.github/workflows/pages.yml` builds and publishes on push to `main`.
- **Hugging Face Spaces** — `hf-space/README.md` carries the HF frontmatter; serve `site/` as static.
- **Vercel** — `vercel.json` runs `mkdocs build` and serves `site/`.
- **Netlify** — `netlify.toml` does the same.
- **Cloudflare Pages** — same build, same output directory.

Pick one or all four; the build is identical.

## Reference inheritance

The reference for the harness/knowledge/pipeline pattern is Taylor Amarel's
DueCare safety ecosystem ([`TaylorAmarelTech/gemma4_comp`](https://github.com/TaylorAmarelTech/gemma4_comp))
plus the LLM Safety Framework ([`TaylorAmarelTech/llm-safety-framework`](https://github.com/TaylorAmarelTech/llm-safety-framework)).
Those repos are cloned into `_reference/` for offline study; nothing under
`_reference/` is republished here.

The taxonomy generalizes the DueCare contract — `HarnessSpec`,
`HarnessLogicPath`, `HarnessModelTarget`, `HarnessPackContract`,
`KnowledgeObject` — to apply across any industry: healthcare, finance,
legal, manufacturing, retail, education, gov, security, climate, and so on.

## License

MIT. See `LICENSE`.
