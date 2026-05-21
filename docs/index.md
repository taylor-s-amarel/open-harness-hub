# Open Harness Hub — single-page catalog index

Auto-generated from `scripts/build_index_page.py` against 223 live artifacts. Run that script to refresh after any catalog change.

Use `python scripts/oh_hub.py describe <id>` for the full manifest + dependency tree of any entry below.

## Stats

- **Total artifacts:** 223
- **Artifact types:** 12
- **Industries:** 38

## Table of contents

- [harness (9)](#harness)
- [pipeline (44)](#pipeline)
- [benchmark (1)](#benchmark)
- [rule-pack (24)](#rule-pack)
- [knowledge-pack (22)](#knowledge-pack)
- [tool (7)](#tool)
- [persona (17)](#persona)
- [adapter (9)](#adapter)
- [rubric (15)](#rubric)
- [dataset (7)](#dataset)
- [processor (45)](#processor)
- [pattern (23)](#pattern)

## harness

- **`harness/aml-investigation`** — AML Investigation  
  _finance, finance.aml_ • Harness for AML suspicious-transaction review. Composes the AML-analyst persona, sanctions-screening heuristic, FATF-typology classifier, financial-PII privacy gate, FATF-typology …
- **`harness/appsec-code-audit`** — AppSec Code Audit harness  
  _security, security.appsec, software_ • CWE-cite-first AppSec audit harness for source-code review. Detects secrets-in-code + injection + crypto/auth weaknesses + describes attack vectors + proposes fixes.
- **`harness/clinical-decision-support`** — Clinical Decision Support  
  _healthcare, healthcare.clinical_ • Healthcare-specific harness for differential-diagnosis reasoning. Composes the clinical-reasoner persona, red-flag classifier rules, HIPAA PHI privacy gate, clinical-guideline RAG,…
- **`harness/code-act-jupyter`** — Code-Act Jupyter (tool-augmented reasoning via sandboxed Python)  
  _ai, scientific_research, education_ • Harness that wraps a model call with a Python execution loop. The model emits `<code>...</code>` blocks; the harness runs them in a sandboxed Jupyter kernel; stdout / stderr / repr…
- **`harness/contract-redline`** — Contract Clause Redlining harness  
  _legal, legal.contract, legal.compliance_ • Playbook-cite-first harness for commercial contract review. Surfaces red-flag clauses + proposes concrete redline language + cites the playbook clause family for every finding.
- **`harness/esg-disclosure-grading`** — ESG Disclosure Grading harness  
  _esg, supply_chain, compliance_ • Wraps the ESG supplier-policy-grading flow as a reusable harness with persona + GREP + RAG + tools layers. Targets local-Ollama or Anthropic/OpenAI for the judge model arm; emits c…
- **`harness/radiology-report-review`** — Radiology Report Review harness  
  _healthcare, healthcare.radiology_ • RADS-aware + Fleischner-aware harness for grading radiology reports with HIPAA-safe PHI redaction. Wraps `pipeline/radiology-report- grading` with reusable layers.
- **`harness/redact-pii-text`** — Redact PII (text)  
  _cross_industry_ • Deterministic text PII redactor. Regex + NER patterns + a per-pattern replacement contract; emits an audit log of (sha256(original), action). No model call by default.
- **`harness/text-safety-review`** — Text Safety Review  
  _cross_industry_ • A general-purpose text harness that composes persona + GREP + RAG + tools + (optional) online grounding around a model call. Designed to produce cited, bounded, citation-first resp…

## pipeline

- **`pipeline/anonymized-illicit-recruitment-pattern-sharing`** — Anonymized cross-org pattern sharing for illicit recruitment corridors  
  _esg, supply_chain, compliance_ • Mechanism for cross-industry knowledge sharing of systemic bad actors (rogue labor brokers, repeat-offender contractors, illicit recruitment corridors) WITHOUT leaking corporate-co…
- **`pipeline/awq-quantized-inference`** — AWQ-quantized LLM inference (alternative to bitsandbytes nf4)  
  _ai_ • Serve a 4-bit AWQ (Activation-aware Weight Quantization) checkpoint for inference. AWQ preserves activation statistics, generally delivering lower perplexity drop than naive nf4. T…
- **`pipeline/brand-safe-product-photo`** — Brand-Safe Product Photo  
  _creative, retail_ • Image-generation pipeline that composes a cinematic-photography persona, style-reference RAG, lens-physics RAG, GREP guard rules, a tool call to a text-to-image model, and an outpu…
- **`pipeline/chat-with-pdf-citations`** — Chat with PDF (with citations)  
  _cross_industry_ • The canonical "upload a PDF, ask questions, get cited answers" pipeline used by vercel/ai-chatbot, lobe-chat, codertom/chat-with-pdf, etc. Full layered chain:   pdf-to-text →   rec…
- **`pipeline/climate-disclosure-review`** — Climate disclosure review (TCFD + ISSB IFRS S2 + ESRS E1)  
  _climate, esg, finance, compliance_ • Grade a corporate climate disclosure against the rubric. Sixth vertical proving the architecture's industry-agnosticism. Same 6-step chain: prose → PII redact → GREP → RAG → judge …
- **`pipeline/code-act-jupyter-loop`** — Code-act Jupyter loop  
  _ai, software_ • The OpenInterpreter pattern: model emits Python code in fenced blocks, runtime renders the message + executes the code in a Jupyter kernel, streams the observation back into the mo…
- **`pipeline/code-review-with-risk-score`** — Code review with risk score  
  _software, software.codereview, security_ • Full layered code-review pipeline. Composes:   persona (senior engineer) →   grep (secret-leak guards on the diff) →   classifier (clinical-style red-flag screen for OWASP categori…
- **`pipeline/code-security-review`** — Code security review (CWE-cite-first AppSec audit)  
  _security, security.appsec, software, software.codereview_ • Review source code against `rubric/code-security-review-v1`. Uses the SAME chain shape as ESG / radiology / contract review: structured-to-prose → secrets-redact → GREP (vuln + sec…
- **`pipeline/contract-clause-review`** — Commercial contract clause review (cite-first redlining)  
  _legal, legal.contract, legal.compliance_ • Review a commercial contract against `rubric/contract-review-quality- v1`. Reuses the SAME primitives as the ESG + radiology grading pipelines: structured-to-prose → PII redact → G…
- **`pipeline/deep-research-supervisor-workers`** — Deep research: supervisor + parallel workers  
  _ai, media, cross_industry_ • LangChain's open_deep_research pattern. A supervisor LLM decomposes the user query into research briefs and dispatches N parallel researcher subagents (each gets its own context + …
- **`pipeline/deep-research-with-citations`** — Deep research with citations  
  _cross_industry, media_ • The "deep research" pattern popularized by Perplexity and the Anthropic orchestrator-workers cookbook. Fully layered:   redact (PII out before external search) →   persona (researc…
- **`pipeline/deep-tier-supplier-audit`** — Deep-tier (T1→T4+) supplier audit with traceability  
  _esg, supply_chain, compliance_ • Multi-step audit pipeline that walks a supplier graph from tier-1 (direct supplier) down to tier-3 and tier-4+ (raw-material origin / sub-sub-contractors). At each tier:  1. Resolv…
- **`pipeline/deepseek-r1-code-interpreter-math`** — DeepSeek-R1 / QwQ + Python code-interpreter for math reasoning  
  _ai, scientific_research, education_ • The winning AIMO-2 shape: a reasoning-distilled LLM (DeepSeek-R1- Distill-Qwen-7B / QwQ-32B) generates Python code that solves a math problem, the code runs in a Jupyter / sandbox …
- **`pipeline/differential-diagnosis`** — Differential Diagnosis  
  _healthcare, healthcare.clinical_ • Educational decision-support pipeline. Given (presentation, history, exam) text, returns a ranked differential diagnosis with cited guideline sections, ICD-10 code candidates, and …
- **`pipeline/email-triage-and-draft`** — Email triage + reply draft  
  _retail, retail.support, cross_industry_ • Customer-support email workflow. Layered chain:   redact PII →   grep (prompt-injection guard on email body — emails often carry attack     content from untrusted senders) →   clas…
- **`pipeline/everything-research-pipeline`** — Everything research pipeline (kitchen-sink, 22 passes)  
  _cross_industry_ • A comprehensive research pipeline that demonstrates every layer the hub supports — 22 distinct passes from raw input through model call through iterative refinement to delivery.
- **`pipeline/full-vendor-due-diligence`** — Full vendor due-diligence (ESG + AppSec + Legal — kitchen-sink)  
  _cross_industry, compliance, supply_chain, security_ • Cross-vertical kitchen-sink pipeline. Accepts a vendor onboarding packet containing (a) ESG/supply-chain disclosure, (b) representative code bundle, (c) draft MSA, and runs each th…
- **`pipeline/gxp-validation-review`** — GxP validation review (21-CFR-11 + Annex 11 + ALCOA+)  
  _pharma, pharma.gxp, compliance_ • Review a GxP-validated electronic-records system against the rubric. Same 6-step chain as ESG / radiology / legal / AppSec — fifth vertical proving the architecture's industry-agno…
- **`pipeline/knowledge-graph-from-corpus`** — GraphRAG: knowledge-graph from corpus + global/local query  
  _ai, cross_industry_ • Microsoft GraphRAG pattern. Extract entities + relationships from documents into a graph; build community summaries via Leiden clustering; query via local (ego-network), global (ma…
- **`pipeline/large-model-faiss-rag`** — Large-model FAISS RAG (Platypus2-70b style)  
  _ai, scientific_research, education_ • Use a large (70B-class) instruction-tuned model with FAISS-indexed Wikipedia retrieval. The "go big or go home" Kaggle pattern that wins multi-choice-with-context competitions.
- **`pipeline/llm-judge-essay-grading`** — LLM-judge essay grading (with adversarial prompt prefix)  
  _ai, education_ • Run a frontier LLM as judge on candidate essays, using a few-shot prompt with adversarial prefix patterns to discourage gaming. The "you can't please them all" pattern: grade stric…
- **`pipeline/mixed-criteria-demo`** — Mixed success-criteria demo (regex + semantic + deterministic + LLM + composite)  
  _cross_industry, compliance, legal_ • Demonstrates `pattern/composable-success-criteria`. The pipeline runs the contract-clause-review chain, then evaluates its output against EVERY criterion kind:
- **`pipeline/multi-agent-debate-with-judge`** — Multi-agent debate with judge  
  _ai_ • Two or more debater personas argue different sides of a question across N rounds. A judge persona scores the final positions. Used for hard reasoning tasks where stress-testing imp…
- **`pipeline/multi-doc-qa-subquestion`** — Multi-document QA with sub-question decomposition  
  _cross_industry_ • LlamaIndex's SubQuestionQueryEngine pattern in pipeline form. The user asks a compound question; an LLM decomposes it into sub-questions; each sub-question runs its own retrieval; …
- **`pipeline/multi-model-judging-ensemble`** — Multi-model judging ensemble  
  _ai_ • Run inference across N different LLMs (e.g. Mixtral / Mistral-7B / Gemma-7B / Llama-3-8B), score each model's prediction with a perplexity baseline, then majority-vote or weighted-…
- **`pipeline/perplexity-baseline-scoring`** — Perplexity-baseline scoring  
  _ai_ • Score candidate answers by their perplexity under a reference LLM. Lower perplexity = better fit. Used as a baseline for prompt-recovery, AI-text-detection, and any task where "flu…
- **`pipeline/plan-execute-critic-loop`** — Plan / execute / critic loop  
  _cross_industry_ • The classic agentic pattern: planner LLM drafts a step list, executor runs the steps (with tool calls), critic LLM reviews the trace + re-plans on failure. Iterates until either th…
- **`pipeline/quantized-llm-inference`** — Quantized LLM inference (4-bit BitsAndBytes)  
  _ai, cross_industry_ • Inference-only path: load a 7-70B LLM with 4-bit BitsAndBytes quantization, run generation with controlled sampling kwargs and a chat template. The lightest production shape — no L…
- **`pipeline/qwen-vllm-rerank-eedi`** — Qwen-32B vLLM retrieval-rerank with logits-processor constraints  
  _ai, education_ • Two-stage retrieval pipeline that won EEDI Mining Misconceptions: 1. Embedding-based retrieve top-K candidate misconceptions 2. Constrain a Qwen-32B-AWQ vLLM call to emit ONLY one …
- **`pipeline/radiology-report-grading`** — Radiology report grading (RADS-aware, Fleischner-aware)  
  _healthcare, healthcare.radiology_ • Grade a radiology report against `rubric/radiology-report-quality- v1`. The pipeline reuses the SAME primitives as the ESG grading pipeline:  1. `processor/structured-to-prose` — f…
- **`pipeline/research-entity`** — Research Entity  
  _cross_industry_ • Given an entity name + entity kind (company / person / place / product), produce a sourced one-page profile. Verifiable, cited, redacted.
- **`pipeline/security-incident-grading`** — Security incident write-up grading (CTI + AppSec chained)  
  _security, threat_intelligence, security.appsec_ • Chains threat-intel IOC review + AppSec code review on incident write-ups: extracts IOCs/TTPs from the report AND grades any attached code-of-concern for known vulnerabilities.
- **`pipeline/self-rag-grade-and-revise`** — Self-RAG: grade-and-revise (concrete implementation)  
  _ai, cross_industry_ • Concrete pipeline implementing `pattern/self-rag`. Retrieve → per-doc relevance grader → rewrite-query loop on irrelevant retrieval → generate with grounding → answer-support grade…
- **`pipeline/storm-persona-curation-article`** — STORM: persona-curation + outline-fanout article  
  _ai, media, education_ • Stanford OVAL's STORM pattern. Generate N personas with different perspectives → run simulated dialogue per persona to curate knowledge → outline → parallel-expand each outline sec…
- **`pipeline/supplier-policy-grading`** — Supplier policy & disclosure grading (CSDDD-aligned)  
  _esg, supply_chain, compliance_ • End-to-end pipeline for grading supplier-submitted policy texts and self-assessments against the EU CSDDD, ILO forced-labor indicators, and the lead company's code of conduct. The …
- **`pipeline/suspicious-transaction-review`** — Suspicious Transaction Review  
  _finance, finance.aml_ • Given a transaction bundle (account, recent transactions, related entities), produce a sanctions-first risk review, FATF typology scoring, and a SAR-style narrative DRAFT (never a …
- **`pipeline/sustainability-report-full-review`** — Sustainability report full review (Climate + ESG-S + ESG-G chained)  
  _climate, esg, compliance, finance_ • Chains 3 sub-pipelines for a comprehensive sustainability-report audit: climate-disclosure-review + (a subset of) supplier-policy- grading focused on social + (a subset of) governa…
- **`pipeline/swe-patch-sample-and-review`** — SWE-agent: sample N patches + reviewer judges  
  _ai, software, software.codereview_ • The princeton-nlp/SWE-agent pattern. Given a bug report + repo: sample N action-rollouts (each producing a candidate patch via file-edit + run- test loop), then a reviewer model ju…
- **`pipeline/synthetic-data-gen-with-teacher-llm`** — Synthetic-data generation with teacher LLM  
  _ai_ • Use a teacher LLM to generate (input, output) training pairs for a downstream student fine-tune. Includes filtering for diversity + difficulty + safety. The pattern that won the pr…
- **`pipeline/threat-intel-ioc-review`** — Threat-intel IOC + TTP review (MITRE ATT&CK aligned)  
  _security, threat_intelligence_ • Ingest a CTI report or incident write-up, extract IOCs + TTPs, validate against MITRE ATT&CK, rate confidence, surface attribution risk. Seventh vertical proving industry-agnostici…
- **`pipeline/twenty-questions-agent`** — 20-questions agent (Akinator-style)  
  _ai, education_ • An agent that plays 20 Questions — asks yes/no questions to narrow down a hidden concept. Uses a candidate set + binary-search-style question generation. The classic agent-game pat…
- **`pipeline/two-time-retrieve-rerank`** — Two-time retrieval + cross-encoder rerank  
  _ai, education, scientific_research_ • Generic two-pass retrieval pipeline distilled from the EEDI-AWQ shape. First-pass: retrieve top-K with the raw query. Refine the query using LLM summary of pass-1. Second-pass: ret…
- **`pipeline/verify-claim-against-corpus`** — Verify Claim Against Corpus  
  _cross_industry, media_ • Given a claim and a corpus, return supports / contradicts / no-evidence with cited passages and a confidence score.
- **`pipeline/vllm-batch-llm-inference`** — vLLM batch LLM inference (with logits-processor-zoo)  
  _ai, education_ • Serve many prompts through a single vLLM engine with shared KV cache + prefix caching. Optional logits-processor-zoo entries (SuppressTokens / AllowedTokens / FixedTokenBias) const…

## benchmark

- **`benchmark/esg-supplier-grading-bench`** — ESG supplier-grading benchmark v1  
  _esg, supply_chain, compliance_ • Runs `pipeline/supplier-policy-grading` against the synthetic supplier disclosure pack test set (3 representative cases: a well- disclosed T1 tech supplier; a T3 textile supplier i…

## rule-pack

- **`rule-pack/aml-typologies-fatf`** — FATF AML typologies (sampled)  
  _finance, finance.aml_ • Classifier rules for common FATF-aligned AML typologies. Each rule is a labeled-example bundle the AML harness uses to score a transaction sequence against known patterns (structur…
- **`rule-pack/clinical-red-flags`** — Clinical red flags  
  _healthcare, healthcare.clinical_ • A classifier rule pack of presenting-symptom patterns that require immediate clinical evaluation. Fires inside the clinical-decision- support harness BEFORE differential reasoning,…
- **`rule-pack/financial-pii-en`** — Financial PII (English)  
  _finance_ • Detection patterns for common financial PII in English transaction narratives and KYC documents — account numbers, IBANs, SWIFT/BIC, card PANs (Luhn-likely), SSN/TIN. Designed to g…
- **`rule-pack/grep-ai-vendor-keys`** — AI vendor API key detectors  
  _security, ai_ • Detection patterns for API keys issued by major LLM / AI vendors — Anthropic, OpenAI, Hugging Face, Cohere, Replicate, Mistral, Groq, Together, fal, Perplexity, Voyage, NVIDIA NIM.…
- **`rule-pack/grep-climate-disclosure-gaps`** — Climate disclosure gap detectors (TCFD / ISSB / ESRS E1)  
  _climate, esg, finance, compliance_ • GREP detectors for the highest-leverage climate-disclosure gaps: missing Scope-3 categories, missing transition plan, board- oversight silence, no 2C scenario analysis, no SBTi com…
- **`rule-pack/grep-cloud-secrets`** — Cloud provider secret detectors  
  _security, cross_industry, ai_ • Detection patterns for cloud-provider access keys and service-account credentials — AWS, GCP, Azure, DigitalOcean, OCI. Converged from gitleaks (`config/gitleaks.toml`), trufflehog…
- **`rule-pack/grep-code-vulnerabilities`** — Code vulnerability + secret-detection GREP pack  
  _security, security.appsec, software_ • GREP detectors for the highest-leverage source-code vulnerabilities + hardcoded secrets + dangerous-function calls. Pair with `pipeline/code-security-review`. Cite each rule with i…
- **`rule-pack/grep-contract-red-flags`** — Commercial contract red-flag detectors  
  _legal, legal.contract, legal.compliance_ • GREP detectors for the 10 highest-leverage contract red-flag patterns: uncapped indemnity, unlimited liability, pre-existing IP assignment, unilateral termination, asymmetric caps,…
- **`rule-pack/grep-esg-environmental-red-flags`** — ESG environmental red-flag detectors (the 'E' of ESG)  
  _esg, supply_chain, compliance, climate_ • GREP detectors for the environmental dimension of supplier disclosures: deforestation, water pollution, hazardous-waste mismanagement, GHG underreporting, biodiversity harm, illega…
- **`rule-pack/grep-esg-forced-labor-red-flags`** — ESG / forced-labor red-flag detectors (the 'S' of ESG)  
  _esg, supply_chain, compliance_ • Heuristic regex detectors for the 11 ILO forced-labor indicators + child labor + recruitment-fee abuse + tier-3/4 supply-chain transparency gaps + 12 high-risk corridors. Designed …
- **`rule-pack/grep-esg-governance-red-flags`** — ESG governance red-flag detectors (the 'G' of ESG)  
  _esg, compliance, finance_ • GREP detectors for the governance dimension: beneficial-ownership opacity, anti-bribery / corruption signals, whistleblower-channel weaknesses, conflict-of-interest, board-independ…
- **`rule-pack/grep-gxp-data-integrity-red-flags`** — GxP data-integrity red-flag detectors (21-CFR-11 / ALCOA+)  
  _pharma, pharma.gxp, compliance_ • GREP detectors for the highest-leverage 21-CFR-11 + ALCOA+ data- integrity violations: missing audit trails, shared accounts, post- hoc record alteration, validation gaps, missing …
- **`rule-pack/grep-ioc-extraction`** — IOC extraction GREP pack (file hashes / domains / IPs / URLs)  
  _security, threat_intelligence_ • Extracts indicators-of-compromise from threat-intel reports, incident write-ups, sandbox outputs. Output IOCs feed into `pipeline/threat-intel-ioc-review` for verification + ATT&CK…
- **`rule-pack/grep-output-safety-image`** — Image-output safety checks  
  _creative, media_ • Post-generation safety check pack for image outputs. Pairs of (detector-call, threshold) plus a watermark presence check. Designed to be called by an image-gen pipeline AFTER the t…
- **`rule-pack/grep-private-key-blocks`** — Private key block detectors  
  _security, cross_industry_ • Detection patterns for PEM-encoded private keys (RSA, EC, DSA, OpenSSH, PGP) and modern formats (Age, Sigstore). Any match is a critical-severity hit — full revocation + key rotati…
- **`rule-pack/grep-prohibited-terms`** — Prohibited Terms (image-gen guard rails)  
  _creative, media_ • GREP guard rail for image-generation pipelines. Blocks prompts that reference real celebrities by name, real trademarks, hate slurs, or explicit sexual content. Severity drives the…
- **`rule-pack/grep-prompt-injection-heuristics`** — Prompt-injection heuristic detectors  
  _security, ai, cross_industry_ • Heuristic regex patterns that flag likely prompt-injection attempts in input, retrieved documents, or tool results. Inspired by garak probe families (`promptinject`, `latentinjecti…
- **`rule-pack/grep-radiology-report-red-flags`** — Radiology report quality + incidental-findings red flags  
  _healthcare, healthcare.radiology_ • GREP detectors for radiology-report quality and incidental-finding follow-up gaps. Designed to be run AFTER `rule-pack/privacy-phi- hipaa-en` redaction. Pair with `pipeline/radiolo…
- **`rule-pack/grep-vcs-platform-pats`** — VCS platform PATs (GitHub, GitLab, Bitbucket, Atlassian)  
  _security, software_ • Detection patterns for Personal Access Tokens issued by code-hosting platforms. Each vendor uses a stable prefix (`ghp_`, `gho_`, `ghu_`, `ghs_`, `ghr_` for GitHub; `glpat-` for Gi…
- **`rule-pack/hybrid-retrieval-policy`** — Hybrid retrieval policy (BM25 + dense + RRF)  
  _cross_industry_ • A RAG retrieval policy pack: BM25 sparse + dense vector + Reciprocal Rank Fusion + optional cross-encoder reranking + 1-hop citation graph expansion. Pipelines and harnesses refere…
- **`rule-pack/phi-hipaa-en`** — PHI (HIPAA 18-identifier) — English text  
  _healthcare_ • Detection patterns for the 18 HIPAA "Safe Harbor" PHI identifiers in English text. Designed to feed `harness/redact-pii-text` and any downstream healthcare pipeline that needs a ha…
- **`rule-pack/privacy-pii-text-en`** — Privacy PII (English text)  
  _cross_industry_ • Baseline GREP rule pack for detecting common PII in English text. Emails, phone numbers, US SSN, passport numbers, IBANs, IPv4. Designed to feed `harness/redact-pii-text` and any d…
- **`rule-pack/sanctions-screening`** — Sanctions screening (deterministic)  
  _finance, finance.aml, finance.kyc_ • Heuristic rule pack for sanctions screening. Each rule is a condition that pairs a normalized entity name (or fuzzy match) with a sanctions list and a fuzz threshold. The harness p…
- **`rule-pack/web-search-allowlist-default`** — Web search allowlist (default)  
  _cross_industry_ • Default online-search rule pack. Allowlist of trusted public-source domains, per-source freshness windows, query sanitization rules, and a small blocklist of dangerous source patte…

## knowledge-pack

- **`knowledge-pack/aml-red-flags-extended`** — AML red flags (extended)  
  _finance, finance.aml, finance.kyc_ • Extended catalog of anti-money-laundering red flags drawn from FATF guidance, FinCEN advisories, and Wolfsberg principles. Complements `knowledge-pack/fatf-typologies-sample` with …
- **`knowledge-pack/climate-disclosure-frameworks`** — Climate disclosure frameworks (TCFD + ISSB IFRS S2 + CDP + ESRS E1)  
  _climate, esg, finance_ • Composite educational extracts of the major climate-disclosure frameworks:  - TCFD (Task Force on Climate-related Financial Disclosures)    recommendations across 4 pillars (Govern…
- **`knowledge-pack/clinical-guidelines-sample`** — Clinical guidelines (sample chunks)  
  _healthcare, healthcare.clinical_ • Sample chunks of clinical-guideline language for catalog-demo purposes. Each chunk has a stable section reference so a citation-first persona can cite by section. Use authoritative…
- **`knowledge-pack/common-abbreviations`** — Common abbreviations (cross-industry sample)  
  _cross_industry_ • Sampled abbreviations and acronyms across healthcare, finance, legal, security, and technology, with expansions and a context tag. Designed for the `expand.abbreviation` processor …
- **`knowledge-pack/common-personas-library`** — Common personas / system-prompt library  
  _cross_industry_ • Reusable persona / system-prompt fragments for common roles — research analyst, code reviewer, customer-support agent, technical writer, translator, tutor, summarizer, fact-checker…
- **`knowledge-pack/contract-law-clauses`** — Commercial contract clause library (composite educational)  
  _legal, legal.contract, legal.compliance_ • Composite, educational reference of common commercial contract clauses with: standard market language, common red-flag variants, why each red flag matters, and a suggested redline.…
- **`knowledge-pack/csddd-and-forced-labor-indicators`** — Global supply-chain due-diligence regulatory pack  
  _esg, supply_chain, compliance, cross_industry_ • Reference pack of (composite, educational) extracts from 12 jurisdictions + 4 international frameworks:
- **`knowledge-pack/drug-interactions-sample`** — Drug-drug interactions (sample, educational)  
  _healthcare, healthcare.pharmacy, healthcare.clinical_ • Composite paraphrases of well-known drug-drug interaction patterns for educational reference. NOT a substitute for an authoritative database (e.g. RxNorm + Lexicomp + Micromedex). …
- **`knowledge-pack/fatf-typologies-sample`** — FATF typologies (sample chunks)  
  _finance, finance.aml_ • Sample paraphrased typology chunks for catalog-demo purposes. Real deployments should ingest the latest FATF and FinCEN typology reports; this pack anchors the data shape and citat…
- **`knowledge-pack/gxp-21-cfr-11-guidelines`** — 21-CFR-11 + EU GMP Annex 11 + ICH + ALCOA+ regulatory pack  
  _pharma, pharma.gxp, healthcare.pharmacy, compliance_ • Composite educational extracts of GxP electronic-records / electronic-signatures / data-integrity guidance:  - US FDA 21 CFR Part 11 (Subpart B — Electronic Records;    Subpart C —…
- **`knowledge-pack/high-risk-corridors-and-sectors`** — High-risk corridors & sector-specific labor / environmental risks  
  _esg, supply_chain, compliance, humanitarian_ • Composite reference of high-risk geographic corridors and product sectors with documented patterns of forced labor, child labor, environmental harm, or governance opacity. Used by …
- **`knowledge-pack/icd10-sample`** — ICD-10 sample  
  _healthcare, healthcare.clinical_ • Sampled subset of ICD-10 diagnosis codes for catalog-demo purposes. Use the public, full ICD-10 release for any production deployment; this pack exists to anchor the data shape, no…
- **`knowledge-pack/iso-country-codes`** — ISO 3166 country codes (sample)  
  _cross_industry, finance, humanitarian_ • ISO 3166-1 alpha-2, alpha-3, numeric codes plus region and a coarse FATF risk hint. Useful for KYC, transaction-graph queries, and cross-border-flow analysis. Sample subset; full l…
- **`knowledge-pack/iso-currency-codes`** — ISO 4217 currency codes  
  _finance, cross_industry_ • ISO 4217 three-letter currency codes with name, numeric code, and minor-unit precision. Useful for finance pipelines that need to validate currency strings or normalize amounts. Sa…
- **`knowledge-pack/lead-company-code-stub`** — Lead-company code-of-conduct stub (placeholder)  
  _cross_industry, esg, supply_chain, compliance_ • Placeholder reference that ESG / vendor pipelines accept as the lead-company-specific code of conduct. Real instances would replace this with the deploying organization's actual co…
- **`knowledge-pack/lens-physics-primers`** — Lens physics primers  
  _creative_ • Short physical-prior descriptors for camera lens behavior. Used by image-gen prompt-shapers so prompts request physically plausible combinations of focal length, aperture, distance…
- **`knowledge-pack/mitre-attack-sample`** — MITRE ATT&CK techniques (sample)  
  _security_ • Sample of MITRE ATT&CK Enterprise tactics + techniques. Each row carries the technique ID, name, tactic, and a one-paragraph description. Use the canonical MITRE source at attack.m…
- **`knowledge-pack/owasp-top-10-llm`** — OWASP Top 10 for LLM Applications (2025)  
  _security, ai_ • OWASP Top 10 risks for LLM-based applications — prompt injection, insecure output handling, training-data poisoning, model DoS, supply chain, sensitive disclosure, plugin design, e…
- **`knowledge-pack/radiology-acrac-fleischner`** — ACR Appropriateness Criteria + Fleischner + ACR RADS rubrics  
  _healthcare, healthcare.radiology, healthcare.clinical_ • Composite, educational extracts of radiology citation backbone:
- **`knowledge-pack/sanctions-list-shape`** — Sanctions list (shape, with placeholder entries)  
  _finance, finance.aml, finance.kyc_ • Reference SHAPE for sanctions list integration. Real data must be pulled from OFAC, UN, EU, HMT, or the institution's licensed provider; this pack illustrates the row schema, not t…
- **`knowledge-pack/spdx-licenses-summary`** — SPDX licenses (summary)  
  _cross_industry, legal, software_ • Sampled summary of common SPDX licenses — permissive, copyleft, non-commercial, public-domain. For each: license_id, category, one-paragraph summary, redistribution-compatible flag…
- **`knowledge-pack/style-references-cinematic`** — Cinematic style references  
  _creative_ • Curated style descriptors for cinematic product / scene photography. Each entry is a textual descriptor of a style — lighting, color palette, composition, atmosphere — with attribu…

## tool

- **`tool/cbp-wro-lookup`** — US CBP Withhold Release Order + UFLPA Entity List lookup  
  _esg, supply_chain, compliance_ • Check a supplier name + geography against:  - US CBP Withhold Release Orders (active)  - US CBP Findings list (escalated WROs that became confirmed    forced-labor determinations) …
- **`tool/json-schema-validator`** — JSON Schema 2020-12 validator  
  _cross_industry_ • Validates a candidate JSON object against a JSON Schema 2020-12 document. Used by `processor/verify-tool-validate-criterion` to enforce structural acceptance bars on pipeline outpu…
- **`tool/lookup-icd10`** — ICD-10 lookup  
  _healthcare, healthcare.clinical_ • Lookup an ICD-10 diagnosis code by code or label substring. Returns code + label + category. Backend-agnostic; intended to bind to a local copy of the WHO ICD-10 release or to an i…
- **`tool/sanctions-check`** — Sanctions list check  
  _finance, finance.aml, finance.kyc_ • Check a normalized entity name against one or more sanctions lists (OFAC SDN, UN Consolidated, EU Consolidated, HMT, or institutional PEP). Returns matches above the configured fuz…
- **`tool/transaction-graph-query`** — Transaction graph query  
  _finance, finance.aml_ • Query a transaction-graph store for one-hop or multi-hop paths between accounts / entities. Used by AML harnesses to find shell layering, circular flows, and rapid-in-rapid-out pat…
- **`tool/txt2img-sdxl`** — Text-to-Image (SDXL)  
  _creative_ • Generic SDXL text-to-image tool. Backend-agnostic — implementations include local Diffusers, Replicate, Hugging Face Inference, fal.ai, Together, or a custom OpenAPI endpoint.
- **`tool/web-search`** — Web Search  
  _cross_industry_ • Generic web search tool. Backend-agnostic — implementations include Brave, Serper, DuckDuckGo, or a self-hosted SearXNG.

## persona

- **`persona/aml-analyst`** — AML Analyst  
  _finance, finance.aml_ • Anti-money-laundering analyst persona. Reasons about transaction patterns, FATF typologies, sanctions hits, and behavioral signals. Produces SAR-style narratives with cited typolog…
- **`persona/cinematic-product-photographer`** — Cinematic Product Photographer  
  _creative, retail_ • A persona for image-gen prompt-shaping. Writes prompts in the voice of a working commercial photographer: specific lens, lighting, aperture, color palette, composition. Refuses cel…
- **`persona/climate-risk-analyst`** — Climate Risk Analyst (TCFD / ISSB IFRS S2 / CDP)  
  _climate, esg, esg.csrd, finance_ • Climate-risk analyst persona for reviewing corporate climate disclosures under TCFD recommendations, ISSB IFRS S2 standard, CDP questionnaires, and the EU CSRD ESRS E1 standard. Ci…
- **`persona/clinical-reasoner`** — Clinical Reasoner  
  _healthcare, healthcare.clinical_ • A clinical-reasoning persona for decision-support assistants. Cites guideline sections, flags red-flag symptoms, distinguishes differential diagnoses, and refuses to give definitiv…
- **`persona/code-consultant`** — Code consultant  
  _software, software.codereview_ • Senior-engineer persona for code review and architecture discussion. Converged from the Anthropic prompt library "Code Consultant", awesome-chatgpt-prompts "Cyber Security Speciali…
- **`persona/contract-reviewer-cite-first`** — Contract Reviewer (citation-first, senior in-house counsel)  
  _legal, legal.contract, legal.compliance_ • Senior in-house counsel persona for reviewing commercial contracts: NDAs, MSAs, SOWs, vendor agreements, employment contracts, license agreements. Citation-first: every red-flag re…
- **`persona/esg-auditor`** — ESG / Supply Chain Due Diligence Auditor (E + S + G)  
  _esg, esg.csddd, esg.modern_slavery, esg.csrd_ • ESG auditor persona covering the full E + S + G dimensions of supply-chain due diligence. Aligned to:
- **`persona/fact-checker`** — Fact Checker  
  _cross_industry, media_ • A careful fact-checker persona. Reasons about claims, evidence, and the gap between them. Prefers primary sources and refuses to confirm controversial claims without independent co…
- **`persona/gxp-auditor`** — GxP Auditor (21-CFR-11 / EU GMP Annex 11 / ICH / ALCOA+)  
  _pharma, pharma.gxp, healthcare.pharmacy, compliance_ • Pharmaceutical/biotech GxP auditor reviewing electronic records, audit trails, and validated systems against 21-CFR-11, EU GMP Annex 11, ICH Q9/Q10, ALCOA+ data-integrity principle…
- **`persona/linux-terminal`** — Linux terminal  
  _cross_industry, software_ • The single most-cloned community persona — model behaves like a Linux terminal, returning only the would-be terminal output. Doubles as a deterministic-IO eval (the same command sh…
- **`persona/math-tutor`** — Math tutor  
  _education, education.tutoring_ • Patient math-tutor persona that uses Socratic prompts and step-by-step reasoning. Diagnoses what the student understands before introducing new material. Useful baseline for `pipel…
- **`persona/radiologist-cite-first`** — Radiologist (citation-first, specialty radiology)  
  _healthcare, healthcare.radiology_ • Specialization of `persona/clinical-reasoner` for radiology report generation and review. Citation-first: every BI-RADS / Fleischner / ACR Appropriateness Criteria assertion is gro…
- **`persona/research-analyst`** — Research Analyst  
  _cross_industry_ • A careful research analyst persona. Cites every claim, prefers primary sources, and refuses to fabricate when evidence is thin.
- **`persona/security-engineer-cite-first`** — Security Engineer (CWE-cite-first AppSec reviewer)  
  _security, security.appsec, software, software.codereview_ • AppSec reviewer persona for source-code review. Citation-first: every red-flag refers to a CWE (Common Weakness Enumeration) entry, OWASP Top 10 category, or the specific MITRE ATT…
- **`persona/support-agent`** — Customer support agent  
  _retail, retail.support, cross_industry_ • Customer-support agent persona. Acknowledges the user's situation, confirms the goal, proposes the next concrete step. Escalates to a human if the issue cannot be solved in two mes…
- **`persona/threat-intel-analyst`** — Threat Intelligence Analyst (MITRE ATT&CK + STIX/TAXII + IOC)  
  _security, threat_intelligence, threat_intelligence.ioc, threat_intelligence.ttp_ • CTI analyst persona for IOC verification, TTP mapping to MITRE ATT&CK techniques, and threat-actor attribution analysis. Citation-first: every assertion cites the ATT&CK technique …
- **`persona/translator-improver`** — Translator + improver  
  _cross_industry, creative_ • The second-most-cloned community persona. Translates input into fluent English (or any target language) AND improves the original for clarity, idiom, and register. Pairs naturally …

## adapter

- **`adapter/anthropic-claude-opus`** — Anthropic Claude Opus (deep-reasoning frontier-class)  
  _ai, cross_industry_ • Anthropic Claude Opus 4.x — deeper reasoning + 1M-context variant for tasks where Sonnet is bottlenecked by reasoning depth (long legal briefs, deep-tier supplier chain traversal, …
- **`adapter/anthropic-claude-sonnet`** — Anthropic Claude Sonnet (frontier-class chat + tool-use)  
  _ai, cross_industry_ • Frontier-class generation + tool-use adapter using Anthropic's Claude Sonnet (4.x family) via the official Anthropic API. Use as the strongest generation arm in benchmarks, the "fr…
- **`adapter/bge-embeddings-local`** — BGE embeddings (local)  
  _cross_industry, ai_ • Local BGE (BAAI General Embeddings) via sentence-transformers. The small variant is 384-dim and runs on CPU; the large variant is 1024-dim and benefits from GPU. Strong English + m…
- **`adapter/google-gemini`** — Google Gemini (multimodal frontier)  
  _ai, cross_industry_ • Google Gemini frontier-class adapter — strongest of the three big-three frontier vendors on multimodal (vision + audio + video) tasks. Use when the pipeline needs to process images…
- **`adapter/ollama-default`** — Ollama (local default)  
  _cross_industry_ • Default local-Ollama transport. Configured for `llama3.1:8b` at `http://localhost:11434`. Override by setting `OLLAMA_HOST` and `OLLAMA_MODEL` env vars at runtime.
- **`adapter/openai-embeddings`** — OpenAI embeddings (text-embedding-3-small/large)  
  _cross_industry, ai_ • OpenAI-compatible embeddings adapter. Defaults to text-embedding-3-small (1536-dim, $0.02 / 1M tokens). Set OPENAI_API_KEY at runtime. Works against the OpenAI API directly, Azure …
- **`adapter/openai-gpt-frontier`** — OpenAI frontier-class chat + tool-use  
  _ai, cross_industry_ • OpenAI's frontier-class chat + tool-use adapter, configured for the latest GPT model at instantiation time. Use as one of the frontier arms in cross-vendor benchmarks; useful when …
- **`adapter/sdxl-local`** — SDXL (local Diffusers)  
  _creative_ • Local SDXL via Hugging Face Diffusers. CUDA preferred; CPU falls back to long inference times. Used by `tool/txt2img-sdxl`.
- **`adapter/vllm-awq-local`** — Local vLLM engine with AWQ-quantized weights  
  _ai_ • Adapter for serving a local LLM via vLLM with AWQ (Activation-aware Weight Quantization) weights. Used in the Kaggle "EEDI" and "AIMO 2" competitions to fit Qwen-32B / DeepSeek-R1-…

## rubric

- **`rubric/aml-investigation-v1`** — AML investigation v1  
  _finance, finance.aml_ • Six-dimension rubric for AML-investigation outputs. Used by `pipeline/suspicious-transaction-review`.
- **`rubric/brand-safe-image-v1`** — Brand-safe image v1  
  _creative, retail_ • Five-dimension rubric for brand-safe image generation. Used by `pipeline/brand-safe-product-photo`.
- **`rubric/climate-disclosure-quality-v1`** — Climate disclosure quality v1 (TCFD/ISSB/ESRS aligned)  
  _climate, esg, finance, compliance_ • Ten-dimension rubric for grading a corporate climate disclosure against TCFD recommendations, ISSB IFRS S2 paragraphs, and ESRS E1 disclosure requirements.
- **`rubric/clinical-grounded-response-v1`** — Clinical grounded response v1  
  _healthcare, healthcare.clinical_ • Six-dimension rubric for clinical-decision-support outputs. Used by `pipeline/differential-diagnosis`.
- **`rubric/code-security-review-v1`** — Code security review v1  
  _security, security.appsec, software_ • Seven-dimension rubric for grading an AppSec code review.
- **`rubric/contract-review-quality-v1`** — Contract review quality v1  
  _legal, legal.contract, legal.compliance_ • Eight-dimension rubric for grading a commercial-contract review. Used by `pipeline/contract-clause-review`.
- **`rubric/esg-env-v1`** — ESG environmental (E) sub-rubric v1  
  _esg, supply_chain, compliance, climate_ • Five-dimension rubric for grading ONLY the environmental dimension of a supplier disclosure. Aligned to CSRD ESRS E1-E5, EUDR, and CSDDD Art. 13 (climate transition plan).
- **`rubric/esg-gov-v1`** — ESG governance (G) sub-rubric v1  
  _esg, compliance, finance_ • Six-dimension rubric for grading ONLY the governance dimension of a supplier disclosure. Aligned to OECD MNE Guidelines (Chapter II general policies + Chapter VII anti-bribery), UK…
- **`rubric/esg-social-v1`** — ESG social (S) sub-rubric v1  
  _esg, supply_chain, compliance, humanitarian_ • Six-dimension rubric for grading ONLY the social dimension of a supplier disclosure. Aligned to ILO 11 forced-labor indicators, CSRD ESRS S1 (own workforce) + S2 (value-chain worke…
- **`rubric/esg-supplier-compliance-v1`** — ESG supplier compliance v1 (full E + S + G)  
  _esg, supply_chain, compliance_ • Twelve-dimension rubric for grading supplier-submitted policy texts, self-assessments, and grievance transcripts against the CSDDD, the ILO forced-labor indicators, the major natio…
- **`rubric/gxp-validation-quality-v1`** — GxP validation review quality v1  
  _pharma, pharma.gxp, compliance_ • Eight-dimension rubric for grading a GxP system validation review. Used by `pipeline/gxp-validation-review`.
- **`rubric/radiology-report-quality-v1`** — Radiology report quality v1  
  _healthcare, healthcare.radiology_ • Seven-dimension rubric for grading a radiology report. Used by `pipeline/radiology-report-grading`.
- **`rubric/research-entity-v1`** — Research Entity v1  
  _cross_industry_ • Six-dimension rubric for entity research outputs. Used by `pipeline/research-entity` as its success criterion.
- **`rubric/threat-intel-quality-v1`** — Threat intelligence report quality v1  
  _security, threat_intelligence_ • Six-dimension rubric for grading a CTI report against the diamond-model + ATT&CK navigator + Admiralty-confidence scheme.
- **`rubric/verification-v1`** — Verification v1  
  _cross_industry, media_ • Four-dimension rubric for fact-verification outputs. Used by `pipeline/verify-claim-against-corpus`.

## dataset

- **`dataset/climate-disclosure-samples`** — Synthetic climate disclosure samples (2 cases)  
  _climate, esg, finance_ • Two synthetic corporate climate disclosures for testing `pipeline/climate-disclosure-review`:  - sample-disclosure-good.json — Acme Corp, manufacturing, board    oversight quarterl…
- **`dataset/code-review-samples`** — Synthetic code-review samples (3 cases)  
  _security, security.appsec, software_ • Three synthetic code bundles for testing `pipeline/code-security-review`. Fully synthetic — values that look like AWS keys / JWT / Slack tokens follow the format documented in AWS …
- **`dataset/contract-samples`** — Synthetic commercial contract samples (3 cases)  
  _legal, legal.contract, legal.compliance_ • Three synthetic commercial contracts for testing `pipeline/contract-clause-review`. Fully synthetic — no real contract data.
- **`dataset/gxp-validation-samples`** — Synthetic GxP validation samples (3 cases)  
  _pharma, pharma.gxp, healthcare.pharmacy, compliance_ • Three synthetic GxP-validated-system packets for testing `pipeline/gxp-validation-review`. Fully synthetic.
- **`dataset/radiology-report-samples`** — Synthetic radiology report samples (3 cases, fully synthetic)  
  _healthcare, healthcare.radiology_ • Three synthetic radiology reports for testing `pipeline/radiology-report-grading`. Fully synthetic — no real patient data.
- **`dataset/supplier-disclosure-pack-schema`** — Supplier disclosure pack schema (canonical input shape)  
  _esg, supply_chain, compliance_ • Canonical input shape that `pipeline/supplier-policy-grading` and `pipeline/deep-tier-supplier-audit` accept as the supplier disclosure pack. Records the JSON Schema of the supplie…
- **`dataset/threat-intel-samples`** — Synthetic threat-intelligence report samples  
  _security, threat_intelligence_ • Synthetic CTI report samples for testing `pipeline/threat-intel-ioc-review`. Includes IOCs (file hashes, IPs, domains, URLs, mutexes, CVEs, ATT&CK technique IDs, BTC addresses) dra…

## processor

- **`processor/action-sampler-multi-rollout`** — Action sampler — N parallel rollouts  
  _ai, software_ • Sample N independent action trajectories for an agent task; return the trajectories + final-state candidates for downstream judging. The N candidates can be reviewed by a separate …
- **`processor/audio-to-text-whisper`** — Audio to text (Whisper)  
  _cross_industry_ • Speech-to-text via a Whisper-family model. Returns transcript + per-segment timestamps + detected language. Wraps `openai-whisper`, `faster-whisper`, or `distil-whisper` based on t…
- **`processor/audit-trace-emitter`** — Audit trace emitter  
  _cross_industry_ • Emit a per-step audit trace including hashed input/output, model version, adapter, applied layers, latency, and cost. Writes to a configured sink (local JSONL, Loki, OpenTelemetry,…
- **`processor/citation-coverage`** — Citation coverage verifier  
  _cross_industry_ • Verify that every factual sentence in a response carries at least one citation marker (e.g. `[1]`, `[smith-2026]`). Returns coverage ratio and a list of uncited sentences for re-pr…
- **`processor/community-summary-mapreduce`** — Community-summary map-reduce (GraphRAG global)  
  _ai, cross_industry_ • Per-community map step (LLM summarizes each Leiden community), then reduce step combines partial answers across communities. The core primitive of GraphRAG's global-search mode.
- **`processor/context-window-packer`** — Context-window packer (Lost-in-the-middle aware)  
  _cross_industry_ • Reorganize retrieved chunks into the model's context window so the most important content lands at the BEGINNING and END of the window (Liu et al. 2023 "Lost in the Middle"). Also …
- **`processor/cost-ceiling-gate`** — Cost ceiling gate  
  _cross_industry_ • Reject a pipeline run if the predicted USD cost exceeds the budget configured for the calling pipeline / user. Uses token-count estimates + adapter pricing to predict cost.
- **`processor/cost-meter`** — Cost meter  
  _cross_industry_ • Emit per-call USD cost accounting given (adapter_ref, input_tokens, output_tokens, cached_tokens). Resolves the adapter's pricing card, multiplies, and writes a metering row to the…
- **`processor/cross-encoder-reranker`** — Cross-encoder reranker  
  _cross_industry, ai_ • Re-rank a list of retrieved candidates with a cross-encoder model (BAAI/bge-reranker-base, Cohere rerank-v3, or similar). Takes top-N candidates from a hybrid retriever and returns…
- **`processor/document-grader`** — Per-document relevance grader (Self-RAG)  
  _ai, cross_industry_ • Score each retrieved document for relevance to the user query. Emits per-doc grade ∈ {relevant, irrelevant, ambiguous} with a confidence score. Used by Self-RAG and CRAG to filter …
- **`processor/embedder-minilm`** — Text embedder (MiniLM-L6-v2)  
  _cross_industry_ • Generate 384-dimensional text embeddings using `sentence-transformers/all-MiniLM-L6-v2`. Suitable for catalog semantic search, RAG retrieval, and de-duplication. Replace with a hig…
- **`processor/escalate-human-review`** — Escalate to human reviewer  
  _cross_industry_ • Route an output (and its full trace + context) to a human reviewer queue. Used when a safety gate fires, a confidence threshold is not met, or a red-flag classifier triggers. Plugg…
- **`processor/hallucination-scorer`** — Hallucination scorer (SelfCheckGPT-style)  
  _cross_industry_ • Score per-sentence hallucination probability by sampling N alternative generations from the same model, then measuring semantic agreement between them. Sentences that vary widely a…
- **`processor/hyde-query-expander`** — HyDE query expander  
  _cross_industry_ • Hypothetical Document Embeddings (HyDE): generate a hypothetical *answer* to the user's query, then embed that hypothetical answer for retrieval instead of (or in addition to) the …
- **`processor/inject-datetime-locale`** — Inject datetime + locale into prompt  
  _cross_industry_ • Replace placeholders like `{{now}}`, `{{today}}`, `{{user_timezone}}`, `{{user_locale}}`, `{{user_currency}}` in the prompt template with the actual values at request time. Fixes t…
- **`processor/inject-output-schema`** — Inject output schema directive  
  _cross_industry, ai_ • Render a target JSON Schema (or Pydantic model) into the prompt as an instruction the model is asked to follow. Pairs with `processor/json-schema-repair` on the response side: if t…
- **`processor/intent-dispatcher`** — Intent dispatcher  
  _cross_industry_ • Classify an incoming message into one of N intents and route to the appropriate downstream pipeline. Backend can be a classifier rule pack, a small local model, or a keyword router…
- **`processor/iterative-revise-loop`** — Iterative revise loop  
  _cross_industry_ • The "send the response back to the LLM with accumulating context" primitive. Loops:   1. Run an inner harness call.   2. Run one or more verification processors on the response.   …
- **`processor/json-schema-repair`** — JSON Schema repair + validate  
  _cross_industry_ • Parse and repair JSON inside a model response, then validate against a JSON Schema. On failure, returns `valid: false` plus the schema errors so the upstream harness can re-prompt …
- **`processor/llm-judge`** — LLM-as-judge  
  _cross_industry_ • Generic LLM-as-judge wrapper. Given (candidate response, rubric, context), returns a per-dimension score with rationale and a weighted-sum overall score. Independent of the model u…
- **`processor/llmlingua-context-compressor`** — LLMLingua context compressor  
  _cross_industry_ • Compress long context (retrieved RAG chunks or prior conversation turns) by selectively pruning low-information tokens before the model sees them. Implementations include LLMLingua…
- **`processor/memory-conversational-store`** — Conversational memory store  
  _cross_industry_ • Read / write conversational memory keyed by (user_id, session_id). Stores the last N turns plus a compressed summary for older turns. Pluggable backend: SQLite (default), Redis, Po…
- **`processor/multi-vector-fusion`** — Multi-vector / multi-query fusion (RRF + weighted)  
  _ai, cross_industry_ • Fuse N ranked candidate lists from independent retrievers (sparse + dense + graph + cross-encoder reranker output) via Reciprocal Rank Fusion or weighted score blending. Returns a …
- **`processor/nsfw-image-classifier`** — NSFW image classifier  
  _creative, media_ • Lightweight NSFW image classifier (CLIP-based zero-shot or a fine-tuned head). Returns probability of NSFW content; pipelines bind to a threshold via the calling rule pack.
- **`processor/official-sources-checker`** — Official-sources analyzer  
  _cross_industry, media, government, healthcare_ • Verify retrieved candidates against an allowlist of authoritative sources (gov, intergovernmental, academic, standards bodies). Returns per-candidate flags:   - is_official: bool  …
- **`processor/pdf-to-text`** — PDF to text  
  _cross_industry_ • Convert a PDF (extractable layer + optional OCR fallback) into plain text with page breaks preserved. Returns text plus per-page byte offsets so downstream chunkers can attribute c…
- **`processor/persona-set-generator`** — Persona-set generator (STORM)  
  _ai, media, education_ • Spawn N personas with distinct perspectives on a topic. Used by STORM's multi-perspective curation and by multi-agent debate pipelines. Each persona carries a role, an angle, prior…
- **`processor/prompt-injection-detector`** — Prompt-injection detector  
  _cross_industry, security_ • Detect prompt-injection / jailbreak attempts in user input, retrieved documents, or tool results. Two-tier: a fast regex / classifier first pass plus an optional small-model classi…
- **`processor/reasoning-framework-selector`** — Reasoning framework selector  
  _cross_industry, ai_ • Pick a reasoning framework (CoT / ReAct / Tree-of-Thoughts / Skeleton-of-Thought / Program-of-Thought / Self-Consistency / none) based on the task profile. Cheap heuristic up front…
- **`processor/recursive-character-chunker`** — Recursive character chunker  
  _cross_industry_ • Split text into chunks using a recursive character splitter (LangChain-style) that prefers paragraph → sentence → word boundaries. Returns chunks with overlap + per-chunk byte offs…
- **`processor/redact-pii-text`** — Redact PII from text (English-centric, MS Presidio-compatible)  
  _cross_industry, healthcare, finance, esg_ • Strip PII from free-form text before downstream LLM calls or hub sharing. Detects: email, phone, IBAN, SSN, passport, national-ID, full names (NER), street addresses, dates of birt…
- **`processor/runtime-tool-selector`** — Runtime tool selector (Toolformer / pydantic-ai)  
  _ai, cross_industry_ • Given a user query + a large registry of tools, semantically select the top-K most likely-relevant tools to expose to the model. Avoids overflowing the context window with every to…
- **`processor/self-consistency-sampler`** — Self-consistency sampler  
  _cross_industry_ • Run N parallel samples of a chain-of-thought reasoning prompt, then majority-vote on the final answer (Wang et al. 2023). Robust to arithmetic and reasoning errors that a single sa…
- **`processor/self-refine-critique`** — Self-Refine critique loop  
  _cross_industry_ • Critique-and-revise loop (Madaan et al. 2023). The same model first drafts an answer, then critiques its own draft against a rubric, then revises. Iterates up to `max_iterations`. …
- **`processor/skeleton-outliner`** — Skeleton outliner (Skeleton-of-Thought)  
  _ai, media, education_ • Generate a skeleton (bullet outline) for a long-form output, then return the outline so parallel sub-expansion can fan out per bullet. Used by Skeleton-of-Thought, STORM, and any p…
- **`processor/structured-to-prose`** — Structured JSON → prose normalizer (for GREP-style rule packs)  
  _esg, supply_chain, compliance, cross_industry_ • Walk a JSON object and emit one prose-like line per leaf value, flattening dict keys into space-separated labels. The output shape is what GREP-family rule packs (regex on natural-…
- **`processor/sub-question-decomposer`** — Sub-question decomposer  
  _cross_industry_ • Break a compound question into N atomic sub-questions, each independently answerable. Used by `pipeline/multi-doc-qa-subquestion` and similar LlamaIndex SubQuestionQueryEngine flow…
- **`processor/two-time-retrieval`** — Two-time retrieval (refine query, re-retrieve)  
  _ai, education_ • Retrieve top-K with the raw query, ask an LLM to compose a refined query incorporating what was found, then re-retrieve. Final retrieval set is the second pass (or union of both, d…
- **`processor/verify-composite-criterion`** — Composite (AND/OR/NOT) success-criterion evaluator  
  _cross_industry_ • Evaluates one `kind: composite` success criterion. Combines child criteria with AND / OR / NOT semantics. Children may themselves be composite — arbitrarily deep nesting allowed. S…
- **`processor/verify-deterministic-criterion`** — Deterministic comparison success-criterion evaluator  
  _cross_industry_ • Evaluates one `kind: deterministic` success criterion. Resolves a target value from the pipeline trace and applies a comparison operator (>, >=, <, <=, ==, !=, in, not_in, is_truth…
- **`processor/verify-llm-judge-criterion`** — LLM-as-judge success-criterion evaluator  
  _cross_industry_ • Evaluates one `kind: llm_judge` success criterion. Wraps `processor/llm-judge` but with an explicit pass/fail threshold and a clear criterion label. The judge adapter is configurab…
- **`processor/verify-regex-criterion`** — Regex success-criterion evaluator  
  _cross_industry_ • Evaluates one `kind: regex` success criterion. Given a target path (resolved from the pipeline trace) + a pattern + a `must_match` flag, returns a pass/fail record with the matched…
- **`processor/verify-semantic-criterion`** — Semantic-similarity success-criterion evaluator  
  _cross_industry_ • Evaluates one `kind: semantic` success criterion. Computes embedding similarity between the target text and each reference topic in `must_cover`; passes if EVERY topic clears `simi…
- **`processor/verify-tool-validate-criterion`** — Tool-validation success-criterion evaluator  
  _cross_industry_ • Evaluates one `kind: tool_validate` success criterion. Invokes an external tool (e.g. `tool/json-schema-validator`, `tool/run-unit-tests`, `tool/iban-checker`) against the target. …
- **`processor/vllm-batched-sampling`** — vLLM batched sampling (SamplingParams + logits processors)  
  _ai_ • Issue an LLM batch through vLLM's `LLM.generate` (or `llm.chat`) with `SamplingParams`. Optional `logits_processors` (e.g. logits-processor-zoo: SuppressTokens, FixedTokenBias, All…

## pattern

- **`pattern/composable-success-criteria`** — Composable success criteria (regex + semantic + LLM-judge + deterministic + tool + composite)  
  _cross_industry, ai, compliance_ • Treat success criteria as first-class composable artifacts rather than a single rubric+threshold check. Six concrete criterion kinds combine via AND / OR / NOT into arbitrary boole…
- **`pattern/corrective-rag`** — Corrective RAG (CRAG)  
  _ai, cross_industry_ • RAG with a three-state retrieval evaluator. After initial retrieval, an evaluator classifies the retrieval as {correct, incorrect, ambiguous}. Correct → strip-and-recompose; incorr…
- **`pattern/evaluator-optimizer`** — Evaluator-Optimizer  
  _ai, cross_industry_ • One LLM call generates a candidate output; a second LLM (or processor) evaluates against a rubric and provides specific feedback; the generator revises. Loops until the evaluator p…
- **`pattern/hyde`** — HyDE (Hypothetical Document Embeddings)  
  _ai, cross_industry_ • Generate a hypothetical answer to the query (allowing hallucination), then embed THAT answer instead of (or alongside) the query, and retrieve against the embedding. Reduces query-…
- **`pattern/k-anonymity-aggregation`** — K-anonymity + HMACed-key cross-organization aggregation  
  _security, esg, compliance, finance_ • Share *aggregated* signal across organizations without revealing per-org provenance. Each org HMACs the key (broker ID, supplier hash, address) with a hub-published salt so the sam…
- **`pattern/multi-agent-debate`** — Multi-Agent Debate  
  _ai_ • Two or more LLM instances argue different sides of a question, with a judge LLM scoring the arguments. Used for hard reasoning problems where stress-testing a position improves acc…
- **`pattern/naive-rag`** — Naive RAG  
  _ai, cross_industry_ • Single-shot retrieval-augmented generation: embed query, retrieve top-k chunks, concatenate into the prompt, generate. The baseline every other RAG variant compares against.
- **`pattern/orchestrator-workers`** — Orchestrator-Workers  
  _ai, cross_industry_ • A central orchestrator decomposes the task and delegates parallel subtasks to worker agents (sometimes with different personas / tools per worker). Workers return structured result…
- **`pattern/plan-and-execute`** — Plan-and-Execute  
  _ai, cross_industry_ • Separate planning from execution. A planner LLM produces an explicit step list; an executor (often a different / cheaper model) runs each step. After execution, a re-planner can up…
- **`pattern/prompt-chaining`** — Prompt Chaining  
  _ai, cross_industry_ • Break a task into a SEQUENCE of LLM calls where each call's output is the next call's input. The simplest agent pattern — no tools, no loops, no routing — just a linear chain. Usef…
- **`pattern/rag-fusion`** — RAG-Fusion  
  _ai, cross_industry_ • Generate N rewrites of the user query, run retrieval for each, and fuse the ranked lists via Reciprocal Rank Fusion. Outperforms single- query retrieval when the user's wording dif…
- **`pattern/react`** — ReAct (Reason + Act)  
  _ai, cross_industry_ • Interleave reasoning steps with tool calls. At each step the model emits one of: Thought (free-form reasoning), Action (tool call), Observation (tool result fed back). Loop until t…
- **`pattern/reflexion`** — Reflexion  
  _ai_ • Add a verbal self-reflection step after each failed attempt. The reflection is appended to memory and shown to the model on the next attempt. Bounded by `max_iters`. Captures the "…
- **`pattern/routing`** — Routing  
  _ai, cross_industry_ • Classify the input and dispatch to the appropriate specialized sub-pipeline. A classifier (LLM, embedder + threshold, or rule pack) picks a route; the chosen sub-pipeline handles t…
- **`pattern/self-rag`** — Self-RAG  
  _ai, cross_industry_ • Reflection-token retrieval-augmented generation. The model first decides whether to retrieve at all, then grades each retrieved document for relevance, generates an answer grounded…
- **`pattern/self-refine`** — Self-Refine  
  _ai, cross_industry_ • Single critique-and-revise pair. The model drafts an answer, then critiques its own draft against a rubric, then revises. One iteration by default; can be looped. Simpler than Refl…
- **`pattern/skeleton-of-thought`** — Skeleton of Thought (SoT)  
  _ai_ • First generate a SKELETON (bullet outline) of the answer, then expand each bullet IN PARALLEL via separate LLM calls. Stitch the expansions into the final answer. Often used for ta…
- **`pattern/step-back-prompting`** — Step-Back Prompting  
  _ai_ • Before answering, the model is prompted to derive a MORE ABSTRACT question that captures the essence of the user's question. Retrieval and reasoning then happen against the abstrac…
- **`pattern/tree-of-thoughts`** — Tree of Thoughts (ToT)  
  _ai_ • At each reasoning step, propose N candidate "thoughts", value/vote each, and expand the best ones via BFS or DFS. Backtrack on dead-ends. Generalizes chain-of-thought from a single…
- **`pattern/two-stage-retrieve-rerank`** — Two-stage retrieve + constrained rerank  
  _ai, education, scientific_research_ • Retrieve K candidates with a cheap embedder (BM25 / dense), then rerank with a stronger but slower model. The reranker can be: a cross-encoder, or an LLM CONSTRAINED to emit only o…
- **`pipeline/deberta-finetune-classification`** — DeBERTa-v3-large fine-tune for closed-set classification  
  _ai, cross_industry_ • DeBERTa-v3-large fine-tuning shape used as the heavy half of nearly every top Kaggle LLM-classification submission since 2023. Combined with `pipeline/tfidf-lightgbm-text-classific…
- **`pipeline/lora-qlora-pairwise-pref-finetune`** — LoRA + QLoRA pairwise-preference fine-tune (Gemma-2-9b 4-bit)  
  _ai, cross_industry_ • Production-verified fine-tune shape for the LMSYS / WSDM Chatbot Arena class of pairwise-preference competitions. Load Gemma-2-9b with 4-bit BitsAndBytes quantization, attach a PEF…
- **`pipeline/tfidf-lightgbm-text-classification`** — TF-IDF + LightGBM text classification  
  _ai, cross_industry, media_ • The non-LLM baseline that consistently wins or co-wins Kaggle text- classification competitions. Char- and word-ngram TF-IDF feature extraction → LightGBM (often stacked with SGDCl…

## Index by industry vertical

### ai

- `adapter/anthropic-claude-opus` — Anthropic Claude Opus (deep-reasoning frontier-class)
- `adapter/anthropic-claude-sonnet` — Anthropic Claude Sonnet (frontier-class chat + tool-use)
- `adapter/bge-embeddings-local` — BGE embeddings (local)
- `adapter/google-gemini` — Google Gemini (multimodal frontier)
- `adapter/openai-embeddings` — OpenAI embeddings (text-embedding-3-small/large)
- `adapter/openai-gpt-frontier` — OpenAI frontier-class chat + tool-use
- `adapter/vllm-awq-local` — Local vLLM engine with AWQ-quantized weights
- `harness/code-act-jupyter` — Code-Act Jupyter (tool-augmented reasoning via sandboxed Python)
- `knowledge-pack/owasp-top-10-llm` — OWASP Top 10 for LLM Applications (2025)
- `pattern/composable-success-criteria` — Composable success criteria (regex + semantic + LLM-judge + deterministic + tool + composite)
- `pattern/corrective-rag` — Corrective RAG (CRAG)
- `pattern/evaluator-optimizer` — Evaluator-Optimizer
- `pattern/hyde` — HyDE (Hypothetical Document Embeddings)
- `pattern/multi-agent-debate` — Multi-Agent Debate
- `pattern/naive-rag` — Naive RAG
- `pattern/orchestrator-workers` — Orchestrator-Workers
- `pattern/plan-and-execute` — Plan-and-Execute
- `pattern/prompt-chaining` — Prompt Chaining
- `pattern/rag-fusion` — RAG-Fusion
- `pattern/react` — ReAct (Reason + Act)
- `pattern/reflexion` — Reflexion
- `pattern/routing` — Routing
- `pattern/self-rag` — Self-RAG
- `pattern/self-refine` — Self-Refine
- `pattern/skeleton-of-thought` — Skeleton of Thought (SoT)
- `pattern/step-back-prompting` — Step-Back Prompting
- `pattern/tree-of-thoughts` — Tree of Thoughts (ToT)
- `pattern/two-stage-retrieve-rerank` — Two-stage retrieve + constrained rerank
- `pipeline/deberta-finetune-classification` — DeBERTa-v3-large fine-tune for closed-set classification
- `pipeline/lora-qlora-pairwise-pref-finetune` — LoRA + QLoRA pairwise-preference fine-tune (Gemma-2-9b 4-bit)
- `pipeline/tfidf-lightgbm-text-classification` — TF-IDF + LightGBM text classification
- `pipeline/awq-quantized-inference` — AWQ-quantized LLM inference (alternative to bitsandbytes nf4)
- `pipeline/code-act-jupyter-loop` — Code-act Jupyter loop
- `pipeline/deep-research-supervisor-workers` — Deep research: supervisor + parallel workers
- `pipeline/deepseek-r1-code-interpreter-math` — DeepSeek-R1 / QwQ + Python code-interpreter for math reasoning
- `pipeline/knowledge-graph-from-corpus` — GraphRAG: knowledge-graph from corpus + global/local query
- `pipeline/large-model-faiss-rag` — Large-model FAISS RAG (Platypus2-70b style)
- `pipeline/llm-judge-essay-grading` — LLM-judge essay grading (with adversarial prompt prefix)
- `pipeline/multi-agent-debate-with-judge` — Multi-agent debate with judge
- `pipeline/multi-model-judging-ensemble` — Multi-model judging ensemble
- `pipeline/perplexity-baseline-scoring` — Perplexity-baseline scoring
- `pipeline/quantized-llm-inference` — Quantized LLM inference (4-bit BitsAndBytes)
- `pipeline/qwen-vllm-rerank-eedi` — Qwen-32B vLLM retrieval-rerank with logits-processor constraints
- `pipeline/self-rag-grade-and-revise` — Self-RAG: grade-and-revise (concrete implementation)
- `pipeline/storm-persona-curation-article` — STORM: persona-curation + outline-fanout article
- `pipeline/swe-patch-sample-and-review` — SWE-agent: sample N patches + reviewer judges
- `pipeline/synthetic-data-gen-with-teacher-llm` — Synthetic-data generation with teacher LLM
- `pipeline/twenty-questions-agent` — 20-questions agent (Akinator-style)
- `pipeline/two-time-retrieve-rerank` — Two-time retrieval + cross-encoder rerank
- `pipeline/vllm-batch-llm-inference` — vLLM batch LLM inference (with logits-processor-zoo)
- `processor/action-sampler-multi-rollout` — Action sampler — N parallel rollouts
- `processor/community-summary-mapreduce` — Community-summary map-reduce (GraphRAG global)
- `processor/cross-encoder-reranker` — Cross-encoder reranker
- `processor/document-grader` — Per-document relevance grader (Self-RAG)
- `processor/inject-output-schema` — Inject output schema directive
- `processor/multi-vector-fusion` — Multi-vector / multi-query fusion (RRF + weighted)
- `processor/persona-set-generator` — Persona-set generator (STORM)
- `processor/reasoning-framework-selector` — Reasoning framework selector
- `processor/runtime-tool-selector` — Runtime tool selector (Toolformer / pydantic-ai)
- `processor/skeleton-outliner` — Skeleton outliner (Skeleton-of-Thought)
- `processor/two-time-retrieval` — Two-time retrieval (refine query, re-retrieve)
- `processor/vllm-batched-sampling` — vLLM batched sampling (SamplingParams + logits processors)
- `rule-pack/grep-ai-vendor-keys` — AI vendor API key detectors
- `rule-pack/grep-cloud-secrets` — Cloud provider secret detectors
- `rule-pack/grep-prompt-injection-heuristics` — Prompt-injection heuristic detectors

### climate

- `dataset/climate-disclosure-samples` — Synthetic climate disclosure samples (2 cases)
- `knowledge-pack/climate-disclosure-frameworks` — Climate disclosure frameworks (TCFD + ISSB IFRS S2 + CDP + ESRS E1)
- `persona/climate-risk-analyst` — Climate Risk Analyst (TCFD / ISSB IFRS S2 / CDP)
- `pipeline/climate-disclosure-review` — Climate disclosure review (TCFD + ISSB IFRS S2 + ESRS E1)
- `pipeline/sustainability-report-full-review` — Sustainability report full review (Climate + ESG-S + ESG-G chained)
- `rubric/climate-disclosure-quality-v1` — Climate disclosure quality v1 (TCFD/ISSB/ESRS aligned)
- `rubric/esg-env-v1` — ESG environmental (E) sub-rubric v1
- `rule-pack/grep-climate-disclosure-gaps` — Climate disclosure gap detectors (TCFD / ISSB / ESRS E1)
- `rule-pack/grep-esg-environmental-red-flags` — ESG environmental red-flag detectors (the 'E' of ESG)

### compliance

- `benchmark/esg-supplier-grading-bench` — ESG supplier-grading benchmark v1
- `dataset/gxp-validation-samples` — Synthetic GxP validation samples (3 cases)
- `dataset/supplier-disclosure-pack-schema` — Supplier disclosure pack schema (canonical input shape)
- `harness/esg-disclosure-grading` — ESG Disclosure Grading harness
- `knowledge-pack/csddd-and-forced-labor-indicators` — Global supply-chain due-diligence regulatory pack
- `knowledge-pack/gxp-21-cfr-11-guidelines` — 21-CFR-11 + EU GMP Annex 11 + ICH + ALCOA+ regulatory pack
- `knowledge-pack/high-risk-corridors-and-sectors` — High-risk corridors & sector-specific labor / environmental risks
- `knowledge-pack/lead-company-code-stub` — Lead-company code-of-conduct stub (placeholder)
- `pattern/composable-success-criteria` — Composable success criteria (regex + semantic + LLM-judge + deterministic + tool + composite)
- `pattern/k-anonymity-aggregation` — K-anonymity + HMACed-key cross-organization aggregation
- `persona/climate-risk-analyst` — Climate Risk Analyst (TCFD / ISSB IFRS S2 / CDP)
- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)
- `persona/gxp-auditor` — GxP Auditor (21-CFR-11 / EU GMP Annex 11 / ICH / ALCOA+)
- `pipeline/anonymized-illicit-recruitment-pattern-sharing` — Anonymized cross-org pattern sharing for illicit recruitment corridors
- `pipeline/climate-disclosure-review` — Climate disclosure review (TCFD + ISSB IFRS S2 + ESRS E1)
- `pipeline/deep-tier-supplier-audit` — Deep-tier (T1→T4+) supplier audit with traceability
- `pipeline/full-vendor-due-diligence` — Full vendor due-diligence (ESG + AppSec + Legal — kitchen-sink)
- `pipeline/gxp-validation-review` — GxP validation review (21-CFR-11 + Annex 11 + ALCOA+)
- `pipeline/mixed-criteria-demo` — Mixed success-criteria demo (regex + semantic + deterministic + LLM + composite)
- `pipeline/supplier-policy-grading` — Supplier policy & disclosure grading (CSDDD-aligned)
- `pipeline/sustainability-report-full-review` — Sustainability report full review (Climate + ESG-S + ESG-G chained)
- `processor/structured-to-prose` — Structured JSON → prose normalizer (for GREP-style rule packs)
- `rubric/climate-disclosure-quality-v1` — Climate disclosure quality v1 (TCFD/ISSB/ESRS aligned)
- `rubric/esg-env-v1` — ESG environmental (E) sub-rubric v1
- `rubric/esg-gov-v1` — ESG governance (G) sub-rubric v1
- `rubric/esg-social-v1` — ESG social (S) sub-rubric v1
- `rubric/esg-supplier-compliance-v1` — ESG supplier compliance v1 (full E + S + G)
- `rubric/gxp-validation-quality-v1` — GxP validation review quality v1
- `rule-pack/grep-climate-disclosure-gaps` — Climate disclosure gap detectors (TCFD / ISSB / ESRS E1)
- `rule-pack/grep-esg-environmental-red-flags` — ESG environmental red-flag detectors (the 'E' of ESG)
- `rule-pack/grep-esg-forced-labor-red-flags` — ESG / forced-labor red-flag detectors (the 'S' of ESG)
- `rule-pack/grep-esg-governance-red-flags` — ESG governance red-flag detectors (the 'G' of ESG)
- `rule-pack/grep-gxp-data-integrity-red-flags` — GxP data-integrity red-flag detectors (21-CFR-11 / ALCOA+)
- `tool/cbp-wro-lookup` — US CBP Withhold Release Order + UFLPA Entity List lookup

### creative

- `adapter/sdxl-local` — SDXL (local Diffusers)
- `knowledge-pack/lens-physics-primers` — Lens physics primers
- `knowledge-pack/style-references-cinematic` — Cinematic style references
- `persona/cinematic-product-photographer` — Cinematic Product Photographer
- `persona/translator-improver` — Translator + improver
- `pipeline/brand-safe-product-photo` — Brand-Safe Product Photo
- `processor/nsfw-image-classifier` — NSFW image classifier
- `rubric/brand-safe-image-v1` — Brand-safe image v1
- `rule-pack/grep-output-safety-image` — Image-output safety checks
- `rule-pack/grep-prohibited-terms` — Prohibited Terms (image-gen guard rails)
- `tool/txt2img-sdxl` — Text-to-Image (SDXL)

### cross_industry

- `adapter/anthropic-claude-opus` — Anthropic Claude Opus (deep-reasoning frontier-class)
- `adapter/anthropic-claude-sonnet` — Anthropic Claude Sonnet (frontier-class chat + tool-use)
- `adapter/bge-embeddings-local` — BGE embeddings (local)
- `adapter/google-gemini` — Google Gemini (multimodal frontier)
- `adapter/ollama-default` — Ollama (local default)
- `adapter/openai-embeddings` — OpenAI embeddings (text-embedding-3-small/large)
- `adapter/openai-gpt-frontier` — OpenAI frontier-class chat + tool-use
- `harness/redact-pii-text` — Redact PII (text)
- `harness/text-safety-review` — Text Safety Review
- `knowledge-pack/common-abbreviations` — Common abbreviations (cross-industry sample)
- `knowledge-pack/common-personas-library` — Common personas / system-prompt library
- `knowledge-pack/csddd-and-forced-labor-indicators` — Global supply-chain due-diligence regulatory pack
- `knowledge-pack/iso-country-codes` — ISO 3166 country codes (sample)
- `knowledge-pack/iso-currency-codes` — ISO 4217 currency codes
- `knowledge-pack/lead-company-code-stub` — Lead-company code-of-conduct stub (placeholder)
- `knowledge-pack/spdx-licenses-summary` — SPDX licenses (summary)
- `pattern/composable-success-criteria` — Composable success criteria (regex + semantic + LLM-judge + deterministic + tool + composite)
- `pattern/corrective-rag` — Corrective RAG (CRAG)
- `pattern/evaluator-optimizer` — Evaluator-Optimizer
- `pattern/hyde` — HyDE (Hypothetical Document Embeddings)
- `pattern/k-anonymity-aggregation` — K-anonymity + HMACed-key cross-organization aggregation
- `pattern/naive-rag` — Naive RAG
- `pattern/orchestrator-workers` — Orchestrator-Workers
- `pattern/plan-and-execute` — Plan-and-Execute
- `pattern/prompt-chaining` — Prompt Chaining
- `pattern/rag-fusion` — RAG-Fusion
- `pattern/react` — ReAct (Reason + Act)
- `pattern/routing` — Routing
- `pattern/self-rag` — Self-RAG
- `pattern/self-refine` — Self-Refine
- `pipeline/deberta-finetune-classification` — DeBERTa-v3-large fine-tune for closed-set classification
- `pipeline/lora-qlora-pairwise-pref-finetune` — LoRA + QLoRA pairwise-preference fine-tune (Gemma-2-9b 4-bit)
- `pipeline/tfidf-lightgbm-text-classification` — TF-IDF + LightGBM text classification
- `persona/fact-checker` — Fact Checker
- `persona/linux-terminal` — Linux terminal
- `persona/research-analyst` — Research Analyst
- `persona/support-agent` — Customer support agent
- `persona/translator-improver` — Translator + improver
- `pipeline/chat-with-pdf-citations` — Chat with PDF (with citations)
- `pipeline/deep-research-supervisor-workers` — Deep research: supervisor + parallel workers
- `pipeline/deep-research-with-citations` — Deep research with citations
- `pipeline/email-triage-and-draft` — Email triage + reply draft
- `pipeline/everything-research-pipeline` — Everything research pipeline (kitchen-sink, 22 passes)
- `pipeline/full-vendor-due-diligence` — Full vendor due-diligence (ESG + AppSec + Legal — kitchen-sink)
- `pipeline/knowledge-graph-from-corpus` — GraphRAG: knowledge-graph from corpus + global/local query
- `pipeline/mixed-criteria-demo` — Mixed success-criteria demo (regex + semantic + deterministic + LLM + composite)
- `pipeline/multi-doc-qa-subquestion` — Multi-document QA with sub-question decomposition
- `pipeline/plan-execute-critic-loop` — Plan / execute / critic loop
- `pipeline/quantized-llm-inference` — Quantized LLM inference (4-bit BitsAndBytes)
- `pipeline/research-entity` — Research Entity
- `pipeline/self-rag-grade-and-revise` — Self-RAG: grade-and-revise (concrete implementation)
- `pipeline/verify-claim-against-corpus` — Verify Claim Against Corpus
- `processor/audio-to-text-whisper` — Audio to text (Whisper)
- `processor/audit-trace-emitter` — Audit trace emitter
- `processor/citation-coverage` — Citation coverage verifier
- `processor/community-summary-mapreduce` — Community-summary map-reduce (GraphRAG global)
- `processor/context-window-packer` — Context-window packer (Lost-in-the-middle aware)
- `processor/cost-ceiling-gate` — Cost ceiling gate
- `processor/cost-meter` — Cost meter
- `processor/cross-encoder-reranker` — Cross-encoder reranker
- `processor/document-grader` — Per-document relevance grader (Self-RAG)
- `processor/embedder-minilm` — Text embedder (MiniLM-L6-v2)
- `processor/escalate-human-review` — Escalate to human reviewer
- `processor/hallucination-scorer` — Hallucination scorer (SelfCheckGPT-style)
- `processor/hyde-query-expander` — HyDE query expander
- `processor/inject-datetime-locale` — Inject datetime + locale into prompt
- `processor/inject-output-schema` — Inject output schema directive
- `processor/intent-dispatcher` — Intent dispatcher
- `processor/iterative-revise-loop` — Iterative revise loop
- `processor/json-schema-repair` — JSON Schema repair + validate
- `processor/llm-judge` — LLM-as-judge
- `processor/llmlingua-context-compressor` — LLMLingua context compressor
- `processor/memory-conversational-store` — Conversational memory store
- `processor/multi-vector-fusion` — Multi-vector / multi-query fusion (RRF + weighted)
- `processor/official-sources-checker` — Official-sources analyzer
- `processor/pdf-to-text` — PDF to text
- `processor/prompt-injection-detector` — Prompt-injection detector
- `processor/reasoning-framework-selector` — Reasoning framework selector
- `processor/recursive-character-chunker` — Recursive character chunker
- `processor/redact-pii-text` — Redact PII from text (English-centric, MS Presidio-compatible)
- `processor/runtime-tool-selector` — Runtime tool selector (Toolformer / pydantic-ai)
- `processor/self-consistency-sampler` — Self-consistency sampler
- `processor/self-refine-critique` — Self-Refine critique loop
- `processor/structured-to-prose` — Structured JSON → prose normalizer (for GREP-style rule packs)
- `processor/sub-question-decomposer` — Sub-question decomposer
- `processor/verify-composite-criterion` — Composite (AND/OR/NOT) success-criterion evaluator
- `processor/verify-deterministic-criterion` — Deterministic comparison success-criterion evaluator
- `processor/verify-llm-judge-criterion` — LLM-as-judge success-criterion evaluator
- `processor/verify-regex-criterion` — Regex success-criterion evaluator
- `processor/verify-semantic-criterion` — Semantic-similarity success-criterion evaluator
- `processor/verify-tool-validate-criterion` — Tool-validation success-criterion evaluator
- `rubric/research-entity-v1` — Research Entity v1
- `rubric/verification-v1` — Verification v1
- `rule-pack/grep-cloud-secrets` — Cloud provider secret detectors
- `rule-pack/grep-private-key-blocks` — Private key block detectors
- `rule-pack/grep-prompt-injection-heuristics` — Prompt-injection heuristic detectors
- `rule-pack/hybrid-retrieval-policy` — Hybrid retrieval policy (BM25 + dense + RRF)
- `rule-pack/privacy-pii-text-en` — Privacy PII (English text)
- `rule-pack/web-search-allowlist-default` — Web search allowlist (default)
- `tool/json-schema-validator` — JSON Schema 2020-12 validator
- `tool/web-search` — Web Search

### education

- `harness/code-act-jupyter` — Code-Act Jupyter (tool-augmented reasoning via sandboxed Python)
- `pattern/two-stage-retrieve-rerank` — Two-stage retrieve + constrained rerank
- `persona/math-tutor` — Math tutor
- `pipeline/deepseek-r1-code-interpreter-math` — DeepSeek-R1 / QwQ + Python code-interpreter for math reasoning
- `pipeline/large-model-faiss-rag` — Large-model FAISS RAG (Platypus2-70b style)
- `pipeline/llm-judge-essay-grading` — LLM-judge essay grading (with adversarial prompt prefix)
- `pipeline/qwen-vllm-rerank-eedi` — Qwen-32B vLLM retrieval-rerank with logits-processor constraints
- `pipeline/storm-persona-curation-article` — STORM: persona-curation + outline-fanout article
- `pipeline/twenty-questions-agent` — 20-questions agent (Akinator-style)
- `pipeline/two-time-retrieve-rerank` — Two-time retrieval + cross-encoder rerank
- `pipeline/vllm-batch-llm-inference` — vLLM batch LLM inference (with logits-processor-zoo)
- `processor/persona-set-generator` — Persona-set generator (STORM)
- `processor/skeleton-outliner` — Skeleton outliner (Skeleton-of-Thought)
- `processor/two-time-retrieval` — Two-time retrieval (refine query, re-retrieve)

### education.tutoring

- `persona/math-tutor` — Math tutor

### esg

- `benchmark/esg-supplier-grading-bench` — ESG supplier-grading benchmark v1
- `dataset/climate-disclosure-samples` — Synthetic climate disclosure samples (2 cases)
- `dataset/supplier-disclosure-pack-schema` — Supplier disclosure pack schema (canonical input shape)
- `harness/esg-disclosure-grading` — ESG Disclosure Grading harness
- `knowledge-pack/climate-disclosure-frameworks` — Climate disclosure frameworks (TCFD + ISSB IFRS S2 + CDP + ESRS E1)
- `knowledge-pack/csddd-and-forced-labor-indicators` — Global supply-chain due-diligence regulatory pack
- `knowledge-pack/high-risk-corridors-and-sectors` — High-risk corridors & sector-specific labor / environmental risks
- `knowledge-pack/lead-company-code-stub` — Lead-company code-of-conduct stub (placeholder)
- `pattern/k-anonymity-aggregation` — K-anonymity + HMACed-key cross-organization aggregation
- `persona/climate-risk-analyst` — Climate Risk Analyst (TCFD / ISSB IFRS S2 / CDP)
- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)
- `pipeline/anonymized-illicit-recruitment-pattern-sharing` — Anonymized cross-org pattern sharing for illicit recruitment corridors
- `pipeline/climate-disclosure-review` — Climate disclosure review (TCFD + ISSB IFRS S2 + ESRS E1)
- `pipeline/deep-tier-supplier-audit` — Deep-tier (T1→T4+) supplier audit with traceability
- `pipeline/supplier-policy-grading` — Supplier policy & disclosure grading (CSDDD-aligned)
- `pipeline/sustainability-report-full-review` — Sustainability report full review (Climate + ESG-S + ESG-G chained)
- `processor/redact-pii-text` — Redact PII from text (English-centric, MS Presidio-compatible)
- `processor/structured-to-prose` — Structured JSON → prose normalizer (for GREP-style rule packs)
- `rubric/climate-disclosure-quality-v1` — Climate disclosure quality v1 (TCFD/ISSB/ESRS aligned)
- `rubric/esg-env-v1` — ESG environmental (E) sub-rubric v1
- `rubric/esg-gov-v1` — ESG governance (G) sub-rubric v1
- `rubric/esg-social-v1` — ESG social (S) sub-rubric v1
- `rubric/esg-supplier-compliance-v1` — ESG supplier compliance v1 (full E + S + G)
- `rule-pack/grep-climate-disclosure-gaps` — Climate disclosure gap detectors (TCFD / ISSB / ESRS E1)
- `rule-pack/grep-esg-environmental-red-flags` — ESG environmental red-flag detectors (the 'E' of ESG)
- `rule-pack/grep-esg-forced-labor-red-flags` — ESG / forced-labor red-flag detectors (the 'S' of ESG)
- `rule-pack/grep-esg-governance-red-flags` — ESG governance red-flag detectors (the 'G' of ESG)
- `tool/cbp-wro-lookup` — US CBP Withhold Release Order + UFLPA Entity List lookup

### esg.csddd

- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)

### esg.csrd

- `persona/climate-risk-analyst` — Climate Risk Analyst (TCFD / ISSB IFRS S2 / CDP)
- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)

### esg.modern_slavery

- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)

### finance

- `dataset/climate-disclosure-samples` — Synthetic climate disclosure samples (2 cases)
- `harness/aml-investigation` — AML Investigation
- `knowledge-pack/aml-red-flags-extended` — AML red flags (extended)
- `knowledge-pack/climate-disclosure-frameworks` — Climate disclosure frameworks (TCFD + ISSB IFRS S2 + CDP + ESRS E1)
- `knowledge-pack/fatf-typologies-sample` — FATF typologies (sample chunks)
- `knowledge-pack/iso-country-codes` — ISO 3166 country codes (sample)
- `knowledge-pack/iso-currency-codes` — ISO 4217 currency codes
- `knowledge-pack/sanctions-list-shape` — Sanctions list (shape, with placeholder entries)
- `pattern/k-anonymity-aggregation` — K-anonymity + HMACed-key cross-organization aggregation
- `persona/aml-analyst` — AML Analyst
- `persona/climate-risk-analyst` — Climate Risk Analyst (TCFD / ISSB IFRS S2 / CDP)
- `pipeline/climate-disclosure-review` — Climate disclosure review (TCFD + ISSB IFRS S2 + ESRS E1)
- `pipeline/suspicious-transaction-review` — Suspicious Transaction Review
- `pipeline/sustainability-report-full-review` — Sustainability report full review (Climate + ESG-S + ESG-G chained)
- `processor/official-sources-checker` — Official-sources analyzer
- `processor/redact-pii-text` — Redact PII from text (English-centric, MS Presidio-compatible)
- `rubric/aml-investigation-v1` — AML investigation v1
- `rubric/climate-disclosure-quality-v1` — Climate disclosure quality v1 (TCFD/ISSB/ESRS aligned)
- `rubric/esg-gov-v1` — ESG governance (G) sub-rubric v1
- `rule-pack/aml-typologies-fatf` — FATF AML typologies (sampled)
- `rule-pack/financial-pii-en` — Financial PII (English)
- `rule-pack/grep-climate-disclosure-gaps` — Climate disclosure gap detectors (TCFD / ISSB / ESRS E1)
- `rule-pack/grep-esg-governance-red-flags` — ESG governance red-flag detectors (the 'G' of ESG)
- `rule-pack/sanctions-screening` — Sanctions screening (deterministic)
- `tool/sanctions-check` — Sanctions list check
- `tool/transaction-graph-query` — Transaction graph query

### finance.aml

- `harness/aml-investigation` — AML Investigation
- `knowledge-pack/aml-red-flags-extended` — AML red flags (extended)
- `knowledge-pack/fatf-typologies-sample` — FATF typologies (sample chunks)
- `knowledge-pack/sanctions-list-shape` — Sanctions list (shape, with placeholder entries)
- `persona/aml-analyst` — AML Analyst
- `pipeline/suspicious-transaction-review` — Suspicious Transaction Review
- `rubric/aml-investigation-v1` — AML investigation v1
- `rule-pack/aml-typologies-fatf` — FATF AML typologies (sampled)
- `rule-pack/sanctions-screening` — Sanctions screening (deterministic)
- `tool/sanctions-check` — Sanctions list check
- `tool/transaction-graph-query` — Transaction graph query

### finance.kyc

- `knowledge-pack/aml-red-flags-extended` — AML red flags (extended)
- `knowledge-pack/sanctions-list-shape` — Sanctions list (shape, with placeholder entries)
- `rule-pack/sanctions-screening` — Sanctions screening (deterministic)
- `tool/sanctions-check` — Sanctions list check

### government

- `processor/official-sources-checker` — Official-sources analyzer

### healthcare

- `dataset/radiology-report-samples` — Synthetic radiology report samples (3 cases, fully synthetic)
- `harness/clinical-decision-support` — Clinical Decision Support
- `harness/radiology-report-review` — Radiology Report Review harness
- `knowledge-pack/clinical-guidelines-sample` — Clinical guidelines (sample chunks)
- `knowledge-pack/drug-interactions-sample` — Drug-drug interactions (sample, educational)
- `knowledge-pack/icd10-sample` — ICD-10 sample
- `knowledge-pack/radiology-acrac-fleischner` — ACR Appropriateness Criteria + Fleischner + ACR RADS rubrics
- `persona/clinical-reasoner` — Clinical Reasoner
- `persona/radiologist-cite-first` — Radiologist (citation-first, specialty radiology)
- `pipeline/differential-diagnosis` — Differential Diagnosis
- `pipeline/radiology-report-grading` — Radiology report grading (RADS-aware, Fleischner-aware)
- `processor/official-sources-checker` — Official-sources analyzer
- `processor/redact-pii-text` — Redact PII from text (English-centric, MS Presidio-compatible)
- `rubric/clinical-grounded-response-v1` — Clinical grounded response v1
- `rubric/radiology-report-quality-v1` — Radiology report quality v1
- `rule-pack/clinical-red-flags` — Clinical red flags
- `rule-pack/grep-radiology-report-red-flags` — Radiology report quality + incidental-findings red flags
- `rule-pack/phi-hipaa-en` — PHI (HIPAA 18-identifier) — English text
- `tool/lookup-icd10` — ICD-10 lookup

### healthcare.clinical

- `harness/clinical-decision-support` — Clinical Decision Support
- `knowledge-pack/clinical-guidelines-sample` — Clinical guidelines (sample chunks)
- `knowledge-pack/drug-interactions-sample` — Drug-drug interactions (sample, educational)
- `knowledge-pack/icd10-sample` — ICD-10 sample
- `knowledge-pack/radiology-acrac-fleischner` — ACR Appropriateness Criteria + Fleischner + ACR RADS rubrics
- `persona/clinical-reasoner` — Clinical Reasoner
- `pipeline/differential-diagnosis` — Differential Diagnosis
- `rubric/clinical-grounded-response-v1` — Clinical grounded response v1
- `rule-pack/clinical-red-flags` — Clinical red flags
- `tool/lookup-icd10` — ICD-10 lookup

### healthcare.pharmacy

- `dataset/gxp-validation-samples` — Synthetic GxP validation samples (3 cases)
- `knowledge-pack/drug-interactions-sample` — Drug-drug interactions (sample, educational)
- `knowledge-pack/gxp-21-cfr-11-guidelines` — 21-CFR-11 + EU GMP Annex 11 + ICH + ALCOA+ regulatory pack
- `persona/gxp-auditor` — GxP Auditor (21-CFR-11 / EU GMP Annex 11 / ICH / ALCOA+)

### healthcare.radiology

- `dataset/radiology-report-samples` — Synthetic radiology report samples (3 cases, fully synthetic)
- `harness/radiology-report-review` — Radiology Report Review harness
- `knowledge-pack/radiology-acrac-fleischner` — ACR Appropriateness Criteria + Fleischner + ACR RADS rubrics
- `persona/radiologist-cite-first` — Radiologist (citation-first, specialty radiology)
- `pipeline/radiology-report-grading` — Radiology report grading (RADS-aware, Fleischner-aware)
- `rubric/radiology-report-quality-v1` — Radiology report quality v1
- `rule-pack/grep-radiology-report-red-flags` — Radiology report quality + incidental-findings red flags

### humanitarian

- `knowledge-pack/high-risk-corridors-and-sectors` — High-risk corridors & sector-specific labor / environmental risks
- `knowledge-pack/iso-country-codes` — ISO 3166 country codes (sample)
- `rubric/esg-social-v1` — ESG social (S) sub-rubric v1

### legal

- `dataset/contract-samples` — Synthetic commercial contract samples (3 cases)
- `harness/contract-redline` — Contract Clause Redlining harness
- `knowledge-pack/contract-law-clauses` — Commercial contract clause library (composite educational)
- `knowledge-pack/spdx-licenses-summary` — SPDX licenses (summary)
- `persona/contract-reviewer-cite-first` — Contract Reviewer (citation-first, senior in-house counsel)
- `pipeline/contract-clause-review` — Commercial contract clause review (cite-first redlining)
- `pipeline/full-vendor-due-diligence` — Full vendor due-diligence (ESG + AppSec + Legal — kitchen-sink)
- `pipeline/mixed-criteria-demo` — Mixed success-criteria demo (regex + semantic + deterministic + LLM + composite)
- `rubric/contract-review-quality-v1` — Contract review quality v1
- `rule-pack/grep-contract-red-flags` — Commercial contract red-flag detectors

### legal.compliance

- `dataset/contract-samples` — Synthetic commercial contract samples (3 cases)
- `harness/contract-redline` — Contract Clause Redlining harness
- `knowledge-pack/contract-law-clauses` — Commercial contract clause library (composite educational)
- `persona/contract-reviewer-cite-first` — Contract Reviewer (citation-first, senior in-house counsel)
- `pipeline/contract-clause-review` — Commercial contract clause review (cite-first redlining)
- `rubric/contract-review-quality-v1` — Contract review quality v1
- `rule-pack/grep-contract-red-flags` — Commercial contract red-flag detectors

### legal.contract

- `dataset/contract-samples` — Synthetic commercial contract samples (3 cases)
- `harness/contract-redline` — Contract Clause Redlining harness
- `knowledge-pack/contract-law-clauses` — Commercial contract clause library (composite educational)
- `persona/contract-reviewer-cite-first` — Contract Reviewer (citation-first, senior in-house counsel)
- `pipeline/contract-clause-review` — Commercial contract clause review (cite-first redlining)
- `rubric/contract-review-quality-v1` — Contract review quality v1
- `rule-pack/grep-contract-red-flags` — Commercial contract red-flag detectors

### media

- `pipeline/tfidf-lightgbm-text-classification` — TF-IDF + LightGBM text classification
- `persona/fact-checker` — Fact Checker
- `pipeline/deep-research-supervisor-workers` — Deep research: supervisor + parallel workers
- `pipeline/deep-research-with-citations` — Deep research with citations
- `pipeline/storm-persona-curation-article` — STORM: persona-curation + outline-fanout article
- `pipeline/verify-claim-against-corpus` — Verify Claim Against Corpus
- `processor/nsfw-image-classifier` — NSFW image classifier
- `processor/official-sources-checker` — Official-sources analyzer
- `processor/persona-set-generator` — Persona-set generator (STORM)
- `processor/skeleton-outliner` — Skeleton outliner (Skeleton-of-Thought)
- `rubric/verification-v1` — Verification v1
- `rule-pack/grep-output-safety-image` — Image-output safety checks
- `rule-pack/grep-prohibited-terms` — Prohibited Terms (image-gen guard rails)

### pharma

- `dataset/gxp-validation-samples` — Synthetic GxP validation samples (3 cases)
- `knowledge-pack/gxp-21-cfr-11-guidelines` — 21-CFR-11 + EU GMP Annex 11 + ICH + ALCOA+ regulatory pack
- `persona/gxp-auditor` — GxP Auditor (21-CFR-11 / EU GMP Annex 11 / ICH / ALCOA+)
- `pipeline/gxp-validation-review` — GxP validation review (21-CFR-11 + Annex 11 + ALCOA+)
- `rubric/gxp-validation-quality-v1` — GxP validation review quality v1
- `rule-pack/grep-gxp-data-integrity-red-flags` — GxP data-integrity red-flag detectors (21-CFR-11 / ALCOA+)

### pharma.gxp

- `dataset/gxp-validation-samples` — Synthetic GxP validation samples (3 cases)
- `knowledge-pack/gxp-21-cfr-11-guidelines` — 21-CFR-11 + EU GMP Annex 11 + ICH + ALCOA+ regulatory pack
- `persona/gxp-auditor` — GxP Auditor (21-CFR-11 / EU GMP Annex 11 / ICH / ALCOA+)
- `pipeline/gxp-validation-review` — GxP validation review (21-CFR-11 + Annex 11 + ALCOA+)
- `rubric/gxp-validation-quality-v1` — GxP validation review quality v1
- `rule-pack/grep-gxp-data-integrity-red-flags` — GxP data-integrity red-flag detectors (21-CFR-11 / ALCOA+)

### retail

- `persona/cinematic-product-photographer` — Cinematic Product Photographer
- `persona/support-agent` — Customer support agent
- `pipeline/brand-safe-product-photo` — Brand-Safe Product Photo
- `pipeline/email-triage-and-draft` — Email triage + reply draft
- `rubric/brand-safe-image-v1` — Brand-safe image v1

### retail.support

- `persona/support-agent` — Customer support agent
- `pipeline/email-triage-and-draft` — Email triage + reply draft

### scientific_research

- `harness/code-act-jupyter` — Code-Act Jupyter (tool-augmented reasoning via sandboxed Python)
- `pattern/two-stage-retrieve-rerank` — Two-stage retrieve + constrained rerank
- `pipeline/deepseek-r1-code-interpreter-math` — DeepSeek-R1 / QwQ + Python code-interpreter for math reasoning
- `pipeline/large-model-faiss-rag` — Large-model FAISS RAG (Platypus2-70b style)
- `pipeline/two-time-retrieve-rerank` — Two-time retrieval + cross-encoder rerank

### security

- `dataset/code-review-samples` — Synthetic code-review samples (3 cases)
- `dataset/threat-intel-samples` — Synthetic threat-intelligence report samples
- `harness/appsec-code-audit` — AppSec Code Audit harness
- `knowledge-pack/mitre-attack-sample` — MITRE ATT&CK techniques (sample)
- `knowledge-pack/owasp-top-10-llm` — OWASP Top 10 for LLM Applications (2025)
- `pattern/k-anonymity-aggregation` — K-anonymity + HMACed-key cross-organization aggregation
- `persona/security-engineer-cite-first` — Security Engineer (CWE-cite-first AppSec reviewer)
- `persona/threat-intel-analyst` — Threat Intelligence Analyst (MITRE ATT&CK + STIX/TAXII + IOC)
- `pipeline/code-review-with-risk-score` — Code review with risk score
- `pipeline/code-security-review` — Code security review (CWE-cite-first AppSec audit)
- `pipeline/full-vendor-due-diligence` — Full vendor due-diligence (ESG + AppSec + Legal — kitchen-sink)
- `pipeline/security-incident-grading` — Security incident write-up grading (CTI + AppSec chained)
- `pipeline/threat-intel-ioc-review` — Threat-intel IOC + TTP review (MITRE ATT&CK aligned)
- `processor/prompt-injection-detector` — Prompt-injection detector
- `rubric/code-security-review-v1` — Code security review v1
- `rubric/threat-intel-quality-v1` — Threat intelligence report quality v1
- `rule-pack/grep-ai-vendor-keys` — AI vendor API key detectors
- `rule-pack/grep-cloud-secrets` — Cloud provider secret detectors
- `rule-pack/grep-code-vulnerabilities` — Code vulnerability + secret-detection GREP pack
- `rule-pack/grep-ioc-extraction` — IOC extraction GREP pack (file hashes / domains / IPs / URLs)
- `rule-pack/grep-private-key-blocks` — Private key block detectors
- `rule-pack/grep-prompt-injection-heuristics` — Prompt-injection heuristic detectors
- `rule-pack/grep-vcs-platform-pats` — VCS platform PATs (GitHub, GitLab, Bitbucket, Atlassian)

### security.appsec

- `dataset/code-review-samples` — Synthetic code-review samples (3 cases)
- `harness/appsec-code-audit` — AppSec Code Audit harness
- `persona/security-engineer-cite-first` — Security Engineer (CWE-cite-first AppSec reviewer)
- `pipeline/code-security-review` — Code security review (CWE-cite-first AppSec audit)
- `pipeline/security-incident-grading` — Security incident write-up grading (CTI + AppSec chained)
- `rubric/code-security-review-v1` — Code security review v1
- `rule-pack/grep-code-vulnerabilities` — Code vulnerability + secret-detection GREP pack

### software

- `dataset/code-review-samples` — Synthetic code-review samples (3 cases)
- `harness/appsec-code-audit` — AppSec Code Audit harness
- `knowledge-pack/spdx-licenses-summary` — SPDX licenses (summary)
- `persona/code-consultant` — Code consultant
- `persona/linux-terminal` — Linux terminal
- `persona/security-engineer-cite-first` — Security Engineer (CWE-cite-first AppSec reviewer)
- `pipeline/code-act-jupyter-loop` — Code-act Jupyter loop
- `pipeline/code-review-with-risk-score` — Code review with risk score
- `pipeline/code-security-review` — Code security review (CWE-cite-first AppSec audit)
- `pipeline/swe-patch-sample-and-review` — SWE-agent: sample N patches + reviewer judges
- `processor/action-sampler-multi-rollout` — Action sampler — N parallel rollouts
- `rubric/code-security-review-v1` — Code security review v1
- `rule-pack/grep-code-vulnerabilities` — Code vulnerability + secret-detection GREP pack
- `rule-pack/grep-vcs-platform-pats` — VCS platform PATs (GitHub, GitLab, Bitbucket, Atlassian)

### software.codereview

- `persona/code-consultant` — Code consultant
- `persona/security-engineer-cite-first` — Security Engineer (CWE-cite-first AppSec reviewer)
- `pipeline/code-review-with-risk-score` — Code review with risk score
- `pipeline/code-security-review` — Code security review (CWE-cite-first AppSec audit)
- `pipeline/swe-patch-sample-and-review` — SWE-agent: sample N patches + reviewer judges

### supply_chain

- `benchmark/esg-supplier-grading-bench` — ESG supplier-grading benchmark v1
- `dataset/supplier-disclosure-pack-schema` — Supplier disclosure pack schema (canonical input shape)
- `harness/esg-disclosure-grading` — ESG Disclosure Grading harness
- `knowledge-pack/csddd-and-forced-labor-indicators` — Global supply-chain due-diligence regulatory pack
- `knowledge-pack/high-risk-corridors-and-sectors` — High-risk corridors & sector-specific labor / environmental risks
- `knowledge-pack/lead-company-code-stub` — Lead-company code-of-conduct stub (placeholder)
- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)
- `pipeline/anonymized-illicit-recruitment-pattern-sharing` — Anonymized cross-org pattern sharing for illicit recruitment corridors
- `pipeline/deep-tier-supplier-audit` — Deep-tier (T1→T4+) supplier audit with traceability
- `pipeline/full-vendor-due-diligence` — Full vendor due-diligence (ESG + AppSec + Legal — kitchen-sink)
- `pipeline/supplier-policy-grading` — Supplier policy & disclosure grading (CSDDD-aligned)
- `processor/structured-to-prose` — Structured JSON → prose normalizer (for GREP-style rule packs)
- `rubric/esg-env-v1` — ESG environmental (E) sub-rubric v1
- `rubric/esg-social-v1` — ESG social (S) sub-rubric v1
- `rubric/esg-supplier-compliance-v1` — ESG supplier compliance v1 (full E + S + G)
- `rule-pack/grep-esg-environmental-red-flags` — ESG environmental red-flag detectors (the 'E' of ESG)
- `rule-pack/grep-esg-forced-labor-red-flags` — ESG / forced-labor red-flag detectors (the 'S' of ESG)
- `tool/cbp-wro-lookup` — US CBP Withhold Release Order + UFLPA Entity List lookup

### sustainability

- `persona/esg-auditor` — ESG / Supply Chain Due Diligence Auditor (E + S + G)
- `rule-pack/grep-esg-environmental-red-flags` — ESG environmental red-flag detectors (the 'E' of ESG)

### threat_intelligence

- `dataset/threat-intel-samples` — Synthetic threat-intelligence report samples
- `persona/threat-intel-analyst` — Threat Intelligence Analyst (MITRE ATT&CK + STIX/TAXII + IOC)
- `pipeline/security-incident-grading` — Security incident write-up grading (CTI + AppSec chained)
- `pipeline/threat-intel-ioc-review` — Threat-intel IOC + TTP review (MITRE ATT&CK aligned)
- `rubric/threat-intel-quality-v1` — Threat intelligence report quality v1
- `rule-pack/grep-ioc-extraction` — IOC extraction GREP pack (file hashes / domains / IPs / URLs)

### threat_intelligence.ioc

- `persona/threat-intel-analyst` — Threat Intelligence Analyst (MITRE ATT&CK + STIX/TAXII + IOC)

### threat_intelligence.ttp

- `persona/threat-intel-analyst` — Threat Intelligence Analyst (MITRE ATT&CK + STIX/TAXII + IOC)
