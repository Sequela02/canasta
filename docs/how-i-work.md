# How I work with agents

I'm Ricardo Armenta, also known as Canitas. I want to supervise agents less and
get better proof from them. The outcome is mine; the agent helps me explore,
decide and build. This is how I work today. It works for me, and it may change.

Most of what follows is opinion: my habits, plus advice from people I learn
from. Where a claim rests on a study or an article, I link it. Those are marked
**Evidence**; everything else is my own practice.

## 1. I say Explore, Decide or Build

Explore means the agent looks and reports. It doesn't edit. Decide means it
compares options and recommends one, then stops. Build means it does the thing
we agreed on.

For bigger work I say who it's for, how I'll know it's done, and what's off
limits. A small, clear edit needs none of that.

If something new turns up halfway, it doesn't become part of the task on its
own. I decide whether to continue, change the plan or stop.

## 2. I hand off the task, not the job of figuring out what I meant

A good brief says the goal, what to deliver, what not to touch, how to check
it, and what the agent may and may not do on its own.

Before starting anything big, the agent tells me back what it understood, and
marks its key assumptions as checked, guessed or unknown. It checks the facts
it can check before relying on them.

I started doing this after looking back at a few weeks of my own agent
sessions: I spent a lot of messages correcting misunderstandings and pulling
scope back.

## 3. I make decisions in batches

When the agent needs me, I want the related questions together, each with a
recommendation, what it's based on, and what happens if I choose it. Small
reversible details inside the task it decides itself. Product, taste and
anything that leaves my machine, I decide.

"Continue" means keep working. It never means "publish this" or "merge that".

I keep the scope of a task small and stable. Good ideas that come up along the
way go to a list for later, unless they affect safety or correctness.

## 4. I research to make a decision

Before researching, I name the decision it's for, what I don't know, and how
much time it gets. When the time runs out, I get an answer or a clear "we
don't know this yet". A second opinion is for a specific disagreement, not for
reassurance.

## 5. "Done" needs proof

When the agent says it's done, it tells me which check it ran, what came out,
and what that check doesn't cover. For a bug, I want to see it fail first, then
pass after the fix.

These don't count as proof: the agent saying so, another model agreeing, reading
the code, a test nobody ran, or code that only compiles.

Each kind of check proves something different. Tests show behavior on the cases
they run. A proof shows the code matches its contract. A model check covers the
interleavings in the model. None of them shows I asked for the right thing;
that part is still on me.

**Evidence.** [Simon Willison](https://simonwillison.net/2025/Mar/11/using-llms-for-code/)
stresses testing what the agent writes, and using tools that run the code. I
add one thing: the check's limits next to its result.

## 6. For UI, I want to see it

For a change on screen, I want a screenshot or a recording of the real app,
saying which screen, which data and what was clicked. If the agent couldn't
open the app, it says so instead of guessing. A diagram explains the idea; it
doesn't show the app works. Whether it looks right is my call.

## 7. Work can be picked up where it stopped

If a run stops halfway, it leaves a note: what was asked, what's done, what's
pending, and which checks didn't run. If it isn't sure what a command did, it
says so and doesn't repeat it blindly.

Decisions live in the repo or the issue, not in a chat that gets lost.

**Evidence.** [Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey),
in "Step 5: Engineer the Harness", fixes repeated agent mistakes with better
instructions or tools, and gives agents ways to check their own work. When the
same mistake shows up twice, I try to fix it with a test, a lint rule or a hook
instead of another paragraph of instructions.

## 8. Review matches the risk

Small changes that are easy to undo get a quick check. Changes other people
depend on get integration checks and a closer look. Anything touching security,
money, private data, production, or hard to undo gets an independent review,
and I look at it myself.

I also have a different model family review the work. I think it helps, but I
treat it as something to measure, not a guarantee.

## 9. One agent by default

I start with one agent. I split work only for a second opinion, for parallel
work that doesn't touch the same files, or to keep context small. Each helper
gets a clear piece, its limits and how to check it. I check the result where
it lands, not just the helper's report.

More agents cost coordination. I judge delegation by whether it got the task
done, not by how many agents were running.

## 10. Passing checks don't mean permission

Private data and credentials stay where they belong. Anything outward
(publishing, pushing, opening a PR, deploying, giving access, deleting) needs a
clear yes for that specific thing. Answering a question isn't a yes.

Every PR ends with a **risk note**: can it be undone easily, what it can break,
and what proves it works. The agent **doesn't merge unless the project's own
policy allows it**. In my projects, only docs and tests can merge on their own,
after CI and a review. Behavior changes and anything hard to undo wait for me.

## 11. I measure what got done, not activity

**Evidence.** In [METR's July 2025 study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/),
16 experienced open-source developers took 19% longer on 246 real tasks with
the AI tools of early 2025, while expecting to be faster. That was one setting
and one generation of tools. The [DORA 2025 report](https://dora.dev/research/2025/dora-report/)
describes AI as amplifying what a team already does, good and bad.

So I don't count messages, tokens or PRs as productivity. I look at accepted
work, how much of my time it took, rework, and bugs that got out. I compare
similar tasks, change one habit at a time, and accept "inconclusive" as an
answer.

## What my own sessions told me

Looking back at a few weeks of my agent sessions showed me where I kept
repeating myself: clarifying, narrowing scope, recovering context. That data
is private, and it can't tell me how much time I'd save. It told me which
habits to try. I'll know they work if I get accepted work with less babysitting
and nothing slipping through. If not, I change them.
