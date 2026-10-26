---
name: postgres
description: "Change or diagnose PostgreSQL schemas, queries, indexes, locks, migrations, backups, or upgrades."
---

# PostgreSQL

Keep the schema simple, enforce cross-process invariants in the database, and
optimize from measured plans rather than folklore.

## Establish The Database Contract

1. Identify the production major, extensions, collation, driver, pooler,
   migration tool, backup/restore path, replicas, and Testcontainers image.
2. Use that active major for changes and tests unless an explicit upgrade slice
   changes it, and take the target major from that slice.
3. Read [references/postgres-practice.md](references/postgres-practice.md) for
   modeling, query, migration, and operational guidance.
4. Separate application migration, database-major upgrade, and production data
   repair into independently verifiable slices.

## Modeling And Integrity

- Normalize first; denormalize only for a measured access path with an owner.
- Choose identifiers from domain and distribution requirements. Do not mandate
  UUIDs or sequences universally.
- Use `TIMESTAMPTZ` for instants, exact numeric types for money, and JSONB only
  for data whose shape or querying justifies it.
- Use `NOT NULL`, foreign keys, unique/check/exclusion constraints, and ranges
  for invariants that must survive concurrent processes.
- Add supporting indexes for real predicates, joins, ordering, tenant filters,
  and foreign keys. Every index adds write and maintenance cost.

## Queries And Concurrency

- Capture representative parameters and use `EXPLAIN (ANALYZE, BUFFERS)` for
  high-cost or high-volume queries in a safe environment.
- Prefer keyset pagination for deep ordered traversal; use offset pagination
  when bounded pages and totals are genuinely required.
- Address races with constraints, atomic statements, locks, isolation, or
  idempotency keys. An application check followed by a write is not protection.
- Keep transactions short and make lock ordering, retry behavior, and timeout
  handling explicit.

## Migrations And Operations

- Write forward migrations that are deterministic and safe for the deployment
  sequence. Operational recovery comes from rehearsed backup/restore or rollout
  strategy, not a fictional universal down migration.
- Add preflight queries for legacy values, nullability, duplicates, enum/state
  changes, ownership keys, and expensive rewrites.
- Rehearse risky migrations on production-shaped isolated data and record
  duration, locks, storage growth, and recovery behavior.
- A major upgrade requires extension/driver review, backup and restore or
  `pg_upgrade` rehearsal, collation/index checks, replication review, and
  observed application compatibility.

## Verification

- Run migration-from-baseline and migration-from-supported-production-state.
- Use Testcontainers for dialect, constraint, JSONB, range, lock, isolation,
  generated-column, and Flyway behavior.
- Verify hot plans, concurrency cases, backup/restore evidence, and monitoring.
- Report exactly what was exercised; do not equate compilation with database
  readiness.

