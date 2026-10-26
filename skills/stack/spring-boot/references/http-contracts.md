# HTTP contract practice

## Resource and operation design

- Use stable external identifiers chosen by domain and exposure requirements;
  do not mandate UUIDs for every resource.
- Distinguish commands with meaningful state transitions from partial document
  updates. Reject invalid transitions with a stable conflict/problem contract.
- For asynchronous work, return an operation resource or documented status
  endpoint rather than pretending completion.
- Define request limits, timeouts, retry safety, and cancellation behavior for
  expensive operations.

## Status and errors

Use the most specific standard status that matches the contract. Distinguish
authentication, authorization, absence, validation, conflict, rate limiting,
upstream failure, and internal failure without leaking protected information.

Spring Framework supports `ProblemDetail` and `ErrorResponse` for RFC 9457.
Use stable absolute or documented relative problem types, a safe human detail,
the request instance, and extension members such as a stable error code or
field violations. Do not put exception classes or raw messages on the wire.

- https://docs.spring.io/spring-framework/reference/web/webmvc/mvc-ann-rest-exceptions.html
- https://www.rfc-editor.org/rfc/rfc9457.html

## Versioning and deprecation

Spring Framework 7 supports resolving API versions from path, header, query, or
media type, mapping methods by version, client insertion, and standard
deprecation/sunset headers. Select one strategy only when incompatible evolution
requires it; do not create `/v1` preemptively.

- https://docs.spring.io/spring-framework/reference/web/webmvc-versioning.html

## Pagination

- Enforce maximum page size at the boundary.
- Define deterministic ordering and a stable tie-breaker.
- Treat cursors as opaque and validate their scope/filter association.
- Avoid serializing Spring Data `Page` or persistence models as the permanent
  public contract; map to owned response DTOs and pagination metadata.

## OpenAPI

Keep one canonical contract source per API. Verify that security schemes,
required/nullability semantics, examples, errors, pagination, webhooks, and
deprecations match runtime behavior. Generated output is an artifact, not a
second hand-edited authority.
