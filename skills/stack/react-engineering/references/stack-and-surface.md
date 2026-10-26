## Stack Resolution

Treat package manifests and lockfiles as installed-state authority. Verify
current stable compatibility in official
framework documentation instead of copying exact package versions into skills.

These are cross-project defaults, not claims about a particular company or
repository. Preserve quality, security, and accessibility gates; let repository
evidence override stack selection when a different supported choice is already
owned or materially better suited.

Shared expectations across web surfaces:

- The `typescript-standards` skill owns the compiler line, module resolution and
  import specifiers, the strict tsconfig baseline, type-level idiom, and Biome.
  Those rules are language-wide and are not restated here. Load it alongside this
  skill for any TypeScript work.
- Bun as the default package manager unless repository evidence selects another
  supported runner.
- Bundled application surfaces are bundler-resolved: `module: "preserve"`,
  extensionless relative imports. Do not carry the runtime-resolved `.js`
  specifier convention into bundled code, and do not carry bundler assumptions
  into a published package.
- Framework-owned embedded-language tooling may retain a scoped TypeScript 6
  compatibility dependency only when official compatibility evidence requires
  it. Keep application compilation on the current stable compiler line and
  remove the bridge once the consumer supports the native API.
- The current governed Tailwind CSS major with semantic tokens and CSS-first
  theme configuration.
- Source-owned shadcn/ui components and Base UI primitives where they carry real interaction behavior.
- OKLCH for new token values and the project-selected icon system; do not assume Lucide is the final visual language.

Select the runtime before selecting React-specific libraries:

| Surface                                                                          | Default                                              | Rules                                                                                                                                                                                                                                                |
| -------------------------------------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Authenticated, operational, or data-heavy application                            | React + Vite                                         | Use the governed stable baseline. Use TanStack Router/Query, React Hook Form, Zod, and client state only where the repository pattern and workflow require them. Load `zod-standards` for runtime schemas, migrations, and compilation.              |
| Marketing site, product landing, campaign page, public writing, or documentation | Astro, static output by default                      | Keep static structure in `.astro` components. Add React islands only for behavior that needs client state or browser APIs. Do not add an SPA router or query client by default.                                                                      |
| Public signup, checkout, or portal paired with marketing content                 | Split content and application deployments by default | Let Astro own discoverable content and hand off to the application. Real credential, tenant, payment, or session creation belongs to the application. If one deployment owns both, choose the dominant interaction model and document the exception. |
| Public route inside an established application                                   | Existing application stack                           | An established transactional route takes precedence over the split default. Do not introduce a second runtime for one route. Prerender or server-render indexable content when discoverability matters.                                              |

Treat a landing page and an application as separate product surfaces even when
the landing page links directly to signup or an authenticated application. They
may share tokens, analytics, metadata conventions, and a domain without sharing
a runtime or deployment.

For Astro surfaces, load `astro` and keep this router focused on surface
selection. The core boundary remains:

- Render indexable copy, navigation, pricing, feature content, and calls to action in the initial HTML.
- Hydrate explicit islands only. Static components must not receive a client directive.
- Use shadcn components for real interactions, not as generic marketing-section scaffolding.
- Keep request-demo and lead-capture forms on Astro when they do not create credentials or tenants. Submit them to an owned public backend or serverless boundary with boundary validation, rate limiting, abuse protection, and explicit privacy/consent handling.
- Keep operational credentials, tenant bootstrap state, and authenticated application sessions out of the marketing surface.
- Verify metadata, canonical URLs, sitemap/content discovery, analytics consent, and production Core Web Vitals for public content.
- Measure production output and record exceptions when client JavaScript, SSR, or a single-deployment hybrid is required.

## React Compiler for React + Vite

Prefer the Oxc Rust React Compiler integration for compatible React + Vite
applications. Verify installed compatibility and current integration status
before adoption; do not silently upgrade an existing application's toolchain.
Keep framework-specific setup in its owning framework for other React surfaces.

The [Oxc announcement](https://oxc.rs/blog/2026-08-18-react-compiler-support),
checked 2026-09-08, documents an experimental integration for Vite 8 with
`@vitejs/plugin-react` 6.1.0 or later and the optional `oxc-transform-react`
peer dependency. These are dated compatibility evidence, not permanent version
pins. Install compatible dependencies with the repository's package manager and
configure the React plugin with `react({ compiler: true })`. Account for the
experimental status in the repository's adoption decision and verify the React
runtime target. Remove superseded Babel compiler wiring when replacing it.

When the compiler is enabled and covers the affected code, prefer automatic
memoization in new components and hooks. Do not add `useMemo`, `useCallback`, or
`React.memo` routinely. Keep manual memoization for demonstrated control or
performance needs, and test carefully before removing existing memoization;
removal can change compiler output and effect behavior. This qualification also
applies to manual memoization examples in `performance/`.

Verify compiler activation, compiler diagnostics, a production build, and the
relevant interactions. Fix Rules of React violations and inspect skipped
components rather than assuming every component was optimized. Measure build
and runtime performance separately; published preliminary compiler benchmarks
are not a guaranteed application speedup.

See [React's memoization guidance](https://react.dev/learn/react-compiler/introduction#what-should-i-do-about-usememo-usecallback-and-reactmemo).
