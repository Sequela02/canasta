---
name: architecture-scan
description: "Scan a codebase for the structural changes most worth making: hot spots, shallow modules and hidden coupling, reported as ranked candidates for the user to choose from. User-invoked; to design or review one change, use architecture-review."
disable-model-invocation: true
license: Complete terms in LICENSE.txt
metadata:
  source: "improve-codebase-architecture by Matt Pocock, mattpocock/skills 5863806"
  changes: "Hot spots weigh churn against size and add change coupling, with bot and formatting commits filtered; no candidate is a valid result; each candidate names how it would be verified; a rule a tool can enforce ranks above a rearrangement; Markdown report instead of an HTML page; routes to this pack's architecture-review and domain-modeling instead of codebase-design and grilling"
---

# Architecture scan

Find where the structure of a codebase costs the most, and report candidates for
the user to choose from. This skill proposes; it changes no code.

## 1. Scope before scanning

Decide where to look before looking. Structure pays off where code keeps
changing, so weight recent history:

- If the user named an area, a module or a pain point, scan that.
- Otherwise rank files by **churn against size**: commits touching each file in
  the last six months or so, against its length or a complexity measure when the
  repository has one. Large files that change often come first.
- Add **change coupling**: files in different modules that change in the same
  commits most of the time. Coupling across a boundary is a stronger signal than
  either file's churn.
- Before counting, drop merges and commits from bots, dependency updates,
  formatting, generated files and lockfiles. They inflate churn without
  pointing at design. Leave tests out of coupling: a file and its test are
  meant to change together.

[scripts/hotspots.py](scripts/hotspots.py) does all three from Git history
(Python standard library, read-only); `--help` lists its options.

Read the domain glossary and the decisions (ADRs) for the chosen area first.

## 2. Look for friction

Read the chosen area and note where understanding or changing it is hard:

- One concept that takes several small modules to follow.
- **Shallow** modules, whose interface is nearly as complex as what they hide.
  Apply the **deletion test**: would removing the module concentrate its
  complexity in one place, or just move it around? Concentrating is the signal.
- Pure functions extracted only for testing, while the bugs live in how they are
  called.
- Modules that leak across their **seams**. One adapter behind a seam is a
  hypothetical seam; two make it real.
- Code that is untested, or hard to test through its current interface.
- A bad pattern that keeps reappearing, which a type, a lint rule or a test could
  make impossible.

## 3. Report candidates

Report in Markdown, most valuable first. For each candidate:

- **Files** and the module they belong to, in the glossary's terms.
- **Problem**, with its evidence: churn and size, coupling figures, the deletion
  test's result.
- **Change**, in plain words. No interfaces yet.
- **Gain**: what gets easier to change, understand or test.
- **Check**: which tests or traces show behavior is preserved, and which measure
  should improve.
- **Strength**: `Strong`, `Worth exploring` or `Speculative`.

Rank a change that makes a bad pattern impossible above one that rearranges
modules. Raise a candidate that contradicts a recorded decision only when the
friction justifies reopening it, and say which decision.

## Example candidate (illustrative figures)

- **Files**: `billing/invoice.ts`, `billing/tax.ts`, `orders/checkout.ts`
- **Problem**: 41 commits in six months; `invoice.ts` and `checkout.ts` change
  together in 70% of them across the billing/orders boundary. Deleting `tax.ts`
  only inlines one function that `invoice.ts` alone calls: the module hides
  nothing.
- **Change**: fold `tax.ts` into `invoice.ts`; have `checkout.ts` ask billing
  for a total instead of assembling line items itself.
- **Gain**: a tax change touches one module and one test.
- **Check**: the existing invoice tests pass unchanged; co-changes between the
  two modules drop over the next months.
- **Strength**: Strong.

"No candidate worth the change" is a valid result: report it with what you
examined. Agents asked to improve code rarely stop on their own, and a scan that
always finds something produces churn.

End with the one you would start with and why, then ask which to explore.

## 4. After the user picks

Design the chosen change with `architecture-review`, and keep terms and
invariants in `domain-modeling`. When the user rejects a candidate for a reason a
future scan would need, offer to record it as a decision so it isn't suggested
again. Carry out the change with `refactor`: behavior preserved, the measure
improving, and stop when it no longer does.
