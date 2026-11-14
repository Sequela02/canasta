# Boundary checks

Reference for [`domain-modeling`](../SKILL.md). Two rules, one test per
language, run in CI:

- **Domain purity:** a context's domain code imports no framework,
  persistence, transport or serialization type.
- **Context access:** a context reaches another only through its public API.

Each starting point below assumes contexts as top-level packages
(`<root>/<context>/{domain,application,infrastructure}`) with `application`
as the public API. Adjust the patterns to the repository's layout and check
them against the tool's documentation at the version the repository pins.

## Baseline for an existing codebase

Record today's violations once, commit the record, and fail CI only on new
ones. The baseline is the refactoring backlog: it shrinks as contexts are
fixed, and a pull request that grows it is a review finding.

## Java: ArchUnit

```java
@AnalyzeClasses(packages = "com.example")
class BoundaryTest {
    @ArchTest
    static final ArchRule domainIsPure = FreezingArchRule.freeze(
        noClasses().that().resideInAPackage("..domain..")
            .should().dependOnClassesThat().resideInAnyPackage(
                "org.springframework..", "jakarta.persistence..",
                "jakarta.servlet..", "com.fasterxml.jackson..", "org.hibernate.."));

    // One rule per context; this one protects `booking`.
    @ArchTest
    static final ArchRule bookingIsReachedThroughItsApi = FreezingArchRule.freeze(
        noClasses().that().resideOutsideOfPackage("com.example.booking..")
            .should().dependOnClassesThat().resideInAnyPackage(
                "com.example.booking.domain..", "com.example.booking.infrastructure.."));
}
```

`FreezingArchRule` stores current violations on first run; set
`freeze.store.default.allowStoreCreation=true` in `archunit.properties` for
that run, and commit the store. In a Spring Modulith project with no
violations left, `ApplicationModules.of(Application.class).verify()` replaces
the per-context rules.

## TypeScript: dependency-cruiser

```js
// .dependency-cruiser.cjs
module.exports = {
  forbidden: [
    {
      name: "domain-is-pure",
      severity: "error",
      from: { path: "^src/[^/]+/domain/" },
      to: { dependencyTypes: ["npm", "core"] },
    },
    {
      name: "contexts-meet-through-api",
      severity: "error",
      from: { path: "^src/([^/]+)/" },
      to: { path: "^src/[^/]+/(domain|infrastructure)/", pathNot: "^src/$1/" },
    },
  ],
};
```

dependency-cruiser parses TypeScript only when `typescript` is installed in
the project; with it missing, it cruises zero modules and passes. Record the
baseline with
`depcruise src --output-type baseline --output-to .dependency-cruiser-known-violations.json`
and run CI with `depcruise src --ignore-known`. Add an npm package to
`pathNot` of the first rule when the domain may use it, such as a
validation or Effect library chosen for the domain itself.

## Python: import-linter

```toml
# pyproject.toml
[tool.importlinter]
root_package = "app"
include_external_packages = true

[[tool.importlinter.contracts]]
name = "Domain is pure"
type = "forbidden"
source_modules = ["app.billing.domain", "app.shipping.domain"]
forbidden_modules = ["fastapi", "sqlalchemy", "pydantic", "httpx"]

[[tool.importlinter.contracts]]
name = "Billing is reached through its API"
type = "forbidden"
source_modules = ["app.shipping"]
forbidden_modules = ["app.billing.domain", "app.billing.infrastructure"]
```

Run `lint-imports` in CI. For the baseline, list each current violation under
the contract's `ignore_imports`, and remove entries as they are fixed.
