---
name: technical-writing
description: "Write, edit or rewrite prose so the reader understands it on the first read and nothing true is lost: edit a report for clarity, rewrite a README, make an explanation clearer, cut filler, write a PR description, commit message or message someone will sign. Uses Diátaxis structure and plain-English rules. Not for where docs belong (documentation-hygiene) or interface copy."
license: Complete terms in LICENSE.txt
metadata:
  source: "pstack technical-writing by Lauren Tan, cursor/plugins 2f87c85"
  changes: "Model invocation allowed; condensed to the upstream's terse rule form; added Keep what is true, Text someone signs and Scope; dropped the tab-indent repo rule and the dependency on unslop; action-first reference from canasta's former clear-writing"
---

# Technical writing

Write so a tired engineer understands it on the first read, and so nothing true
is lost on the way.

## Rules above the rest

- Cut every word that does no work. "In order to" is "to".
- Use the short word: "use", not "utilize".
- Write the real symbol, file, flag or command, not a description of it.
- Use the words a developer says out loud. If you name a pattern, say what it
  means the first time.
- When a rule makes a sentence worse, rewrite the sentence another way or leave
  it. A sentence that follows every rule and sounds machine-made has failed.

## Keep what is true

Editing must not change what the text claims.

1. Keep quantities, units, negation, conditions, uncertainty, attribution, code,
   identifiers and quotations exactly.
2. Use facts you were given or verified. Don't invent a detail to make a sentence
   land. If a fact looks wrong, flag it; don't fix it silently.
3. Compare the result with the source before you finish. If a claim became more
   certain or more general, or a condition disappeared, restore it.
4. Leave clear text alone.

## 1. Pick the mode (Diátaxis)

One document, one mode. Does it help the reader act or understand, and are they
learning or working?

| | Learning | Working |
| --- | --- | --- |
| **Act** | Tutorial: say what they will build; every step shows a visible result and what to expect | How-to: steps to one goal; assume competence; allow forks; title it by the task |
| **Understand** | Explanation: one topic and the why: decisions, history, trade-offs. Opinion allowed here only | Reference: describe, dry and complete; mirror the thing's structure; generate it from code when you can |

Don't mix modes. Split the document and link.

## 2. Write the sentences

- Say "you", in the present tense, with a named actor: "the compiler checks", not
  "is checked".
- Write instructions as commands, one per sentence, condition first: "To delete
  the file, run `rm`." Put the common case first.
- Split an instruction past about 20 words and any sentence past about 25.
- Vary the rhythm. Short sentences land a point; a longer one carries a fact with
  its condition. In explanation, take a position.
- Be specific: not "schema changes can cause issues" but "a column rename fails
  the build".
- Keep "the" and "a". Keep "that" where it shows structure.
- Keep "only" and "not" next to the word they change. Make each "it", "this" and
  "they" point at one noun; repeat the noun when unsure.
- Call each thing by one name throughout.
- Break up noun strings: "the script that checks the proto-import budget", not
  "the proto import budget check script".
- Use periods rather than semicolons or em dashes. Skip idioms, metaphors, "etc.",
  "and/or" and "(s)".
- Never write "simply", "easy" or "please" in a procedure.
- Headings state the point, in sentence case. Numbered lists for sequences,
  bullets for the rest. Links say where they go, never "click here".

## 3. Show it small

Put one example beside the claim: a before and after for behavior, a table for
options, a short tree or sequence for structure. Label invented examples as
examples.

## Text someone signs

Messages and posts go out under a person's name. Keep their voice and cut these:

- A caveat that qualifies and reassures in one breath ("small tests, but the jump
  is huge"). State the limit or drop it.
- A verdict about how something feels ("good dogfooding"). Say what happened.
- Equal-length paragraphs, one per topic.
- A closing emoji or pleasantry.

When the voice matters more than polish, give the person the facts and let them
write it.

## Scope

- PR descriptions and commit messages are writing too: a reviewer reads a PR body
  in under a minute, so link logs and tables. The procedure is in `writing-pr`.
  Issues are in `writing-issues`.
- A request that is still unclear goes to `problem-clarification` first.
- Docs for a library, SDK or CLI: read [developer-docs.md](references/developer-docs.md).
  For short replies or work that must show its state across turns, read
  [action-first.md](references/action-first.md).
- Make every count or tree you write true at the commit that lands it, and include
  the command that regenerates it.

## Worked example

Before:

> Configuration of the proto import ratchet budget script parameters is performed
> via budget.json. Note that it's important to remember that running with
> --write, which updates the committed budget to reflect the current count,
> should only be done when lowering it. If exceeded, CI fails.

After:

> `budget.mjs` reads the committed budget from `budget.json` and counts the files
> that import protos. If the count exceeds the budget, CI fails. Run
> `budget.mjs --write` only to lower the budget.
