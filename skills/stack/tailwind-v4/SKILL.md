---
name: tailwind-v4
description: "Tailwind CSS v4: theme tokens in CSS, semantic color utilities, variants, responsive layout, and migrating from v3. Use when a project's CSS imports tailwindcss, when changing class lists or theme tokens, or when a v3 class stops working."
paths: ["**/*.css"]
---

# Tailwind v4

Tailwind v4 is configured in CSS. Read the installed version in `package.json`
and the docs at tailwindcss.com/docs (theme, upgrade guide) when unsure.
Component libraries (shadcn) and color science (OKLCH) have their own guidance;
for OKLCH, MDN's `oklch()` page is enough.

## Procedure

1. Find where the theme lives (the CSS file with `@import "tailwindcss"`) and
   which semantic tokens exist before adding any color or size.
2. Add a token only when a value repeats or carries meaning. Define the value on
   `:root` and expose it to utilities with `@theme inline`.
3. In components, use semantic utilities (`bg-background`, `text-foreground`,
   `border-border`, `text-muted-foreground`), not palette classes or hex values.
4. Use the standard scale. Write an arbitrary value (`w-[37rem]`) only for a real
   one-off measurement; use `bg-(--var)` to reach a CSS variable.
5. Build the layout intrinsically (`flex`, `grid`, `gap-*`, `min-w-0`, container
   queries with `@container`), and add breakpoints where the content needs them.
6. Put repeated visual states in the repository's variant tool (CVA or similar),
   with the consumer's `className` last in `cn()`.
7. Run the project's build, then check in a browser: no unknown classes in the
   output, dark and theme variants resolve, long and translated text wraps, and
   contrast holds after a token change.

## Example

Tokens that follow a runtime theme:

```css
@import "tailwindcss";

@theme inline {
  --color-primary: var(--primary);
  --color-background: var(--background);
}

:root {
  --primary: oklch(0.45 0.15 260);
  --background: oklch(1 0 0);
}
.dark {
  --primary: oklch(0.75 0.12 260);
  --background: oklch(0.2 0 0);
}
```

`inline` puts the variable's value into the utility, so `bg-primary` follows
`--primary` wherever it is overridden, including a `.dark` class on a nested
element. Without it the utility reads a variable resolved at `:root` and can show
the wrong theme. Use plain `@theme` for values that never change at runtime.

## Moving from v3

- Delete `tailwind.config.js` once its contents are in CSS; load a legacy config
  with `@config` only while migrating. Replace `@tailwind base/components/utilities`
  with `@import "tailwindcss"`.
- Class renames: `shadow-sm` to `shadow-xs` and `shadow` to `shadow-sm` (same for
  `rounded` and `blur`), `outline-none` to `outline-hidden`, `ring` to `ring-3`,
  `bg-gradient-to-r` to `bg-linear-to-r`.
- `border` and `divide` default to `currentColor`: name a color.
- The important modifier goes last (`flex!`), arbitrary variable shorthand is
  `bg-(--var)`, and stacked variants read left to right.
- Custom utilities use `@utility`, not `@layer utilities`; dark mode by class uses
  `@custom-variant dark (...)`.
- `hover:` applies only on devices that can hover.
- `npx @tailwindcss/upgrade` does most of this; review its diff.

## Guardrails

- Use `gap-*` instead of `space-x-*` and `space-y-*` on flex and grid.
- Use `size-*` for squares.
- Animate `transform` and `opacity`; name the property in transitions instead of
  `transition-all`; respect `motion-reduce:`.
- Do not copy one value into both the CSS variables and the component code.
- Do not use `accent` for a second brand color; keep it for hover, focus and
  selection surfaces.
- Keep neutral fallback tokens for loading and missing-theme states, and do not
  layer client-side color math over a theme the server already resolved.
- Check whether v4 already has a feature before adding a plugin or helper library.
