---
name: domain-modeling
description: Domain-driven design with checks behind every rule. Use when a
  business term is ambiguous, overloaded or missing from GLOSSARY.md; when
  drawing or changing bounded contexts; when modeling business rules,
  invariants or an aggregate's lifecycle; and when reviewing a domain model.
  Module and dependency shape belongs to architecture-review.
tags:
  - architecture
  - domain-driven-design
  - glossary
  - invariants
---

# Domain Modeling

Domain rules held in prose drift; rules held in types, tests and build checks
hold. Each step below ends in an artifact a tool checks: the glossary, a
boundary test, closed types, a property test.

Skip the tactical steps (3–5) for plain data maintenance with no business
rule, and say so in the pull request. Vocabulary and boundaries apply to every
context.

## 1. Vocabulary

Read `GLOSSARY.md` first: at the repository root, or the per-context file
named in a root `GLOSSARY-MAP.md`. Then, while designing:

- **Challenge** a term that conflicts with the glossary, and ask which
  meaning holds.
- **Sharpen** a vague or overloaded term into a canonical one, using concrete
  scenarios that probe its edges.
- **Cross-check** the code: when a stated rule and the code disagree, quote
  the code and ask which is right.
- **Write** each settled term into the glossary at once, in this shape:

  ```md
  **Reservation**: a seat held for one customer until checkout completes or
  the hold expires.
  _Avoid_: booking, hold
  ```

The glossary holds what terms mean and nothing else; decisions go to an ADR,
and only when the decision is hard to reverse, surprising without context and
the result of a real trade-off. A rename updates the glossary, the code,
tables, events, status values and issue titles in the same commit.

When a name crosses surfaces (persisted, serialized, a public API, a prompt),
trace its contract with [concept contracts](references/concept-contracts.md)
before changing it.

Done when every term the change introduces or renames is in the glossary and
the code uses it.

## 2. Bounded contexts

- Each context is a module that owns its capability, its terms and its data.
  Contexts meet only through each other's public API; translate at that
  boundary. Each context owns its tables and entity classes.
- Domain code imports only the language and its standard library: no
  framework, persistence, transport or serialization types.
- Enforce both with a boundary test in CI, using
  [boundary checks](references/boundary-checks.md). An existing codebase
  records its current violations as a baseline, so only new ones fail.

Done when the boundary test runs in CI and passes against the baseline.

## 3. Decider

For a context whose state changes under business rules, model it as a
decider ([templates](references/decider.md)):

- Commands (`ReserveSeat`), events in the past tense (`SeatReserved`) and
  rejections (`SeatAlreadyTaken`) are closed types, matched exhaustively.
- `decide(command, state)` is pure and returns events or a rejection.
- `evolve(state, event)` applies one event, covers every state and never
  fails.
- The lifecycle is an explicit state type, so an invalid state is
  unrepresentable.
- Size the aggregate to the smallest data that must stay consistent in one
  transaction. Reference other aggregates by identity. A rule spanning
  aggregates gets its own aggregate, or a policy that reacts to events.
- The application service loads state, calls `decide`, applies `evolve`,
  saves and publishes. It holds no business rule.

Store state in the database by default. Choose event sourcing for a context
whose history itself has business value, such as a ledger or an audit trail,
and record that choice in an ADR.

Done when every business rule of the change lives in a `decide` function and
the compiler rejects an unhandled command, event or state.

## 4. Invariants

Write a property-based test for each invariant of a decider: generate command
sequences, fold them through `decide` and `evolve`, and assert the invariant
on every resulting state. Use jqwik in Java, fast-check in TypeScript and
Hypothesis in Python. Where the risk justifies a proof, such as money, hand
`decide` to formal-verification.

Done when each invariant named in the glossary or the plan has a property test
that fails when the rule is removed.

## 5. Skeleton first

A new context starts as a skeleton: glossary entries; command, event,
rejection and state types; `decide` and `evolve` signatures; and the invariant
tests, failing. Implementation follows in a later commit.

## Reviewing a model

Use [review](references/review.md). Lead with findings ordered by severity,
each tied to the language, invariant, lifecycle or coupling evidence behind
it; say plainly when the model is sound.
