# Runtime and API Selection

Read this reference when choosing or reviewing Bun runtime behavior or native
APIs.

## Portability first

Choose the contract before the convenience:

- Use Web-standard APIs (`fetch`, `Request`, `Response`, Web Streams,
  `AbortSignal`, `Blob`) for portable boundaries when their verified semantics
  satisfy the consumer.
- Use `node:` APIs for a Node-compatible artifact only after checking Bun's
  current compatibility page for the exact modules and edge behavior used.
  Bun's compatibility is broad but not complete.
- Use `Bun.*` and `bun:*` when Bun owns deployment or when a Bun-only adapter
  isolates the dependency. Keep domain logic unaware of the runtime API.
- Published libraries must not expose Bun types or require Bun globals unless
  Bun-only operation is their explicit contract.

Install `@types/bun` for Bun-native TypeScript surfaces, but keep authoritative
typechecking in `tsc`. Defer module and `tsconfig` choices to
`typescript-standards`; Bun's generic `moduleResolution: "bundler"` example does
not override the cross-project runtime-resolved package rules.

## Files, processes, and shell

- `Bun.file` is lazy. Handle absent files, size limits, encodings, and untrusted
  paths at the boundary before parsing or returning contents.
- Bun 1.4.0 has an open Windows report where an unsettled rejecting
  `Bun.file(...).text/json` promise can allow a zero exit. Until the exact runtime
  is verified fixed, use top-level await, guard optional reads with `.exists()`,
  or use `node:fs/promises` for that boundary. A report is not prevalence proof.
- Use `Bun.write` only after resolving and validating the destination. Preserve
  atomic/recoverable write semantics when partial files would be harmful.
- Prefer `Bun.spawn({ cmd: [...] })` or the array form over constructing a shell
  command. Set `cwd`, environment, stdio, timeout/`AbortSignal`, and exit-code
  handling explicitly. Await `proc.exited` and settle descendants or resources
  on cancellation.
- Bun Shell escapes interpolated values by default. Never use `{ raw: value }`
  with untrusted or dynamically assembled data. Prefer direct argv when shell
  syntax is unnecessary.
- Capture bounded output or stream it. Do not buffer unbounded child output with
  `.text()` or inherit noisy output in machine-readable protocols.

## Environment and credentials

- Bun auto-loads `.env`, environment-specific `.env.*`, and `.env.local` in
  precedence order. Disable automatic loading with `--no-env-file` or
  `bunfig.toml` `env = false` when CI/production environment injection owns
  values.
- Parse required environment variables into typed configuration once. Reject
  missing or malformed authority/security values and avoid ambient reads in the
  core.
- Never print `process.env`, `Bun.env`, registry tokens, or full subprocess
  environments in routine diagnostics.
- `Bun.secrets` is experimental and intended primarily for local tools. Do not
  substitute it for deployment secret management. Record platform service
  requirements and failure behavior if admitted.

## Servers and networking

- Validate method, route parameters, headers, body size, content type, and
  authentication at the server boundary. Return explicit `Response` values.
- Give `Bun.serve` a bounded error path that does not expose internals or
  secrets. Handle graceful shutdown and in-flight work; do not rely on process
  termination as lifecycle settlement.
- Respect backpressure for streams, WebSockets, sockets, and subprocess pipes.
  A successful write call may not mean the complete payload was accepted.
- Put timeouts and cancellation on outbound requests. Distinguish HTTP error
  responses from transport failures and preserve useful causes without leaking
  credentials.
- Native SQL, Redis, S3, and SQLite clients can remove dependencies in a
  Bun-owned adapter. Adoption still requires transaction, pooling,
  cancellation, retry, data-type, migration, observability, and test parity for
  the actual consumer.

## Bun 1.4 built-ins

Evaluate built-ins by stability and invariant, not novelty:

- `Bun.Image`: validate user-controlled paths and byte/pixel limits; account for
  platform-specific formats/backends and deterministic-output requirements.
- `Bun.WebView`: experimental. Keep browser profiles ephemeral by default,
  close with `using`/`await using`, and preserve Playwright or another mature
  runner when its cross-browser fixtures/reporting are required.
- `Bun.cron`: distinguish in-process callbacks from OS-level persistent jobs.
  OS registration is an external mutation requiring explicit authority,
  ownership, inspect/remove operations, and recovery. In-process jobs do not
  survive process exit and do not overlap while a handler is unsettled.
- `Bun.Terminal`: own PTY cleanup, resize, signals, encoding, and supported OS
  behavior. Do not treat a PTY as an ordinary captured subprocess.
- Markdown, JSON5, XML, JSONL, TOML, YAML, archive, and image parsers: validate
  untrusted input limits and compare extension/error/output semantics before
  replacing a dependency.
- `bun:ffi` and the C compiler: experimental and not suitable as a default
  production boundary. Prefer Node-API for stable native integration; isolate
  unsafe pointers and platform ABI assumptions if FFI is explicitly admitted.
- Experimental HTTP/2, HTTP/3, Bake/app, WebView, Secrets, FFI, or other APIs
  need a named limitation and verification surface. Never hide an experimental
  dependency behind a generic interface and call it stable.

## Compatibility and native code

- Check the current Node.js compatibility table for every behavior that matters;
  labels such as "fully implemented" still list semantic differences.
- Prefer Node-API addons for cross-runtime native integration. Rebuild and smoke
  test native addons after Bun or reported Node ABI target changes.
- Verify Windows, Linux, macOS, x64, and arm64 only to the extent the repository
  supports them. Do not claim platform portability from one local run.

## Official sources

- <https://bun.com/docs/runtime/bun-apis>
- <https://bun.com/docs/runtime/nodejs-compat>
- <https://bun.com/docs/runtime/child-process>
- <https://bun.com/docs/runtime/shell>
- <https://bun.com/docs/runtime/environment-variables>
- <https://bun.com/docs/runtime/http/server>
- <https://bun.com/docs/runtime/secrets>
- <https://bun.com/docs/runtime/webview>
- <https://bun.com/docs/runtime/image>
- <https://bun.com/docs/runtime/cron>
- <https://bun.com/docs/runtime/ffi>
- <https://github.com/oven-sh/bun/issues/39787>
