---
name: codebase-scouting
description: Investigate unclear repository ownership, dependencies, or affected
  tests before a consequential change.
tags:
  - engineering
  - scouting
  - codebase
---

# Codebase Scouting

Use this skill for unclear ownership, uncertain dependencies, architecture-sensitive
behavior, or an explicit impact investigation. Multiple edited files alone do not
require scouting. Reuse established evidence. Scouting establishes a defensible
change boundary; it does not design the
implementation. It investigates repository evidence, not external source research.
Route current external claims, official documentation, standards, papers, and
market evidence to the research workflow; use both only when the decision
requires an explicit repository-to-external comparison.

Workflow:
1. Read the task and repository contract. Start from the named behavior, changed
   files, symbols, failing tests, or observable entry point instead of surveying
   the whole repository. When scouting a diff, record the exact comparison base
   and include uncommitted changes.
2. Identify the owning bounded context, package, and surface. Separate stable
   contracts from implementation details and note dirty-worktree overlap. Locate
   durable rationale only when a non-obvious persistent decision cannot be
   understood safely from code, tests, contracts, and current architecture.
3. Trace evidence in both directions:
   - inward to dependencies, schemas, configuration, and authorities the behavior
     relies on;
   - outward to callers, adapters, DTOs, events, projections, build targets,
     tests, and user-facing consumers.
   Classify each relationship as direct, transitive, or uncertain.
4. Prefer repository-native dependency graphs, build metadata, compiler or
   language-server references, and executable traces. Treat text search and
   naming proximity as leads, not dependency proof. Record the graph or tool and
   the assumptions behind its affected set.
5. Check edges static analysis commonly misses: registration, configuration,
   reflection, code generation, dependency injection, plugins, scripts,
   serialization, database contracts, environment variables, and external APIs.
6. Map verification ownership. Name the smallest focused tests that exercise the
   direct behavior, then the downstream contract, integration, package, or
   workspace gates justified by the impact map. Focused affected tests are a
   fast-feedback gate, not proof of complete impact coverage. Widen verification
   for shared contracts, build or dependency changes, dynamic edges, or uncertain
   reachability.
7. Stop when ownership, contracts, consumer paths, verification ownership, and
   material unknowns are mapped well enough for a bounded planning decision.
   Record searched and unsearched surfaces; do not inventory the repository for
   its own sake.

Evidence discipline:
- Facts, inferences, and unknowns must be distinguishable.
- Every impacted file or target needs a causal path from the task or change seed.
- Absence of a text reference is not evidence that a runtime consumer does not
  exist.
- Do not propose unrelated refactors. Do not turn the map into an implementation plan.

Output:
- scope seed and owning boundary;
- stable contracts and implementation details;
- direct, transitive, and uncertain consumers with evidence-backed file or target
  references;
- verification map, hidden-edge checks, and material unsearched surface;
- smallest defensible change boundary and open risks for planning or specialist
  review.
