---
name: code-review-findings
description: Review completed code changes findings-first with severity,
  evidence, actionable defect risk, and verification gaps.
tags:
  - engineering
  - review
---

# Code Review Findings

Use this skill for quality gates and completed-change review.

Workflow:
1. Read the task, contract, and relevant repository context before judging the
   diff. Fix the comparison point (a commit, branch or merge-base) and include
   uncommitted working-tree changes when they are in scope. Inspect targeted
   surrounding code, dependencies, and tests; avoid indiscriminate context
   loading.
2. Map the changed surface and likely blast radius. Review every human-authored
   line in scope or state the exceptions.
3. Check correctness, regressions, security and authority, boundary direction,
   failure handling, concurrency and data integrity, maintainability, and
   verification gaps. Treat explanation debt as a maintainability or architecture
   risk when safe change depends on creator or session context. Name specialist
   review that remains necessary.
4. Apply two separate lenses and report them separately, because a change can
   pass one and fail the other:
   - **Intent:** against the issue, spec, or request, what is missing or
     partial, what was added beyond it, and what looks implemented but wrong.
     Quote the requirement. Say so when no spec exists.
   - **Standards:** against the repository's documented standards, cite the
     rule. Skip what tooling already enforces; a documented repository
     standard overrides general smells, which stay judgment calls.
   Use an independent reviewer per lens only when risk justifies the cost;
   reviewers agreeing is not evidence.
5. Review tests as production code: confirm that they are correct, reliable,
   behavior-focused, and contribute a distinct behavioral signal. A missing test
   is a finding only when a material behavior is unprotected and a specific test
   would close the gap.
6. Confirm each candidate finding before you report it. Run the narrowest check
   you can without changing the files under review: an existing test, a short
   script, or an executable counterexample. Keep the command and its result.
   Reasoning about the code is a hypothesis, not a confirmation, and a candidate
   that a check refutes is dropped.
7. When confusion reveals durable missing knowledge, repair the narrow canonical artifact:
   clearer code or names first, then tests, the owning architecture or
   operations document, or a decision record when persistent rationale matters.
   A review-thread explanation alone does not resolve the finding.

Finding admission:
- Report only an issue introduced or exposed by the change with a concrete
  condition and material impact.
- Anchor the finding to the narrowest file and line evidence, and explain the
  causal path from input or state to observable failure.
- Rank severity by impact, reach, and recoverability, not by rhetorical
  confidence. If verification is incomplete, say so.
- When you can't run a candidate, for example because it depends on code you
  can't see, reproduce it with a minimal harness or reconstruct the missing
  part from what the diff proves. If you still can't confirm it, report it as
  an unverified finding with its condition, impact and the check that would
  settle it, not only as a verification gap: a real defect demoted to a
  footnote is a missed finding.
- Do not report speculative findings, stylistic preferences, or mechanically
  enforced concerns as defects. A finding is speculative when nothing in the
  change supports it, not when part of its evidence is out of view.
- Do not demand duplicate tests, raw coverage increases, or implementation-detail
  assertions when existing tests already protect the behavior.

Output:
1. Lead with findings ordered by severity; omit summaries before findings.
2. For each finding, give location, triggering condition, impact, evidence,
   and the narrowest correction direction without rewriting the author's
   solution. End it with one status line: `Confirmed: <command> → <result>`,
   or `Unverified: <the check that would settle it>`. A finding supported only
   by reading the code is unverified.
3. State the reviewed surface and any material surface not reviewed, verification
   performed, and residual risk.
4. If no issues are found, say so clearly. Do not invent a finding to avoid an
   empty result.

Do not rewrite the author's intent unless the evidence shows a real problem.
