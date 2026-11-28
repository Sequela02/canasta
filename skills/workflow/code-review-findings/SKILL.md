---
name: code-review-findings
description: "Review a diff, branch or finished change before merge: find bugs, regressions and missing tests, and give each finding a severity, the file and line, and a check that confirms it. Use for 'review this diff before I merge it' and 'check my finished change for bugs'."
tags:
  - engineering
  - review
metadata:
  source: "code-review-and-quality by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "The review dimensions, the approval standard and the structural remedies come from code-review-and-quality; the Intent and Standards lenses, confirmation of every finding by a check, unverified findings and the output block are this pack's own"
---

# Code review findings

Use it to review a completed change before it merges. Report defects the
change introduces or exposes, each confirmed by a check. Approve a change that
improves the code, even when you would have written it differently.

## Procedure

1. Read the task, the issue or spec, and the nearby code before judging the
   diff. Fix the comparison point (a commit, branch or merge-base) and include
   uncommitted changes when they are in scope.
2. Map what changed and what it can reach. Review every human-written line in
   scope, or say which you skipped.
3. Look at the change through these dimensions:
   - correctness: requirement met, edge cases, error paths, races, data
     integrity;
   - tests: correct, reliable, and giving a distinct signal (they are
     production code too);
   - security and authority: input validation, secrets, who may do what;
   - architecture: dependencies pointing the right way, logic in the layer
     that owns it, a new pattern justified;
   - readability: names, control flow, abstractions that earn their weight;
   - performance: unbounded loops or fetches, N+1 queries, work in hot paths.
   Name any specialist review still needed.
4. Review twice and report apart, because a change can pass one and fail the
   other:
   - **Intent:** against the issue, spec or request, what is missing, partial,
     added beyond it, or implemented but wrong. Quote the requirement, or say
     no spec exists.
   - **Standards:** against the repository's written rules, cite the rule. Skip
     what a tool already enforces. A written standard overrides general taste.
5. Confirm each candidate before reporting it. Run the narrowest check that
   leaves the files under review unchanged: an existing test, a short script,
   a counterexample. Keep the command and its result. Reading the code gives a
   hypothesis; a candidate that a check refutes is dropped.
6. When you can't run it, because it depends on code you can't see, build a
   minimal harness or reconstruct the missing part from what the diff shows.
   If it still can't be confirmed, report it as unverified with its condition,
   its impact and the check that would settle it. A real defect left in a
   footnote is a missed finding.
7. When confusion shows missing durable knowledge, fix the narrowest owner:
   clearer code or names, then a test, then the architecture or operations
   doc, then a decision record. A reply in the review thread doesn't fix it.

## What counts as a finding

- It is introduced or exposed by this change, has a concrete triggering
  condition, and a material impact.
- It points to the narrowest file and line and traces the path from input or
  state to the visible failure.
- Severity follows impact, reach and recoverability, not how sure you feel.
- A missing test counts when a specific material behavior is unprotected and a
  named test would close the gap. Existing tests that already protect the
  behavior need no duplicate.
- Style preferences, tool-enforced rules and guesses the change doesn't
  support are left out. A guess is speculative when nothing in the change backs
  it, not when part of its evidence is out of view.

When you flag a structural problem, name the move: replace a conditional chain
with a model, collapse duplicate branches, reuse the existing helper, move
feature logic to its owner, delete a pass-through wrapper. Prefer the remedy
that removes moving parts. State the direction in a sentence; leave the
rewrite to the author.

## Output

Findings first, most severe first, no summary before them. One block per
defect:

```text
1. src/cart.ts:22, medium: a discount over 100% makes the total negative.
   applyDiscount subtracts percent / 100 * total without a cap, so a
   150% coupon charges -50.00 against the spec's "never below zero".
   Fix: clamp the result at zero.
   Confirmed: node -e "<harness>" -> total(100, 150) returned -50.
```

- Line one: `file:line`, severity, the defect.
- Then the condition and impact in a sentence or two; quote the requirement
  for an intent finding.
- Then the correction direction in one sentence.
- Then one status line: `Confirmed: <command> -> <result>`, or
  `Unverified: <the check that would settle it>`. A finding backed only by
  reading the code is unverified, also when you ran nothing.

Report only admitted findings; leave other observations out. Skip a lens that
found nothing. End with one or two lines: the surface reviewed, what you
couldn't review or run, and the residual risk. With no findings, write
`No findings.` and those lines. Cut every word that does no work, and keep
numbers, conditions, identifiers and negations exact.
