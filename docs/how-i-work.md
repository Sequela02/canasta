# How I work with agents

I'm Ricardo Armenta, also known as Canitas. I want less supervision and stronger
evidence—not more ceremony or more agents. I own the outcome; the agent helps
me explore, decide and build. This is my working method, not a proven recipe.

**Opinion** marks my choices and practitioner advice. **Evidence** marks an
observed result with limits. A source can inspire a rule without proving that
rule improves delivery. Sources were checked on 2026-10-26 where accessible;
missing original links are explicitly marked rather than reconstructed.

## 1. I say Explore, Decide or Build

**Opinion.** Explore means findings, not edits. Decide means compare options and
recommend, stopping before implementation. Build means implement the agreed
outcome. For substantial work I name the user, observable finish line, exclusions
and accountable human. A clear small edit needs no interview or elaborate plan.

I use a plan for commitments and a bounded prototype for reversible uncertainty.
New findings do not authorize new scope: I explicitly continue, revise or cancel
when the accepted goal changes. This combines the design-first emphasis in
[Matt Pocock's skills](https://github.com/mattpocock/skills) with the experimental
approach attributed to poteto's [pstack](https://github.com/backnotprop/pstack).
Those are practitioner approaches, not comparative evidence. Gentleman
Programming's [ODD description](https://github.com/Gentleman-Programming/gentle-ai#features)
also distinguishes questions from authorized changes and keeps small work small.

## 2. I hand off the task, not the job of recovering my context

**Opinion.** A brief carries the goal, deliverable, exclusions, check, relevant
source owners and authority limits. Before nontrivial action, the receiver
briefly restates those points and labels consequential premises **verified**,
**inferred** or **unknown**. It checks local facts before relying on them.
A restatement is an alignment check, not an extra approval ritual.

The restatement idea is attributed to poteto in my research digest; the specific
original post's **link not found**. Pocock's repository provides the related
pattern of bounded implementation tasks. My own message analysis also exposed
repeated context and scope corrections; that motivates this habit, not a claim
that restatements have a measured productivity effect.

## 3. I batch decisions and keep the finish line stable

**Opinion.** I want related decisions together: object, recommendation, evidence,
consequence and meaningful alternatives. The agent resolves reversible details
inside scope; I retain product policy, taste and consequential authorization.
“Continue” keeps work flowing. It does not mean “publish this” or “merge that.”

I freeze a small accepted slice and defer adjacent discoveries unless they
invalidate safety, correctness or the core promise. Asynchronous batching is
attributed to Thorsten Ball in the source digest; the specific original post's
**link not found**. My message analysis suggested opportunities to batch related
choices, but did not establish that each short acknowledgment was wasted effort.

## 4. I research only to change a decision

**Opinion.** I name the decision, unknown, budget and stopping condition. Research
ends with an answer or a named gap when that budget expires. Another opinion
needs a specific disagreement. A prototype answers one uncertainty; it is not
permission to build a new product.

The digest attributes an argument against open-ended multi-approach prompting
to **Prompt-Induced Waste — link not found**. I have not independently verified
that paper or its reported numerical effects, so I do not repeat them as fact.
The budget and stopping rule here are my judgment, also motivated by repeated
research directions in my own message analysis.

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
The stronger “ask for irrefutable proof” formulation is attributed to Thorsten
Ball in the digest; the specific original post's **link not found**. Pocock's
skills supply test-first and review practices, not proof that TDD always helps.

## 6. I review the actual UI path

**Opinion.** For a UI change I want a screenshot or recording from the real path,
with revision, viewport, data and interaction named. Sensitive data stays out of
the capture. If the agent cannot render it, it says so. A diagram or generated
image can explain intent; it is not evidence that the app rendered correctly.
I still make the visual and product acceptance decision.

Willison's real-code testing advice motivates exercising the actual path; my
requirement for captures is an extension of it, not a measured finding from that
article. **SWE-Serve — link not found** is named in the digest as a warning about
narrow checks versus end-to-end behavior. I retain the caution without claiming
its experiments or results have been independently verified here.

## 7. I leave work resumable and knowledge in one place

**Opinion.** Interrupted work leaves scope, workspace/revision, completed work,
pending decisions and unrun checks. Unknown side effects remain unknown until
inspected; recovery never blindly replays a consequential action. Durable
decisions and rationale belong with their repository or work item, not in
competing chat summaries. I preserve unrelated edits and remove only task-owned
scratch material when its purpose ends.

The digest attributes persistent progress records to **Anthropic's long-running
agent guidance — link not found**; retrieval of the candidate original page
failed. I do not claim its details as verified. [Mitchell Hashimoto's own
account](https://mitchellh.com/writing/my-ai-adoption-journey) describes developing
a harness and giving agents ways to verify work. My canonical-record rule and
resumption fields are my application of that general direction. Repeated
mistakes should earn an enforcing test, type or lint rule, not another paragraph
of instructions; the particular Hashimoto passage behind that attribution in
the digest was not located, so its **link not found**.

## 8. I scale review to consequences

**Opinion.** I classify risk before building and revisit it when consequences
change. Local reversible changes get focused checks and lightweight review.
Shared behavior needs integration evidence and targeted review. Security, money,
private data, production and difficult-to-reverse contracts require independent
technical review and my examination of the consequential behavior.

Gentleman Programming's linked repository describes proportionate review;
Pocock's work motivates deliberate human judgment. The specific original
one-way-door post attributed to Pocock is **link not found**. My tiers are policy
choices, not experimentally established boundaries. Cross-family review is a
hypothesis worth measuring, not a correctness guarantee.

## 9. I delegate for a named benefit

**Opinion.** One agent is the baseline. I delegate for independent judgment,
disjoint parallel work or context isolation. Each writer gets bounded ownership,
constraints, checks and a stop condition. I verify an adopted result in the
destination workspace; a child report is not integration evidence. Overlapping
writes wait rather than race.

The digest contrasts Gentleman Programming's bounded roles with an **Anthropic
account dated October 2026 — link not found** arguing for simpler architectures.
I have not verified that comparison or a general claim that one agent wins.
Coordination has a cost; more concurrent agents is not itself more throughput.

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
other projects. Gentleman Programming's repository likewise keeps commit, push
and release decisions with the user; my complete action boundary is my own.

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

## What my own analysis can and cannot tell me

**Evidence with limits.** A private analysis of my October 2026 message export
looked at clarification, scope, decisions, research, evidence and continuity.
It separated obvious automated/supervisor records from the comparison pool;
categories overlapped and copied material could still contaminate them. Agent
replies were unavailable. Message counts were not independent failures, time
saved, or proof that a particular agent worked. No private messages or identities
are distributed here.

**Opinion.** That analysis tells me where to try habits, not that this method is
validated. My test is whether I get accepted work with less avoidable supervision
and no hidden quality, privacy or authority regressions. If not, I change it.
