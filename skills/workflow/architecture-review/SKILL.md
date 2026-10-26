---
name: architecture-review
description: Design or review module boundaries, dependency direction, runtime
  coupling, and contract ownership without speculative abstraction, with a
  conditional domain and aggregate lens. Use before adding a module, layer, port,
  or cross-boundary contract, and when reviewing one.
tags:
  - architecture
  - clean-architecture
  - design
  - review
---

# Architecture Review

Use this skill when designing or evaluating architecture, module ownership, or
cross-surface changes.

When the change touches business rules, invariants, aggregate scope or domain
language, also apply the [domain boundaries lens](references/domain-boundaries.md).
It is conditional: do not impose DDD structure on code without such rules.

## Designing a change

Use before writing code that adds a module or layer, crosses a boundary, or
introduces a contract.

1. Find the current owner of the behavior and extend it before creating a new
   one. Keep one owner per behavior.
2. Name the quality a new boundary protects: independent change, testability,
   transactional integrity, or replaceable infrastructure. Without one, add no
   boundary.
3. Point dependencies toward stable policy. Domain and use-case code does not
   import framework, persistence, or transport types; adapters depend on the
   core, never the reverse.
4. Add a port, DTO, adapter, or event only for a second real consumer,
   demonstrated volatility, or a measured coupling problem. Otherwise call the
   concrete code directly.
5. Keep each contract minimal and owned in one place: the smallest data, error,
   and side-effect surface the consumer needs, with no duplicated schemas.
6. State in the plan the owner, the dependency direction, and one simpler design
   you rejected with the guarantee it loses. When guarantees are equal, choose
   the simpler design.
7. When a dependency rule must hold permanently, add an executable check (for
   example ArchUnit or dependency-cruiser) instead of relying on review.

## Reviewing a change

Workflow:
1. Map the intended modules, policy owners, dependency graph, runtime
   composition, and public contracts. Name the quality the boundary protects,
   such as independent change, testability, transactional integrity, or
   replaceable infrastructure.
2. Trace causal dependency paths in both directions. Distinguish source
   dependency from runtime control flow and inspect hidden coupling through
   configuration, dependency injection, registries, reflection, generated code,
   persistence, callbacks, events, and shared operational state.
3. Verify that stable policy does not depend on volatile mechanisms and that
   cross-boundary data, errors, state, and side effects have a named owner and a
   minimal contract. Inspect public exports and whether infrastructure types or
   duplicated schemas leak across the boundary.
4. Identify cycles, duplicated policy or projection ownership, and unjustified
   fan-out. Require executable architecture checks when a durable dependency
   rule can be mechanized.
5. Apply a minimum sufficient complexity gate to material architecture. Name the
   invariant or demonstrated outcome, the simplest viable mechanism, one simpler
   rejected design and the guarantee it loses, concepts added and removed, new
   durable state or lifecycle, exported complexity, and deterministic evidence.
   Prefer the lower total end-to-end complexity when guarantees are equal.
6. Test transferable ownership: identify the owner and what it deliberately does not own,
   entry points, inputs and outputs, authority, whether state is
   canonical, derived, or projected, important failure behavior, verification,
   durable rationale, and the bounded change location. Use a fresh-context maintainer
   probe only for material uncertainty; it tests legibility, not
   correctness.
7. Evaluate tradeoffs. Do not require speculative ports, DTOs, adapters, or
   events that add behavior-free layers without demonstrated volatility,
   coupling reduction, or another real consumer.
8. Route business-language and invariant questions to the domain lens and authority
   or disclosure questions to security review; dependency shape alone proves
   neither domain correctness nor safety.

Output findings first, ordered by severity, and separately from style. For each
finding give the dependency path, affected surface, triggering condition,
impact, evidence, correction direction, protected quality, and residual
tradeoff. State the reviewed and materially unreviewed surface, verification
performed, and residual risk. Distinguish confirmed drift from uncertain
reachability; do not invent a finding when evidence supports none.
