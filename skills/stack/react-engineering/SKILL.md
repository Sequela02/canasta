---
name: react-engineering
description: "Write React components: props and composition, state and effects, data fetching, re-renders, bundle size and measured performance; choose a web runtime or surface. Use when editing .tsx or .jsx components. Not for visual design or styling."
paths: ["**/*.tsx", "**/*.jsx"]
tags:
  - react
  - frontend
  - performance
---

# React engineering

Follow the repository's installed React and its conventions. For current APIs,
read react.dev (`react.dev/llms.txt` lists its pages for agents).

## Procedure

1. Find who owns the component and how neighbors solve the same problem. Change
   one concern at a time.
2. Put state where it is used. Compute values during render from props and state;
   do not copy them into state or sync them with an effect.
3. Use an effect only to synchronize with something outside React (a socket, a
   timer, the DOM). User actions belong in event handlers.
4. Shape a component's API for its callers: a few clear props, `children` or
   compound components instead of a growing set of boolean props, and one
   context per concern.
5. Fetch data in parallel where the requests are independent, and avoid chains
   that wait on each other. Send the client only the data it renders.
6. Performance claims need a measurement: name the interaction, take a profiler
   or bundle measurement as the baseline, change one thing, measure again. A
   matched rule or scanner warning is a lead; trace it in the path users hit
   before you report it.
7. Run the closest check you have (typecheck, lint, the component's tests, a
   production build or a profiled interaction) and say which ran.

For a review, list findings by severity with `file:line` and the evidence, mark
anything you did not confirm as unverified, and say what you did not run. Review
the diff you were given, not the whole codebase.

## Example

A list filters items when a search box changes.

Bad:

```tsx
const [visible, setVisible] = useState(items);
useEffect(() => setVisible(items.filter(i => i.name.includes(q))), [items, q]);
```

This renders twice per keystroke and can show stale results in between.

Good:

```tsx
const visible = items.filter(i => i.name.includes(q));
```

Add `useMemo` only after a profile shows the filter is slow, and not at all when
the React Compiler already covers this component.

## React Compiler

When the compiler is on and covers the code, write plain components and hooks
and skip routine `useMemo`, `useCallback` and `React.memo`. Keep existing manual
memoization until a test and a profile show removing it is safe: it can change
effect behavior. Check that the compiler ran (build output or diagnostics) and
fix Rules of React violations it reports.

## References

- Choosing a runtime, creating a surface, the marketing and application split,
  and compiler setup: [references/stack-and-surface.md](references/stack-and-surface.md).
- Broad performance rules (waterfalls, bundle size, re-renders), written for
  React and Next.js by Vercel: `vercel-labs/agent-skills`, `react-best-practices`.
  Read only the rules for the topic you are working on.

Related: `typescript-standards` for types, `tailwind-v4` for styling.
