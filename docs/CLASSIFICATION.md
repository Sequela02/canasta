# Skill classification — owner review copy

Working file, 2026-10-26. Review, then delete before publication. This table
accounts for all **40 installed skill folders**: **21 workflow, 9 stack,
10 excluded**. `setup-canasta` is new and is not part of that inventory.
One private identifier is deliberately redacted so this file is safe to review
with the public pack; its row uniquely identifies the operations-only folder.

## Basis and limits

The installed origin lock and every folder's files were inspected for licence,
copyright and attribution text. The lock names only three upstream installs;
it is not a complete authorship ledger. “Local procedure” below means no
external authorship notice was found, not independent proof of authorship.
The owner must confirm those rights before release, along with the MIT licence.

Agent-specific metadata and executable helper scripts are not distributed.
Private experiment reports, brand overlays and private UI pilot notes are
omitted, rather than presented as generic public evidence. Tool-role routing
is rewritten as capability-based delegation. References to excluded skills are
replaced by the relevant subject or upstream guidance, not bundled copies.

| Installed skill | Group | Basis / disposition |
| --- | --- | --- |
| architecture-review | workflow | Local review procedure; retains domain-boundary reference. |
| astro | stack | Local implementation guidance; official documentation references. |
| benchmark-readiness-review | workflow | Local evidence and claim-readiness procedure. |
| bun-standards | stack | Local runtime/toolchain opinions and references; helper script omitted. |
| clear-writing | workflow | Local prose procedure and action-first reference. |
| code-review-findings | workflow | Local findings-first review procedure. |
| codebase-scouting | workflow | Local repository investigation procedure. |
| concept-modeling | workflow | Local semantic ownership/modeling procedure. |
| config-projection-review | workflow | Generic canonical-config and projection review; no product internals required. |
| documentation-hygiene | workflow | Local document lifecycle procedure; private UI research appendix omitted. |
| fixing-accessibility | excluded | External authorship: matches ibelick/ui-skills entry point and checklist structure. No local licence notice found. Leave with upstream. |
| formal-verification | workflow | Local contract/proof discipline; supported-tool references retained. Private measurements and meeting notes omitted; no claim they are public evidence. |
| frontend-design | excluded | External authorship declared by owner; local Apache 2.0 licence file and licence frontmatter found. |
| impeccable | excluded | External design toolkit; bundled scripts include copyright and MIT SPDX notices. Local edits do not make the toolkit owner-authored. |
| implementation-planning | workflow | Local evidence-backed sequencing procedure. |
| managed-agent-risk-review | excluded | Review contract for managed-child admission, adapters and lifecycle internals; too specialized for this working-method pack. |
| mcp-builder | excluded | Lock identifies anthropics/skills; local Apache 2.0 licence file found. |
| mobile-native | excluded | Lock identifies emilkowalski/skills; no local licence/copyright notice found. External origin still excludes it. |
| motion | excluded | Mixed authorship: craft-values reference explicitly identifies emilkowalski/skills revision 0e0d3cb3; craft review also attributes an adapted method. Leave out rather than redistribute uncertain material. |
| orchestration-workflow | workflow | Local delegation procedure; fixed tool roles made generic. |
| postgres | stack | Local database procedure with official/practice references. |
| problem-clarification | workflow | Local intent, requirements and uncertainty procedure. |
| product-copy | workflow | Local evidence-led copy procedure; private brand voice and its evaluations omitted. Generic evaluations retained. |
| react-engineering | stack | Local wrapper and stack/surface opinions retained. Vercel-origin composition/performance reference trees are **not copied**; replaced with public upstream links. |
| refactor | workflow | Local behavior-preservation procedure. |
| repository-text-hygiene | workflow | Local encoding, line-ending and Git drift procedure. |
| research | workflow | Local bounded investigation and source appraisal procedure. |
| rust-standards | stack | Local Rust opinions made cross-project. |
| security-scope-review | workflow | Local authority and untrusted-data review; backend references made generic. |
| [private operations skill] | excluded | Private infrastructure, credentials/access paths and production procedures. Not copied. |
| shadcn | excluded | Lock identifies shadcn/ui. No local licence/copyright notice found; external origin is sufficient to exclude. |
| spring-boot | stack | Local Java/backend opinions; private platform names replaced by adopted platform components. |
| stripe-best-practices | excluded | External authorship declared by owner; Stripe-specific upstream-style entry point and reference collection. No local licence/copyright notice found. |
| system-design | workflow | Local design procedure; deployment constraints and decision destinations generalized. |
| tailwind-v4 | stack | Local CSS/token opinions with technical references. |
| tdd | workflow | Local test-first discipline; diagnosing-bugs reference explicitly adapts Matt Pocock revision 5beb35b under MIT. Full upstream notice retained in that reference and a folder-level notice added. Other practitioner ideas are attributed, not copied. |
| typescript-standards | stack | Local language/tooling opinions and official/style-guide citations. Version-sensitive claims require checking against the consuming repository. |
| vitest-testing | stack | Local test-runner diagnosis and evidence procedure. |
| writing-issues | workflow | Local observable acceptance and issue-drafting procedure. |
| writing-pr | workflow | Local aggregate-change drafting procedure; explicit project-policy merge restriction and final risk note. |

## Authorship follow-up

- Confirm local-procedure authorship, especially composite technical references:
  absence of a notice is not a licence grant.
- React's upstream metadata identifies Vercel Engineering; its bundled rule trees
  are intentionally absent from this distribution.
- Accessibility's public matching source:
  <https://github.com/ibelick/ui-skills/blob/main/skills/fixing-accessibility/SKILL.md>.
- The motion exclusion is conservative: owner-authored portions could be
  extracted later after provenance review; no extraction is claimed here.
- No text from the unlicensed pstack snapshot was copied. Practitioner ideas
  are discussed in the method, with attribution and evidence limits.
- The root MIT licence is prepared for owner confirmation, not publication
  authorization. No remote repository, push, release or public install was made.
