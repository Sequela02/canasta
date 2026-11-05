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
2. Give each defect its own finding, written as this block:

   ```text
   1. src/cart.ts:22, medium: a discount over 100% makes the total negative.
      applyDiscount subtracts percent / 100 * total without a cap, so a
      150% coupon charges -50.00 against the spec's "never below zero".
      Fix: clamp the result at zero.
      Confirmed: node -e "<harness>" → total(100, 150) returned -50.
   ```

   - First line: `file:line`, severity and the defect.
   - Then the triggering condition and its impact, in one or two sentences.
     Quote the requirement only for an intent finding.
   - Then the narrowest correction direction, in one sentence, without
     rewriting the author's solution.
   - Last, one status line: `Confirmed: <command> → <result>`, or
     `Unverified: <the check that would settle it>`. Every finding ends with
     one, also when you could run nothing. A finding supported only by reading
     the code is unverified. Don't replace the status lines with a summary of
     what you ran.
3. Report only admitted findings. Leave out observations that fail admission;
   don't list them under another heading.
4. Don't summarize a lens or a standard that found nothing.
5. End with one or two lines: the surface you reviewed, what you couldn't
   review or run, and the residual risk.
6. With no findings, write only `No findings.` and the closing lines of item 5.
   Do not invent a finding to avoid an empty result.
7. Cut every word that does no work. Keep numbers, conditions, identifiers and
   negations exactly.

Do not rewrite the author's intent unless the evidence shows a real problem.
