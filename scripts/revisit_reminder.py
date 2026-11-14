#!/usr/bin/env python3
"""Create and find re-check reminder rows for "keep for now, revisit later" decisions.

See modules/repo-management/MIGRATION_PLAYBOOK.md, section 11. Stdlib only. `row` prints the reminder row for an answer
(default: 90 days after it); `due` lists the reminders in a tracker file whose date has come. It never writes to the tracker.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, timedelta
from pathlib import Path

DEFAULT_DAYS = 90
ID = re.compile(r"^[A-Za-z0-9._-]+$")
ROW_ID = re.compile(r"^\|\s*\*\*([A-Za-z0-9._-]+)\*\*")
RECHECK_ON = re.compile(r"recheck_on (\d{4}-\d{2}-\d{2})")
CLOSED = ("done", "resolved", "closed", "dropped", "superseded", "withdrawn")


def due_date(answered: date, days: int = DEFAULT_DAYS) -> date:
    if days < 1:
        raise ValueError("days must be at least 1")
    return answered + timedelta(days=days)


def build(of: str, title: str, answered: date, days: int = DEFAULT_DAYS, row_id: str = "", drive: str = "<model>", review: str = "owner") -> dict:
    if not ID.match(of):
        raise ValueError("--of must be an ID such as a decision or row ID (letters, digits, . _ -)")
    if row_id and not ID.match(row_id):
        raise ValueError("--id must be letters, digits, . _ -")
    if not title.strip() or "|" in title or "\n" in title:
        raise ValueError("--title must be one line of text without a pipe")
    return {"id": row_id or f"{of}-RECHECK", "kind": "housekeeping", "of": of, "title": title.strip(), "answered": answered.isoformat(),
            "days": days, "due": due_date(answered, days).isoformat(), "drive_model": drive, "review_model": review}


def render_row(row: dict) -> str:
    interval = ("Default interval: " if row["days"] == DEFAULT_DAYS else "Interval chosen by the owner: ") + f"{row['days']} days after the answer."
    return (f"| **{row['id']}** · housekeeping → re-check {row['title']} (`{row['of']}`, answered \"keep for now, revisit later\" on {row['answered']}) "
            f"| **Scheduled {row['due']}.** On or after that date: re-read the facts with the same commands as the first report, say what changed, "
            f"and ask the same question again with a recommendation. Nothing is changed or revoked by the agent. {interval} "
            f"fields: assigned_role claude · origin owner · handoff claude_only · drive_model {row['drive_model']} · review_model {row['review_model']} · "
            f"review_state not_started · recheck_of {row['of']} · recheck_on {row['due']} · blocks [] · blocked_by [] "
            f"in_flight_state {{branch none, step 1/2 (scheduled), last_command \"none yet\", pending_blockers [due {row['due']}], "
            f"next_action \"on or after {row['due']}: re-read and re-ask\"}} "
            f"| A new answer from the owner: keep again (another reminder) or change (a normal row) |")


def due_rows(text: str, today: date) -> list[tuple[str, date]]:
    """Reminder rows (a `recheck_on` date) that are not closed and whose date is today or earlier, oldest first."""
    found = []
    for line in text.splitlines():
        match_id, match_on = ROW_ID.match(line), RECHECK_ON.search(line)
        if not (match_id and match_on):
            continue
        cells = line.strip().strip("|").split(" | ")
        state = cells[1].lstrip("* ").lower() if len(cells) > 1 else ""
        if state.startswith(CLOSED):
            continue
        on = date.fromisoformat(match_on.group(1))
        if on <= today:
            found.append((match_id.group(1), on))
    return sorted(found, key=lambda item: (item[1], item[0]))


def iso(value: str) -> date:
    try:
        return date.fromisoformat(value)
    except ValueError as error:
        raise argparse.ArgumentTypeError(f"{value!r} is not a YYYY-MM-DD date") from error


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    commands = parser.add_subparsers(dest="command", required=True)
    row = commands.add_parser("row", help="print the reminder row for a keep-for-now answer")
    row.add_argument("--of", required=True, help="ID of the decision or row that was answered")
    row.add_argument("--title", required=True, help="what is kept, in a few words, for example: the second maintainer's access")
    row.add_argument("--answered", required=True, type=iso, help="date of the answer, YYYY-MM-DD")
    row.add_argument("--days", type=int, default=DEFAULT_DAYS, help=f"re-check after this many days (default {DEFAULT_DAYS})")
    row.add_argument("--id", default="", help="ID for the new row (default: <of>-RECHECK)")
    row.add_argument("--drive", default="<model>")
    row.add_argument("--review", default="owner")
    row.add_argument("--format", choices=["row", "json"], default="row")
    due = commands.add_parser("due", help="list the reminders whose date has come")
    due.add_argument("--file", required=True, type=Path)
    due.add_argument("--today", type=iso, default=None, help="YYYY-MM-DD (default: today)")
    args = parser.parse_args(argv)
    try:
        if args.command == "row":
            built = build(args.of, args.title, args.answered, args.days, args.id, args.drive, args.review)
            print(json.dumps(built, indent=2) if args.format == "json" else render_row(built))
            return 0
        today = args.today or date.today()
        found = due_rows(args.file.read_text(encoding="utf-8"), today)
    except (ValueError, OSError) as error:
        print(f"FAIL: {error}")
        return 2
    for row_id, on in found:
        late = (today - on).days
        print(f"{row_id} is due today" if late == 0 else f"{row_id} was due {on.isoformat()} ({late} day(s) overdue)")
    print(f"{len(found)} reminder(s) due" if found else "No reminders due")
    return 0


if __name__ == "__main__":
    sys.exit(main())
