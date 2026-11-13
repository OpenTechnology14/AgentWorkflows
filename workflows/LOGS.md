# Four project logs

> **Status:** Maintained reusable policy (`AW-POLICY-LOGS-04`) · Target-project rules retain authority

**Rule.** Every project keeps four plain Markdown logs. Whichever agent session does the work appends to them.

| Log | Path | Holds | Shape |
|---|---|---|---|
| `CHANGELOG.md` | repository root | user-visible changes by pull request, short, in user language, newest first | plain Markdown list |
| `docs/TECHNICAL_NOTES.md` | `docs/` | technical detail by pull request: what, why, trade-offs, migration notes | plain Markdown list |
| `docs/BUGS.md` | `docs/` | bugs noticed while coding, not only reported ones; zero ceremony: any coding session can append without a formal bug-report process | table with columns: ID, Severity, Found in PR, Status, Note |
| `docs/POTENTIAL_GAPS.md` | `docs/` | things flagged "this might be a gap" during work, before they are filed as proposals | table with columns: ID, Where noticed, PR, Hypothesis, Next step |

Defaults, which a project may replace and which stay provisional until the owner answers three open questions (the root-plus-`docs/` layout versus one `logs/` folder; the `BUG-nnn` and `GAP-nnn` IDs with a three-level severity; whether `Logs: none.` is required, recorded as `AW-D06` to `AW-D08` in the library repository's proposal record): the layout, the `Logs: none.` line, IDs `BUG-001` and `GAP-001` counting up; severity `high | medium | low`; status `open | fixed | wont-fix | promoted`. The bugs log is not the project's bug tracker and not the [bug workflow](BUGS.md): it is the quick note a session leaves when it spots something, so nothing noticed is lost. Promote an entry to a registered row when its severity is high, or when it is still open after the PR that found it merges; a quick note never replaces triage. The technical notes are kept apart from the changelog so the changelog stays readable.

**IDs and PR numbers.** Take the next free number when you write the entry. If two branches collide, the later one renumbers its entry and its references at merge. Before the PR exists, write `this PR` in the PR column and replace it with the number once the PR is opened.

**Per-row registration.** Each pull request already names its work row in its body. The logs cite the PR; the row's evidence cell lists the log entry IDs it created (for example `BUG-004, GAP-002`). A bug or gap that grows into work is promoted by registering a row, and the entry records it (`Status: promoted → <row ID>` for a bug, `Next step: registered as <row ID>` for a gap). Nothing in a log approves work.

**Entry gate.** Every pull request body closes with one line pointing at the logs it touched. Grammar: `Logs:`, then the log names separated by commas, each optionally followed by its entry IDs in parentheses, separated by commas:
`Logs: CHANGELOG, TECHNICAL_NOTES, BUGS (BUG-004, BUG-005), POTENTIAL_GAPS (GAP-002)`. If it touched none: `Logs: none.`

**Reporting.** When a session reports back to the orchestrator, its summary is bullet status plus new decisions only: what is done, what is blocked, and each new decision with its `**Question:**` line. Evidence still appears, one line each: what was verified and the result, and any blocker. The detail behind it stays in the logs and is linked, not pasted. The orchestrator reports to the owner the same way.

**Starter content.** Create a missing log with a title and a one-sentence description, then: `docs/BUGS.md` gets the table header `| ID | Severity | Found in PR | Status | Note |`; `docs/POTENTIAL_GAPS.md` gets `| ID | Where noticed | PR | Hypothesis | Next step |`; `CHANGELOG.md` gets an `Unreleased` heading; `docs/TECHNICAL_NOTES.md` takes one entry per PR with What, Why, Trade-offs and Migration notes. The full empty templates are in `templates/project-log-starter/` in the library repository.

**Why.** Detail that lives in chat is lost when the session ends, and a report padded with it hides the decisions the owner must make. Four small logs keep detail findable, and a short report keeps decisions visible.

**Canonical example.** A session notices a flaky retry while fixing an export job, appends `BUG-007`, ends its PR body with `Logs: CHANGELOG, TECHNICAL_NOTES, BUGS (BUG-007)`, and reports in three bullets and one decision.

**Entry-gate impact.** A pull request may not merge without its `Logs:` line. This library supplies the rule; the project's pull request template, reviewer or checks apply it. Missing logs are created from the starter and an existing log is never overwritten.
