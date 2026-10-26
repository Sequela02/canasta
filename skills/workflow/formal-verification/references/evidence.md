# Evidence behind the formal-verification skill

Research cutoff 2026-10-03. The public sources below inform this skill.
Private experiments and conversations are not distributed as public evidence.
Proof establishes the stated contract under its assumptions, not user intent.

## Published work

- LemmaScript: "The prover checks the LLM's proposals — the LLM is not
  trusted, only the prover"; "The answer is a verdict, not a survey: correct,
  or not correct yet"; the person's job "shifts to reviewing the contract".
  [Design](https://docs.lemmascript.org/design/),
  [how the loop works](https://docs.lemmascript.org/how-the-loop-works/),
  [agent guidance](https://docs.lemmascript.org/agents/).
- Midspiral's lemmafit verifies on every save and continues until the proof
  goes through, with no fixed round count; its guarantees report maps
  requirements to proofs.
  [lemmafit](https://midspiral.com/blog/introducing-lemmafit-a-verifier-in-the-ai-loop/)
- ClaimCheck restates a proved contract without the request and compares;
  96.3% agreement over 108 comparisons, "a probabilistic sanity check that
  requires human review and approval".
  [ClaimCheck](https://midspiral.com/blog/claimcheck-narrowing-the-gap-between-proof-and-intent/)
- The intent envelope: soundness (reject invalid actions) is not completeness
  (accept every valid one); "a kernel that rejects everything would pass all
  safety tests". Completeness needs its own proof obligation.
  [Midspiral](https://midspiral.com/blog/intent-envelope-proofs-for-completeness-not-just-soundness/)
- Lahiri, Intent Formalization (2026): "there is no oracle for specification
  correctness other than the user"; models struggle with quantifiers,
  recursive predicates and ghost variables.
  [arXiv:2603.17150](https://arxiv.org/abs/2603.17150); specification
  completeness by mutation, [FMCAD 2024](https://arxiv.org/abs/2406.09757);
  [nl2postcond](https://nl2postcond.github.io/).
- Clover: consistency among description, annotations and code accepted up to
  87% of correct programs and rejected every adversarial incorrect one.
  [arXiv:2310.17807](https://arxiv.org/abs/2310.17807)
- Vericoding benchmark, 12,504 specifications: LLM-generated verified code
  succeeded 82.2% in Dafny, 44.2% in Verus, 26.8% in Lean.
  [arXiv:2509.22908](https://arxiv.org/abs/2509.22908)
- EXVERUS repairs proofs from validated counterexamples, more accurately and
  with fewer tokens than verifier messages alone; Dafny's default output names
  the obligation but not the inputs.
  [arXiv:2603.25810](https://arxiv.org/abs/2603.25810)
- Martin Kleppmann: AI-written proofs make formal verification cheap enough to
  go mainstream, because "automated proof checkers won't be fooled" by
  plausible nonsense. [Blog](https://martinkl.substack.com/p/ai-will-make-formal-verification)
- AWS Cedar: an executable model with proofs plus differential random testing
  against production; moved from Dafny to Lean when proofs of
  meta-theoretic properties became brittle under Dafny and Z3 updates.
  [Amazon Science](https://www.amazon.science/blog/how-we-built-cedar-with-automated-reasoning-and-differential-testing),
  [arXiv:2407.01688](https://arxiv.org/abs/2407.01688)
- AWS Cryptographic Material Providers Library, Dafny compiled to Java:
  [repository](https://github.com/aws/aws-cryptographic-material-providers-library).
- OpenJML releases: [GitHub](https://github.com/OpenJML/OpenJML/releases).

## Open questions

- Whether counterexamples in feedback reduce proof attempts for a given task.
- When proof coverage can replace a correctness-review lens, and what remains.
- When agents should add contracts where none exist.

These are questions to measure, not established benefits.
