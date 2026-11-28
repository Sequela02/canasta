---
name: formal-verification
description: "Prove code against a contract while you work, and keep the contract honest: work on code with //@ LemmaScript contracts, write or strengthen a contract, decide whether a function deserves a proof, review what a proof covers, or choose which kind of verification fits a property. TypeScript with LemmaScript and Dafny; Java through a Dafny core or property tests."
---

# Formal verification

A proof checks the code against the contract. Nothing checks the contract against
what the user wanted except you. Three artifacts, three owners:

| Gap | Settled by |
| --- | --- |
| Code against contract | The prover. Final for what the contract says. |
| Contract against request | You, with the checks below; the operator when the request leaves intent open. |
| Code outside any contract | Tests and review. |

A proof covers the encoded contract, under its `requires`, its translation and
its toolchain. It does not show the product is right.

## Prove while you work

1. After every change to a file with contracts, prove it:
   `lsc regen --backend=dafny <file>.ts` (see
   [references/lemmascript.md](references/lemmascript.md)).
2. When it fails, the message names an obligation. Either the code is wrong, or
   the proof needs a loop invariant or an assertion. Keep going until it proves,
   or until you can name the obligation you can't discharge.
3. Read the verified count. "0 verified" means the contracts attached to nothing:
   check for a stray line between the `//@` lines and the function.
4. A timeout says nothing about the code, either way.

To make a proof pass, fix the code or add an invariant or lemma. Leave the
contract as the request defined it: don't loosen an `ensures`, add a `requires`
to an existing contract, or add `//@ assume`. If the request really asks for
different behavior, change the contract and say so in your summary.

## Write a contract from the requirement

1. Write the rule in plain words from the request before you read the code. A
   contract copied from the code proves the code equals itself.
2. Cover each case the request names, including boundaries (`<` against `<=`,
   empty, maximum).
3. **Mutate.** Change the body in one place (swap a returned value, flip a
   comparison, move a number by one) and prove again. A mutant that still proves
   is behavior the contract allows: strengthen the contract, or report it.
4. **Restate.** Say the contract in plain words without looking at the request,
   then compare. Send mismatches the request doesn't settle to the operator.
5. **Check vacuity.** An `ensures` that repeats a `requires`, or holds for every
   input, proves nothing.

Example, `clamp(x, lo, hi)`:

```ts
//@ requires lo <= hi
//@ ensures \result >= lo && \result <= hi
```

A body that returns `hi` always satisfies this contract. That surviving mutant
shows the contract is too weak. Add the missing cases:

```ts
//@ ensures x < lo ==> \result === lo
//@ ensures x > hi ==> \result === hi
//@ ensures lo <= x && x <= hi ==> \result === x
```

When a bug passes a proved contract, the contract allowed it. If the request rules
the behavior out, fix the code and strengthen the contract so the buggy version
fails, then flag the contract change. If the request is ambiguous, ask.

## Where to prove

Prove code that is nearly pure, has a rule you can state exactly, and is costly to
get wrong: permission and policy decisions, money and quota math, state
transitions, parsers with exact acceptance rules. Use tests for UI, I/O,
framework wiring and orchestration (`tdd`). If you must bend code into an odd shape
to satisfy the prover, test it instead. Add contracts to code that has none only
when asked.

## Choose the kind of verification

Pick by the claim you need.

| Property | Use | Establishes | Limit |
| --- | --- | --- | --- |
| A function's result for every admitted input | Dafny, or LemmaScript for TypeScript | The contract, for every input it admits | As strong as the contract |
| Whether steps can happen in a bad order: races, protocols, lifecycles | A model checker (TLA+ with TLC, or Quint) | The model's invariants over all reachable states, or up to a bound | A model isn't the code; replay its traces against the code or say it isn't linked |
| What the real code does | Tests, property tests | The inputs tested | Nothing untested |
| Whether a test or contract catches a fault | Mutation | Sensitivity to those faults | Not that the spec matches intent |
| Whether a spec matches the request | Review | A judgment | Never a proof |

- Prefer the tool the repository already uses. A new one needs a reason: the
  claim, run time, runtime such as a JVM, readable counterexamples.
- Write the contract or model from the requirement, not from the code it checks.
- Watch a check fail on a planted fault before you trust its pass.
- Proofs of single functions don't add up to their composition: check each call
  boundary.
- Say which claim you made: a proof, a complete search of a finite model, or a
  bound.

## Report

- What proved: tool, version, verified count.
- What each proof assumes (`requires`, any `assume`) and doesn't cover: callers,
  unannotated code, inputs its `requires` excludes.
- Each contract you added, strengthened or changed, and why.
- Mutants that still prove, and any obligation still failing.

Show the contracts, not the prover's output. A proof that couldn't run isn't a
pass.

## References

- TypeScript with LemmaScript and Dafny: [references/lemmascript.md](references/lemmascript.md)
- Java: [references/java.md](references/java.md)
- Why these rules, with measurements: [references/evidence.md](references/evidence.md)
