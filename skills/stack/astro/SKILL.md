---
name: astro
description: "Build or debug Astro pages, content collections, islands, rendering, assets, and site configuration."
---

# Astro

Use Astro for content-first surfaces and ship the least client JavaScript that
fully supports the required behavior. Read the repository manifests before choosing APIs or changing dependencies; this
skill is not version authority.

## Workflow

1. Identify the surface, output mode, deployment target, content source, and
   interactions.
2. Keep document structure, content, navigation, metadata, and non-interactive
   components in `.astro` files.
3. Add a framework island only when behavior needs component state or an
   existing framework component. Choose the least eager `client:*` directive
   that still meets the interaction requirement.
4. Prefer build-time content and static output for landings. Introduce
   on-demand rendering, server islands, sessions, actions, or adapters only
   when request-specific behavior proves the need.
5. Use Astro image components, semantic HTML, canonical metadata, structured
   content schemas, and accessible forms.
6. Use browser-native cross-document View Transitions for navigation when they
   satisfy the experience. Add a client router only for features that require
   it and account for script lifecycle changes.
7. Run the repository's Astro check, typecheck, build, and browser verification.
   Inspect rendered metadata, responsive layout, keyboard navigation, reduced
   motion, asset output, and client JavaScript.

## Boundaries

- Do not turn a content site into a React SPA.
- Do not hydrate static navigation, cards, layout, or copy.
- Do not add an adapter to a fully static deployment.
- Do not access browser APIs in server frontmatter.
- Do not add Motion or GSAP for page navigation that native View Transitions
  express cleanly.
- Do not copy framework versions into this skill. Consult the resolved stack
  profile and current official documentation.
- Keep credential, tenant, checkout, and authenticated application workflows
  behind the owning application boundary unless the architecture explicitly
  assigns them to Astro server routes.

## Reference

Read [references/implementation.md](references/implementation.md) when choosing
rendering, hydration, content, transition, or verification patterns. For APIs
that may have changed, consult Astro's official documentation and `llms.txt`
before implementing.
