---
name: react-engineering
description: Build or review React component contracts, composition, rendering, data flow, bundle, and performance; choose a web runtime or surface. Use for React code, not for visual direction or styling.
tags:
  - react
  - frontend
  - performance
---

# React Engineering

One entry point for React implementation and review. Repository evidence owns
the installed stack, versions and conventions; these references are defaults
and must not override a documented repository choice.

Load only the reference the change needs:

| Change | Reference |
| --- | --- |
| Choosing a runtime, adding a dependency, creating a surface, React Compiler, or the marketing/application boundary | [stack-and-surface.md](references/stack-and-surface.md) |
| Rendering, re-renders, data fetching, waterfalls, bundle size, server/client work | [React performance guidance](https://react.dev/learn/react-compiler) and the upstream [Vercel rules](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices); consult only the relevant topic |
| Reusable component APIs, boolean-prop growth, compound components, context shape | [React composition guidance](https://react.dev/learn/passing-data-deeply-with-context) and upstream [composition patterns](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) |

Procedure:

1. Find the component's owner and existing patterns before adding new ones.
   Change one concern at a time.
2. For a performance claim, measure first: name the interaction, the
   profiler or bundle evidence, and the baseline. A rule match is a lead, not a
   finding; confirm it in the code path users hit.
3. A static scanner (such as React Doctor, when a repository adopts it as a
   command) produces candidates, not findings. Reproduce or trace each before
   reporting it, and copy no fix the code path does not need.
4. Verify with the closest executable check: typecheck, lint, the component's
   tests, a production build, or a profiled interaction. Say which ran.

For a review, lead with findings by severity with `file:line` evidence, and
state what was not verified. Do not run a whole-codebase audit unless asked.

Related: `typescript-standards` for types and `tailwind-v4` for styling.
Use the project's accessibility, visual-design and animation guidance as needed.
Upstream reference collections are linked, not bundled in this pack.
