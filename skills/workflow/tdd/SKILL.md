---
name: tdd
description: "Change behavior test-first in small vertical slices, design trustworthy test oracles, or diagnose flaky, slow, redundant, or weak tests."
---

# TDD

Work in small behavior increments, each proven by a test that failed for the
right reason first. Test-first order is a feedback discipline, not a quality
guarantee; the evidence is in [references/evidence.md](references/evidence.md).

## Agent failure modes

Coding agents fail at TDD in known ways. These rules override convenience:

- Never edit, delete, skip, or weaken a test to make it pass. If a test looks
  wrong, stop and report why; changing it is the operator's decision.
- Do not special-case test inputs or detect the test environment in
  production code.
- Do not mock code you own. Mock only at real system boundaries (network,
  clock, third-party services), and keep the semantics the claim depends on.
- Assert literal expected values. Do not recompute the expected value the way
  the code does; a tautological test passes by construction.
- Do not write all tests up front. Tests written before any implementation
  describe imagined behavior.

## Before the first test

1. Identify the observable behavior, its owning boundary, affected consumers,
   and the closest existing test owner.
2. Choose the seam: the public interface where the behavior is observed without
   reaching inside. Test only through agreed seams; when the seam is unclear,
   ask before writing tests.
3. Choose the oracle. A specification or regression oracle comes from a
   requirement, contract, issue reproduction, or domain invariant, never only
   from the current implementation. A characterization oracle records current
   behavior and counts as preservation evidence only.
4. In unclear legacy code, add narrow characterization tests first, then the
   intended failing test.

## Vertical slices

Repeat for each increment, one test at a time:

1. Write one test for the smallest behavior that can fail and pass on its own.
2. Run it and confirm it fails because the behavior is absent, not because of
   syntax, environment, fixtures, or an unrelated baseline failure.
3. Implement only enough to pass it, preserving repository invariants.
4. Rerun it and read the result, not just the exit code.
5. Refactor only while behavior stays the same, rerunning the tests that cover
   the affected code and its callers.

Then run the owning suite and affected downstream suites; widen to the full
gate when risk, integration, or repository rules require it. If a failing test
is impractical, say why and use the closest independent executable check.

## Choose the layer by risk

Use the narrowest layer that faithfully observes the behavior:

- Pure or domain tests for calculations, decisions, state transitions, invariants.
- Integration tests for real wiring, persistence, protocols, configuration, and
  dependency behavior invisible below the boundary.
- Contract tests for agreed consumer and provider shape and semantics.
- End-to-end tests for a few critical journeys lower layers cannot prove.
- Runtime-specific probes when the runtime, browser, OS, or packaging changes
  behavior.

Follow risks and oracles, not fixed pyramid ratios. To prove a change in the
running product, follow [references/end-to-end-verification.md](references/end-to-end-verification.md).

## Hard bugs

For a reported failure, reproduce it before fixing it. When the cause is not
obvious, follow [references/diagnosing-bugs.md](references/diagnosing-bugs.md): build a command that goes red on
this exact symptom, minimise it, test falsifiable hypotheses, and turn the
minimal repro into the regression test. Set a budget for the investigation
and report what was tried when it runs out; a trivial bug needs no ranked
hypothesis list.

## Keep tests valuable

- Before adding a test, search the owning layer for one that covers the same
  behavior and strengthen it instead.
- A new test must protect a distinct behavior, regression, boundary, or failure
  mode, and fail with an actionable message.
- Coverage finds unexercised code; targeted mutation on changed, high-risk code
  checks assertion sensitivity. Neither percentage is a goal or proof.
- Remove obsolete or implementation-coupled tests only with evidence that the
  behavior stays protected elsewhere.

## Determinism and fixtures

- Use synthetic, portable values. Never put operator paths, credentials, tokens,
  or raw incident payloads in tests.
- Use isolated temporary resources, and restore clocks, environment, globals,
  working directory, mocks, files, and handles.
- Replace sleeps with a deterministic clock or event.
- A retry that passes is evidence of nondeterminism, not verification. Fix the
  cause, or quarantine with an owner, reason, and removal condition.

## Completion report

- Behavior covered, oracle source, layers, and the focused and broader gates run
  with their results.
- Every test file added, changed, or deleted, with the reason for each. A change
  to an existing assertion must name the requirement that justifies it.
- Residual untested risk.

Do not claim that red-green-refactor itself proves correctness.
