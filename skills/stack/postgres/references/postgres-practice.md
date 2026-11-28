# PostgreSQL practice

Find the supported majors and release notes at
https://www.postgresql.org/support/versioning/ and
https://www.postgresql.org/docs/release/. Keep patch versions in runtime
configuration and images, not in docs or skills.

## Recording a plan

Write down the SQL, the bind values, the data size, the settings that affect the
plan, estimated against actual rows, buffers, time, loops, sort spills and locks.
Fix the largest evidenced cost first.

## Choosing indexes

- Order columns by equality first, then range or sort, using real selectivity.
- Partial index: a stable hot subset. Expression index: a stable lookup such as
  `lower(email)`.
- GIN, GiST or BRIN only when the query uses what they serve.
- Drop an index only after watching real workload and planning the rollout.

## Reviewing a migration

For each statement note its lock level, whether it rewrites the table, how long
it takes, disk and WAL growth, the effect on replicas and how you recover.
Changes that cannot land at the same moment as every consumer use expand,
migrate, contract.

## Reviewing a major upgrade

Read the release notes for removed settings, authentication changes, extension
and collation changes. Take a backup, restore it somewhere safe, run
`pg_upgrade` or dump/restore there, and run the application's tests against it.
