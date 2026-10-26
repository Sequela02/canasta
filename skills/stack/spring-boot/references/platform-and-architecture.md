# Platform and architecture

## Version resolution

- Prefer the current LTS Java line for production services. A newer
  feature release is not automatically the production target.
- Use a stable Spring Boot line compatible with the repository Java toolchain
  and the required Spring ecosystem. Follow Boot dependency management.
- Use the current compatible Gradle release through the wrapper. Validate
  plugins, bytecode tools, configuration cache, CI, and IDE import before
  upgrading.
- Keep exact versions in executable stack configuration, wrappers, manifests,
  lockfiles, or migration records, not durable skill prose.

At the 2026-07-22 scout, official documentation showed Java 25 as the current
LTS baseline used by this opinionated baseline, Spring Boot 4.1 as stable and compatible through
Java 26, and Gradle 9.6.1 as current. Re-check these sources before a migration:

- https://openjdk.org/projects/jdk/
- https://docs.spring.io/spring-boot/system-requirements.html
- https://docs.gradle.org/current/release-notes.html

## Modular architecture

- Prefer packages by bounded context or feature over a repository-wide stack of
  controllers, services, and repositories.
- Expose a small application API from each module and keep implementation
  packages closed.
- Use events for meaningful decoupling, not to hide a synchronous call graph.
- If Spring Modulith is adopted, verify module cycles and internal-package
  access with `ApplicationModules.verify()` and use module tests for important
  collaborations.
- Keep domain events distinct from external integration events. Translate at
  the outbound boundary and version externally consumed schemas deliberately.

Official reference:

- https://docs.spring.io/spring-modulith/reference/verification.html
- https://docs.spring.io/spring-modulith/reference/testing.html

## Modernization sequence

1. Record the current wrapper, toolchain, framework, plugin, dependency, image,
   schema, and public-contract baseline.
2. Read official migration guides and list breaking changes affecting the repo.
3. Upgrade the smallest coherent platform slice.
4. Resolve repository-owned deprecations instead of suppressing them.
5. Run contract, security, persistence, container, and operational checks.
6. Remove temporary migration code once all real consumers have moved.

