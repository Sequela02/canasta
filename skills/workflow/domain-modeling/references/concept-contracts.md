# Concept contracts

Reference for [`domain-modeling`](../SKILL.md), for a name that crosses
surfaces: persisted, serialized, in a public API, in a prompt or generated
into another artifact. Such a name is a contract; changing it has consumers.

## Model before naming

1. Start from representative scenarios and observable behavior: what varies,
   what must stay invariant, which distinctions users or implementers need.
2. Define the concept's owner, audience, lifecycle and boundaries. Split
   dimensions that vary independently instead of hiding them in one
   overloaded label or a bag of optional fields.
3. Test the model against counterexamples and repository evidence. Keep
   confirmed facts, inferences, contradictions and unknowns apart.
4. Use one canonical term per concept within its context, and different
   terms for materially different concepts. Name the translation owner where
   two contexts, locales or audiences genuinely differ.

## Trace the contract

Inspect the active surfaces: owning types, configuration, schemas, tools,
APIs, runtime branches, persistence, events, UI, tests, fixtures,
documentation, prompts and generated projections. Record only the fields
that exist:

- definition, scenarios, canonical term and machine identifier;
- owner, lifecycle, audience and boundaries;
- independent dimensions and invariants;
- deliberate translations;
- active consumers, compatibility policy, migration path and version impact.

Remove an alias once it has no active consumer and no migration needs it.

## Put knowledge in its owner

- Types, schemas and configuration own allowed vocabulary and structure.
- Code and tests own behavior and invariants.
- `GLOSSARY.md` owns what business terms mean.
- An ADR owns a decision that is hard to reverse, surprising without context
  and the result of a real trade-off.
- Repository guidance points to the owner instead of copying it.

Prefer enforcement through closed types, schemas, mappings, contract tests or
config constraints.
