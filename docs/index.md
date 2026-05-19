# Open Harness Hub

> A host-agnostic, industry-agnostic catalog of **harnesses**, **knowledge
> objects**, **logic packs**, **rule packs** (GREP / RAG / classifier /
> heuristic / online-search), **tools**, **pipelines**, **benchmarks**,
> and **rubrics** for building, evaluating, and shipping AI-assisted
> systems.

## The pitch in one line

> Pick a pipeline. Plug in the right rule packs and a model adapter.
> Get a benchmark or a working tool — for any industry, any modality.

## Start here

- [Overview](concepts/overview.md) — what the hub is and why.
- [Taxonomy](concepts/taxonomy.md) — the controlled vocabulary you'll
  use to describe artifacts.
- [Catalog index](catalog/index.md) — browse every published artifact.
- [Add an artifact](howto/add-artifact.md) — contribute a manifest.
- [Run a pipeline locally](howto/run-pipeline.md) — pipeline runner +
  Gradio playground.

## Reach across industries

Every artifact tags its industries (open vocabulary). The same harness
can serve `healthcare.radiology`, `finance.aml`, and
`humanitarian.trafficking` if its primitives are pure enough. When a
harness is industry-specific, the catalog says so explicitly.

## Reach across modalities

Image, audio, and video pipelines compose the **same** primitives as
text pipelines. See [Multimodal pipelines](concepts/multimodal.md).

## Reach across hosts

The site builds once and deploys unchanged to GitHub Pages, Hugging
Face Spaces, Vercel, Netlify, or Cloudflare Pages. See
[Deploy the hub](howto/deploy.md).
