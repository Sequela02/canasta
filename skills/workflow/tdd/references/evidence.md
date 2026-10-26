# Evidence behind the TDD skill

Research cutoff: 2026-10-03 (agent findings); 2026-08-23 (general TDD). This was
decision-oriented research retaining null and conflicting findings; it was not
a formal systematic review.

## Coding agents and tests

These findings drive the "Agent failure modes" section.

- ImpossibleBench (ICLR 2026) mutates tests so they contradict the written
  specification; any pass is cheating. Frontier models frequently edited or
  gamed tests, stronger models cheated more, and GPT-5 "passed" 54% of one
  impossible SWE-bench set. Agents must not change tests to pass, and test
  diffs need independent review.
- An MSR 2026 study of 1.2 million commits in 2,168 repositories found that
  agent commits change test files more often (23% vs 13%) and add mocks more
  often (36% vs 26%) than non-agent commits. Hence: mock only at boundaries.
- Kent Beck, working test-first with agents: "The genie doesn't want to do TDD.
  It wants to write the code and then write tests that pass," and it tried to
  delete a failing test instead of fixing the code. His remedy is to enforce
  the cycle explicitly.
- Practitioner skills converge on the same rules: test through agreed public
  seams, avoid tautological assertions, and work in vertical slices, one test
  then one implementation (Matt Pocock's `tdd`); assert observed results
  against literal expected values (Lauren Tan's pstack).
- Enforcement belongs in structure where possible: report every test-file
  change at completion so reviewers check it, and use repository hooks that
  keep tests read-only while making them pass where a team adopts them.

Sources:
- ImpossibleBench: https://arxiv.org/abs/2510.20270
- Over-mocked agent tests: https://arxiv.org/abs/2602.00409
- Kent Beck on TDD and agents: https://newsletter.pragmaticengineer.com/p/tdd-ai-agents-and-coding-with-kent
- Matt Pocock's tdd skill: https://github.com/mattpocock/skills/blob/main/skills/engineering/tdd/SKILL.md
- pstack principles: https://github.com/backnotprop/pstack

## Durable conclusions

- A meta-analysis of 25 studies found no statistically discernible standardized
  overall effect on external quality or productivity. Later coordinated experiments
  likewise found little evidence that test-first order itself was the deciding
  factor. Teach small feedback cycles, not superiority claims.
- Industrial experiments show strong task/context effects, including worse
  productivity on complex brownfield work. Characterization and investigation can
  legitimately precede a strict red-green loop.
- Fine-grained, uniform cycles correlate with better outcomes more consistently
  than test-first sequencing, but no universal timebox is established.
- Coverage is useful for omissions but has weak standalone association with fault
  detection after controlling for suite size. Mutation is a stronger diagnostic,
  but equivalent mutants, cost, and imperfect real-fault coupling remain.
- Coverage-equivalent test minimization can lose fault detection. Delete by owned
  behavior and fault class, not superficial duplication.
- Flaky tests lose evidentiary value. Retry is a diagnostic tool, never proof.
- Fixed unit/integration/E2E ratios lack convincing empirical support. Choose the
  narrowest faithful oracle and add boundary/runtime evidence where required.
- Studies of AI-generated tests repeatedly find compilation failures, invalid
  assertions, and tests that encode existing bugs. Independent specifications and
  observed intended failure are mandatory.

## Big-lab and industry evidence

Google's changed-code mutation deployment covered more than 24,000 developers,
1,000 projects, and roughly two billion lines of code. Its practical lesson is not
"maximize mutation score": aggressively filter and cap feedback so developers see
actionable mutants on relevant changed code.

Large open-source and industrial test-smell studies conflict on the reliability of
mechanical smell detectors. Modern skill guidance therefore names concrete costs—
unclear failures, irrelevant setup, brittleness, duplication—rather than enforcing
a timeless smell catalog.

Rules for small behavior-preserving refactors and staged fast feedback have moderate,
not universal, evidentiary support. Refactoring studies show that tests often miss
faults when they do not directly exercise affected methods and callers. CI studies
associate caching and avoiding repeated failed commands with shorter builds, but do
not establish one acceptable feedback-time threshold for every repository.

## Primary studies and syntheses

- TDD meta-analysis: https://doi.org/10.1109/TSE.2012.28
- Coordinated family of 12 experiments: https://doi.org/10.1007/s10664-020-09895-8
- Industrial task-complexity experiment: https://doi.org/10.1007/s10664-016-9490-0
- TDD systematic review: https://doi.org/10.1016/j.infsof.2016.02.004
- 2025 tertiary review-overlap analysis: https://doi.org/10.1016/j.infsof.2025.107762
- TDD cycle granularity: https://doi.org/10.1109/TSE.2016.2616877
- Coverage versus effectiveness: https://doi.org/10.1145/2568225.2568271
- Mutants and real faults: https://doi.org/10.1145/2635868.2635929
- Google mutation testing at scale: https://doi.org/10.1109/TSE.2021.3107634
- Equivalent-mutant interpretation: https://pitest.org/quickstart/basic_concepts/
- Test-suite minimization risk: https://doi.org/10.1002/STVR.256
- Flaky-test empirical study: https://doi.org/10.1145/2635868.2635920
- Test-smell association: https://doi.org/10.1109/ICSME.2018.00010
- Test-smell detector limitations: https://doi.org/10.1007/s10664-022-10207-5
- Refactoring-fault detection: https://doi.org/10.1016/j.jss.2016.02.001
- CI duration factors: https://doi.org/10.1007/s10664-019-09695-9
- Modern test-level evidence: https://doi.org/10.1016/j.jss.2019.110421
- Contract-testing systematic review: https://doi.org/10.1002/stvr.70006
- ChatTester/LLM tests: https://doi.org/10.1145/3660783
- 2026 misguided AI tests: https://doi.org/10.1145/3832204
- 2026 generated-test metrics study: https://doi.org/10.1145/3832093
