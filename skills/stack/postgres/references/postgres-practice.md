# PostgreSQL practice

## Version posture

At the 2026-07-22 scout, PostgreSQL 18 was the current supported major and 19
was still in beta. Re-check the official supported-version and release pages
before changing the target:

- https://www.postgresql.org/docs/current/index.html
- https://www.postgresql.org/docs/release/
- https://www.postgresql.org/docs/current/upgrading.html

Keep exact patch versions in runtime configuration and images. Adopt a new
major only through an explicit data and operations migration.

## Feature selection

- Consider ordered UUID generation, temporal/range constraints, generated
  columns, enhanced `RETURNING`, skip scans, and newer monitoring views only
  when they simplify a real requirement.
- Do not assume a planner feature removes the need to design and verify indexes.
- Review authentication deprecations, extensions, collations, full-text indexes,
  checksums, wire-protocol compatibility, and replication changes during major
  upgrades.

## Plan review

Record the SQL, representative bind values, data scale, server settings relevant
to the plan, actual/estimated rows, buffers, timing, loops, sort spills, and lock
behavior. Optimize the largest evidenced cost before rewriting everything.

## Index review

- Match column order to equality, range, ordering, and selectivity evidence.
- Use partial indexes for stable hot subsets and expression indexes for stable
  canonical lookup expressions.
- Use GIN/GiST/BRIN only for access patterns they actually serve.
- Remove redundant or unused indexes only after workload evidence and rollout
  planning.

## Migration review

Classify operations by lock level, table rewrite potential, duration, disk/WAL
growth, replication effect, and rollback/recovery path. Prefer expand/migrate/
contract for changes that cannot be deployed atomically with all consumers.
