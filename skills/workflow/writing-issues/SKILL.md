---
name: writing-issues
description: Draft or revise an issue, bug report, or feature request with
  concrete impact, evidence, and observable acceptance criteria; use when
  preparing an issue for a tracker.
tags:
  - writing
  - engineering
  - issues
---

# Writing Issues

Use for issue titles and bodies. Apply clear-writing for prose and examples;
use problem-clarification only when missing information materially affects the
issue. Writing a draft does not require implementing the proposed solution.

1. Read the request, relevant evidence, repository contribution rules, and the
   applicable issue template. Check related issues and work when accessible;
   distinguish a duplicate from a related problem. Do not invent tracker IDs,
   labels, priority, links, or checks. State an unavailable material source once.
2. Name the problem or desired capability in the title. Open with who or what
   is affected, the trigger or unmet need, and why it matters. Describe current
   and desired behavior in terms someone can observe without this conversation.
3. For a bug, give the smallest known reproduction, relevant environment or
   revision, expected versus actual result, and supporting evidence. Say when
   the report has not been reproduced. Keep suspected causes and proposed fixes
   separate from observations; a plausible explanation is not a diagnosis.
4. For a feature, explain the use case and constraints. Include a proposed
   solution only when useful and label its decision status. Do not turn an
   initial request into a committed architecture or an implementation inventory.
5. State observable acceptance criteria that distinguish success from the current
   problem. For an investigation, name the question and evidence needed to resolve
   it instead of promising a fix. Include scope boundaries, dependencies, or open
   decisions only when they prevent a material misunderstanding.
6. When breaking a plan into several issues, write one per independently
   verifiable slice (see implementation-planning), describe the end-to-end
   behavior it delivers rather than a layer inventory, and list the issues that
   block it, using the tracker's native blocking link where it has one. Show
   the breakdown before creating anything; approving it does not authorize
   publishing or labels.
7. Follow the repository template, including instructions to omit inapplicable
   sections. Without a template, a small issue can be one paragraph plus an
   acceptance sentence. Use numbered reproduction steps or a comparison when
   helpful; omit empty headings and generic checklists. Preserve necessary facts
   while removing credentials and private data from publication-bound evidence.
8. Recheck that the title and body describe the same problem, links exist, and
   acceptance criteria are requirements rather than claims of completed work.
   Return the draft, or use the existing authorized tracker workflow if creation
   or updating was requested. Never infer publication authority from this skill.
