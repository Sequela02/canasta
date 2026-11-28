# Astro implementation notes

## Pick the rendering

| Content | Use |
| --- | --- |
| Landing, docs, blog, pricing, legal | Static HTML (the default) |
| Interactive widget | Client island, lazy directive |
| One personalized block on a static page | Server island (`server:defer`) |
| A route that needs request data | On-demand route plus an adapter |

Route caching is stable in current Astro; check the docs for the installed major
before relying on `cache` or `routeRules`.

## Content and metadata

- Define collection schemas in the content config; use a loader for local or
  remote content instead of crawling files by hand.
- Import local images and render them with Astro's image components.
- Build canonical URLs from the `site` setting.
- Give each page a title, description, canonical, social tags, `lang` and one `h1`.

## Scripts

- Package imports work in normal `<script>` tags, which Astro bundles. A script
  with `is:inline` is left alone and cannot import packages.

## Forms

Keep a simple contact form static-first: validate on the server again, rate
limit, ask for consent, show pending and error states, and let it submit without
JavaScript when you can.

## Verify

1. `astro check` and the production build.
2. List the emitted routes and assets.
3. Use the project's browser test tool for navigation, forms, breakpoints, focus
   order and reduced motion.
4. Check title, canonical, Open Graph, sitemap, robots and the 404 page.
