import json
from pathlib import Path
import tempfile
import unittest

from route_evals import Corpus, run, stem, tokenize


def write_skill(root: Path, name: str, description: str) -> None:
    folder = root / "skills" / "workflow" / name
    folder.mkdir(parents=True)
    (folder / "SKILL.md").write_text(f"---\nname: {name}\ndescription: \"{description}\"\n---\n\n# {name}\n", encoding="utf-8")


def write_cases(root: Path, name: str, positive: list[str], negative: list[tuple[str, str | None]]) -> None:
    (root / "evals").mkdir(exist_ok=True)
    data = {
        "skill_name": name,
        "trigger": {
            "positive": [{"prompt": p} for p in positive],
            "negative": [{"prompt": p, **({"owner": o} if o else {})} for p, o in negative],
        },
    }
    (root / "evals" / f"{name}.json").write_text(json.dumps(data), encoding="utf-8")


class RouteEvalsTest(unittest.TestCase):
    def test_stem_folds_related_forms(self):
        self.assertEqual(stem("tests"), stem("test"))
        self.assertEqual(stem("specification"), stem("specify"))

    def test_tokenize_drops_stop_words_and_applies_aliases(self):
        self.assertEqual(tokenize("Fix the docs"), ["fix", stem("document")])

    def test_rank_prefers_shared_vocabulary(self):
        corpus = Corpus({"tdd": "write a failing test first", "refactor": "change structure without behavior"})
        self.assertEqual(corpus.rank("add a failing test")[0][0], "tdd")

    def test_passing_catalog(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "tdd", "Write a failing test first, then the code that passes it.")
            write_skill(root, "refactor", "Restructure code without changing behavior: rename, move, remove duplication.")
            write_cases(root, "tdd", ["write a failing test", "test first please", "add a failing test for the bug"],
                        [("rename this class", "refactor"), ("move this function", "refactor")])
            write_cases(root, "refactor", ["rename this class", "remove duplication here", "move this function"],
                        [("write a failing test", "tdd"), ("test first please", "tdd")])
            errors, _, summary = run(root, None)
            self.assertEqual(errors, [])
            self.assertIn("rank-1 rate 100%", summary)

    def test_reports_missing_cases_and_a_wrong_owner(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_skill(root, "tdd", "Write a failing test first.")
            write_skill(root, "refactor", "Restructure code without changing behavior.")
            write_cases(root, "tdd", ["write a failing test"], [("write a failing test", "refactor")])
            errors, _, _ = run(root, None)
            joined = "\n".join(errors)
            self.assertIn("refactor: no case file", joined)
            self.assertIn("need 3 / 2", joined)
            self.assertIn("tdd: ranked #1 for negative", joined)


if __name__ == "__main__":
    unittest.main()
