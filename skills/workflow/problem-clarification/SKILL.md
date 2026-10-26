---
name: problem-clarification
description: Clarify a materially ambiguous problem, requirement, or design
  decision; stress-test a proposal when requested. Skip routine work whose
  outcome is already clear.
tags:
  - engineering
  - requirements
  - decisions
---

# Problem Clarification

Before a nontrivial step, restate in your own words the goal, who it serves,
the deliverable, what is excluded, and the check that will show it worked. A
wrong restatement is cheaper to correct than wrong work. For a clear, small
edit, skip it.

Use when unresolved intent would materially change the outcome, scope,
acceptance criteria, or a consequential design choice, or when the user asks
to stress-test a proposal. A request to write an issue or PR alone does not
require an interview. Use clear-writing for the resulting explanation.

1. Inspect the supplied evidence and existing work before reopening questions:
   relevant code, guidance, issues, decisions, and active branches or worktrees
   when they concern this effort. Treat drafts and prior agent conclusions as
   evidence to check, not settled truth. Investigate discoverable facts yourself.
2. State the affected person or system, trigger, observed and desired behavior,
   impact, and what would demonstrate success. Separate observations, hypotheses,
   proposals, and decisions. For new capabilities, describe the unmet need rather
   than inventing a broken behavior. Mark missing evidence honestly.
3. Identify only consequential unresolved decisions and their dependencies.
   Ask a small batch of questions answerable now, with a recommendation and its
   tradeoff. Defer questions whose premises depend on unanswered ones. Reuse
   the user's prior answers; do not ask for facts available in the environment.
4. Continue independent investigation while waiting. Never treat silence as a
   decision or answer on the user's behalf where their input is required.
   Resolve routine implementation choices within the already authorized scope.
5. Probe the uncertain boundary with a concrete example, counterexample, or
   failure scenario. When only running code can answer the question, build one
   throwaway prototype: state the single question it answers and its budget;
   for logic or state, a small pure module with a minimal driver that shows
   the state after each action; for appearance, a few structurally different
   variants switchable in place. Keep it in the session scratch or an isolated
   worktree, record the verdict and the question it settled, and discard the
   code unless the user adopts it. Use concept-modeling only for conflicting or overloaded
   terminology; use research for external evidence and
   implementation-planning for sequencing an established objective.
6. Stop when remaining uncertainty no longer changes the authorized outcome or
   safe next step. For an explicitly requested interview, present the resulting
   understanding for the user's response. Otherwise continue authorized work
   without adding a confirmation gate. Record durable decisions at their existing
   owner; do not create a parallel glossary, tracker, or planning lifecycle.

Output the problem, acceptance criteria, and any material unresolved decision
in the smallest useful form. A hypothesis is not a confirmed cause; agreement
on a proposal is not evidence that it works.
