---
name: spring-boot
description: "Build Spring Boot backends in Java or Kotlin: package and module layout, transactions, JPA vs SQL, configuration, REST API design, security wiring, observability, tests and version upgrades. Use when editing Java or Kotlin backend code, a Gradle or Maven build, or application.yml."
paths: ["**/*.java", "**/*.kt", "**/pom.xml", "**/build.gradle*", "**/application*.yml", "**/application*.properties"]
---

# Spring Boot

Use the platform the way the repository already does, and use the versions it
pins. Version-specific questions go to the docs for those versions:
`docs.spring.io/spring-boot` for Boot, `docs.spring.io/spring-framework` for the
framework, and the system-requirements page for Java and build-tool support.

## Procedure

1. Read the build file, the wrapper, `application*.yml` and the package layout.
   Find the installed Boot, Spring Framework and Java versions, the persistence
   approach and the test setup.
2. Place the change: domain rule, application service, adapter (web, persistence,
   client) or configuration. Keep domain code free of Spring, JPA, Jackson and HTTP
   types, and put transaction boundaries on application services.
3. Constructor injection, immutable configuration, and records for DTOs and small
   values. Bind settings with a validated `@ConfigurationProperties` class; make
   security settings fail startup when missing.
4. Map between transport, domain and persistence models. Do not return JPA
   entities or raw exception messages from an endpoint.
5. For the database use the repository's choice: JPA for aggregates and routine
   transactional access, explicit SQL or jOOQ for reports and bulk work. Migrations
   go through Flyway or the owned tool, never schema auto-generation in production.
6. Keep transactions short and never hold one open across a slow remote call. For a
   side effect that must happen after commit, use an outbox or durable event and
   make retries idempotent.
7. Test at the narrowest layer that proves the behavior (see testing reference),
   then run the repository's build gates. If packaging or startup files changed,
   start the container image.

## Example

An endpoint creates an order and calls a payment provider.

Bad: `@Transactional` on the controller, with the payment HTTP call inside the
transaction. A slow provider holds a database connection, and a failure after the
charge leaves no record.

Good: the application service saves the order and an outbox row in one short
transaction. A worker calls the provider with an idempotency key and records the
result; the order moves to a visible `PAYMENT_PENDING` or `PAID` state.

## Choose by need

| Work | Read |
| --- | --- |
| Boot or Java upgrade, modules, observability | [references/platform-and-persistence.md](references/platform-and-persistence.md) |
| REST resources, errors, pagination, versioning, OpenAPI | [references/api-contracts.md](references/api-contracts.md) |
| Choosing tests, slices, Testcontainers, security tests | [references/testing.md](references/testing.md) |
| Generating or publishing an SDK from the API | [references/sdk-generation.md](references/sdk-generation.md) |
| SQL, indexes, locks, Flyway data migrations | the `postgres` skill |
| Auth, tenant isolation, CSRF, CORS, secrets | the `security-scope-review` skill |
| Domain rules and boundaries | `domain-modeling`, `architecture-review` |

## Guardrails

- Prefer starters and the Boot-managed dependency versions; pin one only with a
  compatibility or security reason, written next to it.
- Use Spring MVC with `RestClient` for blocking services. Do not mix Reactor into a
  blocking JDBC request path without an end-to-end need.
- Turn on virtual threads only after checking the workload (blocking I/O), limiting
  concurrency to scarce downstreams and comparing under load.
- Do not put secrets, tokens, personal data or unbounded identifiers in metric
  labels or logs.
- Remove a compatibility path once its consumer or migration window is over.
- Before you call an upgrade done, run API contract tests, persistence, security,
  migrations and the packaged image, and list any you could not run.
