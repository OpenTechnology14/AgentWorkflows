"""The two-tier decision-gate policy (AW-POLICY-DECISIONS-05, third shape 2026-11-17) reaches the workflow, templates, reviewer
duty, indexes and manifest, and the library's own gate records follow the shape the policy defines.

Tier 1 is `**Question:** <plain question?> **Suggested:** <one to three words>`; tier 2 is the section `Reasoning for <ID>`.

The checker below is a small reference for that shape. A project's index generator applies the same rules to its own gates; this
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
QUESTION_WORDS, SUGGESTED_WORDS = 25, 3
GATE_LINE = re.compile(r"\*\*Question:\*\*\s*(?P<q>.*?\?)\s*\*\*Suggested:\*\*\s*(?P<s>.*)$", re.S)
IDENTIFIER = re.compile(r"\b[A-Z][A-Z0-9]{0,7}-[A-Z]?\d+[A-Za-z]?\b")
NOT_AN_ID = {"GPT", "UTF", "ISO", "SHA", "AES", "RSA", "TLS", "SSL", "HTTP", "H", "MD", "USB", "MP"}


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def plain(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"\*\*|__|`", "", re.sub(r"\[([^\]\n]*)\]\([^)\n]*\)", r"\1", text))).strip()


def words(text: str) -> list:
    return re.findall(r"[\w$%][\w$%.'/-]*", plain(text))


def thin(text: str, figure_ok: bool = False) -> bool:
    """True when a labelled line is not an answer: empty, one word, a placeholder, or None/Unknown without a reason. A single
    figure such as $0 is an answer only where a figure is asked for (money, effort)."""
    lead = re.match(r"^(none|unknown)\b\s*[—–:,.-]*\s*(.*)$", plain(text), re.I | re.S)
    if lead:
        return len(words(lead.group(2))) < 2
    return "[[" in text or (len(words(text)) < 2 and not (figure_ok and re.search(r"\d", text)))


def labelled(lines):
    parts, current, fenced = [], None, False
    for line in lines:
        if re.match(r"^\s*```", line):
            fenced, current = not fenced, None
            continue
        found = None if fenced else re.match(r"^\s*(?:[-*+]\s+)?\*\*([^*\n]+?):\*\*[ \t]*(.*)$", line)
        if found:
            current = [found.group(1).strip().lower(), found.group(2).strip()]
            parts.append(current)
        elif current and not fenced and line.strip() and line[0] in " \t" and not re.match(r"^\s*[-*+]\s", line) and not line.lstrip().startswith("|"):
            current[1] += " " + line.strip()
        else:
            current = None
    return parts


def ordered(parts, wanted, figures=()):
    """Problems with the wanted labels: each must follow the one before and hold an answer (Downstream impact may be empty)."""
    problems, at = [], 0
    for label in wanted:
        index = next((i for i in range(at, len(parts)) if parts[i][0] == label.lower()), None)
        if index is None:
            problems.append(f"{label} is missing or out of order")
            continue
        at = index + 1
        if label != "Downstream impact" and thin(parts[index][1], label in figures):
            problems.append(f"{label} is not an answer")
    return problems


def section(text: str, gate: str):
    """The body of `Reasoning for <gate>` outside fenced code and comments; the first heading with the anchor decides."""
    lines, fenced, heads = re.sub(r"<!--.*?-->", "", text, flags=re.S).split("\n"), False, []
    for i, line in enumerate(lines):
        if re.match(r"^\s*```", line):
            fenced = not fenced
        elif not fenced and re.match(r"^#{1,6}\s", line):
            heads.append((i, len(line) - len(line.lstrip("#")), line.lstrip("#").strip()))
    anchor = re.sub(r"[^\w\s-]", "", f"reasoning for {gate}".lower()).replace(" ", "-")
    for n, (i, level, title) in enumerate(heads):
        if re.sub(r"[^\w\s-]", "", title.lower()).replace(" ", "-") != anchor:
            continue
        if title.lower() != f"reasoning for {gate}".lower():
            return None
        return lines[i + 1:next((j for j, deeper, _ in heads[n + 1:] if deeper <= level), len(lines))]
    return None


def simple_problems(cell: str):
    """Tier 1: `**Question:** ...? **Suggested:** ...`. Returns (problems, the suggested words)."""
    found = GATE_LINE.search(re.sub(r"<!--.*?-->", "", cell, flags=re.S))
    if not found:
        return ["the cell has no '**Question:** ...? **Suggested:** ...' line"], ""
    question, suggested, problems = found.group("q").strip(), found.group("s").strip().rstrip(".").strip(), []
    if question.count("?") != 1 or not (question[:1].isupper() or re.match(r"[a-z]+[A-Z]", question)) or len(question.split()) > QUESTION_WORDS:
        problems.append("the question is not one capitalised sentence of at most 25 words ending in a question mark")
    if not 1 <= len(words(suggested)) <= SUGGESTED_WORDS or re.search(r"[?|`\[\],;:]|\*\*|https?://", suggested):
        problems.append("the suggested answer is not one to three plain words")
    flat = plain(question + " " + suggested)
    if "`" in question or "|" in question or "](" in question or "http" in question or any(m.group(0).split("-")[0] not in NOT_AN_ID for m in IDENTIFIER.finditer(flat)) or re.search(r"\.md\b", flat):
        problems.append("the line is not in plain words")
    return problems, suggested


def mark_in(text: str) -> str:
    return "Suggested" if re.search(r"\(Suggested\)\s*$", text.strip()) else ""


def name_of(title: str) -> str:
    return re.sub(r"\s*\(Suggested\)\s*$", "", title.split(":", 1)[1]).strip()


def resolve(suggested: str, options):
    """The letters of the options the suggested words name: by `Option <letter>` or by the option's exact name."""
    wanted = suggested.strip().rstrip(".").lower()
    return sorted({letter for letter, name in options if wanted == f"option {letter}".lower() or wanted == name.lower()})


def reasoning_problems(lines, suggested, author_required=False):
    problems, pre, blocks, fenced = [], [], [], False
    for line in lines:
        fenced ^= bool(re.match(r"^\s*```", line))
        heading = None if fenced else re.match(r"^#{1,6}\s+(.*?)\s*$", line)
        (blocks.append((heading.group(1), [])) if heading else (blocks[-1][1] if blocks else pre).append(line))
    context = labelled(pre)
    problems += ordered(context, TOP_LINES)
    if author_required and not re.search(r"\bauthor", next((text for label, text in context if label == "context"), ""), re.I):
        problems.append("Context must say the source records no recommendation and the suggestion is the author's")
    options = [(m.group(1), title, body) for title, body in blocks for m in [re.match(r"Option ([A-D]):\s*\S", title)] if m]
    letters = [letter for letter, _, _ in options]
    if letters not in (list("AB"), list("ABC"), list("ABCD")):
        problems.append("the Option headings must run from A without gaps, two to four of them")
    for letter, title, _ in options:
        if not 1 <= len(words(name_of(title))) <= 3:
            problems.append(f"Option {letter}'s name is not one to three words")
    named = resolve(suggested, [(letter, name_of(title)) for letter, title, _ in options])
    if len(named) != 1:
        problems.append(f"the suggested words '{suggested}' must name exactly one option, by 'Option <letter>' or by its name")
    for letter, title, body in options:
        if mark_in(title) != ("Suggested" if [letter] == named else ""):
            problems.append(f"only the suggested option's heading carries (Suggested); Option {letter} is wrong")
        problems += [f"Option {letter}: {p}" for p in ordered(labelled(body), OPTION_LINES, figures=("Money", "Effort"))]
    tail_at = next((i for i, (title, _) in enumerate(blocks) if title.lower().startswith("trade-offs")), None)
    if tail_at is None:
        return problems + ["the Trade-offs sub-heading is missing"]
    tail = [line for _, body in blocks[tail_at:] for line in body]
    table = next(([tail[i], *tail[i + 2:]] for i in range(len(tail) - 1) if tail[i].startswith("|") and re.match(r"^\|[\s:|-]+\|\s*$", tail[i + 1])), None)
    if table is None:
        problems.append("Trade-offs has no table")
    else:
        rows = [[c.strip() for c in line.strip().strip("|").split("|")] for line in table if line.startswith("|")]
        if [(re.match(r"[A-D]", c) or [""])[0] for c in rows[0][1:]] != letters:
            problems.append("the Trade-offs columns do not match the options")
        elif [mark_in(c) for c in rows[0][1:]] != ["Suggested" if [letter] == named else "" for letter in letters]:
            problems.append("only the suggested option's column carries (Suggested)")
        if len(rows) < 3 or any(len(r) != len(rows[0]) or not all(re.search(r"\w", plain(c)) for c in r) for r in rows):
            problems.append("Trade-offs needs two axes, every cell filled")
    return problems + ordered(labelled(tail), TAIL_LINES)


def gate_rows(text: str):
    return [line for line in text.split("\n") if re.match(r"^\| `AW-D\d+` \|", line)]


class DecisionGatePolicy(unittest.TestCase):
    def test_workflow_defines_both_tiers_the_limits_and_the_parts_in_order(self):
        text = read("workflows/DECISIONS.md")
        self.assertIn("AW-POLICY-DECISIONS-05", text)
        for phrase in ("**Question:**", "**Suggested:**", "one to three words", "at most 25 words", "Nothing else", "Nothing follows it but an optional full stop",
                       "names exactly one option", "by letter (`Option B`) or by that option's name", "Never invent a figure", "Unknown —", "None —",
                       "decision gate template", "never seen the project",
                       "at least two words", "In Money and Effort a single figure such as `$0` or `$40 a month` is enough",
                       "the Context line says so", "so the row carries no pointer", "carries `(Suggested)` at the end of its heading",
                       "two to four options", "the Suggested words name that recommendation"):
            self.assertIn(phrase, text, phrase)
        order = [text.index(f"**{part}**") for part in ("Context", "Prerequisites", "Trade-offs", "Downstream impact", "Cost of deferring", "Worst case")]
        self.assertEqual(order, sorted(order))
        order = [text.index(f"| **{line}** |") for line in OPTION_LINES]
        self.assertEqual(order, sorted(order))
        for heading in ("## Tier 1: the simple answer", "## Tier 2: the full reasoning", "## Review"):
            self.assertIn(heading, text)
        for retired in ("450", "(Recommended)", "re-lettered", "Reasoning: ["):
            self.assertNotIn(retired, text, f"{retired!r} belongs to the second shape")

    def test_the_policy_names_the_four_review_checks(self):
        review = read("workflows/DECISIONS.md").split("## Review", 1)[1].split("## ", 1)[0]
        for phrase in ("never seen the project", "real, distinct choice", "complete and honest", "two tiers agree", "not presented to the owner",
                       "the Context line says it is the author's"):
            self.assertIn(phrase, review, phrase)

    def test_the_canonical_example_passes_the_checks_it_describes(self):
        example = re.search(r"```markdown\n(.*?)```", read("workflows/DECISIONS.md"), re.S).group(1)
        line, body = example.split("\n\n", 1)
        problems, suggested = simple_problems(line)
        self.assertEqual(problems, [])
        self.assertEqual(suggested, "Yes")
        self.assertEqual(reasoning_problems(section("# x\n\n" + body, "D-12"), suggested), [])

    def test_the_gate_template_has_both_tiers_with_every_part_and_option_pre_structured(self):
        text = read("templates/DECISION_GATE.md")
        self.assertIn("## Tier 1: the simple answer", text)
        self.assertIn("## Tier 2: the full reasoning", text)
        self.assertIn("**Question:** [[", text)
        self.assertIn("**Suggested:** [[one to three words]]", text)
        self.assertIn("Nothing else goes in it: no options, no pointer, no explanation", text)
        self.assertIn("Add `(Suggested)` to the heading of the option the suggested words name, and to its column in the Trade-offs table", text)
        body = text.split("## Tier 2: the full reasoning", 1)[1]
        for letter in "ABC":
            self.assertIn(f"#### Option {letter}:", body)
        for line in OPTION_LINES:
            self.assertEqual(body.count(f"- **{line}:**"), 3, line)
        for line in TOP_LINES + TAIL_LINES:
            self.assertIn(f"**{line}:**", body, line)
        self.assertIn("| Axis | A | B | C |", body)
        self.assertGreater(text.count("[["), 40, "every blank is a placeholder, so an unfilled template is rejected by the checks")

    def test_an_unfilled_template_fails_the_checks(self):
        text = read("templates/DECISION_GATE.md")
        body = text.split("### Reasoning for", 1)[1]
        problems = reasoning_problems(section("# x\n\n### Reasoning for" + body, "[[Gate ID]]"), "[[one to three words]]")
        self.assertTrue(problems)
        self.assertTrue(any("not an answer" in problem for problem in problems))

    def test_the_other_templates_point_at_the_gate_template_and_the_new_shape(self):
        proposal, question = read("templates/PROPOSAL.md"), read("templates/QUESTION.md")
        self.assertIn("(DECISION_GATE.md)", proposal)
        for phrase in ("Tier 1", "Tier 2", "**Suggested:** one to three words", "Nothing else", "Context, Prerequisites", "what it is, unlocks, blocks, risks, effort, money",
                       "a trade-offs table", "the worst case if the suggested option is wrong", "two to four options"):
            self.assertIn(phrase, proposal, phrase)
        self.assertIn("(DECISION_GATE.md)", question)
        self.assertIn("- Suggested: one to three words", question)
        self.assertNotIn("(Recommended)", question + proposal)
        self.assertIn("Option chosen (letter)", read("templates/DECISION.md"))
        self.assertIn("Reasoning it was answered against", read("templates/DECISION.md"))
        self.assertIn("Decision gates added or changed", read("templates/REVIEW.md"))

    def test_the_reviewer_duty_is_in_the_drive_and_review_workflow(self):
        text = read("workflows/DRIVE_REVIEW.md")
        self.assertIn("(DECISIONS.md#review)", text)
        self.assertIn("reads the question and the suggested answer cold", text)
        self.assertIn("records that they did", text)

    def test_manifest_and_indexes_list_the_workflow_and_the_template(self):
        manifest = json.loads(read("packaging/manifest.json"))
        self.assertIn("workflows/DECISIONS.md", manifest["references"])
        self.assertIn("templates/DECISION_GATE.md", manifest["references"])
        self.assertEqual(manifest["version"], "0.5.0")
        self.assertIn("(DECISIONS.md)", read("workflows/README.md"))
        self.assertIn("workflows/DECISIONS.md", read("packaging/ENTRYPOINT.md"))
        self.assertIn("(DECISION_GATE.md)", read("templates/README.md"))

    def test_the_proposal_record_follows_the_format_it_defines(self):
        text = read("docs/proposals/DECISION_GATES_TWO_TIERS.md")
        rows = gate_rows(text)
        self.assertEqual(len(rows), 4, "AW-D09 to AW-D12")
        for row in rows:
            cell = row.split("|")[2]
            gate = row.split("|")[1].strip(" `")
            problems, suggested = simple_problems(cell)
            self.assertEqual(problems, [], gate)
            body = section(text, gate)
            self.assertIsNotNone(body, gate)
            self.assertEqual(reasoning_problems(body, suggested), [], gate)
        for retired in ("450 characters", "(Recommended)", "Reasoning: ["):
            self.assertNotIn(retired, text.split("## Where the rule meets earlier shapes", 1)[1].split("## Decision gates", 1)[1], retired)


class ReferenceCheckerTests(unittest.TestCase):
    """The reference checker above has to reject what the policy says it rejects, or the tests above prove nothing."""

    GOOD = "**Question:** Ship it now? **Suggested:** Yes"

    def test_the_simple_line_rules(self):
        self.assertEqual(simple_problems(self.GOOD), ([], "Yes"))
        self.assertEqual(simple_problems(self.GOOD + ".")[0], [])
        self.assertEqual(simple_problems("Why. " + self.GOOD)[0], [])
        for words3 in ("Keep private", "90-day re-check", "Option B", "Force-push", "Keep it private"):
            self.assertEqual(simple_problems(f"**Question:** Ship it now? **Suggested:** {words3}")[0], [], words3)
        for bad in (self.GOOD + " and then some more", self.GOOD.replace("Yes", "Keep it all private"), self.GOOD.replace("Yes", ""), "**Question:** Ship it now?",
                    "**Question:** Ship it now? A (Recommended): yes. B: no.", self.GOOD.replace("Ship it now?", "Ship it now"), self.GOOD.replace("Ship it now?", "Ship P-12 now?"),
                    self.GOOD.replace("Ship it now?", "Open `make` now?"), self.GOOD.replace("Ship it now?", " ".join(["go"] * 26) + "?"),
                    self.GOOD.replace("Yes", "Yes, because"), self.GOOD.replace("Yes", "Yes?"), self.GOOD.replace("Yes", "[Yes](x.md)"), self.GOOD.replace("Ship it now?", "Ship it? Now?")):
            self.assertNotEqual(simple_problems(bad)[0], [], bad[:70])

    def options_doc(self, suggested="Keep private", names=("Keep private", "Go public"), marks=("Suggested", "")):
        out = ["", "- **Context:** Why now.", "- **Prerequisites:** None — nothing else is needed.", ""]
        for letter, name, mark in zip("ABCD", names, marks):
            out += [f"#### Option {letter}: {name}" + (f" ({mark})" if mark else ""), ""]
            out += [f"- **{label}:** {'None — nothing to add here.' if label in ('Money', 'Incompatible with', 'Needs first') else 'A plain answer here.'}" for label in OPTION_LINES] + [""]
        header = " | ".join(letter + (f" ({mark})" if mark else "") for letter, mark in zip("ABCD", marks))
        out += ["#### Trade-offs", "", f"| Axis | {header} |", "|---|" + "---|" * len(names), "| Cost | " + " | ".join("Low" for _ in names) + " |", "| Speed | " + " | ".join("Fast" for _ in names) + " |", "",
                "- **Downstream impact:**", "  - **Changes:** One file.", "  - **Unblocks:** The release.", "- **Cost of deferring:** Nothing waits.", "- **Worst case:** An afternoon of rework.", ""]
        return out

    def test_the_suggested_words_must_name_exactly_one_option(self):
        self.assertEqual(reasoning_problems(self.options_doc(), "Keep private"), [])
        self.assertEqual(reasoning_problems(self.options_doc(), "keep private."), [])
        self.assertEqual(reasoning_problems(self.options_doc(), "Option A"), [])
        self.assertEqual(reasoning_problems(self.options_doc(marks=("", "Suggested")), "Option B"), [])
        self.assertEqual(reasoning_problems(self.options_doc(marks=("", "Suggested")), "Go public"), [])
        for wrong in ("Keep it", "Option C", "Yes", "B"):
            self.assertTrue(any("must name exactly one option" in p for p in reasoning_problems(self.options_doc(), wrong)), wrong)
        clash = self.options_doc(names=("Option B", "Go public"))
        self.assertTrue(any("must name exactly one option" in p for p in reasoning_problems(clash, "Option B")))

    def test_only_the_suggested_option_carries_the_mark_in_its_heading_and_its_column(self):
        self.assertTrue(any("only the suggested option's heading" in p for p in reasoning_problems(self.options_doc(marks=("", "")), "Keep private")))
        self.assertTrue(any("only the suggested option's heading" in p for p in reasoning_problems(self.options_doc(marks=("Suggested", "Suggested")), "Keep private")))
        self.assertTrue(any("only the suggested option's heading" in p for p in reasoning_problems(self.options_doc(marks=("", "Suggested")), "Keep private")))
        doc = self.options_doc()
        broken = [line.replace("A (Suggested)", "A") for line in doc]
        self.assertTrue(any("column carries (Suggested)" in p for p in reasoning_problems(broken, "Keep private")))

    def test_option_names_and_letters(self):
        self.assertTrue(any("not one to three words" in p for p in reasoning_problems(self.options_doc(names=("Keep the repository private for now", "Go public")), "Option A")))
        self.assertTrue(any("run from A without gaps" in p for p in reasoning_problems([line.replace("Option B:", "Option C:") for line in self.options_doc()], "Keep private")))
        three = self.options_doc(names=("Keep private", "Go public", "Wait"), marks=("Suggested", "", ""))
        self.assertEqual(reasoning_problems(three, "Keep private"), [])

    def test_the_context_names_the_author_when_the_row_records_no_default(self):
        doc = self.options_doc()
        self.assertTrue(any("author's" in p for p in reasoning_problems(doc, "Keep private", author_required=True)))
        with_author = [line.replace("Why now.", "The source records no recommendation, so the suggestion is the author's.") for line in doc]
        self.assertEqual(reasoning_problems(with_author, "Keep private", author_required=True), [])

    def test_thin_lines_are_not_answers(self):
        for thin_text in ("", "None", "n/a", "Nothing", "Unknown", "None — ok", "[[what it is]]"):
            self.assertTrue(thin(thin_text), thin_text)
        for fine in ("None — no spend at all.", "Unknown — needs a vendor quote.", "About one hour of work (estimate)."):
            self.assertFalse(thin(fine), fine)

    def test_a_single_figure_is_an_answer_only_for_money_and_effort(self):
        for figure in ("$0.", "$40/month", "3"):
            self.assertTrue(thin(figure), figure)
            self.assertFalse(thin(figure, figure_ok=True), figure)
        self.assertEqual(ordered([("risks", "3")], ["Risks"]), ["Risks is not an answer"])
        self.assertEqual(ordered([("money", "$0.")], ["Money"], figures=("Money",)), [])
        self.assertEqual(ordered([("money", "$0.")], ["Money"]), ["Money is not an answer"])

    def test_a_section_is_found_by_its_exact_title_and_the_first_heading_decides(self):
        doc = "# x\n\n### Reasoning for D-1.2\n\n- one\n\n### Reasoning for D-12\n\n- two\n"
        self.assertEqual(section(doc, "D-1.2"), ["", "- one", ""])
        self.assertIsNone(section(doc, "D-12"), "GitHub gives the second heading the anchor -1, so a link to it opens the first section")
        self.assertIsNone(section("<!--\n### Reasoning for X\n-->\n", "X"))
        self.assertIsNone(section("```\n### Reasoning for X\n```\n", "X"))


if __name__ == "__main__":
    unittest.main()
