---
name: benchmark-readiness-review
description: Judge benchmark validity, reproducibility, comparability, and claim
  readiness with tiered evidence verdicts.
tags:
  - eval
  - benchmark
  - readiness
---

# Benchmark Readiness Review

Use this skill to audit benchmark or eval designs, runs, leaderboards, deployment
decisions, and public performance claims. Review the measurement and evidence;
do not infer readiness from a headline score or a benchmark's reputation.

Review contract:
1. Define the claim before reading the aggregate. Record the claim type
   (bounded regression or deployment decision, controlled comparison, maximum
   elicitation or capability ceiling, or safeguard robustness), measured
   construct, intended decision, target population or task distribution, and
   cutoff. Name the evaluated object exactly: model, model-plus-harness, product
   system, safeguard, or process. Do not attribute a system result to one part.
2. Audit tasks, data, and ground truth. Inspect a risk-based sample across
   passes, failures, subgroups, and edge cases; run reference solutions where
   possible; and check solvability, ambiguity, label quality, scorer coverage,
   unintended constraints, duplicates, and representativeness. Investigate
   contamination or answer leakage, browsing exposure, shortcut or reward
   hacking, saturation, distribution shift, and test-set selection or tuning.
   Keep development, validation, and held-out evidence distinct.
3. Freeze the protocol and execution identity: benchmark, dataset, task,
   harness, adapter, scorer, and judge versions or hashes; model and provider
   revision, route, reasoning setting, prompts, tools, retrieval, memory,
   safeguards, and authority; sampling parameters and seeds; concurrency;
   turn, token, attempt, time, and cost budgets; hardware, sandbox, resource
   enforcement, dependencies, and commit; and retry, timeout, stopping,
   exclusion, and invalid-run policies. A controlled comparison keeps
   predeclared tasks, scoring, budgets, and harness conditions equivalent or
   uses paired trials. Maximum elicitation may optimize each system, but must be
   labeled as a system-to-system comparison and disclose the optimization.
4. Verify execution integrity through the ordinary product contract. An adapter
   must not add benchmark-only prompts, tools, credentials, authority, answer
   access, or recovery paths. Detect provider fallback, route drift, partial
   execution, caching, cross-trial state, and mixed cohorts. Distinguish a model
   failure from an instrument failure: model-caused failures stay in the metric
   denominator; infrastructure, harness, or grader failures remain visible as
   invalid and follow only the predeclared retry policy.
5. Validate scoring against the construct. Prefer the outcome or final state
   over a prescribed path; use trajectory constraints only when the path is
   itself a requirement, such as policy, security, or resource use. Exercise
   scorers with reference answers, known failures, edge cases, and shortcut
   probes. For human or model-based grading, retain the rubric and judge prompt,
   model, version, and sampling settings; measure human calibration, agreement,
   and error by subgroup; and test judge sensitivity to position, verbosity,
   style, self-preference, and candidate identity. Validate user simulators and
   model graders separately from the system under test.
6. Review the analysis plan and accounting. State the primary metric, unit of
   analysis, denominator, aggregation, threshold, and direction before comparing
   results. Prefer paired analysis on the same tasks when supported. Report
   sample size, repetitions, effect size, and an uncertainty interval computed
   at the actual sampling unit; include subgroup and failure analysis, the full
   distribution when averages hide tails, and corrections or cautions for
   multiple comparisons and tuning. Distinguish pass@k candidate coverage from
   pass^k repeated-success reliability and report pass^1 when applicable. Keep
   unsupported, failed, invalid, retried, excluded, and unknown trials in the
   reconciliation. Report quality and safety beside latency, token, and cost
   evidence instead of collapsing incompatible properties into one score.
7. Verify evidence and reproducibility. Retain per-item trials, inputs, outputs,
   final states, transcripts or trajectories, tool calls, scorer outputs,
   diagnostics, usage, costs, exclusions, and immutable artifact identities.
   Separate repeatability (same team and setup), reproducibility (independent
   rerun from the frozen package), and independent replication (new data or
   design). Artifact availability does not prove independent reproduction.
8. Bound every conclusion to the tested system, task distribution, protocol,
   benchmark version, and date. Compare results only when the benchmark rules
   make them comparable; otherwise report separate cohorts. Treat official or
   verified leaderboard status as a separate fact, not validity proof. Disclose
   adverse evidence, conflicts of interest, unreviewed surfaces, and whether the
   benchmark result transfers to the claimed deployment. Production monitoring,
   incident evidence, user research, or controlled online experiments may still
   be required for a deployment claim.

Verdict:
- blocked: a critical construct, task, scorer, execution, identity, or accounting
  defect prevents the result from supporting the stated decision;
- diagnostic-only: useful for debugging or eval development, but not for a
  controlled decision or comparative claim;
- internal-decision-ready: valid and repeatable enough for the stated bounded
  internal decision, with uncertainty and limitations reported;
- external-evaluation-ready: the frozen protocol, lawful inputs, implementation,
  raw evidence, and instructions form a portable package another evaluator can
  run; this does not assert that reproduction occurred;
- public-claim-ready: the exact public wording is supported by comparable
  evidence, uncertainty, limitations, protocol disclosure, benchmark rules, and
  an explicit reproduction or replication status.

Output findings first, ordered by how strongly they cap the verdict. Then state
exactly one highest justified verdict, the reviewed claim and evaluated object,
cohort and benchmark snapshot, evidence satisfying the tier, contradictory or
adverse rows, verification performed, reviewed and unreviewed surface, repair
needed for the next tier, and residual uncertainty. The readiness gates are
conjunctive and monotonic: one critical failure caps the verdict even when other
evidence is strong.
