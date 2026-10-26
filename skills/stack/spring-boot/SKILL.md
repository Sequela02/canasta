---
name: spring-boot
description: "Implement or review Java/Spring backend services, transactions, persistence adapters, configuration, and operations, and route API, security, PostgreSQL, and testing work to their references and skills."
---

# Spring Boot Backend

Use the platform deliberately. Do not turn a version bump into an architectural
rewrite or encode exact patch versions in this skill.

## Relevant Evidence

1. Inspect the build or runtime configuration needed by the change. Toolchain
   upgrades need wrapper, dependency, image, and CI evidence; ordinary service
   edits can reuse the established platform context.
2. Use the repository's installed versions for implementation. Take target
   versions only from an explicit upgrade request or a written project standard.
3. Read [references/platform-and-architecture.md](references/platform-and-architecture.md)
   for runtime selection, modernization, modules, and framework rules.
4. Read [references/persistence-and-operations.md](references/persistence-and-operations.md)
   for JPA/SQL selection, transactions, integrations, and observability.
5. Load the related skills below only when the change crosses their contracts.

## Related Skills

| Work | Load |
| --- | --- |
| PostgreSQL schema, SQL, indexes, locks, query plans, Flyway data migration, database upgrade | `postgres` |
| REST resource design, DTOs, errors, pagination, compatibility, OpenAPI, API versioning | [references/api-contracts.md](references/api-contracts.md) |
| Authentication, authorization, tenant isolation, cookies/tokens, CSRF/CORS, secrets, abuse controls | `security-scope-review` with its Spring backend reference |
| Unit, architecture, slice, integration, contract, migration, container, or regression tests | [references/testing.md](references/testing.md), with `tdd` for test-first discipline |
| Domain model or module boundaries | `architecture-review` |
| Behavior-preserving cleanup | `refactor` |
| Stripe integration | Stripe's official integration guidance; keep domain orchestration in the backend boundary |

A new authenticated endpoint with a schema change needs Spring, API, security,
PostgreSQL, and testing guidance; a pure domain invariant needs none of them.
Prefer platform components the repository has already adopted, such as an adopted platform component,
over building a parallel one.

## Architecture Invariants

- Domain code has no Spring, JPA, Jackson, HTTP, or migration annotations.
- Application services own use-case orchestration and transaction boundaries;
  domain types own business invariants.
- Adapters translate transport and persistence models instead of exposing JPA
  entities or infrastructure exceptions as public contracts.
- Bounded contexts communicate through explicit application contracts or
  events, not direct access to another context's entities and repositories.
- Prefer a modular monolith. Use Spring Modulith or ArchUnit for executable
  module boundaries when the repository adopts them; do not add either as
  decorative architecture.
- Delete compatibility paths after their documented consumer or migration
  window ends.

## Spring And Java Posture

- Prefer constructor injection, immutable configuration, records for transport
  DTOs and small values, sealed types only when the closed hierarchy is real,
  and exhaustive handling for domain states.
- Use typed, validated `@ConfigurationProperties`; fail closed for security,
  authority, and governance configuration.
- Prefer focused Boot starters and Boot-managed dependency versions. Pin only
  with an evidenced compatibility or security reason.
- Use Spring MVC and `RestClient` for ordinary blocking services. Do not mix
  Reactor into a blocking JDBC request path without an end-to-end need.
- Use virtual threads only for compatible blocking I/O workloads. Protect
  scarce downstream resources with explicit concurrency limits and validate
  behavior with JFR, metrics, and load evidence.
- Treat preview features as opt-in experiments unless the repository explicitly
  enables and tests them.

## Persistence And Side Effects

- Keep JPA entities in infrastructure and map them to domain models.
- Choose JPA for aggregate persistence and routine transactional access; use
  explicit SQL or jOOQ for query-heavy/read-model work only where adopted.
- Keep transactions narrow. Never hold a database transaction open across a
  slow remote call without a demonstrated consistency design.
- Make retries, idempotency, outbox/event publication, and observable failure
  states explicit for external side effects.
- Use Flyway or the repository's owned migration tool; never production DDL
  auto-generation.

## Runtime And Verification

- Expose meaningful health, readiness, metrics, traces, and structured logs.
  Never put secrets, tokens, personal data, or unbounded identifiers in labels.
- Keep wrapper, toolchain, CI, builder image, runtime image, and docs aligned.
- Run focused compilation/tests first, then repository quality and build gates.
- When platform files change, verify the container image and startup path.
- Do not claim migration readiness without testing API contracts, persistence,
  security, migrations, runtime packaging, and the affected production path.

