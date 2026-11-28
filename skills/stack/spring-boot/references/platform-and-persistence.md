# Platform, modules, persistence, observability

## Versions and upgrades

- Production services run on a current long-term-support Java release and a
  stable Boot line that supports it. Check the system-requirements page before
  choosing; a newer Java feature release is not automatically the target.
- Use the current build-tool release through the wrapper, and check plugins,
  bytecode tools, configuration cache, CI and IDE import before upgrading it.
- Keep exact versions in the build, wrapper and lockfiles, not in docs.

Upgrade in steps:

1. Record the wrapper, toolchain, framework, plugin, dependency and image versions
   and the public contracts.
2. Read the official migration guide and list the breaking changes that touch the
   repository.
3. Upgrade the smallest coherent slice.
4. Fix deprecations in your own code instead of suppressing them.
5. Run contract, security, persistence, container and operational checks.
6. Delete temporary migration code once all consumers have moved.

## Modules

- Organize packages by feature or bounded context, not one folder each for
  controllers, services and repositories.
- Give each module a small public API and keep implementation packages closed.
- Use events when they decouple, not to hide a synchronous call graph. Keep domain
  events separate from integration events, and translate at the outbound boundary.
- With Spring Modulith, run `ApplicationModules.verify()` in the build and add
  module tests for important collaborations. Otherwise enforce boundaries with
  ArchUnit.

## Persistence

| Need | Default |
| --- | --- |
| Aggregate lifecycle, routine transactional access | JPA adapter with explicit mapping |
| Reports, projections, bulk work, database-specific SQL | Explicit SQL or jOOQ, where adopted |
| Schema changes | Flyway or the repository's migration tool |
| Database behavior tests | Testcontainers with the production database and major |

Choose ids, enums, cascades, fetch types and pagination from the domain and the
measured queries, not from a rule. Look at the generated SQL and plan for hot paths.

## Transactions and side effects

- Transactions belong on application services.
- Use constraints and locks for invariants that span processes.
- A network call inside a transaction needs a timeout, an idempotency key and a
  defined failure state.
- Use an outbox when a committed change must lead to an external effect.
- Retry only failures you have classified as transient, outside a transaction
  already marked rollback-only, with a bounded count and a visible end state.

## Observability

- Use Actuator and Micrometer Observation; keep automatic instrumentation where it
  exists.
- Metric and trace dimensions stay low-cardinality; put per-user ids in protected
  logs only when needed.
- Propagate trace context across your own HTTP and messaging boundaries.
- Watch latency, traffic, errors, saturation, queue delay, connection-pool pressure
  and key domain operations.
- Redact credentials, tokens, payment data and personal information.
