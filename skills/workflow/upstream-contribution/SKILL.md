---
name: upstream-contribution
description: "Prepare an issue, commit or pull request for a project you don't maintain, following its contribution and AI policy, its conventions and its CI. Use before writing anything to submit to another project's repository."
---

# Upstream contribution

The project's rules decide what you submit. Your own organization's
conventions, such as risk notes, merge policies, templates and attribution
habits, stay out unless the project asks for them.

A maintainer's review time is the scarce resource: each submission should be
worth more to the project than the time it takes to read and review it.

1. **Read the project's rules before writing.** Read `CONTRIBUTING`, any AI or
   agent policy it links, its pull request and issue templates, any
   contributor `AGENTS.md`, and three recently merged pull requests from
   outside contributors. Note what it asks for and what it forbids.
2. **See where the maintainers' attention is.** Check recent merges and
   releases, and which recent outside issues they answered and which they
   left open. A report in an area under active work gets read; a report in a
   deprioritized area, or one that asks them to settle a design question,
   often waits. Tell the user when the contribution falls in the second group.
3. **Stop when the policy forbids the contribution.** If it rules out this
   contribution as prepared, for example AI help on an issue reserved for
   newcomers or an AI-written description, don't write the submission. Tell
   the user which rule applies and what the policy allows instead: another
   issue, doing it without AI, or asking the maintainers.
4. **One problem, reproduced.** Each submission carries one problem the user
   has seen fail with the smallest case that shows it. Facts come first; a
   suspected cause is labelled as suspected. Where a decision is needed,
   propose a concrete answer for the maintainers to accept or reject.
5. **Open with the short version.** The first two or three sentences say what
   fails, how to see it, and what was expected, in words the user would
   write. Supporting detail follows; when it runs long, put it in a collapsed
   `<details>` section. Lead with the general problem, then cite the
   project's own stated rule it breaks, then your case as evidence. Keep your
   own product out: the reproduction must stand without it.
6. **Disclose AI use exactly as the project asks.** Follow its placement (pull
   request description, commit trailer or both) and its format. Don't use a
   format it forbids, such as an `Assisted-by:` trailer. If it says nothing,
   ask the user; a disclosure says what the human checked themselves. Never
   add a sign-off, DCO line or CLA statement for the human; they add their
   own.
7. **Match the project's style.** Copy the title format, sections, length and
   tone of its merged pull requests. Address the project, not one maintainer.
8. **Make the smallest change that fits its design.** Before submitting, review
   the diff against its standards, and check that every pattern you copied has
   a reason that applies here.
9. **Predict CI only by reproducing it.** Use the same workflow, platform,
   branches and job types. Name any job you didn't run.
10. **Send one at a time.** With several reports for one project, submit the
    most valuable first and let its reception guide the rest. When it goes
    unanswered, follow the project's stated process; otherwise wait two to
    three weeks and add one reply that brings new information.
11. **The user posts it.** The user reviews and posts, or approves, everything
    that leaves their machine.

[Sources](references/sources.md) lists the evidence behind these rules and
where it is only observation or opinion.
