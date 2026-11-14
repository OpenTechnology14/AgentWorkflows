"""The two-tier decision-gate policy (AW-POLICY-DECISIONS-05) reaches the workflow, templates, indexes and manifest."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HEADINGS = ["Context", "Trade-offs", "Downstream impact", "Cost of deferring"]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


class DecisionGatePolicy(unittest.TestCase):
    def test_workflow_defines_both_tiers_and_the_four_headings_in_order(self):
        text = read("workflows/DECISIONS.md")
        self.assertIn("AW-POLICY-DECISIONS-05", text)
        self.assertIn("**Question:**", text)
        self.assertIn("`Reasoning:`", text)
        self.assertIn("- **Context:** why now", text)
        self.assertIn("#reasoning-for-<gate-id>", text)
        self.assertNotIn("four headings", text)
        positions = [text.index(f"**{heading}**") for heading in HEADINGS]
        self.assertEqual(positions, sorted(positions))

    def test_proposal_template_carries_a_reasoning_block_with_the_four_headings(self):
        text = read("templates/PROPOSAL.md")
        self.assertIn("### Reasoning for", text)
        for heading in HEADINGS:
            self.assertIn(f"- **{heading}:**", text)

    def test_question_and_decision_templates_point_at_the_reasoning(self):
        self.assertIn("- Reasoning:", read("templates/QUESTION.md"))
        self.assertIn("Reasoning it was answered against", read("templates/DECISION.md"))

    def test_manifest_and_indexes_list_the_workflow(self):
        self.assertIn("workflows/DECISIONS.md", json.loads(read("packaging/manifest.json"))["references"])
        self.assertIn("(DECISIONS.md)", read("workflows/README.md"))
        self.assertIn("workflows/DECISIONS.md", read("packaging/ENTRYPOINT.md"))

    def test_the_proposal_record_uses_the_format_it_defines(self):
        text = read("docs/proposals/DECISION_GATES_TWO_TIERS.md")
        section = text.split("### Reasoning for AW-D09", 1)[1].split("\n## ", 1)[0]
        for heading in HEADINGS:
            self.assertRegex(section, rf"- \*\*{re.escape(heading)}:\*\* \S")
        self.assertIn("(#reasoning-for-aw-d09)", text)


if __name__ == "__main__":
    unittest.main()
