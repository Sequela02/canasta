> Reference for `security-scope-review`, formerly the `backend-security` skill.

# Backend Security

Fail closed and prove the denied paths. Security decisions belong at explicit
boundaries and must remain consistent across HTTP, application, and data access.

## Security Workflow

1. Identify assets, actors, trust boundaries, entry points, authority source,
   tenant scope, sensitive data, and failure consequences.
2. Trace untrusted input from transport through authorization and persistence
   to every side effect.
3. Reuse an adopted platform component and owned security components where adopted. Do not implement a
   second JWT, session, lockout, cookie, or protection model locally.
4. Apply authentication and coarse request policy at the edge, then enforce
   use-case ownership and tenant authorization before data access or mutation.
5. Add negative tests for missing, invalid, expired, wrong-role, wrong-owner,
   wrong-tenant, replayed, forged, and abuse-rate cases.
6. Read [spring-security-practice.md](spring-security-practice.md)
   for detailed controls and review questions.

## Invariants

- Authentication proves an identity; it does not grant access by itself.
- Never trust tenant, organization, role, price, ownership, or state supplied
  by a client without authoritative validation.
- Scope repository queries by authorized tenant/owner where possible and still
  enforce database integrity. Avoid fetch-then-check leaks.
- Validate input shape and business constraints at boundaries. Parameterize SQL
  and restrict dynamic identifiers to allowlists.
- Keep secrets in an owned secret system; never log or return credentials,
  tokens, cookies, payment data, or raw personal data.
- Protect expensive and sensitive operations with rate limits, bounded work,
  timeouts, request-size limits, and idempotency where applicable.
- Deny by default when issuers, audiences, keys, policy data, or authority
  configuration is absent or ambiguous.

## Browser And Token Posture

- Choose server session/cookie, OAuth2 client, or resource-server token flows
  from the actual client and authority model.
- For browser cookies, set Secure, HttpOnly, appropriate SameSite, narrow Path
  and Domain, rotation, expiry, and CSRF protection consistent with the flow.
- For bearer tokens, validate signature, issuer, audience, time claims, and the
  required scopes/authorities. Do not treat decoded claims as validated.
- Keep CORS an explicit allowlist and remember that CORS is not authorization.

## Gate

Run focused authorization and tenant-isolation tests, dependency/secret scans
available to the repository, security configuration startup checks, and the
broader backend gates. Report any production identity provider, key rotation,
WAF/rate limit, or infrastructure control not exercised locally.

