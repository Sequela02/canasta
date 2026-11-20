---
name: formal-verification
description: "Prove code against a contract while you work, and keep the contract honest: work on code with //@ LemmaScript contracts, write or strengthen a contract, decide whether a function deserves a proof, review what a proof covers, or choose which kind of verification fits a property. TypeScript with LemmaScript and Dafny; Java through a Dafny core or property tests."
---

# Formal Verification

A change to proved code involves three artifacts: the **request**, the
**contract** (the `//@` lines), and the **code**. Each gap has one owner:

| Gap | Settled by |
| --- | --- |
| Code against contract | The prover. Final for what it covers; no model re-decides it. |
| Contract against request | You, by the checks below; the operator when the request leaves intent open. |
| Code outside any contract | Tests and review, as for any code. |

A proof establishes only the encoded contract, subject to its assumptions,
translation, toolchain and trusted base; it does not establish product intent.
Check those limits and the contract rather than treating proof success as
unconditional correctness.

## Prove while you work

When you change a file that has contracts:

1. Prove it after every change, not once at the end. TypeScript:
   `lsc regen --backend=dafny <file>.ts` (see
   [references/lemmascript.md](references/lemmascript.md)).
2. Keep going until it proves. A failure names an obligation: either the code
   is wrong, or the proof needs a loop invariant or an assertion. There is no
   fixed round limit; stop only when you cannot make progress, and then say
   exactly which obligation still fails.
3. Read the count. "0 verified" is not a pass: the contracts were not attached
   to anything (a stray line between `//@` lines and the function, a block
   comment, or a parse problem).
4. A timeout or an unfinished proof says nothing about the code either way.

Never make a proof pass by weakening it:

- do not remove or loosen an `ensures`, or add a `requires` to an existing
  contract;
- do not add `//@ assume` (it is only for constraining `//@ havoc` values);
- change a contract only when the request asks for different behavior, and say
  so in your summary.

## Write a contract from the requirement

1. State the rule in plain words from the request, issue, or domain invariant
   before reading the implementation. A contract copied from the code proves
   the code equals itself.
2. Cover every case the requirement names, including boundaries (`<` against
   `<=`, empty, maximum). A missing case is the most common gap: a clamp whose
   contract only says "result in range" proves even when it returns the
   maximum for values below the minimum.
3. Check strength by mutation: change the body in one place (swap a returned
   value, flip a comparison, move a number by one, swap `+` and `-`) and
   prove again. A mutant that still proves is behavior the contract allows.
   Strengthen the contract or report the gap.
4. Check fit by restatement: restate the contract in plain words without
   looking at the request, then compare the restatement with the request.
   Mismatches go to the operator when the request does not settle them.
5. Check vacuity: an `ensures` that restates a `requires`, or holds for every
   input, proves nothing.

## When a bug passes a proved contract

The contract allowed it. When the request clearly rules the behavior out, fix
the code **and** strengthen the contract so the buggy version would fail, keep
it provable, and loosen nothing else. Flag the contract change for the
operator. Only when the request itself is ambiguous does the decision go to
the operator instead.

## Where to prove

Prove only code that is pure or nearly pure, has a rule you can state
precisely, and is costly to get wrong: permission and policy decisions, money
and quota calculations, state transitions and domain invariants, parsers and
validators with exact acceptance rules. Do not prove UI, I/O, framework
wiring, or orchestration; use tests there (`tdd`). Code bent into an unnatural
shape to satisfy a prover is a signal to test instead.

Add contracts to code that has none only when the request or the repository's
instructions ask. A new contract takes the same checks as a strengthened one.

## Report

- What proved, with tool and version, and the verified count.
- What each proof takes as given (`requires`, any `assume`) and what it does
  not cover: callers, unannotated code, inputs its `requires` exclude.
- Every contract you added, strengthened, or changed, and why.
- Mutants that still prove, and any obligation left failing.

Contracts are readable as written; show them, not the prover's output. A proof
that could not run is not a pass.

## Choose the kind of verification

Let the property choose the tool, not the language, what is installed or a
default. Each kind establishes a different claim:

| Property | Fits | Establishes | Boundary |
| --- | --- | --- | --- |
| A function's result for every admitted input: contracts, algorithms, parsers | A verifier that runs on the code (Dafny; LemmaScript for TypeScript) | The encoded contract, for every input it admits | As strong as the contract, no stronger |
| Whether steps can happen in a bad order: races, protocols, lifecycles | A model checker over a small model of the design (TLA+ with TLC or tla-ts; Quint, which quint-check runs without a JVM) | The model's invariants, over every reachable state or up to a bound | A model is not the code: link it by replaying its traces against the code, or say it is not linked |
| What the real code does in its environment | Tests and property-based tests | The inputs and environments tested | Nothing untested |
| Whether a test, contract or model catches a fault | Mutation of the code, and of the contract or property | Sensitivity to those faults | Not that the specification matches the intent |
| Whether a specification captures the request | Review against the requirement | A judgment | Never a proof |

- Prefer the tool the repository already uses; its configuration and
  instructions name it. Choose a new one by the claim you need and its cost
  (runtime such as a JVM, run time, readable counterexamples), and say why.
- Write a contract or model from the requirement before reading the code it
  checks. One derived from the code, or from code that may be wrong, repeats
  the code's mistakes and still passes; it is not an independent oracle.
- A check you have never seen fail proves nothing: show it failing on a
  planted fault before trusting its pass.
- Proofs of single functions don't add up to a proof of their composition;
  check the obligations at each call boundary.
- State the claim exactly: a proof, complete exploration of a finite model,
  or a bound; and what the contract or model leaves out.
- To set up model checking for a system, `create-formal-verification-skill`
  (pstack) generates a project skill, and `maintain-formal-verification-skill`
  keeps it in line with the code.

## Language specifics

- TypeScript, LemmaScript with Dafny: [references/lemmascript.md](references/lemmascript.md)
- Java: [references/java.md](references/java.md)
- Why these rules, with measurements and sources: [references/evidence.md](references/evidence.md)
