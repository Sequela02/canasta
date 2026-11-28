---
name: astro
description: "Build Astro pages with the least client JavaScript: when a component needs an island, which client:* directive to use, static vs on-demand rendering, content collections, View Transitions. Use when editing .astro files or astro.config."
paths: ["**/*.astro", "**/astro.config.*"]
---

# Astro

Ship HTML. Add JavaScript only where a user interaction needs it.

Versions and APIs move: read the Astro version in `package.json` and the docs for
it at docs.astro.build. The Astro Docs MCP server (`https://mcp.docs.astro.build/mcp`)
serves current docs to agents. Run `npx @astrojs/upgrade` only when asked to upgrade.

## Procedure

1. Find the output mode (`output` and adapter in `astro.config.*`), the content
   source and the interactions the page needs.
2. Write structure, copy, navigation, cards and metadata as `.astro` components.
   They render at build time and send no JavaScript.
3. For each interactive piece, ask what breaks without client JavaScript. If
   nothing breaks, it stays `.astro`. If something does, make one small island
   and pick the lazier directive that still works:
   `client:visible` (below the fold) < `client:idle` (not urgent) < `client:load`
   (must work at first paint). `client:only` skips server HTML; use it for
   components that cannot render on the server.
4. Keep pages static. Use on-demand rendering or a server island (`server:defer`)
   only for content that differs per request, and add an adapter only then.
5. Use `astro:assets` images, a content collection with a schema for repeated
   content, and a unique title, description and canonical URL per page.
6. For page navigation animation, start with native cross-document View
   Transitions. Add `<ClientRouter />` only for what native cannot do (persisted
   elements, shared state); it makes scripts run once, so re-run setup on
   `astro:page-load`.
7. Check: run the project's `astro check` and `build`, then open the built page.
   Confirm each island is justified, the JavaScript shipped is what you expect
   (network tab or `dist/_astro`), keyboard navigation works, and navigation is
   correct with `prefers-reduced-motion: reduce`.

## Example

A pricing page with a monthly/yearly toggle and a feature table.

Bad: the whole page is `<Pricing client:load />`, so the table hydrates too.

Good: the table and copy stay in `Pricing.astro`. Only `<BillingToggle client:visible />`
is an island. If the toggle only switches visible numbers, a `<script>` that sets a
`data-` attribute on the section and CSS that shows one price is smaller still.

## Guardrails

- Browser APIs (`window`, `document`) run in a `<script>` or an island, not in
  frontmatter, which runs on the server.
- Credential, tenant, checkout and signed-in flows belong to the application that
  owns them; Astro routes handle them only when the architecture says so.
- Validate form posts again on the server, with rate limiting.

More on rendering choice, content, forms and verification:
[references/implementation.md](references/implementation.md).
