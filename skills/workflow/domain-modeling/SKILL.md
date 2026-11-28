---
name: domain-modeling
description: "Domain-driven design with a check behind every rule. Use when a business term is ambiguous, overloaded or missing from GLOSSARY.md; when drawing bounded contexts; when modeling business rules, invariants or an aggregate's lifecycle; when a command may be retried, two writers race, a side effect leaves the database or a client works offline; and when reviewing a domain model. Module and dependency shape belongs to architecture-review."
tags:
  - architecture
  - domain-driven-design
  - glossary
  - invariants
metadata:
  source: "domain-modeling by Matt Pocock, mattpocock/skills bbadaa6"
  changes: "Takes the glossary format and the challenge, sharpen, cross-check and write-down practice; adds bounded-context boundary tests, the decider, invariant property tests and integration patterns, each ending in a check a tool runs"
---

# Domain modeling

Rules held in prose drift. Rules held in a glossary, a closed type, a boundary
test or a property test stay true. Each step below ends in one of those.

For plain data maintenance with no business rule, do steps 1 and 2 only and say
so in the pull request.

## 1. Vocabulary

Read `GLOSSARY.md` (at the root, or the per-context file listed in
`GLOSSARY-MAP.md`). While designing:

- **Challenge** a term that conflicts with the glossary: "the glossary says
  cancellation means X; you seem to mean Y. Which holds?"
- **Sharpen** a vague term into one canonical term, and probe its edges with
  concrete scenarios.
- **Cross-check** the code. When a stated rule and the code disagree, quote the
  code and ask which is right.
- **Write** each settled term into the glossary at once:

  ```md
  **Reservation**: a seat held for one customer until checkout completes or
  the hold expires.
  _Avoid_: booking, hold
  ```

The glossary holds meanings only, never design or implementation notes. A
decision goes in an ADR when it is hard to reverse, surprising without context
and a real trade-off. A rename updates the glossary, code, tables, events,
status values and issue titles in one commit. A name that crosses a surface
(stored, serialized, public API, prompt) needs
[concept contracts](references/concept-contracts.md) first.

Done when every term the change adds or renames is in the glossary and the code
uses it.

## 2. Bounded contexts

- A context owns its capability, terms and data. Contexts meet only through
  each other's public API and translate at that edge.
- Domain code imports no framework, persistence, transport or serialization
  types.
- Enforce both with a CI boundary test
  ([boundary checks](references/boundary-checks.md)). An existing codebase
  records its current violations as a baseline so only new ones fail.

Done when the boundary test runs in CI and passes.

## 3. Decider

For a context whose state changes under business rules
([templates](references/decider.md)):

- Commands (`ReserveSeat`), past-tense events (`SeatReserved`) and rejections
  (`SeatAlreadyTaken`) are closed types, matched exhaustively.
- `decide(command, state)` is pure and returns events or a rejection.
  `evolve(state, event)` applies one event and never fails.
- The lifecycle is an explicit state type, so an invalid state cannot be built.
- An aggregate is the smallest data that must be consistent in one transaction.
  It refers to other aggregates by id. A rule across aggregates becomes its own
  aggregate or a policy reacting to events.
- The application service loads, calls `decide`, applies `evolve`, saves and
  publishes. It holds no rule.

Store state by default. Use event sourcing only when the history itself has
business value (a ledger, an audit trail), and record that in an ADR.

Done when every rule lives in a `decide` function and the compiler rejects an
unhandled command, event or state.

## 4. Invariants

For each invariant of a decider, write a property test: generate command
sequences, fold them through `decide` and `evolve`, assert the invariant on
every state (jqwik, fast-check, Hypothesis). Where the risk justifies a proof,
such as money, use `formal-verification`.

A new context starts as a skeleton: glossary entries, the closed types, the
`decide` and `evolve` signatures and these tests, failing. Implementation
follows in a later commit.

Done when each invariant has a test that fails when you delete the rule.

## 5. Integration

Add the pattern the risk calls for, with its check
([patterns](references/integration.md)):

| Risk | Pattern |
| --- | --- |
| A command that moves money or stock may be retried | idempotency key |
| Two writers race on one aggregate | optimistic concurrency |
| A side effect leaves the database | transactional outbox |
| A flow spans aggregates | process manager |
| A client works offline | local queue, server authority |

Done when each risk the change introduces has its pattern and a passing check,
or the pull request names the risk accepted.

## Example

A request says "cancel the order". The glossary has **Order** (a customer's
purchase) and **Shipment** (goods leaving the warehouse).

- Probe: "Can a shipped order be cancelled? Can one line be?"
- Answer: only unshipped orders, whole order.
- Write: `**Cancellation**: ending an unshipped **Order** before it ships.`
  `_Avoid_: void, abort`.
- Decider: `CancelOrder` on a `Shipped` state returns `OrderAlreadyShipped`.
- Invariant test: for any command sequence, a shipped order never reaches
  `Cancelled`.

## Review a model

Use [the review checklist](references/review.md). Findings first, most severe
first, each tied to the language, invariant, lifecycle or coupling evidence.
Say plainly when the model is sound.
