# Use case: ESG / Supply-Chain Due Diligence (CSDDD-aligned)

## What this answers

> "We need to audit our deep-tier supplier networks (tier 3 and tier
> 4+) for forced labor and grade supplier-submitted policies against
> the EU CSDDD, ILO indicators, and our own code of conduct — without
> hiring 100 more ESG analysts."

## Catalog ingredients

| Layer | Artifact | Role |
|---|---|---|
| Persona | `persona/esg-auditor` | Structured, citation-first ESG auditor system prompt |
| GREP rule pack | `rule-pack/grep-esg-forced-labor-red-flags` | First-pass detector for 13 red-flag categories incl. ILO indicators 1-11 + corridor flags |
| RAG knowledge pack | `knowledge-pack/csddd-and-forced-labor-indicators` | Citation backbone: CSDDD articles, ILO indicators, Modern Slavery Act §54, LkSG, SB 657 |
| PII redaction | `rule-pack/privacy-pii-text-en` + `processor/redact-pii-text` | Strips worker grievance transcript PII before LLM call |
| Judge rubric | `rubric/esg-supplier-compliance-v1` | 7-dimension grading rubric |
| Grading pipeline | `pipeline/supplier-policy-grading` | Persona → PII redact → GREP → RAG (CSDDD + lead code) → judge → propose remediation |
| Multi-tier audit | `pipeline/deep-tier-supplier-audit` | Walks T1 → T4+ with `processor/iterative-revise-loop`; escalates high-severity |
| Cross-org sharing | `pipeline/anonymized-illicit-recruitment-pattern-sharing` | k-anonymity gate before hub-sharing systemic broker / corridor patterns |

## End-to-end flow

```
[Supplier disclosure pack]
        │
        ▼ rule-pack/privacy-pii-text-en + processor/redact-pii-text
[PII-redacted text]
        │
        ▼ rule-pack/grep-esg-forced-labor-red-flags
[Red-flag hits with severity + category]
        │
        ▼ rule-pack/hybrid-retrieval-policy → knowledge-pack/csddd-and-forced-labor-indicators
[ILO + CSDDD + national-code citations]
        │
        ▼ rule-pack/hybrid-retrieval-policy → lead-company code of conduct
[Lead-code citations]
        │
        ▼ processor/llm-judge + rubric/esg-supplier-compliance-v1
[Structured findings: severity, indicator, evidence, tier, remediation]
        │
        ▼ harness/text-safety-review (with persona/esg-auditor)
[CSDDD Art. 10 remediation proposal: corrective action, supplier right of reply, 60-day milestone]
        │
        ▼ processor/audit-trace-emitter
[Audit trace for board oversight per CSDDD Art. 26]
```

## How tier 3 / tier 4+ traversal works

`pipeline/deep-tier-supplier-audit` uses `processor/iterative-revise-loop`
as the outer agent:

1. **Iter 1**: Resolve T1 supplier → grade T1 → expand T1's known T2 set.
2. **Iter 2**: For each T2, grade → expand T3 set.
3. **Iter N**: Grade T(N-1) → expand T(N) set. **Surface audit_gaps**
   when a tier cannot be resolved (typical at T ≥ 3 — most factories
   in Asia subcontract through informal labor agencies whose books
   don't surface in the lead supplier registry).
4. **Termination**: max_depth reached OR every leaf resolved.
5. **Aggregation**: `processor/multi-vector-fusion` rolls up per-tier
   findings into a chain-wide compliance report.
6. **Escalation**: `processor/escalate-human-review` routes any
   high-severity finding to the compliance team.

## Cross-organization knowledge sharing (without breaching confidentiality)

`pipeline/anonymized-illicit-recruitment-pattern-sharing` implements a
k-anonymity + HMAC scheme:

1. Each org's findings → `processor/redact-pii-text` (worker names
   stripped).
2. Broker IDs → HMACed with hub-published salt (so same broker
   produces same hash everywhere, but the hash is not invertible).
3. Bucketed by `(broker_hash, corridor, indicator_category,
   90-day-window)`.
4. Buckets with `count < k` (default k = 5) are dropped — small
   buckets could be re-identified back to the source org.
5. Surviving buckets are signed and published.
6. Member orgs query: "have these indicators been seen against this
   broker / corridor?" → returns aggregate count + severity, never
   per-org provenance.

Inspired by FATF Recommendation 18 info-sharing principles, adapted
to the ESG / forced-labor context. The k threshold is a tunable
trade-off: higher k = stronger anonymity, weaker signal; lower k =
faster pattern surfacing, more re-identification risk.

## What this is NOT

- A legal opinion. Real CSDDD compliance requires jurisdiction-
  specific legal sign-off, BSA-officer-equivalent review, and CSDDD
  Art. 26 board-level oversight.
- A determination of forced labor. The pipeline produces RISK FLAGS
  with citations. The lead company's compliance officer makes the
  determination after the supplier's right of reply (CSDDD Art. 10).
- A substitute for on-the-ground audits at high-risk tiers — those
  remain mandatory under CSDDD risk-based due diligence.

## Reference for proposers of this use case

Catalog: `github.com/taylor-s-amarel/open-harness-hub`. All artifacts
listed above validate against `schemas/` and emit to 13 standards
formats (Croissant, MCP, Agent Skills, HF cards, lm-eval-harness,
promptfoo, CycloneDX-ML, OpenLineage, C2PA, EU AI Act, SPDX 3.0,
JSON-LD, DPV).

The CSDDD-aligned pack is `lifecycle: experimental` — feedback
welcome on indicator coverage, multi-lingual GREP patterns, and the
k-anonymity threshold default.
