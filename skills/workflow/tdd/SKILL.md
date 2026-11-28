---
name: tdd
description: "Fix a bug or add behavior test-first: write a failing test for the bug, watch it fail, then fix it. Also for choosing trustworthy test oracles and diagnosing flaky, slow or weak tests. Not for restructuring that keeps behavior (refactor)."
metadata:
  source: "test-driven-development by Jesse Vincent, obra/superpowers 22f0b46; diagnosing-bugs by Matt Pocock, mattpocock/skills 5beb35b"
  changes: "The core rule and the worked red/green example come from superpowers; the reference on diagnosing hard bugs comes from mattpocock/skills (see NOTICE); independent oracles, characterization versus specification oracles, agent failure modes, flaky-test handling and the limit on what the loop proves are this pack's own"
---

# TDD

If you didn't watch the test fail, you don't know whether it tests the right
thing. Work in small increments, each proven by a test that failed for the
right reason first. Test-first order is a feedback habit, not a guarantee of
quality; the evidence is in [references/evidence.md](references/evidence.md).

## The loop

Repeat for each increment, one test at a time:

1. **Red.** Write one test for the smallest behavior that can fail and pass on
   its own. Run it. Confirm it fails because the behavior is missing, not
   because of syntax, setup or an unrelated failure. Read the message.
2. **Green.** Write only enough code to pass it. Run it again and read the
   result, not just the exit code.
3. **Refactor.** Tidy while the tests stay green, rerunning them and their
   callers.

Then run the owning suite and affected downstream suites, and widen to the
full gate when risk or repository rules call for it. If a failing test is
impractical, say why and use the closest independent executable check.

Worked case: "the total ignores the discount."

```text
Red:    test('applies a 10% discount', () => expect(total([{ price: 50 }], 10)).toBe(45))
        run -> FAIL: expected 45, received 50      (the bug, not a typo)
Green:  total() now subtracts percent / 100 * subtotal
        run -> PASS
Next:   test('never goes below zero at 150%') -> red first, then green
```

A test that passes the first time proves nothing yet: it checks behavior that
already exists, or checks the wrong thing. Fix the test until it goes red for
the right reason.

For a reported bug, reproduce it before fixing it. When the cause isn't
obvious, follow [references/diagnosing-bugs.md](references/diagnosing-bugs.md):
a command that goes red on this symptom, a minimal case, falsifiable
hypotheses, and the minimal case kept as the regression test. Set a budget,
and report what was tried when it runs out.

## Before the first test

1. Name the observable behavior, its owning boundary and the nearest existing
   test.
2. Pick the seam: the public interface where the behavior shows without
   reaching inside. If it is unclear, ask before writing tests.
3. Pick the oracle, the source of the expected value. A specification or
   regression oracle comes from a requirement, contract, bug report or domain
   rule. A characterization oracle records what the code does now and proves
   preservation only. In unclear legacy code, write narrow characterization
   tests first, then the failing test for the change.

## Rules that agents break

- When a test looks wrong, stop and report why. Changing it is the operator's
  decision; editing, skipping or weakening it to get green is not allowed.
- Production code has no special cases for test inputs and no test-environment
  detection.
- Mock only at real boundaries (network, clock, third-party services), keeping
  the semantics the claim depends on. Code you own runs for real.
- Take each expected value from an independent oracle. A test that repeats the
  implementation's calculation keeps its mistakes.
- Write tests one at a time, after the behavior is clear. Tests written all
  up front describe behavior you imagined.

## Choose the layer by risk

Use the narrowest layer that shows the behavior faithfully: pure tests for
calculations and state transitions; integration tests for wiring,
persistence, protocols and configuration; contract tests for the agreed shape
between consumer and provider; a few end-to-end tests for critical journeys;
runtime probes when the browser, OS or packaging changes the result. To prove
a change in the running product, follow
[references/end-to-end-verification.md](references/end-to-end-verification.md).

## Keep tests worth having

- Search the owning layer for a test of the same behavior and strengthen it
  before adding another.
- Each new test protects a distinct behavior, regression or failure mode, and
  fails with a message that says what broke.
- Coverage shows code nothing runs; mutation testing on changed, high-risk
  code shows whether assertions notice change. Neither number proves anything.
- Remove an obsolete or implementation-coupled test only with evidence the
  behavior stays protected.

## Flaky and slow tests

- Use synthetic, portable values: no operator paths, credentials or raw
  incident data.
- Use isolated temporary resources and restore clocks, environment, globals,
  working directory, mocks and handles.
- Replace sleeps with a controllable clock or an event.
- A retry that passes shows nondeterminism. Find the cause, or quarantine the
  test with an owner, a reason and a removal condition.

## Report

Behavior covered, oracle source, layers, and the focused and broader gates run
with their results. Every test file added, changed or deleted, with the
reason; a changed assertion names the requirement behind it. Residual untested
risk. Red-green-refactor does not by itself prove correctness, so say what was
checked and no more.
