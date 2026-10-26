# Spring security practice

## Authority design

- Document the issuer of identity, issuer of permissions, tenant membership
  source, role/scope mapping, revocation model, and cache/failure behavior.
- Keep resource server, OAuth2 client/login, and authorization server roles
  distinct. Do not create an authorization server inside an application merely
  because it needs to validate access tokens.
- Use method or application-layer authorization for use-case decisions and
  repository scoping for defense in depth.

Official reference:

- https://docs.spring.io/spring-security/reference/servlet/oauth2/index.html
- https://docs.spring.io/spring-security/reference/servlet/authorization/method-security.html

## Common review paths

- Horizontal and vertical privilege escalation.
- Cross-tenant identifiers and existence leaks.
- Mass assignment and unsafe DTO-to-entity binding.
- SQL/command/template injection and unsafe dynamic query fragments.
- SSRF, open redirects, webhook origin/signature validation, and file uploads.
- CSRF, CORS, cookie flags, session fixation, logout and token revocation.
- Password/key storage, rotation, algorithms, randomness, and error timing.
- Deserialization, polymorphic types, oversized payloads, archive bombs, and
  unbounded pagination or export work.
- Actuator/management exposure, debug endpoints, structured-log leakage, and
  high-cardinality denial-of-service.
- Dependency advisories, unsupported components, and insecure build plugins.

## OAuth2 resource servers

Validate JWT or opaque tokens through Spring Security's supported resource
server mechanisms. Validate issuer and intended audience where applicable, map
authorities deliberately, and test claim absence and malformed claim types.
Prefer authority names that reflect the external contract rather than silently
rewriting every provider's role model.

## Errors and observability

Return stable unauthenticated/forbidden problem contracts without revealing
whether a protected resource exists. Record security-relevant events with
correlation and outcome, but redact secrets and personal data. Metrics should
use bounded dimensions.

