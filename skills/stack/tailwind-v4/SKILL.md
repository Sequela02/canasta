---
name: tailwind-v4
description: "Configure Tailwind CSS v4 or change its tokens, utilities, responsive styles, and v3 migrations."
---

# Tailwind v4

Use Tailwind CSS v4 as a CSS-first design-system layer. Keep this skill focused on Tailwind mechanics, tokens, utilities, variants, and maintainability. Use the upstream shadcn guidance (not bundled) for component registry/API work. For color conversion, palettes, contrast and gamut, read [references/oklch/index.md](references/oklch/index.md) and only the topic file it points to.

## Sources

Prefer official Tailwind documentation when behavior is uncertain:

- Theme variables: https://tailwindcss.com/docs/theme
- Styling with utility classes: https://tailwindcss.com/docs/styling-with-utility-classes
- Upgrade guide: https://tailwindcss.com/docs/upgrade-guide
- Tailwind v4 announcement: https://tailwindcss.com/blog/tailwindcss-v4

## Baseline

- Tailwind v4 is CSS-first. Treat the main CSS file as the source of theme configuration.
- Use `@import "tailwindcss";` in the CSS entrypoint.
- Use `@theme` for values that should generate utilities.
- Use `@theme inline` when mapping Tailwind utility tokens to runtime CSS variables, especially with shadcn-style semantic variables.
- Keep runtime semantic values in `:root`, `.dark`, or theme selectors; keep utility-generating names in `@theme`.
- Tailwind v4 targets modern browsers: Safari 16.4+, Chrome 111+, and Firefox 128+. If a project must support older browsers, keep that as explicit product/platform debt.

## Token Model

Use this split:

```css
@import "tailwindcss";

@theme inline {
  --color-primary: var(--primary);
  --color-background: var(--background);
  --font-sans: var(--font-body);
}

:root {
  --primary: oklch(0.45 0 0);
  --background: oklch(1 0 0);
  --font-body: system-ui, sans-serif;
}
```

Rules:

- Define new color values in OKLCH.
- Use semantic names for component code: `bg-background`, `text-foreground`, `border-border`, `text-muted-foreground`.
- Avoid raw palette utilities inside reusable components unless the token is intentionally local.
- Do not duplicate the same value in both component code and CSS variables.
- Do not put theme-variant values directly inside static `@theme` blocks when they need runtime theme switching.
- Define semantic state tokens such as success, warning, info, and destructive when the product needs them; consume those names through component variants instead of palette-string props or local color maps.
- Treat `accent` as a restrained interaction surface for hover, focus, selection, and low-emphasis controls—not as a second CTA, warning, or unrelated brand color.
- Keep neutral fallback tokens for boot, loading, offline, and missing-theme states. Once an authoritative runtime theme is available, do not layer client-side color derivations over it.

## Utility Composition

- Prefer standard scale utilities over arbitrary values.
- Use arbitrary values only for real one-off geometry, measured layout constraints, or token bridging.
- Use `gap-*` instead of `space-x-*`/`space-y-*` for flexible layouts.
- Use `size-*` for square elements.
- Use `min-w-0` and `min-h-0` in flex/grid children that contain text, tables, charts, or scroll areas.
- Use container queries (`@container`, `@sm:`, `@lg:`) when component width matters more than viewport width.
- Use logical properties in CSS when directionality matters.

## Components

- Do not create CSS classes that secretly reimplement component variants.
- Use CVA or the repository's existing variant system for components with repeated visual states.
- Put consumer `className` last in `cn()` merging.
- Keep Tailwind classes readable: group by layout, box, typography, color, state, then motion when the class list is long.
- Extract a component or variant when repeated class bundles represent behavior or a reusable semantic state.
- Do not extract just to hide normal Tailwind usage.

## Responsive And State

- Prefer intrinsic responsive layouts over breakpoint-heavy designs.
- For simple responsive grids, consider `grid-template-columns: repeat(auto-fit, minmax(280px, 1fr))` in CSS or equivalent Tailwind arbitrary grid only when it improves the layout.
- Use data-attribute variants from primitives for state (`data-[state=open]:...`) instead of manual class switching.
- Keep hover-only behavior behind interaction-capable devices when it changes meaning.
- Ensure long labels, Spanish copy, and dynamic content can wrap or truncate intentionally.
- Prefer native scrolling. If styling is needed, derive quiet scrollbar colors from semantic tokens and preserve platform behavior; reserve custom scroll components for bounded widgets.
- Keep full-app shell scrolling in the shell. Do not add page-level viewport-height classes or competing overflow containers as a local layout fix.

## Motion And Performance

- Animate `transform` and `opacity` by default.
- In Tailwind v4, transform-related properties can be independent CSS properties; verify transition utilities affect the property you actually animate.
- Avoid animating layout properties.
- Do not leave `will-change` permanently applied.
- Use reduced-motion variants or CSS media queries for movement.

## Anti-Patterns

- Hardcoded hex/rgb/hsl colors in reusable JSX.
- Arbitrary pixel values for normal spacing, type, radius, or width scale.
- `transition-all` on interactive components.
- Negative letter spacing as a default polish move.
- Overusing `grid` where `flex` or normal document flow is simpler.
- Theme tokens split across several CSS files without a clear owner.
- Tailwind config files kept around as fake authority after migrating to v4.
- Adding plugins or helper libraries before checking whether v4 has the feature natively.

## Verification

For Tailwind changes, run the project's normal CSS/build check. When available, also verify:

- No unknown utility classes in build output.
- Dark/theme variants resolve correctly.
- Long text and responsive states do not overflow.
- Contrast remains acceptable after token changes.
- shadcn components still use the expected `base` API and semantic tokens.
