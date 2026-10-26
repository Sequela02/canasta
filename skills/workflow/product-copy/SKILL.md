---
name: product-copy
description: "Write or revise interface and marketing copy, CTAs, claims, microcopy, or bilingual product wording."
---

# Product Copy

Write useful copy from product truth. This is a cross-project standards layer, not a brand voice, campaign strategy, or substitute for repository evidence.

## Authority

1. Read the repository's product, audience, brand, evidence, legal, and content owners before drafting. Existing authority outranks examples in this skill.
2. Do not invent customers, outcomes, metrics, pricing, availability, support commitments, security properties, integrations, or product maturity.
3. Mark a material missing fact as a content dependency. Do not disguise it with vague language.
4. Apply a named brand-voice overlay only to work owned by that brand. Never carry an organization's voice, another client's vocabulary, or a pilot's metaphors into an unrelated product.

## Boundaries

- A copywriting or copy-editing workflow may own drafting technique, conversion framing, or editorial passes. This skill supplies cross-project authority, evidence, terminology, multilingual, and whole-surface standards.
- Page argument and section order live in [page-architecture.md](references/page-architecture.md), with [evidence-and-objections.md](references/evidence-and-objections.md) and [surface-contracts.md](references/surface-contracts.md). It is an explicit-use canary: load it only when the operator asks for page architecture. This skill owns wording once the communication job is known.
- Capturing product screenshots or mockups as copy evidence: [product-capture.md](references/product-capture.md).
- Product strategy owns positioning and audience selection. Copy may expose an ambiguity but must not silently decide it.
- Repository guidance owns UI terminology and domain names.
- Legal, compliance, security, and commercial owners approve consequential claims. Copy review is not approval.
- Use a general writing skill for long-form documentation, ADRs, reports, or correspondence whose primary job is not product communication.

## Build an evidence and vocabulary packet

Before drafting material copy, collect the smallest useful packet:

- audience language from authorized interviews, research notes, sales calls, support themes, onboarding material, or domain documentation;
- current product behavior from the shipped interface, product captures, acceptance criteria, or maintained documentation;
- approved claims and their evidence owners;
- objections, questions, and terms people actually use;
- the repository's voice, glossary, legal constraints, and locale-specific guidance.

Separate audience vocabulary from publishable evidence. A phrase heard in a call may improve wording; it is not automatically a testimonial, market claim, or representative finding. Record gaps instead of laundering assumptions through fluent prose. Read [evidence-and-locale.md](references/evidence-and-locale.md) for a compact intake and locale procedure.

## Drafting standard

- Lead with the information or action the reader needs, at the reader's level of technical knowledge.
- Prefer concrete behavior, responsibility, and consequence over hype or abstract transformation language.
- Keep headings informative. Editorial or playful language is valid when the literal meaning remains available in context.
- Use technical detail when it helps the reader decide, operate, integrate, migrate, or assess risk. Connect implementation facts to the consequence the audience evaluates; do not use stack names as borrowed credibility.
- Name uncertainty honestly. Avoid absolute language unless the evidence and authority support it.
- Preserve the project's vocabulary. Use one name for the same object and one phrase for the same action unless the interface requires a deliberate distinction.
- Apply a literal-comprehension pass. A target reader should be able to explain what a heading or CTA means, what happens next, and why it belongs here without knowing the team's internal metaphor or strategy language.

Do not flatten every brand into one terse conversational voice. Derive formality, technical depth, energy, humor, sentence rhythm, and directness from the audience and repository. Editorial, playful, technical, premium, and operational voices can all pass when they are coherent, useful, and evidence-bound.

## Diagnose generic AI-copy patterns

Review these as symptoms, not forbidden sentence shapes:

- vague transformation claims with no changed behavior;
- abstract CTAs that conceal destination or commitment;
- fake conversational intimacy unsupported by the brand;
- automatic three-part rhetorical lists;
- repeated contrast formulas such as “not X, but Y”;
- empty section labels that announce no information;
- over-explaining a simple action;
- slogan fragments that fail literal reading;
- technical implementation language presented as customer value without its consequence.

Keep an apparent pattern when it accurately expresses the brand, content relationship, or audience's domain language. Change it when the same structure could be pasted into an unrelated product without loss.

## Surface adaptation

### Marketing and product pages

- Express the offer, fit, evidence, and next action without repeating the hero promise as filler.
- Bind material claims to authorized proof. Keep the claim no stronger than its evidence.
- Maintain one primary action concept across navigation, hero, sections, and final CTA. Labels may differ when they truthfully clarify the expected input, destination, or immediate effect; they must not imply different offers.
- Welcome both an existing problem and a new idea only when the company truly accepts both; state the invitation plainly rather than hiding it inside an abstract diagnosis.

### Interface copy

- Name the action and its consequence. Put recovery guidance where the user can act on it.
- Distinguish empty, loading, denied, validation, conflict, destructive, and system-failure states when their next steps differ.
- Do not blame the user, expose internal exceptions, or use reassuring language that hides an unresolved failure.

### Technical and release-facing product messages

- Verify version, compatibility, security, reliability, availability, and migration claims against their current owner.
- Describe changed behavior, user or operator impact, required action, and known limitation when those facts are relevant.

## Whole-surface review

1. Read navigation, headings, CTA labels, form labels, state messages, and adjacent sections together.
2. Flag repeated words and claims by function: useful terminology, intentional motif, or redundant echo. Do not replace words mechanically with synonyms.
3. Check that headings alone preserve the intended hierarchy and that action labels match the destination or effect.
4. Confirm that tone does not increase claim strength beyond the evidence.
5. Report unresolved facts and approval dependencies separately from copy edits.

## English and Mexican Spanish

- Treat English and `es-MX` as authored locale variants, not a source string and a literal mirror.
- Preserve meaning, confidence, claim strength, and action consequence while allowing natural syntax and rhythm in each language.
- Use a project glossary and approved audience corpus for product terms, pronouns, register, and domain vocabulary. Do not invent Mexican slang or familiarity to sound local.
- Localize dates, numbers, currency, units, form examples, and legal/commercial wording through the implementation's locale owner rather than hardcoding them in copy.
- Recheck length, hierarchy, terminology, and controls in the rendered interface. Pseudolocalization cannot replace review of the actual `es-MX` surface.
- For public, regulated, or high-consequence copy, require an authorized in-market or qualified language reviewer; the skill can prepare the review packet but cannot manufacture that approval.

## Output

Return the revised copy or copy system, the audience vocabulary and evidence used, material assumptions, blocked claims, voice decisions, and any cross-surface or multilingual inconsistencies that remain.
