"""The repository-management module: the playbook keeps its sections and the sync tracker check catches bad files."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import sync_tracker  # noqa: E402

MODULE = ROOT / "modules" / "repo-management"
SECTIONS = ["## 1. When to migrate", "## 2. What blocks", "## 3. OSS-readiness checklist", "## 4. The fresh-repository procedure",
            "## 5. Reference migrations", "## 6. Cautionary tale", "## 7. OSS compatibility matrix", "## 8. Public considerations",
            "## 9. After the flip", "## 10. What a migration does not do"]


def check(text: str) -> list[str]:
    top, pairs = sync_tracker.parse(text)
    return sync_tracker.problems(top, pairs)


class Playbook(unittest.TestCase):
    def test_every_section_is_present_in_order(self):
        text = (MODULE / "MIGRATION_PLAYBOOK.md").read_text(encoding="utf-8")
        positions = [text.index(heading) for heading in SECTIONS]
        self.assertEqual(positions, sorted(positions))

    def test_the_reference_migrations_and_the_generated_artifact_case_are_recorded(self):
        text = (MODULE / "MIGRATION_PLAYBOOK.md").read_text(encoding="utf-8")
        for name in ("Job Hunter", "Agent Workflows library", "MyFeed"):
            self.assertIn(name, text)
        self.assertIn("proposal-dashboard.html", text)
        self.assertIn("73 rows", text)

    def test_the_procedure_names_the_pitfalls_that_were_hit(self):
        text = (MODULE / "MIGRATION_PLAYBOOK.md").read_text(encoding="utf-8")
        for phrase in ("refs/pull/*", "${SHA}:refs/heads/main", "noreply", "read back"):
            self.assertIn(phrase, text)


class SyncTracker(unittest.TestCase):
    def example(self) -> str:
        return (MODULE / "sync_tracker.yaml").read_text(encoding="utf-8")

    def test_the_synthetic_example_is_valid(self):
        self.assertEqual(check(self.example()), [])

    def test_a_missing_key_is_reported(self):
        self.assertTrue(any("missing owner" in p for p in check(self.example().replace("    owner: maintainers\n", "", 1))))

    def test_drift_without_a_reason_is_reported(self):
        text = self.example().replace('    drift_reason: "Three private commits since the last export; the next export is planned"\n', '    drift_reason: ""\n')
        self.assertTrue(any("needs a drift_reason" in p for p in check(text)))

    def test_a_bad_revision_kind_drift_and_date_are_reported(self):
        text = (self.example().replace("1111111111111111111111111111111111111111", "abc", 1)
                .replace("kind: snapshot", "kind: copy", 1).replace("drift: none", "drift: maybe", 1)
                .replace("last_synced_at: 2026-01-15", "last_synced_at: 15/01/2026", 1))
        joined = "\n".join(check(text))
        for expected in ("40 lowercase hex", "kind must be", "drift must be", "YYYY-MM-DD"):
            self.assertIn(expected, joined)

    def test_an_address_as_owner_is_rejected(self):
        self.assertTrue(any("not an address" in p for p in check(self.example().replace("owner: maintainers", "owner: someone@example.invalid", 1))))

    def test_a_duplicate_id_is_reported(self):
        self.assertTrue(any("duplicate id" in p for p in check(self.example().replace("id: example-archive", "id: example-snapshot", 1))))


if __name__ == "__main__":
    unittest.main()
