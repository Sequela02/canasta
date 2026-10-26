# Persistence and operations

## Persistence selection

| Need | Default |
| --- | --- |
| Aggregate lifecycle and ordinary transactional access | JPA adapter with explicit mapping |
| Complex reporting, projections, bulk work, database-specific SQL | Explicit SQL or jOOQ where adopted |
| Schema evolution | Flyway or repository-owned migration tool |
| Database behavior tests | Testcontainers using the production database family and active major |

Avoid universal ID, enum, cascade, fetch, or pagination rules. Choose them from
domain identity, public exposure, cardinality, lifecycle, and measured query
behavior. Always inspect generated SQL and query plans for hot paths.

## Transactions and side effects

- Place transaction boundaries in application services.
- Use database constraints and locking for invariants shared across processes.
- Treat network calls inside transactions as a risk requiring timeout,
  idempotency, and failure-state design.
- Use an outbox or durable event publication when a committed state change must
  eventually produce an external effect.
- Retry only classified transient failures, outside a transaction already
  marked rollback-only, with bounded attempts and observable exhaustion.

## Observability

- Use Actuator and Micrometer Observation for service health and meaningful
  operations. Prefer automatic instrumentation where it already exists.
- Use low-cardinality dimensions for metrics and traces. Put high-cardinality
  identifiers in appropriately protected logs or trace fields only when needed.
- Propagate trace context across owned HTTP and messaging boundaries.
- Define service-level signals for latency, traffic, errors, saturation, queue
  delay, connection-pool pressure, and critical domain operations.
- Redact credentials, tokens, payment data, and personal information.

Official reference:

- https://docs.spring.io/spring-boot/reference/actuator/observability.html
- https://docs.spring.io/spring-boot/reference/actuator/metrics.html
