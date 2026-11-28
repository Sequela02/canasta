---
name: benchmark-readiness-review
description: Check whether benchmark or performance numbers are valid, reproducible and fair to compare, before you report a speedup, publish a claim, compare results with someone else's, or act on an eval score. Gives a verdict from blocked to public-claim-ready.
license: Complete terms in NOTICE
metadata:
  source: "pstack benchmark-checklist by Lauren Tan, cursor/plugins 2f87c85"
  changes: "The seven questions are adapted; the claim, the evidence package and the verdict tiers are canasta's"
tags:
  - eval
  - benchmark
  - reproducibility
---

# Benchmark readiness review

A benchmark number is evidence for one sentence. Write that sentence first, then
check whether the run supports it. Don't read readiness from a headline score or
a benchmark's reputation.

## 1. Write the claim

State it in the words you would ship: "export is 30% faster at p50 on the 60k-row
dataset". Name:

- the thing measured (a model alone, a model plus harness, a product, a
  function),
- the decision it supports (internal choice, regression gate, public claim),
- the task set and the date.

A result for a system is not a result for one of its parts.

## 2. Ask the seven questions

Answer each with evidence from a run, not a guess from reading the code.

1. **What limits it?** Name the limiter (CPU, I/O, the load generator, a lock) from
   a profile taken in a run you don't report. A change that didn't move the
   number is explained by the limiter.
2. **Was every side tuned the same way?** Same build, flags, data, versions,
   cache warmth. A side left on defaults means you compared settings, not
   implementations.
3. **Does the number break a limit?** Bytes per second against disk and network
   bandwidth. Time saved against the time the changed piece took: removing 10% of
   the run speeds it up by at most about 11%. A result past a limit measured
   something else.
4. **Did anything fail?** Count errors, timeouts and retries, and check that
   outputs are correct, not just present. A rejection is fast.
5. **Does it reproduce?** At least 5 runs per side, alternating A, B, A, B. Report
   the median and range. A gap smaller than the run-to-run spread is no
   difference.
6. **Does it matter?** Put a micro result next to the end-to-end path a user waits
   on, as a share of the whole.
7. **Did the work happen?** Confirm it ran inside the timed region: rows written,
   bytes read, result used. Lazy code and timeouts produce numbers for work that
   never happened.

For an eval of a model or agent, also check:

- **Tasks and answers.** Sample passes and failures, run reference solutions,
  look for leaked answers, duplicates and unsolvable items.
- **Scorer.** Score outcomes, not paths. Try the scorer on known-good, known-bad
  and shortcut answers. For a model judge, record its prompt and version.
- **Failure kind.** A model failure stays in the denominator. A harness or grader
  failure is marked invalid and retried only as the predeclared policy says.
- **Uncertainty.** Report the sample size and an interval at the real sampling
  unit. pass@k and pass^k answer different questions; say which.

## 3. Freeze and record

Write down what another person needs to rerun it: commit, dataset, harness and
scorer versions, model and route, prompts, tools, seeds, budgets, hardware, retry
and exclusion rules. Run the project's checks at the base first: a run whose base
fails is not a result. Keep per-item outputs, not only the aggregate.

Repeatable means the same team reran it. Reproducible means someone else reran it
from the frozen package. Published artifacts alone prove neither.

## 4. Give one verdict

The tiers are conjunctive: one critical failure caps the verdict.

- **blocked**: a defect in the task, scorer, execution or accounting means the
  result can't support the claim.
- **diagnostic-only**: useful for debugging, not for a decision or comparison.
- **internal-decision-ready**: valid and repeatable for the stated internal
  decision, with limits reported.
- **external-evaluation-ready**: the package lets another evaluator rerun it. No
  one has yet.
- **public-claim-ready**: the exact public wording is supported by comparable
  evidence, uncertainty, disclosed protocol and a stated reproduction status.

Compare with someone else's numbers only when their protocol matches yours;
otherwise report two separate cohorts.

## Report

Findings first, strongest cap first. Then the verdict, the claim, the evidence
that meets the tier, and the repair needed for the next tier. Lead with the
number, its unit, the run count, the range and the limiter:

> Inconclusive. p50 41 ms to 33 ms, median of 7 runs per side, range 32 to 35 ms
> after, limited by JSON parsing on one core. Errors were not counted (question
> 4), so the speedup is unconfirmed. Next tier: count failures and rerun.

Say which questions you could not check. A claim you can't name the limiter for is
inconclusive.
