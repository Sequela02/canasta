# Stack and surface

These are defaults. A repository's documented choice wins. Read versions from
manifests and lockfiles and check compatibility in official docs; do not copy
version numbers into this skill.

## Defaults for web surfaces

- Package manager: Bun, unless the repository uses another.
- TypeScript rules (module resolution, import specifiers, `tsconfig`) are in
  `typescript-standards`. Bundled application code resolves through the bundler:
  `module: "preserve"`, extensionless relative imports.
- Styling: current Tailwind with semantic tokens (`tailwind-v4`). Source-owned
  shadcn/ui components, with Base UI primitives where behavior matters. OKLCH for
  new color tokens.

## Pick the runtime before the library

| Surface | Default | Notes |
| --- | --- | --- |
| Signed-in, operational or data-heavy app | React + Vite | Add TanStack Router and Query, React Hook Form and Zod only where the repository already does or the workflow needs them. |
| Marketing site, landing page, docs, public writing | Astro, static output | `.astro` components for structure; React islands only for state or browser APIs. No SPA router or query client by default. See `astro`. |
| Public signup, checkout or portal next to marketing | Separate deployments | Astro serves discoverable content and hands off to the app. Credentials, tenants, payments and sessions belong to the app. |
| Public route inside an existing app | The existing stack | Do not add a second runtime for one route. Prerender or server-render it when search engines need it. |

A landing page and an application are different products even when they share
tokens, analytics and a domain.

For marketing surfaces: put copy, navigation and pricing in the first HTML;
hydrate explicit islands only; send lead forms to an owned public endpoint with
validation, rate limiting and consent; keep operational credentials and
authenticated sessions off the marketing site; check metadata, canonical URLs,
sitemap and production Core Web Vitals; record why when you ship client
JavaScript, SSR or a single-deployment hybrid.

## React Compiler in React + Vite

The compiler can run through Babel or through Oxc (`oxc-transform-react`, wired
by `@vitejs/plugin-react`). Check the plugin's and Oxc's current docs for the
installed Vite and React versions and for the integration's status before
adopting it; do not upgrade an existing toolchain silently. Replace Babel
compiler wiring only when you adopt the Oxc one.

Confirm it ran, read its diagnostics, build for production and exercise the
interactions. Measure build time and runtime separately; published benchmarks do
not promise a speedup in your app.
