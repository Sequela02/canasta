# API contracts

The wire format is a product. Use ordinary HTTP semantics and your domain's words.

## Procedure

1. List the consumers, the compatibility window, the data class and any generated
   clients.
2. Model resources and operations from domain behavior. Use a domain action
   (`POST /orders/{id}/cancel`) when the operation is not plain create, read,
   update or delete.
3. Decide request, response, validation, status codes, errors, pagination,
   concurrency and retry behavior before you write the controller.
4. Update the canonical schema (OpenAPI, or the code that generates it) and
   regenerate clients with the owned tool only.
5. Write contract tests for success, validation, authorization, conflict, missing
   resource, rate limit and representative failures.

## Defaults

- Return the resource directly. Add a `{success, data, error}` envelope only if a
  real cross-API contract needs it.
- Errors use RFC 9457 Problem Details (`ProblemDetail`, `ErrorResponse`): a stable
  `type`, a safe `detail`, the request `instance`, and extension members such as a
  stable error code or field violations. Never put exception classes, stack
  traces or raw messages on the wire, and do not reveal that a tenant's resource
  exists.
- Pick the most specific standard status, and tell apart unauthenticated,
  forbidden, not found, invalid, conflict, rate limited, upstream failure and
  internal failure.
- Reject invalid state transitions with a stable conflict problem.
- For long work, return an operation resource or status endpoint instead of
  pretending it finished. Set limits, timeouts and retry safety.
- Bound list sizes. Use keyset (cursor) pagination for deep or changing lists, with
  a fixed order and a tie-breaker, and treat cursors as opaque. Offset pages suit
  small lists that need totals. Map Spring Data `Page` to your own response type.
- Give retry-prone mutations an idempotency key or a conditional request.
- Use stable external ids chosen for the domain and exposure; UUIDs are not
  mandatory.

## Compatibility

- Prefer adding fields. Removing a field, renaming an enum value, changing
  nullability, defaults or a status is a breaking change.
- Version only when an incompatible consumer forces it, one way, with deprecation
  and sunset information. Spring Framework 7 supports API versioning by path,
  header, query parameter or media type; do not add `/v1` ahead of need. API
  versions are separate from release versions.
- Test serialization of records, enums, time, money, ids, errors and polymorphic
  types against the Jackson version the project uses.

## OpenAPI and SDKs

Keep one canonical contract. Check that security schemes, required and nullable
fields, examples, errors, pagination and deprecations match runtime behavior.
Generated output is an artifact: no hand edits. For client generation see
[sdk-generation.md](sdk-generation.md).

## Gate

Run schema lint, check the implementation against the schema, diff the generated
SDK, run consumer and provider tests and authorization cases, and plan the
migration order. Name any consumer you could not exercise.

Docs: Spring Framework reference, "Error Responses" and "API Versioning"; RFC 9457.
