# Runtime, tests, build

## Runtime APIs

- `Bun.file` is lazy: handle a missing file, size limits and untrusted paths
  before reading.
- Give `Bun.serve` an `error` handler that hides internals, validate method, body
  size and auth at the boundary, and shut down gracefully.
- Set a timeout on outbound `fetch` and tell HTTP errors from network failures.
- `Bun.secrets` is for local tools, not deployment secrets.
- `bun:ffi` is experimental. For native code shared with Node, use Node-API addons
  and rebuild them after a Bun upgrade.
- Test on each OS and CPU the repository supports; one local run is not portability.

## Tests

- `bun run test` runs the package script; `bun test` runs Bun's own runner. A script
  can alias Node to Bun (`[run].bun`, `--bun`), so print `process.execPath` before
  comparing runtimes.
- `bun test` shares one module registry across files unless you pass `--isolate`.
  `--parallel` runs files in worker processes; time it on the real suite and give
  each worker its own ports and databases (`BUN_TEST_WORKER_ID`).
- A retry that passes is a flaky test: record the first failure.
- For code that runs on several runtimes, keep one portable suite and a few small
  probes per runtime.

## Build

- Run server code directly unless startup, distribution or assets justify a bundle.
- Set `--target` (`browser`, `bun`, `node`) on purpose.
- Embed only values meant to be public; never inline secret environment variables.
- A successful build does not show the target starts: run a smoke test.
- `bun build --compile` embeds Bun. Treat the executable as a release artifact:
  smoke-test it on the target OS and CPU, and declare assets and config explicitly.

## Containers and CI

- Copy manifests and `bun.lock`, run `bun ci`, then copy source. Never copy local
  `node_modules` into an image for another platform.
- Use a multi-stage build and a non-root user, and keep build credentials out of layers.
- Start the final image with production config and check it shuts down cleanly.

## Measuring speed

State the workload, correctness check, Bun version, OS, CPU, worker count and
cache state. Warm up, interleave variants, run several times and report the median
and spread. Keep profiles and heap snapshots out of the repository; they can hold
secrets.
