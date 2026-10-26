> Reference for `spring-boot`, formerly the `backend-testing` skill.

# Backend Testing

Prove behavior and production risk with the narrowest test that exercises the
real contract. Do not optimize for a universal coverage percentage.

## Select The Test Boundary

| Contract | Preferred test |
| --- | --- |
| Domain invariant or state transition | Plain managed JUnit, no Spring |
| Application orchestration and ports | Plain test with fakes or focused mocks |
| Module dependency rules | Spring Modulith or ArchUnit when adopted |
| Controller HTTP semantics and security | MVC slice with the repository's current Boot test starter |
| JSON contract | JSON slice or explicit mapper contract test |
| JPA mapping, query, constraint, lock, migration | Data slice or integration test with PostgreSQL Testcontainers |
| Outbound HTTP adapter | REST client slice plus provider contract fixture |
| Full startup or cross-adapter flow | `@SpringBootTest` only when smaller tests cannot prove it |
| Public SDK/event/API compatibility | Consumer/provider or schema contract test |

Read [spring-testing.md](spring-testing.md) when choosing
Boot annotations, clients, mocks, or container wiring.

## Workflow

1. Name the behavior, consumer, failure mode, and observable result.
2. Reproduce a bug with the smallest failing test when practical.
3. Match the production database, serialization, security, clock, and runtime
   behavior needed by the contract.
4. Keep fixtures synthetic, portable, minimal, and explicit.
5. Assert public behavior, persisted state, emitted events, and side effects;
   avoid private implementation details.
6. Run the focused test; widen to module or repository gates when affected
   contracts or repository requirements justify them.

## High-Risk Coverage

- Tenant and organization isolation, ownership checks, and denied paths.
- Payment/webhook signatures, idempotency, retries, ordering, and state changes.
- Booking, inventory, admission, expiration, clocks, and concurrent conflicts.
- Flyway preflights, migration from supported states, and startup failure.
- JSON records, enums, time, money, errors, pagination, and SDK-facing DTOs.
- Logs, metrics, and traces for critical operations without secret or
  high-cardinality leakage.
- Timeouts, unavailable dependencies, partial failures, retry exhaustion, and
  recovery behavior.

## Test Quality

- Prefer behavior names over framework-oriented names.
- Mock external boundaries, not the business rules being tested.
- Avoid overspecified interaction counts unless the call itself is the contract.
- Keep repeated setup visible until a fixture or factory removes substantial
  noise without hiding the scenario.
- Quarantine is temporary debt with an owner and removal condition, never a
  permanent answer to flaky tests.
- Coverage reports are navigation aids. Missing risk coverage matters more than
  an arbitrary percentage.

## Gate

Use repository-defined commands. Typical Gradle sequencing is a specific test,
the owning test task, integration or architecture tests, quality gates, build,
and container smoke verification when packaging changed. Report unavailable
Docker/provider/system dependencies as residual risk.

