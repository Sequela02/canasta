# Slow suites and CI

## Find the owner of the time

1. Record a baseline: three or more runs, cold and warm cache, same machine.
2. Read Vitest's duration buckets (transform, setup, import, tests, environment).
   The agent-oriented reporter (`minimal`, alias `agent`) hides them; use
   `--reporter=default`, or default plus `json` with `outputFile`, while you
   diagnose. Setting a reporter yourself turns off the automatic GitHub Actions
   reporter, so add `github-actions` back when CI needs annotations.
3. Apply the lever for the bucket that dominates:

| Bucket | Lever |
| --- | --- |
| Import or transform | Look at import durations and large barrel files; cut the import graph at ownership boundaries. Use dependency optimization only for a measured costly dependency. |
| Setup or environment | Time setup per file. `globalSetup` runs once in another scope and does not replace `setupFiles`. |
| Test bodies | Remove real waits, extra subprocesses and network, repeated setup and oversized fixtures, keeping the real contract. |
| CPU contention | Share one worker budget across packages, pools, services and CI jobs; benchmark fixed budgets on the target host. |
| Memory or hangs | Profile with a simpler worker setup and a watchdog; lower concurrency only after telling a leak from contention. |

## Switches that change meaning

Turning these on is a semantics change, not a speed setting:

- `isolate: false`: only for a stateless project that passes repeated shuffled
  runs.
- Pool: start with `forks`. `threads` fits only when you need no `process.chdir`,
  native modules or process isolation.
- Sharding splits files, not tests. Check how uneven the files are and how much
  setup repeats before sharding. Merging blob reports works in run mode only and
  leaves out attachments; collect `attachmentsDir` separately and check shard,
  test, report and artifact counts.
- A persistent module cache is a local experiment until invalidation on source,
  alias, plugin, environment and config changes is shown to work.

## Comparing runs

State the invariant that must still hold, versions, host, cache state, seed and
order, reporter, `maxWorkers`, file parallelism, pool, other load, and memory
pressure. Hold them fixed, separate cold from warm, interleave variants, and report
the median with spread or p95. Record failures, retries, hangs and memory use. One
fast run is not a result.

## Handling output

CPU and heap profiles, traces and reports can hold secrets and personal data. Use
synthetic workloads, write them to an ignored folder, and review or redact before
you commit, attach or paste them anywhere.
