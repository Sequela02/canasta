---
name: refactor
description: "Change code structure without changing behavior: refactor, clean up, remove duplication or dead code, rename, move, or simplify. For a change in behavior, use tdd instead."
---

# Refactor

A refactor changes structure and keeps observable behavior exactly the same.
If behavior must change, it is not a refactor: split it out and use `tdd`.

## Agent failure modes

Coding agents often change behavior while "refactoring" (in published studies,
about one recommended refactoring in fourteen changed functionality or broke
syntax). These rules override convenience:

- Never mix a behavior change into a refactor, not even a "small fix" you
  notice. Report it, and if asked, do it as a separate change.
- One named transformation at a time (extract function, inline, rename, move,
  replace conditional), each leaving the code buildable and its checks green.
- Use the compiler, type system, IDE, or AST tools for renames and moves
  instead of editing text by hand when they are available.
- Absence of static references does not prove code is dead: check
  configuration, reflection, registration, generated code, scripts, and
  entry points first.
- Do not add an abstraction, layer, or wrapper unless it removes demonstrated
  duplication, coupling, or confusion.

## Before editing

1. Name the behavior that must not change: public APIs, outputs, persisted or
   serialized data, errors, ordering, side effects, authorization decisions,
   and performance where it is part of the contract.
2. Find every consumer of the code you will touch.
3. Make sure a check would catch drift. If the existing tests are weak around
   the code, add characterization tests first; they record current behavior,
   right or wrong.
4. Name the structural problem you are fixing and stay inside it. Adjacent
   cleanup the user did not ask for gets mentioned, not done.

## What to fix

- Duplicated logic: one owner per behavior.
- Dead code, commented-out code, and compatibility paths with no remaining
  consumer: delete them in the same change.
- Wrappers and layers with a single caller that add nothing: inline them.
- Swallowed exceptions: fail fast or handle the error deliberately.
- Complex conditionals, unclear names, magic numbers.
- Explanations made obsolete by the move: delete them rather than keep a
  historical copy beside the new owner.

Leave mechanical rules (unused or wildcard imports, `any`, formatting) to the
repository's linters and formatters. If a rule you keep fixing has no linter,
propose one instead of fixing it by hand every time.

Do not refactor generated code, applied migrations, third-party code, or
configuration files.

## Verify

- After each transformation, run the narrowest check that could expose drift;
  then check affected dependents in proportion to their reach and risk.
- Where tests are weak or the change crosses a boundary, compare before and
  after directly: characterization, differential, or trace evidence.
- Review the final diff for accidental changes to defaults, constants, errors,
  ordering, transactions, async behavior, authorization, data shape, and
  resource use.

## Commit and report

- Keep structure and behavior in separate commits (Kent Beck's *Tidy First?*):
  a refactor commit contains no behavior change.
- Report the behavior preserved, the transformations applied, the checks run
  and their results, and any residual uncertainty. If equivalence could not be
  established, say so and treat the work as a behavior change.
