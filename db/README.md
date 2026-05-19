# Database mappings — Open Harness Hub

This directory defines how every Open Harness Hub manifest persists in
real databases. The canonical schema is **PostgreSQL** (`postgres/schema.sql`);
the other backends derive from it.

| File | Backend | Use |
|---|---|---|
| `postgres/schema.sql` | PostgreSQL / SQLite | Canonical relational store. |
| `mongodb/collections.md` | MongoDB / Couchbase / Firestore | Document store. |
| `redis/keys.md` | Redis / DynamoDB | Runtime cache & ephemeral run state. |
| `vector/spec.md` | Pinecone / Weaviate / Qdrant / Chroma / pgvector | Catalog semantic search + RAG retrieval. |

## Why four backends

| Workload | Best fit |
|---|---|
| "Find every `harness` in industry `healthcare` with capability `extraction`" | Relational. Fast index scans, joinable. |
| "Give me the full manifest of `harness/text-safety-review`" | Document. One read, no joins. |
| "Was this pipeline run cached in the last hour?" | Key-value. Sub-millisecond. |
| "Find similar rule packs to mine" / RAG retrieval | Vector. Approximate-nearest-neighbor. |

Most real deployments use **two**: PostgreSQL + pgvector (or PostgreSQL +
Pinecone/Weaviate). Redis is a nice-to-have for high-throughput hosted
catalogs.

## Loaders

`scripts/db/` (planned) contains:

- `load_postgres.py` — read every YAML manifest under `catalog/`, validate,
  insert into the PostgreSQL schema.
- `load_mongodb.py` — same, but into MongoDB collections.
- `build_vector_index.py` — produce embeddings for the catalog and
  knowledge indexes; write to the configured vector backend.

All loaders are idempotent: rerunning them updates rows by `id` rather
than inserting duplicates.
