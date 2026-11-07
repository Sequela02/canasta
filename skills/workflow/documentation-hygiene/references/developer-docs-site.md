# Developer docs: placement and drift

For placing, moving or retiring the pages of a library, SDK or CLI docs set,
its examples, and the files agents read. What goes on each page belongs to
`technical-writing` (its developer-docs reference).

## One source, many copies

- One editable source tree. The docs site, the copy inside the package and
  the agent files are generated from it. Never edit a copy.
- The navigation or manifest changes in the same change as an added, moved
  or removed page.
- Every generated file has a check that regenerates it and fails on a diff,
  in CI. Without one, a generated file decays into a hand-edited copy.

## Examples

- Runnable examples live as files in a folder that is typechecked and run,
  and pages include them.
- Inline blocks either run through a doctest tool or are labeled excerpts.
- A test comparing a copied block with its file is the fallback when the
  docs tool cannot include files.

## Files for agents

Each has one owner and is generated from the docs:

- `llms.txt`, `llms-full.txt` and a Markdown version of each page;
- docs or an `AGENTS.md` shipped inside the published package, listed in the
  package's `files` and checked by the packing step;
- a skill for the package's users, which changes with every user-facing
  change.

A file that restates the docs by hand is a cache: it needs a regenerate step
or a named owner who updates it.

## The same change updates the docs

A change to a public export, command, flag, configuration key, environment
variable, default, error code or exit code updates, in the same change:

- its reference entry;
- every guide that names it (search for the symbol);
- the files for agents;
- the changelog entry.

## Versions and retirement

- Docs describe released behaviour. Label anything unreleased.
- Generate the changelog from change files where the repository uses them,
  and never edit the generated file.
- A breaking change gets a migration page. Docs for older versions stay
  frozen.

## Optional: test the docs with questions

Keep a list of real user questions, each with the facts a correct answer
contains. An agent answers them from the docs alone, and a miss names the
page to fix. Adding a question is fine; deleting one or weakening its facts
to make the test pass is not. It costs model calls, so run it when the docs
change.
