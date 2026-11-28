---
name: security-scope-review
description: Review an endpoint, tool or config for security holes, such as authorization gaps, leaked API tokens and credentials, unvalidated untrusted input, injection, SSRF and over-broad permissions. Traces each risky action to the code that enforces it.
license: Complete terms in NOTICE
metadata:
  source: "security-and-hardening by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "Threat-model-first step and the rule that trust follows who wrote a value are adapted; the enforcement-boundary trace, the evidence rules and the Spring reference are canasta's"
tags:
  - security
  - review
  - authorization
---

# Security scope review

For each action that can hurt someone, find the line of code that stops the wrong
caller. If you can't point at it, report a finding. A scanner pass, a refusal in a
prompt or a tidy module boundary is not that line.

## Procedure

1. **Map the surface.** List who calls (principals), what is worth stealing or
   breaking (assets), and where untrusted data enters: HTTP input, uploads,
   webhooks, third-party responses, model output, repository text, and values
   another process wrote. Trust follows who wrote a value, not the channel that
   delivered it.
2. **Trace each risky action** from input to effect: input, parsing, the
   authorization check, the effect, the log line. Write the trace as
   `route -> handler -> check at file:line -> effect`.
3. **Check authorization, not only login.** Right before the effect, does the
   code compare this caller with this resource, this operation and the current
   policy? Authenticated is not authorized. A check in the UI or in a prompt
   doesn't count.
4. **Check credentials.** Follow each token and secret through prompts, logs,
   errors, storage and child processes. Each should be scoped to one audience,
   short-lived where possible, revocable, and absent from output.
5. **Check every hop from untrusted data** into a file path, shell command, SQL
   or template, outbound URL, or renderer: traversal, injection, SSRF and
   redirects, size limits.
6. **Check the failure paths.** Missing or contradictory authority means deny.
   Look at retries, cancellation, rate limits and error messages that reveal
   internals.
7. **Prove it.** Write a negative test that fails without the check: user B
   requests user A's resource and gets 403 or 404. If you can't run it, mark the
   finding unverified.

Prompt injection is an authorization problem. Ask what the tool is allowed to do
when the text it read is hostile, and enforce that outside the prompt.

## Example

Request: "Review this endpoint for authorization holes."

```
GET /invoices/:id
  handler: loads Invoice by id, returns it
  check:   requireLogin() only (auth.ts:12)
```

Finding, high: any logged-in user can read any invoice by changing `:id` (IDOR).
Fix: load with `where id = :id and org_id = session.orgId`; return 404 on a miss.
Test: user from org B requests an org A invoice id and expects 404. Unverified
until that test runs.

## Report

Findings by severity, each with the trigger path, impact, evidence (file:line or
the failing test), and the smallest fix. Then what you reviewed, what you
didn't, and the checks you ran. For a Spring backend (cookies, tokens, tenant
isolation, CSRF, CORS, method security), read
[references/spring-backend.md](references/spring-backend.md).
