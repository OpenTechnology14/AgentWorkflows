"""The two-tier decision-gate policy (AW-POLICY-DECISIONS-05, tightened 2026-11-16) reaches the workflow, templates, reviewer
duty, indexes and manifest, and the library's own gate records follow the shape the policy defines.

The checker below is a small reference for the shape. A project's index generator applies the same rules to its own gates; this
one only has to prove that the policy, its canonical example, its template and this library's own records agree with each other.
"""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OPTION_LINES = ["What it is", "Unlocks", "Blocks", "Risks", "Effort", "Money", "Incompatible with", "Needs first"]
TOP_LINES = ["Context", "Prerequisites"]
TAIL_LINES = ["Downstream impact", "Changes", "Unblocks", "Cost of deferring", "Worst case"]
LINE_LIMIT, QUESTION_WORDS = 450, 25


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\*\*|__|`", "", re.sub(r"\[([^\]\n]*)\]\([^)\n]*\)", r"\1", text))).strip()


def words(text: str) -> list:
    return re.findall(r"[\w$%][\w$%.'/-]*", plain(text))


def thin(text: str) -> bool:
    """True when a labelled line is not an answer: empty, one word, a placeholder, or None/Unknown without a reason."""
    lead = re.match(r"^(none|unknown)\b\s*[—–:,.-]*\s*(.*)$", plain(text), re.I | re.S)
    if lead:
        return len(words(lead.group(2))) < 2
    return len(words(text)) < 2 or "[[" in text


def labelled(lines):
    parts, current = [], None
    for line in lines:
        found = re.match(r"^\s*(?:[-*+]\s+)?\*\*([^*\n]+?):\*\*[ \t]*(.*)$", line)
        if found:
            current = [found.group(1).strip().lower(), found.group(2).strip()]
            parts.append(current)
        elif current and line.strip() and line[0] in " \t" and not re.match(r"^\s*[-*+]\s", line) and not line.lstrip().startswith("|"):
            current[1] += " " + line.strip()
        else:
            current = None
    return parts


def ordered(parts, wanted):
    """Problems with the wanted labels: each must follow the one before and hold an answer (Downstream impact may be empty)."""
    problems, at = [], 0
    for label in wanted:
        index = next((i for i in range(at, len(parts)) if parts[i][0] == label.lower()), None)
        if index is None:
            problems.append(f"{label} is missing or out of order")
            continue
        at = index + 1
        if label != "Downstream impact" and thin(parts[index][1]):
            problems.append(f"{label} is not an answer")
    return problems


def section(text: str, gate: str):
    """The body of `### Reasoning for <gate>`, outside fenced code, up to the next heading of the same or a higher level."""
    lines, fenced, heads = text.split("\n"), False, []
    for i, line in enumerate(lines):
        if re.match(r"^\s*```", line):
            fenced = not fenced
        elif not fenced and re.match(r"^#{1,6}\s", line):
            heads.append((i, len(line) - len(line.lstrip("#")), line.lstrip("#").strip()))
    for n, (i, level, title) in enumerate(heads):
        if title.lower() == f"reasoning for {gate}".lower():
            return lines[i + 1:next((j for j, deeper, _ in heads[n + 1:] if deeper <= level), len(lines))]
    return None


def reasoning_problems(lines, letters):
    problems, pre, blocks, fenced = [], [], [], False
    for line in lines:
        fenced ^= bool(re.match(r"^\s*```", line))
        heading = None if fenced else re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        (blocks.append((heading.group(1), [])) if heading else (blocks[-1][1] if blocks else pre).append(line))
    problems += ordered(labelled(pre), TOP_LINES)
    options = [(m.group(1), title, body) for title, body in blocks for m in [re.match(r"Option ([A-D])\b", title)] if m]
    if [letter for letter, _, _ in options] != letters:
        problems.append("the Option headings do not match the simple line")
    for letter, title, body in options:
        if ("Recommended" in title) != (letter == "A"):
            problems.append(f"Option {letter} must say (Recommended) only on A")
        problems += [f"Option {letter}: {p}" for p in ordered(labelled(body), OPTION_LINES)]
    tail_at = next((i for i, (title, _) in enumerate(blocks) if title.lower().startswith("trade-offs")), None)
    if tail_at is None:
        return problems + ["the Trade-offs sub-heading is missing"]
    tail = [line for _, body in blocks[tail_at:] for line in body]
    table = next(([tail[i], *tail[i + 2:]] for i in range(len(tail) - 1) if tail[i].startswith("|") and re.match(r"^\|[\s:|-]+\|\s*$", tail[i + 1])), None)
    if table is None:
        problems.append("Trade-offs has no table")
    else:
        rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in table if line.startswith("|")]
        if [c[0] for c in rows[0][1:]] != letters:
            problems.append("the Trade-offs columns do not match the options")
        elif ["Recommended" in c for c in rows[0][1:]] != [True] + [False] * (len(letters) - 1):
            problems.append("the Trade-offs header must mark A (Recommended) and no other column")
        if len(rows) < 3 or any(len(r) != len(rows[0]) or not all(r) for r in rows):
            problems.append("Trade-offs needs two axes, every cell filled")
    return problems + ordered(labelled(tail), TAIL_LINES)


def simple_problems(cell: str):
    """Tier 1: the line after **Question:** up to the pointer. Returns (problems, option letters)."""
    head = re.split(r"\bReasoning:", cell.split("**Question:**", 1)[1], maxsplit=1)[0]
    flat, problems = plain(head), []
    sentence = re.match(r"^(.*?\?)\s*(.*)$", flat, re.S)
    if not sentence or flat.count("?") != 1 or not sentence.group(1)[:1].isupper() or len(sentence.group(1).split()) > QUESTION_WORDS:
        problems.append("the question is not one capitalised sentence of at most 25 words ending in a question mark")
    if len(flat) > LINE_LIMIT:
        problems.append("the line is over 450 characters")
    if "`" in head or re.search(r"\]\(|https?://|\b[A-Z][A-Z0-9]{0,7}-[A-Z]?\d+\b|\.md\b", head):
        problems.append("the line is not in plain words")
    marks = list(re.finditer(r"(?:(?<=\s)|^)([A-Z])(?: \((Recommended)\))?:(?=\s|$)", sentence.group(2) if sentence else ""))
    letters = [m.group(1) for m in marks]
    if letters not in (["A", "B"], ["A", "B", "C"]) or [m.group(2) for m in marks] != ["Recommended"] + [None] * (len(marks) - 1):
        problems.append("the options must be A (Recommended) and B, and C only for a third choice")
    return problems, letters


def gate_rows(text: str):
    return [line for line in text.split("\n") if re.match(r"^\| `AW-D\d+` \|", line)]


class DecisionGatePolicy(unittest.TestCase):
    def test_workflow_defines_both_tiers_the_limits_and_the_parts_in_order(self):
        text = read("workflows/DECISIONS.md")
        self.assertIn("AW-POLICY-DECISIONS-05", text)
        for phrase in ("**Question:**", "`Reasoning:`", "at most 25 words", "at most 450 characters", "#reasoning-for-<gate-id>", "Never invent a figure",
                       "Unknown —", "None —", "decision gate template", "answered by someone who has never seen the project"):
            self.assertIn(phrase, text, phrase)
        order = [text.index(f"**{part}**") for part in ("Context", "Prerequisites", "Trade-offs", "Downstream impact", "Cost of deferring", "Worst case")]
        self.assertEqual(order, sorted(order))
        order = [text.index(f"| **{line}** |") for line in OPTION_LINES]
        self.assertEqual(order, sorted(order))
        for heading in ("## Tier 1: the simple answer", "## Tier 2: the full reasoning", "## Review"):
            self.assertIn(heading, text)

    def test_the_policy_names_the_four_review_checks(self):
        review = read("workflows/DECISIONS.md").split("## Review", 1)[1].split("## ", 1)[0]
        for phrase in ("never seen the project", "real, distinct choice", "complete and honest", "two tiers agree", "not presented to the owner"):
            self.assertIn(phrase, review, phrase)

    def test_the_canonical_example_passes_the_checks_it_describes(self):
        example = re.search(r"```markdown\n(.*?)```", read("workflows/DECISIONS.md"), re.S).group(1)
        line, body = example.split("\n\n", 1)
        problems, letters = simple_problems(line)
        self.assertEqual(problems, [])
        self.assertEqual(reasoning_problems(section("# x\n\n" + body, "D-12"), letters), [])
        self.assertLessEqual(len(plain(line.split("**Question:**")[1].split("Reasoning:")[0])), LINE_LIMIT)

    def test_the_gate_template_has_both_tiers_with_every_part_and_option_pre_structured(self):
        text = read("templates/DECISION_GATE.md")
        self.assertIn("## Tier 1: the simple answer", text)
        self.assertIn("## Tier 2: the full reasoning", text)
        self.assertIn("**Question:** [[", text)
        self.assertIn("A (Recommended):", text)
        self.assertIn("Reasoning: [below](#reasoning-for-[[", text)
        body = text.split("## Tier 2: the full reasoning", 1)[1]
        for letter in "ABC":
            self.assertIn(f"#### Option {letter}", body)
        for line in OPTION_LINES:
            self.assertEqual(body.count(f"- **{line}:**"), 3, line)
        for line in TOP_LINES + TAIL_LINES:
            self.assertIn(f"**{line}:**", body, line)
        self.assertIn("| Axis | A (Recommended) | B | C |", body)
        self.assertGreater(text.count("[["), 40, "every blank is a placeholder, so an unfilled template is rejected by the checks")

    def test_an_unfilled_template_fails_the_checks(self):
        text = read("templates/DECISION_GATE.md")
        body = text.split("### Reasoning for", 1)[1]
        problems = reasoning_problems(section("# x\n\n### Reasoning for" + body, "[[Gate ID]]"), ["A", "B", "C"])
        self.assertTrue(problems)
        self.assertTrue(any("not an answer" in problem for problem in problems))

    def test_the_other_templates_point_at_the_gate_template_and_the_full_reasoning(self):
        proposal, question = read("templates/PROPOSAL.md"), read("templates/QUESTION.md")
        self.assertIn("(DECISION_GATE.md)", proposal)
        for phrase in ("Tier 1", "Tier 2", "Context, Prerequisites", "what it is, unlocks, blocks, risks, effort, money", "a trade-offs table", "the worst case"):
            self.assertIn(phrase, proposal, phrase)
        self.assertIn("(DECISION_GATE.md)", question)
        self.assertIn("- A (Recommended):", question)
        self.assertIn("- Reasoning:", question)
        self.assertIn("Option chosen (letter)", read("templates/DECISION.md"))
        self.assertIn("Reasoning it was answered against", read("templates/DECISION.md"))
        self.assertIn("Decision gates added or changed", read("templates/REVIEW.md"))

    def test_the_reviewer_duty_is_in_the_drive_and_review_workflow(self):
        text = read("workflows/DRIVE_REVIEW.md")
        self.assertIn("(DECISIONS.md#review)", text)
        self.assertIn("reads the simple line cold", text)
        self.assertIn("records that they did", text)

    def test_manifest_and_indexes_list_the_workflow_and_the_template(self):
        references = json.loads(read("packaging/manifest.json"))["references"]
        self.assertIn("workflows/DECISIONS.md", references)
        self.assertIn("templates/DECISION_GATE.md", references)
        self.assertIn("(DECISIONS.md)", read("workflows/README.md"))
        self.assertIn("workflows/DECISIONS.md", read("packaging/ENTRYPOINT.md"))
        self.assertIn("(DECISION_GATE.md)", read("templates/README.md"))

    def test_the_proposal_record_follows_the_format_it_defines(self):
        text = read("docs/proposals/DECISION_GATES_TWO_TIERS.md")
        rows = gate_rows(text)
        self.assertEqual(len(rows), 3, "AW-D09, AW-D10 and AW-D11")
        for row in rows:
            cell = row.split("|")[2]
            gate = row.split("|")[1].strip(" `")
            problems, letters = simple_problems(cell)
            self.assertEqual(problems, [], gate)
            self.assertIn(f"(#reasoning-for-{gate.lower()})", cell)
            body = section(text, gate)
            self.assertIsNotNone(body, gate)
            self.assertEqual(reasoning_problems(body, letters), [], gate)


class ReferenceCheckerTests(unittest.TestCase):
    """The reference checker above has to reject what the policy says it rejects, or the tests above prove nothing."""

    GOOD = "**Question:** Ship it now? A (Recommended): yes, ship it now. B: no, hold it for a week. Reasoning: [below](#reasoning-for-d-1)"

    def test_the_simple_line_rules(self):
        self.assertEqual(simple_problems(self.GOOD)[0], [])
        for bad in (self.GOOD.replace("A (Recommended)", "A"), self.GOOD.replace("B:", "C:"), self.GOOD.replace("Ship it now?", "Ship P-12 now?"),
                    self.GOOD.replace("Ship it now?", "Ship it now"), self.GOOD.replace("yes, ship it now.", "yes, " + "x" * 450 + "."),
                    self.GOOD.replace("Ship it now?", "Open `make` now?"), self.GOOD.replace("Ship it now?", " ".join(["go"] * 26) + "?")):
            self.assertNotEqual(simple_problems(bad)[0], [], bad[:60])

    def test_thin_lines_are_not_answers(self):
        for thin_text in ("", "None", "n/a", "Nothing", "Unknown", "None — ok", "[[what it is]]"):
            self.assertTrue(thin(thin_text), thin_text)
        for fine in ("None — no spend at all.", "Unknown — needs a vendor quote.", "About one hour of work (estimate)."):
            self.assertFalse(thin(fine), fine)


if __name__ == "__main__":
    unittest.main()
