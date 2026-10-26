---
name: implementation-planning
description: Produce repository-evidenced implementation sequences for scoped,
  nontrivial changes with decisions, dependencies, verification, and recovery.
tags:
  - engineering
  - planning
---

# Implementation Planning

Use this skill when sequencing dependencies, consequential decisions, or recovery
needs make a plan useful. Reuse current repository evidence; a separate scouting
pass is needed only for unresolved questions. Skip a full plan for one obvious
low-risk edit; state the change and focused verification instead.

Workflow:
1. State the intended outcome, acceptance evidence, and non-goals. Preserve the
   user's actual contract rather than expanding it into adjacent cleanup.
2. List material assumptions, unknowns, and decisions. Do not hide unresolved
   product, architecture, authority, security, or data-safety decisions inside an
   implementation step. Resolve choices within the authorized outcome using
   evidence; ask for direction when a consequential ambiguity or scope expansion
   cannot be resolved from the request and repository contract.
   For material architecture, name the simplest materially different design and
   the required invariant it cannot preserve. Future flexibility alone is not a
   sufficient reason to add permanent concepts.
3. Ground the affected surface in current repository evidence.
   Treat files and symbols as exact only when confirmed by repository evidence;
   label other surfaces as candidates to verify during execution.
4. Split work by coherent behavior or invariant. Prefer tracer-bullet slices:
   each cuts a narrow, complete path through every layer it touches, can be
   demonstrated or verified on its own, and fits one fresh context. A wide
   mechanical change (a rename or retype across many call sites) instead goes
   expand, migrate in batches, contract, each batch green on its own. When a
   design question blocks a slice, plan a throwaway prototype that answers it
   first (see problem-clarification). Each slice must leave a safe,
   reviewable intermediate state and name:
   - its outcome and why it is necessary;
   - confirmed files, symbols, contracts, and owning surface;
   - the slices that block it, and those it blocks;
   - focused verification and its expected completion signal;
   - rollback, roll-forward, or recovery when state or deployment can escape the
     repository.
5. Order prerequisites before consumers. Do not parallelize slices that share a
   prerequisite or write surface. Mark slices independent only when their state,
   ownership, and verification do not conflict.
6. Include contract, data, config, generated-artifact, documentation, cleanup,
   and surface-parity work only when evidenced consumers require it. Schedule
   failing behavior proof before production edits when TDD is practical, without
   designing or writing the test in the plan.
   Preserve durable rationale in its natural owner only when future maintainers
   need it to challenge or replace a persistent decision; do not preserve the
   design conversation.
7. End with proportionate completion gates and residual risk. Name focused,
   downstream, integration, or broader gates justified by the dependency surface;
   do not use a ritual full-suite step as generic boilerplate.
8. Re-scout and revise the plan when execution, tests, or repository changes
   invalidate a premise, reveal a new dependency, or broaden the surface. Remove
   or supersede stale steps instead of executing them ceremonially.

Output:
- objective, acceptance evidence, and non-goals;
- confirmed evidence, assumptions, open decisions, and candidate surfaces;
- numbered slices with outcome, owned surface, dependencies, verification signal,
  and recovery;
- final gates and residual risks.

When the work spans many files or more than one session, write the plan to a
file (the repository's plan location, or the session scratch directory when it
has none) and implement it in a fresh session that starts from that file. The
file, not the conversation, carries the context, so research and failed
attempts do not crowd the implementation.

Prefer the smallest plan that fully satisfies the requested behavior. Every step
must change or verify something real. Do not invent paths, line numbers, time
estimates, approvals, or rollback guarantees. A plan-only request ends with the
plan. For an implementation request, proceed into authorized execution after
planning and continue through verification and necessary repairs. Planning alone
is not completion. A prose plan does not
grant write authority, approval, or completion evidence; use the repository's
structured plan, work-item, or approval system when one exists.
