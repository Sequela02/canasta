---
name: postgres
description: "Design PostgreSQL schemas, write safe migrations, and speed up slow queries, locks and races. Use when editing SQL or migrations, adding an index or constraint, reading EXPLAIN output, or planning a backup, restore or major upgrade."
paths: ["**/*.sql", "**/db/migration/**"]
---

# PostgreSQL

Let the database enforce what must always be true, and change it from measured
plans, not habit.

For a long rule-by-rule checklist (indexes, RLS, connection pooling, locking),
use Supabase's `supabase-postgres-best-practices` skill (MIT, works on any
Postgres) or the Postgres docs for the major version you run.

## Procedure

1. Find what runs in production: the major version, extensions, the driver,
   pooler and migration tool, and how backups are restored. Write and test
   against that major, in the same image your tests use.
2. For a schema change, state each rule the data must obey and put it in the
   database: `NOT NULL`, foreign keys, `UNIQUE`, `CHECK`, exclusion constraints.
   An application check followed by a write races; a constraint does not.
3. Pick types by meaning: `timestamptz` for instants, `numeric` for money,
   `text` for strings, `jsonb` only for data that really varies in shape.
   Normalize first. Choose identifiers from the domain, not by habit.
4. Index the predicates, joins, orderings and foreign keys that queries use.
   Each index slows writes, so tie each one to a query.
5. For a slow query, run `EXPLAIN (ANALYZE, BUFFERS)` with real parameter
   values on production-sized data, fix the largest cost, and run it again.
6. For a migration, label every statement with its lock and whether it rewrites
   the table, then follow "Safe migrations" below. Run it from a baseline schema
   and from a copy of the supported production state, and record duration and locks.
7. Say what you ran. Compiling the application does not show the database works.

## Safe migrations

Migrations move forward. Recovery comes from tested backups and expand, migrate,
contract rollouts, not from a down script nobody ran.

Example: add a required `status` column to a large `orders` table.

Bad:

```sql
ALTER TABLE orders ADD COLUMN status text NOT NULL;
```

It fails on existing rows. The "fix" of backfilling and then `SET NOT NULL` in
one transaction holds a lock that blocks writes while it scans the table.

Good, in separate deployable steps:

```sql
SET lock_timeout = '2s';
ALTER TABLE orders ADD COLUMN status text;                 -- instant
-- application starts writing status; backfill in batches
ALTER TABLE orders ADD CONSTRAINT orders_status_nn
  CHECK (status IS NOT NULL) NOT VALID;                    -- brief lock
ALTER TABLE orders VALIDATE CONSTRAINT orders_status_nn;   -- scans, writes continue
ALTER TABLE orders ALTER COLUMN status SET NOT NULL;       -- uses the check, no scan
ALTER TABLE orders DROP CONSTRAINT orders_status_nn;
```

Other habits: `CREATE INDEX CONCURRENTLY` on live tables (outside a transaction);
a preflight query for duplicates or bad values before adding a constraint;
`lock_timeout` on every DDL statement so it fails instead of queueing behind a
long transaction and blocking everyone behind it.

## Concurrency

- Keep transactions short. Fix a lock order, set timeouts, and retry on
  serialization failure and deadlock.
- Make writes idempotent with a unique key or `INSERT ... ON CONFLICT`.
- Page deep result sets with keyset pagination (`WHERE (created_at, id) < ($1, $2)`);
  use offset only for small bounded pages.

## Major upgrades

Treat an upgrade as its own change, separate from application migrations and
from data repair. Check extensions and the driver, collation and index
compatibility, and replication. Rehearse a restore or `pg_upgrade` on a copy,
and run the application against it. See
[references/postgres-practice.md](references/postgres-practice.md).
