"""Regression checks for architecture-scan's hot-spot script (standard library only)."""

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/workflow/architecture-scan/scripts/hotspots.py"


def git(repo, *args, author="Dev <dev@example.com>"):
    name, email = author[:-1].split(" <")
    env = {"GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email, "GIT_COMMITTER_NAME": name,
           "GIT_COMMITTER_EMAIL": email, "PATH": __import__("os").environ["PATH"]}
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, env=env)


class HotspotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        git(self.repo, "init", "-q")
        self.files = ["server/src/a.ts", "web/src/b.ts", "server/src/a.test.ts", "web/package-lock.json"]
        for f in self.files:
            (self.repo / f).parent.mkdir(parents=True, exist_ok=True)
        for i in range(6):
            self.commit(f"feat: change {i}", self.files, i)
        self.commit("chore(deps): bump", ["web/src/b.ts"], 99, author="renovate[bot] <bot@example.com>")

    def commit(self, message, files, i, author="Dev <dev@example.com>"):
        for f in files:
            (self.repo / f).write_text(f"line {i}\n" * (i + 1), encoding="utf-8")
        git(self.repo, "add", "-A")
        git(self.repo, "commit", "-q", "-m", message, author=author)

    def run_script(self):
        return subprocess.run([sys.executable, "-I", str(SCRIPT), str(self.repo), "--since", "1 year ago"],
                              capture_output=True, text=True, check=True).stdout

    def test_filters_bots_lockfiles_and_tests(self):
        out = self.run_script()
        self.assertIn("6 commits since", out)
        self.assertNotIn("package-lock.json", out)
        self.assertIn("server/src/a.ts  <->  web/src/b.ts", out)
        self.assertNotIn("a.test.ts  <->", out)
        self.assertNotIn("<->  server/src/a.test.ts", out)


if __name__ == "__main__":
    unittest.main()
