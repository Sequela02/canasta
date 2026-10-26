# How I work with agents

I'm Ricardo Armenta, also known as Canitas. I want less supervision and stronger
evidence—not more ceremony or more agents. I own the outcome; the agent helps
me explore, decide and build. This is my working method, not a proven recipe.

**Opinion** marks my choices and practitioner advice. **Evidence** marks an
observed result with limits. A source can inspire a rule without proving that
rule improves delivery. The linked sources support the claims beside them;
the remaining rules are my own practices, not research findings.

## 1. I say Explore, Decide or Build

**Opinion.** Explore means findings, not edits. Decide means compare options and
recommend, stopping before implementation. Build means implement the agreed
outcome. For substantial work I name the user, observable finish line, exclusions
and accountable human. A clear small edit needs no interview or elaborate plan.

I use a plan for commitments and a bounded prototype for reversible uncertainty.
New findings do not authorize new scope: I explicitly continue, revise or cancel
when the accepted goal changes. Planning and experimentation serve different
jobs in my work: one coordinates an agreed change; the other tests a premise.
Neither needs to become a mandatory process for every task.

## 2. I hand off the task, not the job of recovering my context

**Opinion.** A brief carries the goal, deliverable, exclusions, check, relevant
source owners and authority limits. Before nontrivial action, the receiver
briefly restates those points and labels consequential premises **verified**,
**inferred** or **unknown**. It checks local facts before relying on them.
A restatement is an alignment check, not an extra approval ritual.

My own review of a few weeks of my agent sessions showed me how often I had
to recover context or correct scope. That motivates this habit; it does not
establish that restatements improve productivity.

## 3. I batch decisions and keep the finish line stable

**Opinion.** I want related decisions together: object, recommendation, evidence,
consequence and meaningful alternatives. The agent resolves reversible details
inside scope; I retain product policy, taste and consequential authorization.
“Continue” keeps work flowing. It does not mean “publish this” or “merge that.”

I freeze a small accepted slice and defer adjacent discoveries unless they
invalidate safety, correctness or the core promise. I batch choices to reduce
avoidable interruptions, not to eliminate conversation. A short acknowledgment
can still be useful; fewer messages is not my goal.

## 4. I research only to change a decision

**Opinion.** I name the decision, unknown, budget and stopping condition. Research
ends with an answer or a named gap when that budget expires. Another opinion
needs a specific disagreement. A prototype answers one uncertainty; it is not
permission to build a new product.

The budget and stopping rule are my judgment. I want enough investigation to
make the decision responsibly, with the remaining uncertainty visible, rather
than an open-ended search for another reassuring opinion.

## 5. I ask for evidence matched to the claim

**Opinion.** A completion claim names the revision, check, observed result and
limits. For a reported bug I want reproduction before repair when feasible,
then the regression check passing. Tests exercise behavior; a proof establishes
its encoded contract under assumptions; a model explores the interleavings it
actually models. None independently establishes that I asked for the right thing.

**Not behavioral evidence:** confidence, an agent's report, reviewer agreement,
code reading, popularity, an unrun test, compilation alone, or model agreement.
Passing checks inform my acceptance; they do not perform it for me.

[Simon Willison's account](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
explicitly emphasizes testing generated code and using tools that can run it.
My reporting requirements go further: I want the check's limits beside its
result, so I can judge whether the evidence answers the actual question.

## 6. I review the actual UI path

**Opinion.** For a UI change I want a screenshot or recording from the real path,
with revision, viewport, data and interaction named. Sensitive data stays out of
the capture. If the agent cannot render it, it says so. A diagram or generated
image can explain intent; it is not evidence that the app rendered correctly.
I still make the visual and product acceptance decision.

Willison's real-code testing advice motivates exercising the actual path; my
requirement for captures is an extension of it, not a measured finding from that
article. A narrow check may leave layout, interaction and integration risks
untested; I decide which real paths need additional evidence.

## 7. I leave work resumable and knowledge in one place

**Opinion.** Interrupted work leaves scope, workspace/revision, completed work,
pending decisions and unrun checks. Unknown side effects remain unknown until
inspected; recovery never blindly replays a consequential action. Durable
decisions and rationale belong with their repository or work item, not in
competing chat summaries. I preserve unrelated edits and remove only task-owned
scratch material when its purpose ends.

These resumption fields and the canonical-record rule are my own practice.
[Mitchell Hashimoto's account](https://mitchellh.com/writing/my-ai-adoption-journey),
in “Step 5: Engineer the Harness,” describes responding to recurring agent
mistakes with better guidance or programmed tools, and giving agents ways to
verify their work. I take the same opportunity to improve the feedback available
to the next run. Which intervention fits depends on the failure; another
instruction is not always the answer.

## 8. I scale review to consequences

**Opinion.** I classify risk before building and revisit it when consequences
change. Local reversible changes get focused checks and lightweight review.
Shared behavior needs integration evidence and targeted review. Security, money,
private data, production and difficult-to-reverse contracts require independent
technical review and my examination of the consequential behavior.

My tiers are policy choices, not experimentally established boundaries.
Cross-family review is a hypothesis worth measuring, not a correctness
guarantee. I want review effort to follow the possible harm, not a fixed ritual.

## 9. I delegate for a named benefit

**Opinion.** One agent is the baseline. I delegate for independent judgment,
disjoint parallel work or context isolation. Each writer gets bounded ownership,
constraints, checks and a stop condition. I verify an adopted result in the
destination workspace; a child report is not integration evidence. Overlapping
writes wait rather than race.

This is not a claim that one agent always wins. Coordination has a cost;
I judge delegation by whether its independent result helps complete the task,
not by how many agents are active.

## 10. I separate outward authority from technical success

**Opinion.** Private data, credentials and project identities stay inside their
approved audience. I use minimum necessary, redacted context for external
research, issues and captures. Publishing, pushing, opening PRs, deploying,
granting access and destructive actions need explicit, bounded authorization
naming the object and conditions. An answered question does not grant it.

Every PR ends with a **risk note: one-way or two-way door, blast radius,
evidence**. The agent **never merges unless the project's stated policy allows
it**. A narrow queue policy may allow a low-risk class after its specified CI,
review and risk-note conditions; without that policy, the agent does not merge.
My present preference is to keep behavior changes and irreversible actions under
explicit owner judgment. This is a policy choice, not automatic authority for
other projects. The action boundary here is my own: technical success and
permission to act are separate decisions.

## 11. I measure accepted outcomes, not activity

**Evidence.** [METR's July 2025 randomized study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)
reports that 16 experienced open-source developers took 19% longer with the
studied early-2025 AI tools on 246 real tasks. It is one setting and tool era,
not evidence that every developer or current agent is slower. The
[DORA 2025 report page](https://dora.dev/research/2025/dora-report/) describes AI
as amplifying existing organizational strengths and weaknesses; that synthesis
is not a causal estimate of the value of this pack.

**Opinion.** I track accepted delivery, owner-active and elapsed time,
interventions, rework, escaped defects and evidence gaps. I keep denominators,
unfinished tasks, changed scope, external waiting and follow-up windows visible.
Messages, tokens, PRs and agent counts may explain cost, but are not productivity.
I compare similar tasks, change one practice at a time and allow “inconclusive.”

## What my own review can and cannot tell me

**Personal observation, not a public study.** My own review of a few weeks of my
agent sessions helped me notice recurring clarification, scope and recovery
work. The session data is private and is not distributed here. I cannot infer
time saved or comparative agent quality from those observations.

**Opinion.** That review tells me where to try habits, not that this method is
validated. My test is whether I get accepted work with less avoidable supervision
and no hidden quality, privacy or authority regressions. If not, I change it.
