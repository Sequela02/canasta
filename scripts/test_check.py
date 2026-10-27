"""Regression checks for the public agent inventory (standard library only)."""

from pathlib import Path
import shutil
import tempfile
import unittest

from check import check


class AgentInventoryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        source = Path(__file__).resolve().parents[1]
        for name in ("agents", "skills", "docs", ".claude-plugin"):
            shutil.copytree(source / name, self.root / name)
        for name in ("README.md", "LICENSE"):
            shutil.copy2(source / name, self.root / name)

    def test_pack_passes(self):
        self.assertEqual([], check(self.root))

    def test_missing_role(self):
        (self.root / "agents/clerk.md").unlink()
        self.assertIn("Agent inventory mismatch", check(self.root))

    def test_fixed_model(self):
        path = self.root / "agents/worker.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "name: worker", "name: worker\nmodel: example/model"), encoding="utf-8")
        self.assertIn("Nonportable agent metadata: agents/worker.md", check(self.root))

    def test_per_tool_model(self):
        path = self.root / "agents/advisor.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "name: advisor", "name: advisor\ncodex.model: example"), encoding="utf-8")
        self.assertIn("Nonportable agent metadata: agents/advisor.md", check(self.root))

    def test_readme_inventory(self):
        path = self.root / "README.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "agents/explorer.md", "agents/clerk.md"), encoding="utf-8")
        self.assertIn("Agent missing from README: explorer", check(self.root))


if __name__ == "__main__":
    unittest.main()
