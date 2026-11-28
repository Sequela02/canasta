# Skill evals

`scripts/route_evals.py` checks that each skill's description loads it for the
prompts it should handle and not for the ones another skill owns. Each
`evals/<skill>.json` lists those prompts:

```json
{
  "skill_name": "tdd",
  "trigger": {
    "positive": [{ "prompt": "Write a failing test for this bug, then fix it" }],
    "negative": [{ "prompt": "Clean up this code without changing its behavior", "owner": "refactor" }]
  }
}
```

- A positive prompt must rank its skill within `top_k` (3 by default).
- A negative prompt must not rank its skill first, and its `owner`, when given,
  must outrank it.
- Each skill needs at least three positive and two negative prompts.
- No two descriptions may be near-duplicates.

```sh
python scripts/route_evals.py                 # report
python scripts/route_evals.py --min-rank1 90  # also fail below a rank-1 floor
```

Write prompts the way a user would type them, not in the description's words.
When a prompt fails, fix the description; a case is changed only when it was
wrong.

The check is lexical (TF-IDF over names and descriptions), so it can't judge
meaning, and it only compares this pack's skills with each other. It catches a
description missing the words users say, and one so broad it outranks the right
skill. Whether an agent follows a skill once loaded needs a behavioral eval,
which this pack doesn't have yet.

The method and the tokenizer come from the deterministic tier of
[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/evals)
(MIT), which in turn builds on Anthropic's skill-creator evals.
