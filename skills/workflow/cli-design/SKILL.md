---
name: cli-design
description: "Design or review a command-line interface that people, scripts and coding agents run: commands, flags, output, --json, exit codes, help, errors, prompts, signals. Use before adding or changing a command or flag, and when reviewing one. Not for the library a command wraps (api-design)."
tags:
  - cli
  - design
  - review
---

# CLI design

A command line is an API whose callers are people, scripts and agents. An agent
reads the exit code, then stdout, and never answers a prompt. Design for it and
for a person at a terminal at once.

When the CLI wraps a library, design the library first with `api-design`: the
command maps arguments onto it and prints its result. Document the CLI with
`technical-writing`.

## Design a command line

Stop when a step shows that no consumer needs the feature.

1. **Consumers.** List the real callers (a person, an agent's tool call, a CI
   job), each with the exact command line it will run.
2. **Result.** Fix the result type first. `--json` prints exactly that result;
   the CLI adds fields only for failures before the library is called.
3. **Grammar.** One synopsis per command: at most one positional (usually the
   input file), a long name for every flag, value names, repeatable flags,
   defaults, mutual exclusions. Reuse the wrapped tool's names.
4. **Outcomes.** One row per outcome: exit code, stream, summary line, JSON
   `status`. Include usage error, crash, interrupt and timeout.
5. **Errors.** For each failure a user can cause: the message and the next
   command or flag to try.
6. **Terminal behavior.** Color, progress and prompts, for a TTY and a pipe.
7. **Help.** `--help` per command, leading with examples, and short help when
   required input is missing.
8. **Contract tests first**: [contract tests](references/contract-tests.md).

For a change to an existing CLI, run steps 2 to 5 and 8 on the diff and mark
every removed or renamed flag, exit code or JSON field as breaking.

## Rules

**Parsing**

- Use the platform parser in strict mode (`util.parseArgs` with `strict: true`,
  clap, argparse). An unknown flag, missing value, bad value or extra positional
  is a usage error.
- Prefer flags to positionals. Reserve `-h`/`--help` and `--version`. Standard
  names: `--json`, `-n`/`--dry-run`, `--no-input`, `-o`/`--output`,
  `-q`/`--quiet`, `-f`/`--force`. `--` ends options; `-` is stdin or stdout.
- A value that can hold commas (an expression) takes a repeated flag, not a
  comma list.
- No catch-all command and no prefix matching of command names.

**Output**

- The result goes to stdout. Progress, logs, warnings, hints and errors go to
  stderr.
- Default to human-readable output. `--json` prints one JSON document with the
  same exit code. Add another format only for a consumer that needs it; JSON
  Lines only for long runs that emit events.
- After parsing succeeds, `--json` failures use the result's error shape on
  stdout. Usage errors stay text on stderr, since no result exists yet.
- Same input, same bytes. Timestamps and durations go in a separate field or
  stay out.
- `--json` fields, exit codes, flag names and environment variables are a
  versioned interface. Human text may change.

**Exit codes**

- 0 only when the command did what was asked. A check that examined nothing is
  not a success.
- Usage error 2. Uncaught crash 1. Interrupt 130 (SIGINT) or 143 (SIGTERM),
  after bounded cleanup.
- Give another code only to an outcome a caller branches on, and publish the
  table. Stay clear of the shell (126 to 165, 255), the runtime (Node uses 1
  and 3 to 14) and any wrapped tool. For a Node CLI, 20 to 29 is clear of all.

**Errors and help**

- Every error says what went wrong, where, and the next command to run, with
  the key line last. No stack trace for an expected error.
- `--help` goes to stdout with exit 0, shows defaults and leads with examples.
  Missing required input prints short help to stderr with the usage code.

**Terminal and environment**

- No required prompt. Without a TTY on stdin, or with `--no-input`, fail fast
  and name the flag to pass. Read stdin only when it is not a TTY or `-` is
  given.
- Color and animation only on a TTY; honor `NO_COLOR`, `TERM=dumb` and
  `--no-color`. On a pipe, print progress as plain lines.
- Print something within about 100 ms for anything slow. Bound every wait with
  a default timeout, which is its own outcome, never success.
- Configuration precedence: flags, environment, project file, user file.
  Secrets come from a file or stdin, never a flag.
- Commands that change state are safe to rerun. Destructive ones take
  `--dry-run` and an explicit `--yes` or `--force`.

## Example

A checker, `tool check <file> --rule <name>`:

| Outcome | Exit | Stream | JSON `status` |
| --- | --- | --- | --- |
| rule holds | 0 | stdout summary | `passed` |
| rule violated | 20 | stdout summary | `failed` |
| unsupported input | 21 | stdout summary | `unsupported` |
| timeout | 22 | stdout summary | `timeout` |
| bad flag or missing file argument | 2 | stderr usage | none |
| crash | 1 | stderr | none |

`tool check a.txt --rule` exits 2 with `--rule needs a value` and the usage
line on stderr, and nothing on stdout.

## Review an existing CLI

Run the checklist in [contract tests](references/contract-tests.md). Report
each failure with the command line that shows it, its exit code and output, and
the rule it breaks.

## Done when

- the synopsis, the outcome table and the error messages exist;
- the contract tests run the built binary and pass;
- the stable surface (flags, exit codes, JSON fields) is listed in the docs.

[Sources](references/sources.md) holds the evidence and where sources disagree.
