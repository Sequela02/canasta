---
name: refactor
description: "Refactor, clean up, simplify, rename, move, extract a function, or remove duplication and dead code, keeping behavior exactly the same. Not for changing behavior (tdd)."
metadata:
  source: "code-simplification by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "Takes the rule of 500 and the Chesterton's fence check; adds characterization tests before editing, a list of behavior to pin, and a final diff review"
---

# Refactor

A refactor changes structure and keeps behavior identical. When behavior has to
change, split that part out and use `tdd`.

## Procedure

1. **Pin the behavior.** Write down what must not change: public API,
   outputs, persisted or serialized data, errors, ordering, side effects,
   authorization decisions, and performance when it is part of the contract.
2. **Find every consumer** of the code you will touch: callers, tests,
   configuration, scripts, generated code.
3. **Get a check that would catch drift.** If tests are thin around this code,
   write characterization tests first. They record what the code does today,
   right or wrong, and pass before you edit.
4. **Name the one structural problem** you are fixing (duplication, a name
   that misleads, a wrapper with one caller, a tangled conditional). Mention
   neighbouring cleanup in the report and leave it alone.
5. **Apply one transformation at a time**: extract, inline, rename, move,
   replace a conditional. Use the compiler, IDE or an AST tool for renames and
   moves. Run the narrowest check after each step; the code builds and passes
   before the next one. A change over about 500 lines is a codemod, not hand edits.
6. **Delete what the change makes dead**: commented-out code, compatibility
   paths with no consumer, comments that described the old shape.
7. **Review the final diff** for drift in defaults, constants, errors, ordering,
   transactions, async behavior, authorization, data shape and resource use.
8. **Commit structure apart from behavior.** Report the behavior pinned, the
   transformations, the checks and their results, and anything you could not
   show equivalent. A change you cannot show equivalent is a behavior change.

## Before removing anything

No static reference does not mean dead. Search configuration, reflection,
registries, generated code, scripts and entry points. Read `git blame` for why
it was written (Chesterton's fence). Remove it only when you can say why it
is no longer needed.

## Example

While extracting `applyDiscount` out of `checkout`, you see it rounds down
where the price list rounds half up.

- Bad: fix the rounding in the same commit. The refactor now changes totals
  and a reviewer reading "extract function" misses it.
- Good: extract with the rounding as it is, run the characterization test,
  and report "rounding in `applyDiscount` looks wrong; left unchanged." If the
  owner wants it fixed, that is a second change through `tdd`.

## Leave to tools and owners

- Mechanical rules (unused imports, formatting, `any`) belong to the linter.
  When you keep fixing the same rule by hand, propose the lint rule.
- Generated code, applied migrations and third-party code are changed at their
  source, not refactored in place.
- Add an abstraction only to remove demonstrated duplication, coupling or
  confusion. Fewer lines is not the goal; faster reading is.
