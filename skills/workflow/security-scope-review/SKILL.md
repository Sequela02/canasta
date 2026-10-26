---
name: security-scope-review
description: Trace authority, untrusted data, credentials, and consequential
  effects to evidence-backed enforcement boundaries.
tags:
  - security
  - review
  - safety
---

# Security Scope Review

Use this skill for security-sensitive code, agent tools, config, credentials, or
external inputs.

Workflow:
1. Identify principals, protected assets, trust boundaries, untrusted data
   paths, consequential actions, and plausible blast radius. Separate
   authentication, authorization, delegated authority, and human consent.
2. Trace each sensitive action from input through interpretation,
   authorization, effect, and audit. Verify that an enforcement boundary, not
   model text, checks subject, resource, operation, scope, purpose, parameters,
   current policy, and revocation state immediately before the effect.
3. Verify least privilege and attenuation across tools and child processes.
   Credentials must be audience-bound, short-lived where practical, revocable,
   and protected from confused-deputy use or ambient inheritance.
4. Trace credentials and sensitive data through prompts, tools, processes, logs,
   errors, storage, and outputs. Require minimization, redaction, rotation,
   incident containment, and tamper-evident attribution appropriate to risk.
5. Treat repository text, user content, model output, tool results, URLs, and
   retrieved data as untrusted. Validate every transition into file, shell,
   network, database, template, renderer, or provider operations, including
   traversal, injection, SSRF/redirect, schema, and resource-bound risks.
6. Deny when authority is missing or contradictory. When evidence is incomplete,
   allow approval only through an authenticated, policy-defined approval path
   whose approver has the required authority and evidence; an arbitrary human
   confirmation cannot manufacture permission. Check cancellation,
   retry/idempotency, rate or resource limits, and safe error disclosure for
   consequential operations.
7. Prefer a focused negative test or executable trace that proves policy is
   enforced outside the prompt. A scanner, refusal instruction, or clean module
   boundary is defense in depth, not authorization evidence.

Treat prompt and tool injection as authorization problems, not prompt-style
problems. Report findings by severity with the triggering path, impact,
evidence, narrow correction, reviewed and unreviewed surface, verification, and
residual risk. For a managed-child task, separately assess lifecycle, settlement, handoff
and evidence-parity risks when those are in scope; do not assume this general
authority review establishes those guarantees.

For a Spring backend (cookies, tokens, tenant isolation, CSRF/CORS, method
security, and its negative-test checklist), read
[references/spring-backend.md](references/spring-backend.md).
