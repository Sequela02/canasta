# SDK and client generation practice

## Purpose

Keep API consumers aligned with one wire contract without making generated code
the product-facing design. Apply this practice across languages, frameworks, and
repository layouts. Tool selection remains owned by the target ecosystem and
the consuming repository.

## Ownership

- Keep one canonical, machine-readable contract per API. A code-first service
  owns it through implementation, annotations, and contract tests; a spec-first
  service owns it in the reviewed specification. Do not treat a generated
  snapshot as a second hand-edited authority.
- Give operations and schemas stable public names. Incidental controller method,
  class, or file names must not silently define the SDK API.
- Generate only from a tested contract snapshot produced by an owned,
  reproducible command. Pin the generator and its material configuration.
- Place generated files behind an explicit generated boundary. They must be
  disposable and must never contain manual edits.

## Generated and handwritten boundaries

Generate the parts whose correctness follows directly from the wire contract:

- request and response types;
- paths, parameters, bodies, and response decoding;
- authentication metadata;
- ordinary endpoint functions;
- mechanical framework integrations when the generator supports them reliably.

Write code only where consumer meaning is not fully expressed by the contract:

- credential injection and coordinated session renewal;
- safe retry, cancellation, streaming, or pagination ergonomics;
- domain-oriented workflows that compose operations;
- stable error translation for the consuming product;
- framework adapters that add demonstrated value.

Handwritten code imports generated types. It must not redeclare wire DTOs,
duplicate endpoint paths, or wrap every generated operation merely to rename it.
Application routing, forms, components, and general UI state do not belong to a
transport SDK. Keep framework-specific adapters optional and separate from the
framework-independent client boundary.

## Package boundary

Keep a generated client local to one application while it has one code consumer.
Create a separately versioned or published SDK only when an active second
codebase, an external consumer, or an independent release contract requires it.
Documentation consumers and agents that can consume the machine-readable
contract directly do not by themselves justify another package lifecycle.

Do not force all languages through one generator. Every language may select an
ecosystem-appropriate generator while consuming the same released contract and
meeting the same compatibility gates.

## Compatibility and release

- Evolve contracts additively by default. Treat removed fields, renamed
  operations or enums, narrower inputs, wider required outputs, changed
  nullability, and altered error or status semantics as consumer-impacting.
- Keep API versions, SDK package versions, and application releases distinct.
- Use semantic versioning for a published SDK after its public surface is
  declared. A breaking generated or handwritten public change requires a major
  release; compatible features require a minor release; compatible fixes require
  a patch release.
- Sequence releases from compatible provider behavior to SDK publication to
  consumer adoption. Do not deploy an incompatible provider contract before its
  consumers can use it unless an explicit parallel-version migration exists.
- Commit generated source or build output only when the repository's release or
  review contract requires it. Name its owner and verify reproducibility; do not
  commit artifacts merely because generation exists.

## Verification gate

For every material contract or SDK change:

1. Produce the contract snapshot from the intended provider revision.
2. Lint and validate the snapshot.
3. Compare it with the released baseline for consumer-impacting changes.
4. Run provider contract tests for representative success and failure behavior.
5. Regenerate from a clean generated directory and prove deterministic output.
6. Type-check, build, and test the generated client and handwritten extensions.
7. Exercise representative consumers or report which consumers were not
   verified.
8. Record release order, deprecation, and migration evidence when compatibility
   requires coordination.

Generated code proves only that a description can produce code. It does not
prove that runtime behavior matches the description or that the resulting SDK is
safe and usable.

## Legacy migration

Stop adding duplicated wire types and endpoint implementations first. Migrate a
bounded consumer surface at a time, characterize its observable behavior, adopt
generated types and operations, preserve only justified ergonomic extensions,
and remove the replaced manual authority. Do not rewrite a working multi-client
SDK in one step solely to achieve generation consistency.

## External anchors

- OpenAPI Specification: https://spec.openapis.org/
- Semantic Versioning: https://semver.org/
