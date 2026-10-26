# Java

No in-place Java prover supports the current Java LTS, so choose by how much
assurance the component needs. Rechecked 2026-10-03.

## A Dafny core compiled to Java

For a small, high-assurance component (policy evaluation, a calculation
library) that a Spring service calls through a plain Java interface. Dafny
emits ordinary Java source and a runtime library that run on current JDKs;
AWS builds its Cryptographic Material Providers Library this way, and
LLM-written Dafny verifies far more often than other proof languages (82% in
the vericoding benchmark, against 44% for Verus and 27% for Lean).

- Costs a second language and a generated-code boundary. Use it only when the
  component justifies that.
- Never hand-edit the generated Java.
- Test the boundary where Java values enter and leave the core; that is where
  the proof's assumptions meet real data.

## A verified model plus differential testing

For a component that must stay in production Java but has a precise
specification: write an executable model in Dafny, prove the model's
properties, then run differential random tests that feed the same generated
inputs to the model and the production code and compare outputs. This is
AWS's process for Cedar (with Lean): proofs and differential tests both found
bugs before release, and no release ships unless the model, proofs, and
differential tests are current.

## Property-based tests

For everything else with a rule you can state: jqwik properties written from
the requirement. They sample inputs instead of covering all of them; report
them as tests, not proofs.

## JML with OpenJML

Checks `//@ requires` and `//@ ensures` in place, but OpenJML's releases are
numbered for Java 21 (latest 21.0.28), so code using later syntax or APIs does
not compile under it. Use it only for a module that compiles as Java 21, and
recheck its releases first.
