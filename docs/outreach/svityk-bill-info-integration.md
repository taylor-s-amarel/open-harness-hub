# Outreach draft — Sviatoslav Grabovsky (Bill_info AI integration)

Sviatoslav,

I'm Taylor Amarel — I run [github.com/taylor-s-amarel/open-harness-hub](https://github.com/taylor-s-amarel/open-harness-hub), an MIT-licensed catalog of harnesses + pipelines + design patterns + rule packs for AI engineering. Your Bill_info AI submission for the Gemma 4 Good Hackathon landed in front of me at the perfect moment and the architecture maps almost 1:1 into the catalog's vocabulary. I integrated it as a first-class reference vertical and three reusable design patterns, all with attribution to you + your HF Space + the repo.

**Where it lives**

- Use-case doc: [`docs/use-cases/refugee-bureaucracy-translation.md`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/docs/use-cases/refugee-bureaucracy-translation.md)
- Pipeline manifest: [`catalog/pipelines/bureaucracy-translation/bill-info-extract-fraud-detect-recommend.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/pipelines/bureaucracy-translation/bill-info-extract-fraud-detect-recommend.yaml)
- Knowledge pack (Verbraucherzentrale 10-indicator taxonomy): [`catalog/knowledge-packs/verbraucherzentrale-fake-inkasso-indicators.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/knowledge-packs/verbraucherzentrale-fake-inkasso-indicators.yaml)
- Rule pack (11 GREP detectors): [`catalog/rule-packs/grep/fake-inkasso-fraud-flags.yaml`](https://github.com/taylor-s-amarel/open-harness-hub/blob/main/catalog/rule-packs/grep/fake-inkasso-fraud-flags.yaml)
- Persona, rubric, dataset, Gemma 4 26B adapter — all linked + attributed.

**Three design patterns I extracted from your work** (because they generalize beyond Bill_info AI):

1. **`pattern/two-stage-extract-then-judge`** — first call extracts every relevant field; second call judges/classifies given that context. You wrote it well: *"focused criteria do not compete with extraction for the model's attention."* Retroactively also applies to ~10 other pipelines in the catalog (supplier policy grading, radiology report grading, contract clause review).

2. **`pattern/critical-tier-output-override`** — on `likely_scam`, every UI component is FORCED into one consistent anti-scam message rather than letting the model mix "pay if correct" + "might be a scam" in a single response. This is the specific architectural safety property your writeup calls out, and it generalizes (CBP-WRO halts in ESG, PHI-unredacted halts in radiology, ITAR-technical-data halts in trade).

3. **`pattern/refuse-on-redacted`** — null over hallucination on missing/redacted fields, UI renders as user-language "unknown" not "0" or "". Your 100% refusal accuracy on 7 redacted documents is the published baseline.

All three pattern manifests cite you as primary author, link to your HF Space + GitHub repo, and include the eval metrics from your writeup (96% extraction / 95.8% field accuracy / 100% redacted refusal / 8.5s latency).

**Why I think this matters for your project**

1. **Visibility**: the catalog is intentionally a discovery surface — anyone running `oh-hub search verbraucherzentrale` or `oh-hub describe pipeline/bill-info-extract-fraud-detect-recommend` lands on your work. There's a peer-registry comparison doc (`docs/comparison/peer-registries.md`) framing the hub as Docker-Hub-for-harnesses, which is exactly Hassan Gasim's framing on the related thread.

2. **NGO path**: your roadmap explicitly targets Caritas / Diakonie / Verbraucherzentrale. The catalog already has the standards-format emitters (Croissant / MCP / Agent Skills / HF cards) so any NGO that adopts your pipeline gets the publication formats for free + a fork point for their jurisdiction (e.g. CFPB for US, ACCC for AU).

3. **The three design patterns travel**: developers will hit your patterns through other verticals (radiology, contract review, etc.) and the Bill_info AI attribution travels with them. Every one of the 24 industry-grading verticals in the catalog now has a "you-might-want-the-Bill_info-patterns" path.

**What I'd love your input on**

1. **Anything I got wrong** about the pipeline shape, the 10 Verbraucherzentrale indicators, or the eval methodology. The catalog is plain YAML in git — open a PR or issue with corrections.

2. **Whether the three-pattern attribution is the right framing**. I lead with the patterns because they're reusable, but you might prefer the pipeline-as-primary framing. Either way — your call.

3. **NGO partnerships**: I have no formal NGO contacts in the Verbraucherzentrale ecosystem; if your conversations with Caritas / Diakonie / VZ would benefit from the broader catalog framing as a vehicle for cross-org-anonymized sharing of fake-Inkasso patterns (similar to FATF Rec. 18 information sharing — there's a `pattern/k-anonymity-aggregation` artifact in the catalog already), I'd love to support that.

4. **Co-author the spec**: `docs/spec/HARNESS_HUB_SPEC.md` is intentionally co-authorable. If Bill_info AI's "ten seconds of attention" design philosophy belongs in the spec as a UX principle (it should), I'd love your wording.

**Concrete next step**

If any of this is helpful, the lowest-friction follow-up is opening an issue or PR on [taylor-s-amarel/open-harness-hub](https://github.com/taylor-s-amarel/open-harness-hub) — even a one-line "the integration looks accurate, you can refer to this in the README" is useful.

If you'd rather chat, I'm at amarel.taylor.s@gmail.com.

Either way: thank you for shipping Bill_info AI publicly under Apache 2.0. The architecture is small enough to understand in one read + sharp enough to be unambiguous evidence that the cite-first + critical-override + refuse-on-redacted patterns produce safer outputs for vulnerable users than general-purpose chat. That belongs in the catalog with your name on it.

— Taylor
