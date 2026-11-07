# Developer docs

For the docs of a library, SDK or CLI: README, quickstart, guides,
reference, examples and the files agents read. The layers in `SKILL.md`
still apply. API shape belongs to `api-design`, command-line shape to
`cli-design`, and where each file lives to `documentation-hygiene`.

## Two readers on every page

A person and a coding agent read the same page. The agent arrives from a
search or a link, without the sidebar. So every page opens with what the
subject does and when to use it, uses headings named by task or symbol,
and links its prerequisites instead of assuming them.

## Page contracts

**README.** Orientation, not a tutorial. In order: one sentence on what it
does; what it is not, when people often misread it; install and
requirements; one runnable example with its result; stability or status;
links to the quickstart, reference, changelog and contributing guide. Keep
it short enough to read in a minute, about 80 lines; longer needs a reason.

**Quickstart.** One path from a stated starting environment to one
observable result. List the prerequisites, show the expected output at each
step, and end with links to the next pages. It is run from a clean install
before it ships. A temporary path (clone and pack before a package is on the
registry) states the condition that removes it.

**Guide.** One complete workflow, named by the task ("Check a model from
TypeScript", not "API"). Make forks explicit ("If you need x, do y"). Link
reference entries instead of restating them.

**Reference entry.** Titled with the exact symbol or command. One sentence
that starts with a verb. Then the signature, the options with their
defaults, what it returns, what it throws or which exit codes it uses,
its stability, and one minimal example. Say how "omitted", `null`, empty
and disabled differ. Generate signatures and option tables from the types
or the CLI definition, and write the doc comments they come from by the
same rules.

**CLI reference.** Per command: synopsis, flags with defaults, exit codes,
the `--json` output shape, and environment variables. The page and
`--help` come from one source, or a test compares them.

**Explanation.** Why the design is this way: what a result guarantees and
what it does not, and the limits. Keep it apart from the reference tables.

**Troubleshooting.** Symptom first, the exact error string as the tool
prints it, a check that tells the causes apart, and how to confirm the fix.

**Changelog and migration.** Latest first, one entry per version, grouped
as Added, Changed, Deprecated, Removed, Fixed, Security. Each breaking
change gets a migration page with before-and-after code.

## Examples are code

- Every runnable block compiles and runs in CI: a doctest tool, or example
  files that are typechecked and executed.
- Prefer one source: the page includes the example file, or a script
  generates the page from it. A test that compares a copied block with its
  file is the fallback when the docs tool cannot include files.
- Show the expected result as a comment (`// => 20 states`) or an assertion,
  not in prose.
- Real use, not toy code. Keep an example only for behaviour the signature
  doesn't show.
- Label an excerpt as an excerpt, and don't make it click-to-copy.
- Never put a real secret in an example.

## Commands and placeholders

Introduce every block with a sentence. Write placeholders in uppercase
(`FILE`, `INVARIANT`) and explain each after the block. A click-to-copy
block holds only runnable commands.

## Stability words

Define `stable`, `unstable` and `experimental` once for the project and say
what each promises, for example: `unstable` may change in a minor release,
`experimental` in any release. Every deprecation names its replacement.

## Claims and their evidence

| Claim about | Check it against |
| --- | --- |
| How it behaves | the code and its tests |
| What is public | the exports and types |
| When it became available | the changelog or the release |
| Planned behaviour | nothing: label it as planned |

Copy error strings from the code or a real run. Never invent one.

## Files for agents

- Serve each page as Markdown, or keep the Markdown source readable in the
  repository.
- `llms.txt`: one file at the docs root. Its H1 and summary say what the
  project is, when to use it and its limits. For a small project it can be a
  one-file brief. For a larger docs set, follow [llmstxt.org](https://llmstxt.org/):
  link lists of `.md` pages, with the full text in `llms-full.txt`.
- Ship the docs, or an `AGENTS.md` that points into them, inside the
  published package when agents in other projects are expected readers, so
  they read the docs that match the installed version.
- Generate these files from the docs. One written by hand needs an owner
  and a check that it still matches.

## Done when

- every runnable block passed its check, or is labeled as not run;
- every reference entry has its purpose, options, errors and an example, or
  a reason for none;
- the quickstart ran from a clean install;
- every claim was checked against the table above.
