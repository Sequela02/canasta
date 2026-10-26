> Reference for `architecture-review`, formerly the `ddd-boundary-review` skill.

# DDD Boundaries

Use this lens when domain language, bounded contexts, or ownership boundaries
matter, while modeling or while reviewing.

Here ownership means business capability, language, invariant, lifecycle, and
change authority. Module placement, dependency direction, composition, and
technical contract ownership stay with the main `architecture-review` procedure.

## Modeling a domain

Use before modeling a new business capability, or before changing one whose
rules are not trivial.

1. Decide whether DDD is warranted. Use aggregates, value objects, and domain
   events only where real invariants and business rules exist; keep simple data
   maintenance as a plain service.
2. Take the language from domain sources: the operator, product docs, and
   existing code, and name types and methods exactly as the domain does. When
   a term is ambiguous, overloaded, or means different things across surfaces,
   settle it with the concept-modeling skill before building on it.
3. Draw each bounded context: the capability it owns, the terms it defines, and
   what it deliberately does not own.
4. Size each aggregate to the smallest set of data that must stay consistent in
   one transaction. Reference other aggregates by identity, and use domain
   events across aggregates only when a consumer exists.
5. Put each rule in the aggregate or entity that owns the data, not in an
   application service; services orchestrate.
6. Across contexts, translate at the boundary through a published contract or an
   anti-corruption layer. Never share tables or entity classes between contexts.
7. State in the plan the contexts, the aggregates with their invariants, the
   events and their consumers, and the open domain questions.

## Reviewing a model

Workflow:
1. Establish the business capability, stakeholders, ubiquitous language,
   invariants, lifecycle, authority, and change ownership from domain evidence.
   State what evidence is missing instead of inferring a model from package
   names alone.
2. Distinguish bounded contexts from packages, services, databases, and
   deployment units. Within each context, verify that terms have consistent
   meanings; allow the same word to mean different things across contexts when
   translation is explicit.
3. Locate an aggregate at the smallest set that must preserve invariants
   atomically. Identify its root, transaction and concurrency boundary,
   cross-aggregate references, consistency timing, and emitted domain events.
   Reject oversized aggregates and distributed transactions without a proven
   invariant.
4. Across contexts, name the upstream and downstream relationship, translation
   owner, integration contract, consistency model, and active consumers.
   Distinguish an intentional shared kernel or published language from an
   accidental convenience import.
5. Check for leaked language, shared persistence ownership, anemic domain
   models, unrelated service responsibilities, temporal coupling, and
   compatibility machinery without an active consumer.
6. Do not introduce DDD patterns where domain complexity does not justify them.
   A simple data-maintenance capability may need fewer concepts, not more
   ceremony.

Report findings first and ordered by severity. For each finding give the
triggering language, invariant, lifecycle, ownership, or coupling evidence;
impact; and narrow correction direction. State the reviewed and materially
unreviewed surface, verification performed, residual uncertainty and risk, and
say clearly when evidence supports no finding. Do not use DDD terminology as a
substitute for business evidence.
