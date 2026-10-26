---
name: system-design
description: "Design a system or a cross-component change before building it: requirements with numbers, components and data ownership, consistency, failure, capacity, and deployment, recorded as a design doc and an ADR. Use only when the user asks for a system design or names this skill, never on your own initiative."
---

# System Design

For decisions above one codebase's modules: which processes and data stores
exist, how they talk, where they run, how they fail and recover. Hand the rest
to the owning skill: domain rules and modules inside a codebase to
`architecture-review`, ambiguous terms to
`concept-modeling`, the build sequence to `implementation-planning`.

Write in the repository's documentation language.

## 1. Frame the decision

- State the one question being decided and what is out of scope.
- Read the product's own instructions, direction or architecture docs,
  existing decisions, and the code that already exists. Do not redesign what
  is already decided; build on it or name the decision you would revisit.

## 2. Requirements, with numbers

- Functional: the journeys the design must serve.
- Non-functional, each as a number or an explicit unknown: users and
  concurrency, request rate, data volume and growth, latency, acceptable data
  loss (RPO) and downtime (RTO), availability, privacy and security
  constraints, budget, and who operates it day to day.
- Never invent a number. Ask, or write it as an assumption the operator must
  confirm.

## 3. Constraints from where it runs

- Read the operator's deployment standards and cite the constraints relied on:
  resource budgets, hosting, state stores, observability, secrets and releases.
- For a client-operated deployment, take constraints from the product's docs or
  the operator rather than assuming the developer's infrastructure.
- If a required standard is missing, propose its owning location and wording in
  the design; do not edit unrelated policy as part of the design task.

## 4. Start from the simplest shape

Begin with one deployable unit (a modular monolith), PostgreSQL as the source
of truth, and the standards and technology already in use. Every added
service, queue, cache, data store, or vendor must name the requirement it
meets and the simpler option that fails that requirement.

## 5. Components and data

- For each component: its responsibility, the data it owns (one owner per piece
  of data), its interface, and its callers.
- For each flow: the consistency it needs (strong, or eventual and how stale),
  idempotency for retries, and ordering.
- Diagram the C4 context and container levels in Mermaid.

## 6. Failure, security, operations

- For each component and dependency: what happens when it is slow, down, or
  wrong; how it is detected; how it recovers.
- Backups with a tested restore (a backup never restored is not a backup),
  deployment and rollback, and the data migration path.
- Trust boundaries: authentication, authorization, secrets, network exposure.

## 7. Capacity

Estimate data size at one and three years, peak load, and resource use
against the host's budget. Show the arithmetic.

## 8. Options and decision

Compare at least two viable options against the requirements, choose one, and
name what the choice gives up.

## 9. Challenge it

Before deciding, obtain an independent architecture review using an available reviewer with the draft and ask it to
find the weakest assumption and the failure the design misses. Do this every
time this skill runs; skip it only when the operator says so. Record its
objections and how the design answers each one.

## 10. Record

- The design doc in the product repository, where its docs live.
- An ADR (context, decision, consequences, status) in the product's decision
  records, or `docs/decisions/` when it has none. When the decision affects
  more than one product or shared infrastructure, link it from the shared
  decision record too.
- Status stays Proposed until the operator accepts it.
- End with the unresolved questions the operator must answer.

## Before finishing

Check the design doc contains every item; add what is missing:

- [ ] Requirements with numbers or marked assumptions, including RPO and RTO
- [ ] Constraints, with the deployment standard or product doc each one comes from
- [ ] A Mermaid C4 context and container diagram
- [ ] Failure, recovery, and security for each component
- [ ] Capacity arithmetic
- [ ] At least two options compared, and what the choice gives up
- [ ] The advisor's objections and the answers
- [ ] An ADR with status Proposed, and the unresolved questions

Sources behind this procedure: [references/sources.md](references/sources.md).
