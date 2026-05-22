# Outreach draft - CiteMind team (local AI research wiki for PDFs)

CiteMind team,

I'm Taylor Amarel - I run [github.com/taylor-s-amarel/open-harness-hub](https://github.com/taylor-s-amarel/open-harness-hub), an MIT-licensed catalog of harnesses, pipelines, knowledge objects, design patterns, and rule packs for AI engineering. Your CiteMind submission for the Gemma 4 Good Hackathon landed in front of me and the architecture maps cleanly into the catalog's vocabulary. I integrated it as a first-class reference vertical and three reusable design patterns, with attribution to your team + the submission writeup.

**Where it lives**

- Use-case doc: [`docs/use-cases/local-first-research-wiki.md`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/docs/use-cases/local-first-research-wiki.md)
- Pipeline manifest: [`catalog/pipelines/local-research-wiki/citemind-pdf-to-research-wiki.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/pipelines/local-research-wiki/citemind-pdf-to-research-wiki.yaml)
- Persona: [`catalog/personas/local-first-research-tutor.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/personas/local-first-research-tutor.yaml)
- Knowledge pack (CiteMind architecture-as-reference): [`catalog/knowledge-packs/citemind-architecture-reference.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/knowledge-packs/citemind-architecture-reference.yaml)
- Rubric (citation fidelity): [`catalog/rubrics/citemind-citation-fidelity-v1.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/rubrics/citemind-citation-fidelity-v1.yaml)
- Processors: `pdf-extract-with-ocr-fallback`, `page-aware-chunker`, `local-embedder`, `hybrid-bm25-vector-retrieve`, `concept-graph-extractor`.

**Three design patterns extracted** (because they generalize beyond CiteMind):

1. **[`pattern/local-first-with-cited-answers`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/patterns/local-first-with-cited-answers.yaml)** - local PDF + chunks + embeddings + chat history + audit trace on the user's machine; cloud is opt-in via explicit API key. Every answer carries a (page, span) citation. Generalizes to legal review, defense documentation, BSL-4 SOP study, refugee Inkasso letter review.

2. **[`pattern/source-document-to-persistent-knowledge-layer`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/patterns/source-document-to-persistent-knowledge-layer.yaml)** - the document is the persistent state, not the chat. Wiki pages + concept graph + study guide + bookmarks + notes accumulate onto a long-lived layer the user can return to. Generalizes to compliance audits, regulatory cross-references, ESG disclosure review.

3. **[`pattern/concept-graph-from-text`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/patterns/concept-graph-from-text.yaml)** - relationships extracted as first-class entities (typed edges with source anchors) rather than as a side effect of free-text mention. Generalizes to ESG materiality maps, supply-chain graphs, drug-interaction graphs, DFARS clause flow-down maps.

**Why I think this matters for your project**

1. **Visibility** - the catalog is intentionally a discovery surface. Anyone running `oh-hub describe pattern/local-first-with-cited-answers` or `oh-hub describe pipeline/citemind-pdf-to-research-wiki` lands on your work + the design patterns it crystallized.

2. **The three patterns travel** - developers will hit them through other verticals (defense, biosecurity, ESG, refugee Inkasso) and the CiteMind attribution travels with them. Every one of the catalog's 34+ industry-grading verticals now has a "you-might-want-the-CiteMind-patterns" path.

3. **NGO / education path** - your roadmap may target educational + privacy-sensitive settings (universities, public libraries, legal aid clinics, regulated industries). The catalog already has the standards-format emitters (Croissant / MCP / Agent Skills / HF cards) so any institution adopting CiteMind gets the publication formats for free.

**What I'd love your input on**

1. **Repo URL + author handles** - I left the upstream URL + license as TBD in the manifests. Open a PR or issue with the canonical URL + how you'd like to be credited.
2. **Anything I got wrong** about the architecture, the SQLite schema, or the pattern attribution.
3. **Whether you want to be a co-author on the spec** - `docs/spec/HARNESS_HUB_SPEC.md` is intentionally co-authorable. If CiteMind's "every answer cites a page" discipline belongs in the spec as a UX requirement (it should), I'd love your wording.
4. **Education partnerships** - if your conversations with universities or libraries would benefit from the broader catalog framing as a shared registry of pipelines + patterns, I'd love to support that.

**Concrete next step**

If any of this is helpful, the lowest-friction follow-up is opening an issue or PR on [taylor-s-amarel/open-harness-hub](https://github.com/taylor-s-amarel/open-harness-hub) - even a one-line "the integration looks accurate, here is our repo URL" is useful.

If you'd rather chat, I'm at amarel.taylor.s@gmail.com.

Either way: thank you for building CiteMind. The architecture is small enough to understand in one read + sharp enough to be unambiguous evidence that local-first, source-grounded, persistent learning layers are a real category - not a stunt. That belongs in the catalog with your team's name on it.

- Taylor
