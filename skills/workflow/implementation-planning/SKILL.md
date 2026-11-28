---
name: implementation-planning
description: "Plan how to implement a change before coding: break a feature into steps with their dependencies, write an implementation plan another agent can follow, with decisions, verification and recovery. Skip one obvious low-risk edit."
tags:
  - engineering
  - planning
metadata:
  source: "writing-plans by Jesse Vincent, obra/superpowers 22f0b46; to-tickets by Matt Pocock, mattpocock/skills bbadaa6; planning-and-task-breakdown by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "A step is done when the implementer can write exactly one reasonable thing (superpowers); dependency-linked vertical slices and expand-contract for wide changes (to-tickets); checkpoints after two or three slices and risky slices first (planning-and-task-breakdown); confirmed versus candidate files, open product decisions left to the user and recovery are this pack's own"
---

# Implementation planning

A plan holds the decisions the implementer can't make alone, in steps they can
check. Use it when dependencies, a consequential decision or recovery make the
order matter. For one obvious low-risk edit, state the change and its check
instead.

## Procedure

1. Write the outcome, the evidence that will show it worked, and what is out
   of scope. Keep to the request; leave adjacent cleanup out.
2. Read the affected code. Mark each file and symbol *confirmed* (you opened
   it) or *candidate* (to verify during the work). Don't invent paths or line
   numbers.
3. List decisions and assumptions apart. Settle what the repository answers.
   Leave a product or business rule the request didn't state, such as what a
   total includes, as an open decision: give your answer and ask the user to
   confirm. The same goes for architecture, security and data-safety choices
   with real consequences.
4. Cut the work into vertical slices: each runs a narrow path through every
   layer it touches, can be shown working alone, and fits one fresh context.
   A rename or retype across many call sites is the exception: add the new
   form beside the old (expand), move callers in batches that each pass
   (migrate), then delete the old (contract). If a design question blocks a
   slice, plan a throwaway prototype first.
5. For each slice write:
   - outcome and why it is needed;
   - confirmed files and the contracts it touches;
   - the slices that block it;
   - its check and the result that means done, a failing test first when
     practical;
   - how to undo or roll forward, when state or a deployment can leave the
     repository.
6. Put prerequisites first and risky slices early. Add a checkpoint every two
   or three slices (tests, build, the main flow). Run slices in parallel only
   when they share no prerequisite, write surface or check.
7. Finish with the gates the dependency surface justifies and the risks left.
8. Re-read the plan before handing it over (below). When the work shows a
   premise was wrong, revise the plan and drop stale steps.

## What a step contains

A step is done when the implementer can write exactly one reasonable thing
from it. A test step names the test and its expected values. A code step names
the file, the signature and the values the spec fixes; the implementer writes
the body. A check step gives the command and the result that means it passed.

```text
Weak:   "Add validation and handle edge cases."
Better: "parseQuantity(input: string): number in src/cart/quantity.ts.
         Throws RangeError for <1 or >99; trims whitespace. Test:
         parseQuantity(' 3 ') === 3, parseQuantity('0') throws."
```

Leave out function bodies the signature and tests already decide. Executors
given full code copy it instead of thinking (obra/superpowers issue 895), and a
plan longer than the code has written the code.

## Self-review

- Each requirement points to a slice.
- No step says "TBD", "handle edge cases" or "write tests for the above".
- Names and signatures match between slices.
- Each slice leaves a state a reviewer can accept.

## Output

Outcome, evidence and exclusions; confirmed facts, assumptions, open decisions
and candidates; numbered slices as in step 5; gates and residual risk. When
handing the plan to another agent, mark each fact verified (with its source),
inferred or unknown, and ask the receiver to restate the goal and the check
before it starts.

For work over many files or sessions, save the plan to the repository's plan
location (or the session scratch directory) and implement from that file in a
fresh session. A plan-only request ends with the plan; an implementation
request continues into the work. A written plan grants no approval and isn't
evidence the work is done; use the repository's work-item system when it has
one.
