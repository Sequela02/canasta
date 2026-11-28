# Testing a Spring Boot service

Prove behavior and production risk with the smallest test that exercises the real
contract. Chase risks, not a coverage number.

## Pick the boundary

| Contract | Test |
| --- | --- |
| Domain rule or state transition | Plain JUnit, no Spring |
| Application orchestration and ports | Plain test with fakes or a few mocks |
| Module dependency rules | Spring Modulith or ArchUnit, where adopted |
| Controller routing, validation, status, errors, security | MVC slice (`@WebMvcTest`) |
| JSON shape | JSON slice or a mapper contract test |
| JPA mapping, queries, constraints, locks, migrations | Data slice or integration test on PostgreSQL via Testcontainers |
| Outbound HTTP client | REST client slice plus a provider contract fixture |
| Startup or cross-adapter flow | `@SpringBootTest`, only when smaller tests cannot prove it |
| Public SDK, event or API compatibility | Consumer and provider or schema contract test |

## Procedure

1. Name the behavior, who relies on it, how it can fail and what you can observe.
2. For a bug, write the smallest failing test first.
3. Match what the contract needs from production: database, serialization,
   security, clock.
4. Keep fixtures synthetic, minimal and visible in the test.
5. Assert public behavior, stored state, emitted events and side effects, not
   private details.
6. Run the focused test, then the module, then the repository gates; report any
   Docker or provider dependency you could not run.

## Spring specifics

- Resolve test APIs from the installed Boot line before writing imports. Recent
  lines offer focused test starters, `MockMvcTester`, `RestTestClient` and
  `@MockitoBean`; do not write wrappers to compile across unrelated generations.
- A controller slice must prove routing, validation, serialization, status,
  headers, error bodies and the real security layer. A data slice uses the
  production database when dialect, locking, JSON, ranges or migrations matter.
- Containers: prefer Boot service connections or the repository's dynamic-property
  pattern, match the production database major, avoid hidden shared containers in
  CI, and wait on container readiness rather than sleeping.
- Security: cover unauthenticated, unauthorized, wrong-tenant, expired or invalid
  token, CSRF-sensitive and allowed paths. Do not switch off method security to
  simplify a slice; use test principals whose claims match the real contract.
- Time and races: inject a clock. For races, run competing transactions in a
  controlled order and assert the database invariant, never a sleep.

## High-risk cases to cover

- Tenant isolation, ownership checks and denied paths.
- Webhook signatures, idempotency, retries, ordering and state changes for payments.
- Bookings, inventory, expiry, clocks and concurrent conflicts.
- Flyway preflights, migration from supported states and startup failure.
- JSON for records, enums, time, money, errors, pagination and SDK DTOs.
- Timeouts, unavailable dependencies, partial failure, retry exhaustion, recovery.

## Test quality

- Name tests after behavior.
- Mock external boundaries, not the rules under test, and do not assert call counts
  unless the call is the contract.
- Keep repeated setup visible until a factory removes real noise.
- A quarantined flaky test is debt with an owner and a removal condition.

Docs: Spring Boot "Testing", Spring Framework "Testing", Testcontainers' Spring Boot guides.
