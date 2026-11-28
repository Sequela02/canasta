---
name: system-design
description: "Design a system or a cross-component change before building it: requirements with numbers, components and data ownership, consistency, failure, capacity and deployment, recorded as a design doc and an ADR. Use only when the user asks for a system design or names this skill, never on your own initiative."
metadata:
  source: "documentation-and-adrs by Addy Osmani, addyosmani/agent-skills e997ac5"
  changes: "Takes the rule to match an existing ADR convention and to supersede, never delete, an old ADR; adds requirements with numbers, capacity arithmetic, an independent challenge and a completeness checklist"
---

# System design

For decisions above one codebase's modules: which processes and data stores
exist, how they talk, where they run, how they fail and recover. Hand the rest
to the owning skill: domain rules and bounded contexts to `domain-modeling`,
modules inside a codebase to `architecture-review`, the build sequence to
`implementation-planning`. Write in the repository's documentation language.

## Procedure

1. **Frame the decision.** State the one question and what is out of scope.
   Read the product's instructions, architecture docs, existing decisions and
   code. Build on what is decided, or name the decision you would reopen.
2. **Requirements, with numbers.** Functional: the journeys to serve.
   Non-functional, each a number or an explicit unknown: users and concurrency,
   request rate, data volume and growth, latency, data loss allowed (RPO) and
   downtime allowed (RTO), availability, privacy and security constraints,
   budget, and who operates it. Ask for a number you lack, or write it as an
   assumption the operator must confirm.
3. **Constraints from where it runs.** Read the operator's deployment standards
   and cite each constraint you rely on: resources, hosting, state stores,
   observability, secrets, releases. For a client-operated deployment, take
   constraints from the product's docs or the client. When a standard is
   missing, propose its owner and wording in the design and leave other
   policy alone.
4. **Start from the simplest shape**: one deployable unit (a modular monolith),
   the data store the product already uses as the source of truth, known
   technology. Each added service, queue, cache, store or vendor names the
   requirement it meets and the simpler option that fails it.
5. **Components and data.** Per component: its job, the data it owns (one owner
   per datum), its interface, its callers. Per flow: the consistency needed
   (strong, or eventual and how stale), idempotency for retries, ordering.
   Draw the C4 context and container levels in Mermaid.
6. **Failure, security, operations.** Per component and dependency: what
   happens when it is slow, down or wrong, how you detect it, how it recovers.
   Backups with a tested restore, deploy and rollback, the data migration path.
   Trust boundaries: authentication, authorization, secrets, network exposure.
7. **Capacity.** Data size at one and three years, peak load, and resource use
   against the host's budget, with the arithmetic shown.
8. **Options and decision.** Compare at least two viable options against the
   requirements, choose one, and name what it gives up.
9. **Challenge it.** Give the draft to an independent reviewer (an advisor or
   reviewer agent) and ask for the weakest assumption and the failure the
   design misses. Do this every run unless the operator says to skip it. Record
   each objection and the design's answer.
10. **Record.** The design doc goes in the product repository where its docs
    live. An ADR (context, decision, alternatives, consequences, status) goes
    in the existing decision records, matching their location, format and
    numbering, or `docs/decisions/` when there are none. Link it from the shared
    record when more than one product is affected. Status stays Proposed until
    the operator accepts. A changed decision gets a new ADR that supersedes the
    old one; old ADRs are not deleted. End with the questions the operator must
    answer.

## Example: requirements with numbers

```text
Peak: 200 req/s (assumption: 10x the 20 req/s average; operator to confirm)
Data: 5 GB now, +2 GB/month -> 29 GB at 1 year, 77 GB at 3 years
RPO 5 min (WAL archiving); RTO 1 h (restore from backup, tested monthly)
Host budget: 4 GB RAM, 80 GB disk -> disk fills in month 37; plan a resize
```

A line without a number reads "Latency: unknown, operator to state".

## Before finishing

The design doc has each of these, or says what is missing:

- [ ] Requirements with numbers or marked assumptions, including RPO and RTO
- [ ] Constraints, each with the standard or doc it comes from
- [ ] A Mermaid C4 context and container diagram
- [ ] Failure, recovery and security per component
- [ ] Capacity arithmetic
- [ ] At least two options compared, and what the choice gives up
- [ ] The reviewer's objections and the answers
- [ ] An ADR with status Proposed, and the unresolved questions

[Sources](references/sources.md) lists the evidence behind this procedure.
