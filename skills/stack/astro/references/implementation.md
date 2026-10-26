# Astro Implementation Reference

## Rendering selection

- Static HTML: default for landings, documentation, blogs, navigation, cards,
  product explanation, pricing content, and legal content.
- Client island: use only for browser state or interaction. Prefer
  `client:visible` below the fold, `client:idle` for non-urgent enhancement,
  and `client:load` only for immediately interactive controls.
- Server island: use for request-specific content that should not force the
  surrounding page into on-demand rendering.
- On-demand route: use only when the route itself requires request-time data.

Never choose a directive from a generic recipe without checking the actual
interaction, bundle, and supported Astro release.

## Content and assets

- Define content schemas at the canonical content configuration entrypoint.
- Use supported loaders for local or remote content instead of hand-built file
  crawling.
- Import local images and render them through Astro image components when
  optimization is valuable. Keep public passthrough assets deliberate.
- Generate canonical URLs from the configured site URL.
- Give every page a unique title, description, canonical URL, social metadata,
  language, heading structure, and index policy.

## Scripts and navigation

- Process npm imports through normal bundled `<script>` elements; do not place
  package imports in scripts that Astro intentionally leaves inline.
- Prefer native cross-document View Transitions for MPA navigation.
- If a client router is justified, reinitialize behavior through documented
  Astro navigation lifecycle events and test back/forward navigation.
- Ensure navigation remains correct with animation disabled and with
  `prefers-reduced-motion: reduce`.

## Forms

- Keep simple lead or contact forms static-first.
- Validate again at the server boundary.
- Include rate limiting, abuse protection, explicit consent, useful error
  messages, pending state, and a no-JavaScript-compatible submission path when
  feasible.

## Verification

Use repository commands rather than assuming a package manager. At minimum:

1. Run Astro's diagnostic/type check when configured.
2. Build the production site.
3. Check emitted routes and assets.
4. Use Playwright for navigation, forms, responsive breakpoints, focus order,
   and reduced motion.
5. Inspect shipped JavaScript and confirm every hydrated island is justified.
6. Verify title, canonical, description, Open Graph, structured data, sitemap,
   robots policy, and 404 behavior where applicable.

## Official sources

- Documentation: https://docs.astro.build/
- Agent-readable documentation: https://docs.astro.build/llms.txt
- Islands: https://docs.astro.build/en/concepts/islands/
- View transitions: https://docs.astro.build/en/guides/view-transitions/
- Content collections: https://docs.astro.build/en/guides/content-collections/
- Images: https://docs.astro.build/en/guides/images/
- Upgrade guides: https://docs.astro.build/en/upgrade-astro/
