# Spring testing reference

## Resolve APIs from the installed line

Inspect the managed Spring Boot and test dependencies before choosing imports.
Modern Boot lines provide focused test starters and newer facilities such as
`MockMvcTester`, `RestTestClient`, and `@MockitoBean`; older supported migration
lines may require different APIs. Do not add compatibility wrappers solely to
make one test source compile across unrelated platform generations.

Official references:

- https://docs.spring.io/spring-boot/reference/testing/index.html
- https://docs.spring.io/spring-framework/reference/testing.html
- https://testcontainers.com/guides/testing-spring-boot-rest-api-using-testcontainers/

## Slice discipline

- A controller slice should prove routing, validation, serialization, status,
  headers, error contracts, and the intended security layer.
- A data slice should use the production database family when dialect, schema,
  locking, generated values, JSON, ranges, or migrations matter.
- A REST client slice should prove request construction, authentication,
  response mapping, error classification, and timeout behavior.
- A full context test should have a stated cross-layer contract that narrower
  tests cannot establish.

## Containers

- Prefer Boot service connections or the repository's explicit dynamic
  property pattern; keep lifecycle understandable.
- Match the active production database major until an explicit migration slice
  changes both tests and runtime target.
- Avoid hidden global reusable-container state in CI.
- Wait for service readiness through container-supported checks, not sleeps.

## Security tests

Exercise unauthenticated, unauthorized, wrong-tenant, expired/invalid token,
CSRF-sensitive, and permitted paths. Do not disable production method security
to simplify a slice. Use test-only principals and decoders whose claims match
the actual contract.

## Concurrency and time

Use controllable clocks for domain time. For races, coordinate competing
transactions deterministically and assert the database-backed invariant rather
than relying on timing sleeps.
