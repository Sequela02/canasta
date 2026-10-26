> Reference for `product-copy`, formerly the `marketing-page-architecture` skill.

# Marketing Page Architecture

**Evaluation status: canary.** Load this reference only when explicitly asked, until the comparative
promotion gate in `documentation-hygiene/references/ui-guidance-research-basis.md` passes.

Shape the page around the visitor's decisions, not a stock section list. Preserve product, brand, legal, and commercial truth in repository-owned sources; this reference owns the reusable reasoning procedure only.

## Authority and boundaries

1. Read the repository's product, brand, content, and evidence owners before proposing structure.
2. Classify the surface before selecting chapters. Read [surface-contracts.md](surface-contracts.md) when the surface or its job is unclear.
3. Do not invent pricing, delivery commitments, guarantees, testimonials, client identity, legal status, or regulated claims. Mark missing authority as an explicit content dependency.
4. Do not prescribe visual style, section geometry, framework, analytics, SEO implementation, or a universal conversion sequence. Route those concerns to their actual owners when the task includes them.

## Workflow

### Establish the page contract

Identify:

- primary audience and the situation that brought them to the page;
- the page's single primary job and next action;
- the category or offer the visitor must understand;
- authorized evidence and material unknowns;
- whether the request is a homepage, campaign landing, service page, product page, portfolio, or another public surface.

If repository evidence answers these questions, proceed without an interview. Ask only for a decision that would materially change the page argument or authorize a claim.

### Build the argument

Create a compact map with these fields:

| Field            | Meaning                                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| Visitor question | The decision or uncertainty the chapter resolves                                                  |
| Chapter job      | The new information introduced                                                                    |
| Relationship     | Claim and proof, sequence, comparison, collection, qualification, or another content relationship |
| Evidence         | The authorized proof required for the claim                                                       |
| Dependency       | What the visitor must already understand                                                          |
| Status           | Required, conditional, unsupported, or blocked                                                    |

Order chapters so each depends only on information already introduced. Separate reading order from implementation order. Introduce category and scope before a narrow example when leading with the example would incorrectly define the whole offer.

Require every chapter to add a new decision-relevant fact. Similar wording in a new layout is still repetition. Give examples, owned products, case studies, and public tools weight proportional to the role they play in the page contract. Evidence for one capability must not accidentally redefine the parent company or broader offer.

Specify relationships and evidence adjacency, not a signature layout. Repetition can be correct when visitors must compare equivalent offers, scan a collection, follow a real sequence, or use documentation-like reference material. Visual design owns how those relationships become geometry at each breakpoint.

Read [evidence-and-objections.md](evidence-and-objections.md) when the page includes proof, FAQs, commercial objections, qualification, or claims that need authorization.

### Remove unsupported structure

- Reject a common industry section when it has no distinct visitor question or evidence.
- Treat FAQ as one possible objection-handling format, not a quota or default.
- Answer an objection where it arises when that is clearer than a consolidated FAQ.
- Treat labels, eyebrows, badges, numbers, and dividers as information structures. Keep them only when they communicate real category, state, sequence, or metadata.
- Do not duplicate the hero promise in a later section without adding evidence or a new decision.
- Remove adjacent sections that describe the same capability at different abstraction levels unless the second supplies evidence, operating boundaries, or a distinct decision.

### Verify the handoff

Before visual design or implementation:

1. Read headings alone in DOM order. They should reconstruct the argument without decorative labels or body-copy dependence.
2. Confirm one primary action concept. Labels may vary when they truthfully clarify input, destination, or immediate effect, but must not change the offer or fragment the conversion path.
3. Bind factual claims to an owner and relevant evidence; place proof beside the claim or objection it qualifies unless a documented reading reason requires separation.
4. Run a whole-page lexical pass across navigation, hero, actions, headings, and adjacent sections. Flag echoes for deliberate review; do not replace words mechanically with synonyms.
5. For multilingual pages, preserve commercial meaning and claim strength rather than translating word-for-word.
6. Report blocked content separately from approved structure and do not fill incomplete inputs with generic sections.

## Output

Return the surface classification, page contract, question-to-chapter map, proposed reading order, evidence dependencies, content relationships, conditional or rejected chapters, and verification findings. Distinguish information-architecture confidence from predicted conversion impact.
