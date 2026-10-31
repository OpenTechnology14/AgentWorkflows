# One list of Kinds, a housekeeping catch-all and an entry gate

> **Status:** Owner-directed implementation · **Date:** 2026-10-31

The owner directed, in a task brief, that all agent work flow through the reporting process and that a catch-all work type absorb anything that fits no existing category. Three open questions were answered by taking the recommended defaults: the taxonomy lives in this library and projects point at it; the catch-all is named `housekeeping`; the intake Kind lists are merged into one. The answer was implicit, so the exact words are not on record and an explicit confirmation stays pending in the owner's private records.

## Evidence

The intake Kind was listed five different ways: the intake template (idea / reported bug / simple change / proposal remainder / review finding), the prompt-translation record (idea | reported bug | confirmed bug | simple change | proposal | review finding), the intake workflow (which also accepted audit or test failures and owner or operator requests), the packaged entrypoint (idea, reported bug, confirmed defect, enhancement, review finding) and the README (ideas, bugs, small changes, proposals, audits and review findings). The only "other" bucket was a bug group, for defects. Recurring work with no home included tests-only slices, wording passes over decision records, ledger cleanups, refreshes of a pinned reference and repository moves.

## Contract

- `workflows/WORK_TYPES.md` is the single source: seven Kinds (idea, bug, simple change, proposal remainder, review finding, audit finding, housekeeping), the housekeeping trigger and rules, and a map from the older wording. "Confirmed" is a bug state and "enhancement" is a simple change.
- `workflows/ENTRY_GATE.md` is "register, then start": a row, one Kind and a stated state before work begins. The project's facilitator persists the row; a worker proposes it.
- The five places that listed Kinds now carry the same list. `tests/test_work_types.py` fails when one diverges or an unlisted file starts its own list.
- Packaging: both workflows join the manifest, and the package version is 0.3.0.

## Consequences and rollout

Every project record that pins this library changes its source hashes. Update the library first, rebuild, then refresh each project's record and its generated check together. A pending library PR stays a visible dependency until it reaches main. Rollback: revert this change, restore the previous manifest version and refresh the references. Private work views keep their rows; only the Kind vocabulary changes.

## Not decided here

Whether to split a Kind later. When three housekeeping items share a shape, propose a new Kind in this library.
