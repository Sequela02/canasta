> Reference for `spring-boot`, formerly the `backend-api-contracts` skill.

# Backend API Contracts

Treat the wire format as a product contract. Prefer ordinary HTTP semantics and
explicit domain meaning over universal wrappers or controller conventions.

## Contract Workflow

1. Identify consumers, authority, compatibility window, data classification,
   idempotency needs, and generated artifacts.
2. Model resources and operations from domain behavior, not CRUD templates.
3. Define request, response, validation, status, error, pagination, filtering,
   concurrency, and retry semantics before implementation.
4. Update OpenAPI or the repository's canonical schema and regenerate SDKs only
   through owned tooling.
5. Add contract tests for success, validation, authorization, conflict, missing
   resources, rate limits, and representative failures.
6. Read [http-contracts.md](http-contracts.md) for detailed
   HTTP and Spring guidance.

When creating, extracting, publishing, or migrating an SDK or generated client,
read [sdk-generation.md](sdk-generation.md).

## Defaults

- Use nouns for resources and HTTP methods for common semantics, but use domain
  actions when the operation is not honest CRUD.
- Return the resource or operation result directly unless a real cross-API
  envelope contract exists. Do not introduce `{success,data,error}` by habit.
- Use RFC 9457 Problem Details for interoperable error bodies, extended with
  stable machine codes and safe validation details where needed.
- Never expose JPA entities, internal exception messages, stack traces, secrets,
  or tenant-sensitive existence information.
- Bound list sizes. Choose cursor/keyset pagination for deep or changing feeds;
  use page/offset semantics only where stable totals and random access matter.
- Use idempotency keys or conditional requests for retry-prone mutations when
  duplicate effects are unacceptable.

## Compatibility

- Prefer additive compatible evolution. Treat removed fields, renamed enum
  values, changed nullability, altered defaults, and status changes as contract
  changes.
- Version only when a real incompatible consumer boundary requires it. Use one
  strategy consistently and publish deprecation/sunset evidence.
- Keep API versions distinct from application release versions.
- Test serialization for records, enums, time, money, identifiers, errors, and
  polymorphic types against the repository's actual Jackson line.

## Gate

Verify schema linting, implementation/schema agreement, generated SDK diff,
consumer/provider tests, authorization behavior, migration sequencing, and
documentation. Report consumers that could not be exercised.
