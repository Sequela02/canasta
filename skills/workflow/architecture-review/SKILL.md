---
name: architecture-review
description: "Design or review module boundaries, dependency direction, layers, ports and who owns a contract. Use before adding a module, layer, port or cross-boundary contract, and when reviewing one. Not for business rules or domain language (domain-modeling), a library's public surface (api-design) or a whole system's design (system-design)."
tags:
  - architecture
  - design
  - review
metadata:
  source: "codebase-design by Matt Pocock, mattpocock/skills bbadaa6"
  changes: "Takes the depth, seam and adapter vocabulary, the deletion test and the one-adapter rule; adds the rejected-design record, executable dependency checks, and findings that separate confirmed from unverified"
---

# Architecture review

A boundary is worth its cost only when it protects something specific. The aim
is deep modules: much behavior behind a small interface, testable through that
interface.

## Words

- **Module**: anything with an interface and an implementation, from a function
  to a package.
- **Interface**: all a caller must know, which includes invariants, ordering,
  errors and configuration, not only the type signature.
- **Deep** module: a small interface over a lot of behavior. **Shallow**: the
  interface is nearly as complex as what it hides.
- **Seam**: the place where a module's interface lives, and where you can
  change behavior without editing the callers.
- **Adapter**: a concrete thing that satisfies an interface at a seam.

## Design a change

1. **Find the current owner** of the behavior and extend it. One owner per
   behavior.
2. **Name what a new boundary protects**: independent change, testability,
   transactional integrity or replaceable infrastructure. With none, add no
   boundary.
3. **Point dependencies at stable policy.** Domain and use-case code imports no
   framework, persistence or transport types; adapters depend on the core.
4. **Apply the deletion test** to every module, port or layer you propose or
   review: if you delete it, does the complexity vanish (a pass-through) or
   reappear in several callers (it earns its place)?
5. **One adapter is a hypothetical seam; two make it real.** Add a port, DTO or
   event for a second real consumer, a demonstrated need to vary, or a measured
   coupling problem. Until then call the concrete code.
6. **Keep each contract small and owned once**: the least data, error and
   side-effect surface the consumer needs, with no duplicated schemas.
7. **Record in the plan** the owner, the dependency direction, and one simpler
   design you rejected with the guarantee it loses. Equal guarantees: take the
   simpler design.
8. **Make a lasting rule a check.** ArchUnit, dependency-cruiser or
   import-linter fail the build; review does not
   ([starting points](../domain-modeling/references/boundary-checks.md)).

## Review a change

1. Map modules, owners, the dependency graph, runtime composition and public
   contracts. State the quality each boundary protects.
2. Trace dependencies both ways. Source imports are not the only coupling: look
   at configuration, dependency injection, registries, reflection, generated
   code, persistence, events and shared operational state.
3. Check that stable policy does not depend on volatile mechanisms, and that
   data, errors and side effects crossing a boundary have one owner. Look for
   leaked infrastructure types and duplicated schemas.
4. List cycles, duplicated policy and fan-out that nothing justifies.
5. Run the deletion test and the adapter count on each new layer.
6. Send business-language questions to `domain-modeling` and authority or
   disclosure questions to `security-scope-review`. A clean dependency graph
   proves neither.

Report findings first, most severe first, separate from style. Each finding
gives the dependency path, the triggering condition, the impact, the evidence,
and the correction. Mark each one **confirmed** (you traced it) or
**unverified** (reachability not shown). State what you did not review. When
the evidence shows no problem, say so.

## Example

A change adds `PaymentGatewayPort`, `StripeGatewayAdapter` and
`PaymentGatewayFactory` for a checkout that calls Stripe only.

- Deletion test: remove the port and factory and the checkout calls the Stripe
  client directly, with no complexity reappearing. They are pass-throughs.
- Adapter count: one adapter, so the seam is hypothetical.
- Finding: shallow layers without a second consumer. Call `stripe.charge`
  directly. Add the port when a second provider or a test double needs it.
