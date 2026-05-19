# GitHub hosting plan

A concrete, end-to-end plan for hosting the Open Harness Hub on GitHub
in a way that doubles as a Claude Code plugin marketplace, an MCP
server distribution, a Croissant dataset index, and a static
documentation site.

## Why GitHub is the right primary host

- **Free for public repos** including Pages, Actions, Discussions,
  Releases, and Packages.
- **Branch protection + CODEOWNERS** matches the catalog's PR-first
  ingest model.
- **Releases** are a natural delivery vehicle for the `dist/` emitter
  outputs (Croissant JSON, MCP bundle, Agent Skills bundle, AIBOM).
- **Pages** is the simplest static host for MkDocs; deploy via Actions
  with no extra service.
- **Plugin marketplaces** in Claude Code (and the Agent Skills
  ecosystem) discover content from git URLs. GitHub is the canonical
  source.

## Repository layout

```
open-harness-hub/                         # repo root
├── README.md                             # public-facing landing
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── SECURITY.md
├── LICENSE
├── CODEOWNERS                            # routing for reviews
├── AGENTS.md                             # cross-tool agent orientation
├── CLAUDE.md                             # Claude-Code-specific notes
├── mkdocs.yml
├── pyproject.toml                        # tooling deps
├── requirements-docs.txt
├── vercel.json
├── netlify.toml
├── _headers / _redirects                 # Cloudflare Pages
├── catalog/                              # SOURCE OF TRUTH (YAML manifests)
├── schemas/                              # JSON Schemas
├── vocabularies/                         # controlled vocabularies
├── taxonomy/SPEC.md                      # canonical taxonomy
├── db/                                   # database mappings (DDL / collections / vector)
├── docs/                                 # MkDocs source
│   ├── ns/context.jsonld                 # JSON-LD context
│   ├── concepts/, howto/, reference/, research/
│   ├── catalog/                          # browser.html + auto-generated pages
│   └── ...
├── scripts/                              # validate, build, run, emit
│   ├── validate.py
│   ├── build_catalog_index.py
│   ├── build_catalog_pages.py
│   ├── run_pipeline.py
│   ├── new.py
│   ├── mine_kaggle_harnesses.py
│   ├── db/build_vector_index.py
│   └── emit/                             # standards emitters
│       ├── croissant.py
│       ├── mcp_server.py
│       ├── agent_skill.py
│       ├── hf_model_card.py              # (planned)
│       ├── lm_eval_harness.py            # (planned)
│       └── ...
├── hf-space/                             # HF Spaces Gradio playground
├── examples/
├── _reference/                           # local clones (gitignored)
├── dist/                                 # build output (gitignored, published via Releases)
└── .github/
    ├── workflows/
    │   ├── validate.yml                  # on every PR
    │   ├── pages.yml                     # on push to main → GitHub Pages
    │   ├── emit.yml                      # on push to main → rebuild dist/ artifacts
    │   ├── release.yml                   # on tag → publish dist/ as Release assets
    │   └── stale.yml                     # housekeeping
    ├── ISSUE_TEMPLATE/
    │   ├── new-harness.yml
    │   ├── new-pipeline.yml
    │   ├── new-rule-pack.yml
    │   ├── new-knowledge-pack.yml
    │   ├── new-tool.yml
    │   ├── bug-report.yml
    │   └── config.yml
    ├── PULL_REQUEST_TEMPLATE.md
    ├── dependabot.yml
    └── FUNDING.yml
```

## Branch & access control

- **Default branch**: `main`. Protected.
- **Required checks**: validate, build-pages, emit (must all pass).
- **Required reviews**: 1 maintainer approval (use CODEOWNERS to route
  by directory).
- **No force-push**, no direct push to `main` for non-admins.
- **Conversation resolution required** before merge.
- **Linear history** (squash merge only) so the changelog is clean.

CODEOWNERS routes catalog directories to topic maintainers:

```
catalog/harnesses/                @core-maintainers
catalog/pipelines/healthcare-*    @healthcare-maintainers
catalog/pipelines/finance-*       @finance-maintainers
catalog/pipelines/generate-image* @creative-maintainers
catalog/rule-packs/privacy/       @privacy-maintainers
schemas/                          @core-maintainers
taxonomy/SPEC.md                  @core-maintainers @standards-wg
```

## CI pipelines

### `.github/workflows/validate.yml` — every PR

```yaml
name: Validate
on:
  pull_request:
  push:
    branches: [main]
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install pyyaml jsonschema
      - run: python scripts/validate.py
      - run: python scripts/build_catalog_index.py
```

Already shipped — see `.github/workflows/validate.yml`.

### `.github/workflows/pages.yml` — Pages deploy on push to main

Already shipped. Builds catalog pages + the index.json + the static
catalog browser, then publishes `site/` to GitHub Pages via
`actions/deploy-pages@v4`.

### `.github/workflows/emit.yml` — rebuild emitter outputs

Runs the standards emitters on push to `main`:

```yaml
name: Emit standards artifacts
on:
  push:
    branches: [main]
jobs:
  emit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install pyyaml
      - run: python scripts/emit/croissant.py
      - run: python scripts/emit/mcp_server.py
      - run: python scripts/emit/agent_skill.py
      - run: python scripts/db/build_vector_index.py --embedder hash
      - uses: actions/upload-artifact@v4
        with:
          name: dist
          path: dist/
          retention-days: 30
      # On main only: commit dist/ back to a dedicated branch for marketplace consumers.
      - if: github.ref == 'refs/heads/main'
        run: |
          git config user.name  "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git checkout -B dist-published
          git add -f dist/
          git commit -m "ci: rebuild dist artifacts" || true
          git push -f origin dist-published
```

The `dist-published` branch is a stable URL for marketplace consumers:
they `git clone --branch dist-published` and get just the emitter
outputs.

### `.github/workflows/release.yml` — Releases on tag

```yaml
name: Release
on:
  push:
    tags: ['v*.*.*']
jobs:
  release:
    runs-on: ubuntu-latest
    permissions: { contents: write }
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install pyyaml jsonschema
      - run: |
          python scripts/validate.py
          python scripts/emit/croissant.py
          python scripts/emit/mcp_server.py
          python scripts/emit/agent_skill.py
          tar -czf dist-${{ github.ref_name }}.tar.gz dist/
          zip  -r  dist-${{ github.ref_name }}.zip    dist/
      - uses: softprops/action-gh-release@v2
        with:
          files: |
            dist-*.tar.gz
            dist-*.zip
          generate_release_notes: true
          fail_on_unmatched_files: true
```

Bundle naming: `dist-v0.1.0.tar.gz` includes Croissant + MCP + Agent
Skills + vector index. One archive, all standards.

## Pages deploy

`mkdocs build --site-dir site` → `actions/deploy-pages@v4`. The static
catalog browser at `docs/catalog/browser.html` is copied as-is by
MkDocs Material. The JSON-LD `@context` at `docs/ns/context.jsonld`
becomes `https://<org>.github.io/<repo>/ns/context.jsonld`.

Custom domain (optional): add `docs/CNAME` containing the apex domain
and configure the DNS A/AAAA records or CNAME per GitHub's docs.

## Releases as the canonical "downloadable hub"

Each Release ships the full `dist/` tree as both `.tar.gz` and `.zip`.
Consumers:

- **HF Hub authors**: pull the Croissant JSON for a dataset card.
- **MCP host operators**: pull `dist/mcp/` and run the stub server.
- **Claude Code users**: pull `dist/agent-skills/` and drop into `.claude/skills/`.
- **Compliance teams**: pull `dist/aibom.cdx.json` (when the CycloneDX
  emitter lands) for procurement review.

## Plugin marketplace mode

The Agent Skills emitter writes
`dist/agent-skills/.claude-plugin/marketplace.json`. Two ways to make
the repo a Claude Code plugin marketplace:

1. **Same-repo marketplace**: publish via the `dist-published` branch.
   Users: `/plugin marketplace add <owner>/<repo>@dist-published`.
2. **Companion repo**: mirror `dist/agent-skills/` to a sibling repo
   (e.g. `open-harness-hub-skills`) on every push. Cleaner separation;
   users add a shorter URL.

For non-Claude Code Agent Skills tools (Cursor, OpenHands, Gemini CLI,
Roo Code, Goose, Letta, …) the same git URL works wherever the tool
supports git-based skill installation. Each tool's docs say where its
skills folder lives; copy the folder there.

## GitHub Discussions

Enable Discussions; create categories:

- **Catalog proposals** (new harness / pipeline / rule pack ideas)
- **Q&A** (how do I…?)
- **Show and tell** (deployments, success stories)
- **Standards & taxonomy** (SPEC changes)
- **Announcements** (releases, breaking changes)

## Discoverability boosters (do these)

1. **`topics`** on the repo: `ai`, `llm`, `harness`, `rag`, `mcp`,
   `claude-code`, `agent-skills`, `pipeline`, `benchmark`, `croissant`,
   `safety`.
2. **GitHub Marketplace listing** (if the repo grows into an Actions
   provider — not urgent).
3. **`opensearch.xml`** in `docs/` so browsers expose hub search.
4. **`humans.txt`** with maintainer credit.
5. **OpenGraph metadata** via MkDocs Material plugin.
6. **A `dataset` topic** on the repo so HF and Google Dataset Search
   notice (alongside the Croissant emissions).

## Security & compliance

- `SECURITY.md` with vuln-report email + 30-day response SLA.
- `dependabot.yml` for pip + actions updates.
- **OpenSSF Scorecard** workflow (badge on README).
- **Sigstore** signing on releases (`cosign sign`); pairs with SLSA
  L2+ provenance from Actions OIDC.
- Branch protection denies force pushes and requires signed commits
  for maintainers.

## Issue & PR templates

`new-harness.yml`, `new-pipeline.yml`, `new-rule-pack.yml`,
`new-knowledge-pack.yml`, `new-tool.yml` — each prompts for the
required envelope fields (id slug, industry, capability, modality,
lifecycle, trust_boundary, license, EU AI Act risk). The PR template
links to `scripts/validate.py` and asks contributors to confirm:

- [ ] Manifest validates (`python scripts/validate.py`).
- [ ] Sample run committed (required for `stable` promotion).
- [ ] License set to MIT / Apache-2.0 / CC-BY-4.0 / CC0 or other
  redistribution-compatible SPDX identifier.
- [ ] No PII in sample data.
- [ ] Industry/capability/modality tags from controlled vocabularies.

## What happens after `git init` and first push

1. **Day 1**: create the repo at `github.com/TaylorAmarelTech/open-harness-hub`,
   push `main`, enable Pages (source = "GitHub Actions"), enable
   Discussions, enable Issues, add topics, copy in CODEOWNERS.
2. **Day 1**: CI runs `validate.yml`, `pages.yml`, `emit.yml`. Pages
   deploy lands at `https://taylorameraltech.github.io/open-harness-hub/`.
3. **Week 1**: cut `v0.1.0` tag. `release.yml` publishes
   `dist-v0.1.0.tar.gz` + `dist-v0.1.0.zip`.
4. **Week 1**: tweet / post the Claude Code plugin marketplace command:
   `/plugin marketplace add TaylorAmarelTech/open-harness-hub@dist-published`.
5. **Week 2-4**: add HF Space deploy (point HF webhook at `hf-space/`),
   add Vercel/Netlify/Cloudflare deploys via their dashboards (each
   reads `vercel.json` / `netlify.toml` / `_headers` already in repo).

## What this hosting plan deliberately doesn't include

- **Self-hosted Gitea/Forgejo**. Possible mirror, not the primary.
- **PyPI package publication**. Hold off until the catalog has a
  Python runtime that's worth publishing as a package.
- **Docker registry**. Use `ghcr.io` if/when the HF Space Dockerfile
  becomes a published image.
- **Paid GitHub features** (Enterprise, Advanced Security). Stay on the
  free tier until volume justifies otherwise.

## TL;DR

GitHub gives us, free, in this exact order: the catalog source of
truth (repo), the contributor workflow (PR + CODEOWNERS + branch
protection), the published artifacts (Releases + Actions), the static
site (Pages), the plugin marketplace (dist-published branch +
marketplace.json), and the discovery layer (topics + Discussions).
Every other deploy target (HF Spaces, Vercel, Netlify, Cloudflare
Pages) reads from this repo.
