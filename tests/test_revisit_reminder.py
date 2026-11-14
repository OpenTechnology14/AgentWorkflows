"""The keep-for-now pattern: the reminder row is built correctly, due dates are computed, and due reminders are found."""
import contextlib
import io
import json
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import revisit_reminder as rr  # noqa: E402


def run(*argv):
    out = io.StringIO()
    with contextlib.redirect_stdout(out):
        code = rr.main(list(argv))
    return code, out.getvalue().strip()


class DueDate(unittest.TestCase):
    def test_the_default_is_ninety_days(self):
        self.assertEqual(rr.due_date(date(2026, 11, 14)), date(2027, 2, 12))

    def test_a_leap_year_counts_its_extra_day(self):
        self.assertEqual(rr.due_date(date(2027, 12, 1)), date(2028, 2, 29))

    def test_another_interval_is_honoured_and_zero_is_refused(self):
        self.assertEqual(rr.due_date(date(2026, 3, 1), 30), date(2026, 3, 31))
        with self.assertRaises(ValueError):
            rr.due_date(date(2026, 3, 1), 0)


class Row(unittest.TestCase):
    def built(self, **extra):
        return rr.build("D-7", "the second maintainer's access", date(2026, 3, 1), **extra)

    def test_the_row_has_three_cells_the_schedule_and_the_links_back(self):
        row = rr.render_row(self.built())
        self.assertEqual(len(row[2:-2].split(" | ")), 3)
        for expected in ("**D-7-RECHECK**", "housekeeping → re-check the second maintainer's access", "**Scheduled 2026-05-30.**",
                         "recheck_of D-7", "recheck_on 2026-05-30", "review_state not_started", "Default interval: 90 days"):
            self.assertIn(expected, row)

    def test_another_interval_and_id_are_stated(self):
        row = rr.render_row(self.built(days=30, row_id="WM-X-RECHECK-01"))
        self.assertIn("**WM-X-RECHECK-01**", row)
        self.assertIn("Interval chosen by the owner: 30 days", row)
        self.assertIn("recheck_on 2026-03-31", row)

    def test_a_pipe_a_blank_title_or_a_bad_id_is_refused(self):
        for bad in ({"of": "D 7", "title": "x"}, {"of": "D-7", "title": "a | b"}, {"of": "D-7", "title": "  "}):
            with self.assertRaises(ValueError):
                rr.build(bad["of"], bad["title"], date(2026, 3, 1))
        with self.assertRaises(ValueError):
            rr.build("D-7", "x", date(2026, 3, 1), row_id="bad id")

    def test_the_command_prints_the_row_or_json_and_rejects_a_bad_date(self):
        code, text = run("row", "--of", "D-7", "--title", "the second maintainer's access", "--answered", "2026-03-01")
        self.assertEqual(code, 0)
        self.assertTrue(text.startswith("| **D-7-RECHECK**"))
        code, text = run("row", "--of", "D-7", "--title", "x", "--answered", "2026-03-01", "--format", "json")
        self.assertEqual(json.loads(text)["due"], "2026-05-30")
        code, text = run("row", "--of", "D-7", "--title", "a | b", "--answered", "2026-03-01")
        self.assertEqual(code, 2)
        with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
            rr.main(["row", "--of", "D-7", "--title", "x", "--answered", "01/03/2026"])


class Due(unittest.TestCase):
    def table(self):
        keep = rr.render_row(rr.build("D-7", "access", date(2026, 3, 1)))
        later = rr.render_row(rr.build("D-8", "mirror", date(2026, 4, 1)))
        closed = rr.render_row(rr.build("D-9", "drift", date(2026, 1, 1))).replace("**Scheduled 2026-04-01.**", "**Done 2026-05-01.**")
        plain = "| **WM-1** · simple change → something | **Done 2026-01-01.** nothing | none |"
        return "\n".join(["# Rows", "", "| Row | State | Next |", "|---|---|---|", keep, later, closed, plain])

    def test_a_reminder_is_due_on_its_date_and_after_but_not_before(self):
        text = self.table()
        self.assertEqual(rr.due_rows(text, date(2026, 5, 29)), [])
        self.assertEqual(rr.due_rows(text, date(2026, 5, 30)), [("D-7-RECHECK", date(2026, 5, 30))])
        self.assertEqual([r for r, _ in rr.due_rows(text, date(2026, 9, 1))], ["D-7-RECHECK", "D-8-RECHECK"])

    def test_closed_rows_and_rows_without_a_recheck_date_are_ignored(self):
        self.assertNotIn("D-9-RECHECK", [r for r, _ in rr.due_rows(self.table(), date(2030, 1, 1))])
        self.assertNotIn("WM-1", [r for r, _ in rr.due_rows(self.table(), date(2030, 1, 1))])

    def test_the_command_reports_overdue_and_none(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "tracker.md"
            path.write_text(self.table(), encoding="utf-8")
            code, text = run("due", "--file", str(path), "--today", "2026-06-02")
            self.assertEqual(code, 0)
            self.assertIn("D-7-RECHECK was due 2026-05-30 (3 day(s) overdue)", text)
            self.assertIn("1 reminder(s) due", text)
            self.assertEqual(run("due", "--file", str(path), "--today", "2026-01-01")[1], "No reminders due")
            self.assertEqual(run("due", "--file", str(Path(tmp) / "missing.md"), "--today", "2026-01-01")[0], 2)


if __name__ == "__main__":
    unittest.main()
