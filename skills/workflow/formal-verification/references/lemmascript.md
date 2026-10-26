# LemmaScript with Dafny

Verified against LemmaScript 0.6.4 and Dafny 4.11 on 2026-10-03. Recheck
[the agent guidance](https://docs.lemmascript.org/agents/) when the version
changes.

## Files

| File | Owner | Rule |
| --- | --- | --- |
| `foo.ts` | You | Source of truth for the program and its `//@` contracts |
| `foo.dfy.gen` | LemmaScript | Generated. Never edit. |
| `foo.dfy` | You and LemmaScript | Source of truth for the proof. Edit by additions only (lemmas, assertions); never change generated lines. |

Follow the repository's convention on committing the generated files.

## Commands

- **After changing a `.ts` with contracts:** `lsc regen --backend=dafny foo.ts`.
  It regenerates, merges your proof additions back in three ways, and verifies.
- **First proof of a new file:** `lsc check --backend=dafny foo.ts`.
- Running `check` first on an existing file rewrites `foo.dfy.gen`, and `regen`
  then refuses ("modifications to generated lines"). Restore the committed
  `foo.dfy.gen` and run `regen` again.
- Never delete `foo.dfy` to regenerate it: that discards the proof additions.
- Always pass `--backend=dafny` explicitly.

Faster iteration and diagnosis, on the `.dfy`:

- one lemma: `dafny verify --filter-symbol=<name> foo.dfy`;
- which conjunct fails: `--isolate-assertions`;
- a slow proof: `--verification-time-limit=<seconds>`.

## Syntax

- `//@ requires P` and `//@ ensures P` directly above the function, with no
  other line in between; `\result` for the return value.
- `//@ invariant P` as the first lines inside a loop. Every loop that a
  postcondition depends on needs invariants strong enough to prove it.
- `forall(j: nat, j < items.length ==> P)` and
  `exists(j: nat, j < items.length && P)`. Not `forall (i: number, ...)` and
  not `\forall i :: ...`: both are rejected.
- `==>` for implication, `===` for equality.
- Nonlinear arithmetic: use Dafny's standard library
  (`import opened Std.Arithmetic.Mul`, `Std.Arithmetic.DivMod`) in the `.dfy`
  rather than hand-written lemmas.

## Model limits

- `number` is a mathematical integer, under production range assumptions.
- `a / b` is real division: `return n / 2` in a function returning `number`
  fails with "Function body type mismatch (expected int, got real)". For a
  quotient, use `//@ type \result real` and a real value on every path; for a
  mean, prove the integer decision (which positions) and compute the mean in
  plain code.
- LemmaScript translates the whole file, so unannotated functions in a file
  with contracts must stay within its subset.
- Regex and other out-of-model code go behind `//@ extern` (deterministic) or
  `//@ havoc` (with `//@ impure` when each call may differ). `//@ assume` is
  only for constraining a havoc'd value.

## Reading a failure

Dafny names the postcondition and the return path that failed, with line
numbers in the generated `.dfy`, not the `.ts`. It gives no input values.
Find the failing `ensures` in the `.ts`, find the path, and decide which is
wrong: the code, or a missing invariant or assertion. Change the contract only
when the request asks for different behavior.

A clean exit with "0 verified" means nothing was proved: the contracts did not
attach. Check for a line between the `//@` block and the function, a contract
inside a block comment, or a malformed annotation.
