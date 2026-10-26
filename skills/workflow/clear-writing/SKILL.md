---
name: clear-writing
description: Write, rewrite, or review prose so it is clear, accurate,
  structured, and appropriate for the audience.
tags:
  - writing
  - plain-language
  - editing
  - communication
---

# Clear Writing

Use this skill when writing, rewriting, or reviewing prose for any audience:
reports, research briefs, explanations, proposals, support replies, product
copy, UI text, public content, internal communication, educational material, or
technical documentation.

Do not use this skill to replace a required brand, legal, academic, regulatory,
or domain-specific style. Apply it inside those constraints.

Issue and PR procedures live in writing-issues and writing-pr. Materially
unclear intent belongs to problem-clarification; do not turn routine editing
into an interview. Existing text and prior agent summaries are claims to check,
not proof of correctness.

Writing and editing procedure:
1. Establish the reader's task, prior knowledge, language, genre, and requested
   scope from available context. Supply the knowledge they need to understand,
   decide, or act that they do not already have. Ask only when missing context
   materially changes the result. Proofreading does not authorize a new argument.
2. Identify what must remain true: quantities and units, negation, conditions,
   uncertainty, causal strength, attribution, and required terminology. Preserve
   evidence, citations, quotations, identifiers, code, tables, and required
   format. Use supplied or verified facts when drafting; do not invent specifics
   to make a sentence persuasive. Flag or check suspected factual errors rather
   than silently strengthening, correcting, or endorsing them. Route material
   factual investigation to research.
3. Repair the reader's path before polishing sentences, within the requested
   scope. Find the buried point, missing prerequisite, unexplained consequence,
   misplaced caveat, or repeated paragraph. Lead with the main point when the
   genre permits; introduce necessary context where the reader needs it. Keep
   evidence and qualifications beside the claims they support. Choose the order
   for this artifact instead of imposing a fixed outline.
4. Make each sentence connect to the next. Resolve ambiguous subjects and
   pronouns; keep modifiers near what they qualify and use stable terms for the
   same concept. Prefer concrete nouns and direct verbs. Keep passive voice when
   the actor is unknown, unimportant, or the receiver is the useful focus. Define
   unfamiliar terms near first use; retain specialist language when it serves
   this reader's precision. Cut filler, hype, empty attribution, and repetition
   while retaining useful explanations and transitions. Follow the author's
   voice and locale; punctuation, sentence length, and vocabulary are contextual
   choices, not universal bans. Shorter is useful only if it is still clear.
5. Check the result against the source and request. Did any claim become more
   certain, general, causal, or precise than the evidence allows? Did a condition,
   exception, unit, or attribution disappear? Can the intended reader understand
   the point and any supported next action without reconstructing missing context?
   Restore lost meaning and remove unsupported additions. Leave already-clear
   passages unchanged unless the requested transformation requires an edit.

Choose the smallest representation that helps the reader:
- a concrete before/after example for behavior;
- pseudocode for logic, a call tree for execution order, or a shallow file tree
  for responsibility;
- a small sequence or data-flow diagram for interactions across boundaries;
- a table for comparable options or measurements.
Use informative headings and lists when they help navigation; make link text
descriptive. Use plain prose when it is already clear. Keep necessary ownership,
ordering, and failure paths visible. Label schematic diffs and hypothetical examples so
they cannot be mistaken for actual patches, captures, or measured results.
Place each representation beside the claim it explains, with a text equivalent
where needed. Do not generate an interactive artifact or a video by default.

When the user asks for concise, scannable, execution-oriented replies, or work
spans turns and its state must stay visible, also apply
[action-first.md](references/action-first.md).

Output:
- If drafting or rewriting, provide the requested text. Keep internal checks
  internal; do not add a draft/audit/final sequence or a self-assigned score.
- If reviewing, list the highest-impact issues first with examples and concrete
  edits.
- Surface unresolved factual uncertainty or conflicting constraints when they
  affect use of the result. Do not fabricate a resolution or a next action.

Reference basis:
- ISO 24495-1 plain language principles: reader need, findability,
  understandability, and usability.
- GOV.UK and other public-sector content design practice: plain words, active
  voice, useful headings, and reader-task orientation.
- Google technical-writing audience guidance: bridge the reader's knowledge gap
  while preserving technical precision.
