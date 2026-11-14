# Reviewing a domain model

Reference for [`domain-modeling`](../SKILL.md). Establish the business
capability, its language, invariants, lifecycle and who may change it from
domain evidence: the glossary, product docs, ADRs, tests and the people who
own the rules. Name missing evidence instead of inferring a model from package
names.

Check, in order:

1. **Language.** Each term means one thing inside its context and matches the
   glossary. The same word may mean different things in two contexts when the
   translation between them is explicit. Flag synonyms, leaked terms from
   another context, and code names the glossary lists under `_Avoid_`.
2. **Contexts.** A bounded context is not a package, service, database or
   deployment unit by default; confirm what it owns and what it deliberately
   does not. Name each cross-context relationship: upstream and downstream,
   who translates, the contract, the consistency model and its active
   consumers. Tell an intentional shared kernel from a convenience import.
3. **Boundary test.** It exists, runs in CI, and covers domain purity and
   cross-context access. A baseline that only grows is a finding.
4. **Aggregates.** Each sits at the smallest set of data that must stay
   consistent atomically, with its root, transaction boundary,
   cross-aggregate references by identity, and emitted events. Flag oversized
   aggregates and distributed transactions without a proven invariant.
5. **Decider.** Business rules live in `decide`, not in the application
   service, a controller or a database trigger. Commands, events, rejections
   and states are closed and matched exhaustively. `evolve` decides nothing.
   An entity with getters and setters and its rules in a service is an
   anemic model: a finding when the context has business rules.
6. **Invariants.** Each has a property test, and the test fails when the rule
   is removed.
7. **Proportion.** A context with no business rule needs fewer concepts, not
   more ceremony. Flag DDD structure that carries no rule as readily as a
   missing one.

For each finding give the evidence (term, invariant, lifecycle or coupling),
its impact and a narrow correction. State what was reviewed, what was not,
and the residual risk.
