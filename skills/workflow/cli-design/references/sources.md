# Sources for cli-design

Read on 2026-11-07.

## Where the rules come from

| Rule | Evidence |
| --- | --- |
| Strict parsing, usage code 2 | Python [argparse](https://docs.python.org/3/library/argparse.html) and Rust [clap](https://docs.rs/clap/latest/clap/error/struct.Error.html) print usage errors to stderr and exit 2 |
| Flags over positionals, long names, standard names | [Command Line Interface Guidelines](https://clig.dev) (CLIG), "Arguments and flags"; Heroku [CLI style guide](https://devcenter.heroku.com/articles/cli-style-guide) |
| `--` and `-` | POSIX [Utility Syntax Guidelines](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap12.html) 10 and 13 |
| stdout for the result, stderr for the rest | CLIG, "Output"; Heroku style guide |
| Human output first, `--json` | CLIG: "Humans come first, machines second", "Display output as formatted JSON if `--json` is passed"; GitHub CLI [formatting](https://cli.github.com/manual/gh_help_formatting); gemini-cli `--output-format json` returns one object with an optional `error` |
| Output is an interface | CLIG, "Future-proofing": subcommands, flags, configuration and environment variables are interfaces; human output may change |
| Exit 0 only on success | CLIG, "The basics"; Quint fixed exiting 0 when no test was selected, so CI could not tell a passing suite from an empty one (quint `cliCommands.ts`, #2056) |
| Avoid colliding codes | POSIX shell (126, 127, above 128 for signals); [Node exit codes](https://nodejs.org/api/process.html#exit-codes) (1, 3 to 14); TLC's codes 10 to 14 (mirrored in tla-ts `src/exit-codes.ts`); [sysexits](https://man.freebsd.org/cgi/man.cgi?query=sysexits&sektion=3) is deprecated |
| Errors with the next command | CLIG, "Errors": rewrite errors for humans, put the key information last; Quint prints the command that reproduces a failing run |
| No required prompts | CLIG, "Interactivity": never require a prompt, `--no-input`; GitHub CLI `GH_PROMPT_DISABLED`; gemini-cli runs headless without a TTY |
| Colour only on a TTY | CLIG, "Output"; [no-color.org](https://no-color.org) |
| Responsive, timeouts | CLIG, "Robustness": print something within 100 ms, make things time out |
| Interrupt | CLIG, "Robustness"; Node signal exits are 128 plus the signal number |
| Configuration and secrets | CLIG, "Configuration" and "Environment variables": precedence, no secrets in flags or environment |
| Agent use | cursor/plugins `cli-for-agents`: every input as a flag, examples in every `--help`, idempotent commands, `--dry-run` and `--yes` |

## Community context

Posts read on X, as context and not as rules:

- Andrej Karpathy, 2026-02-24: agents use CLIs natively; products should be usable through a CLI or MCP, with docs exportable as Markdown.
- Philipp Schmid, 2026-10-26: the Gemini API CLI is stateless and self-describing through `--help` and `--dry-run`, for agents to drive.
- A reply on 2026-11-07: deterministic exit codes and structured stdout give an agent something to assert on.

## Where sources disagree

- **Usage errors under `--json`.** Some agent CLIs report run errors as JSON; argparse, clap and effect's CLI print usage errors as text. The skill keeps usage errors as text, since no result exists yet.
- **Exit code for usage.** 2 (argparse, clap, Bash), 1 (effect's CLI, yargs), 42 (gemini-cli). The skill uses 2.
- **Cancellation.** 130 (Node, gemini-cli) against 2 (GitHub CLI). The skill uses 130.
- **Lists in one flag.** POSIX joins values with commas; repeating the flag is safer when values can contain commas.

## Gaps

- No source gives a versioning scheme for `--json` output, such as a schema version field.
- Signal exit codes and TTY detection on Windows terminals were not checked.
