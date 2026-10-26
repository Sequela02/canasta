# Delegation Roles

Use the smallest useful team. The root agent owns integration, user communication, scope, and the final result. The current environment owns model selection and capability boundaries; this reference owns only task routing and lifecycle discipline.

## Team

| Role | Use |
| --- | --- |
| `advisor` | Difficult architecture, ambiguous cross-boundary choices, security-sensitive decisions, repeated failure, or expensive-to-reverse decisions. |
| `explorer` | A specific repository question, ownership map, dependency trace, or context-heavy read-only investigation. |
| `worker` | A bounded implementation outcome with explicit file or module ownership. |
| `verifier` | Independent completion, requirement, diff, test, and integration verification after implementation. |
| `reviewer` | Defect review of a proposed or completed change, applying only the relevant lenses (risk, reliability, resilience, readability, domain, Java and Spring); also challenges earlier findings. |
| `clerk` | Structured transcription, inventories, searches, output classification, link checks, and concise status work. |

## Routing rules

1. Keep simple, tightly coupled, or single-step work in the root session.
2. Delegate only a concrete bounded outcome or question. Do not use a child as an ambient second opinion.
3. Use `explorer` before implementation only when a specific unresolved repository question would materially improve the plan or preserve root context.
4. Give every `worker` explicit ownership and acceptance evidence. State that other agents may be editing concurrently and that unrelated changes must be preserved.
5. Parallelize only independent tasks whose mutable ownership does not overlap. Respect the active harness concurrency and depth limits; configuration owns their values.
6. Use `advisor` for the hard decision itself; use `reviewer` for skeptical review and `verifier` for independent verification.
7. Treat every reviewer result as a hypothesis until repository evidence or an external oracle supports it. Ask a fresh `reviewer` to challenge earlier findings only when multiple findings or a consequential review decision justify adversarial reconciliation.
8. Wait for every delegated child and inspect its terminal status before depending on its result. Reuse an idle child for a related follow-up when practical.
9. The root agent adopts, rejects, or reconciles child output and remains responsible for the final answer. Missing or unavailable roles do not silently fall back to another model; perform the work in the root session or report the limitation.

## SDD-compatible mapping

| Logical phase | Native role |
| --- | --- |
| init, onboard, repository exploration | `explorer` |
| proposal, architecture, design | `advisor` |
| spec, tasks, archive, mechanical status | `clerk` |
| apply, fix-agent | `worker` |
| verify, judge-a, judge-b | `verifier` plus `reviewer` with the relevant lens |
| review reconciliation | a fresh `reviewer` challenging the findings |

Status and synchronization decisions remain with the root because they integrate lifecycle state rather than perform a delegated phase.

## Completion

Before reporting completion, reconcile child outputs with the current workspace, run or confirm the smallest relevant deterministic checks, and state any unverified surface. Do not claim success from agent agreement alone.
