# Checkpoint discipline

> **Status:** Maintained reusable policy (`AW-POLICY-CHECKPOINT-DISCIPLINE-01`) · Target-project rules retain authority

**Rule.** Every row in progress is checkpointed every *N* tool calls (project-set; default 10). Also checkpoint before any
long-running command, and at every plan-step boundary. A checkpoint writes the row's
[`in_flight_state`](../templates/ROW_SCHEMA.md#in-flight-state):

- branch name
- last command
- current step against the plan
- pending decisions
- blocker, if any

**Why.** Sessions end without warning: usage limits, crashes, restarts. A checkpoint lets any session (Claude, QW or
another agent) recover a wedged row from the record alone. It doesn't have to reconstruct the row from chat history,
and it doesn't redo work that already shipped.

- **Write where it's cheap.** Prefer the coordinator's runtime store. In a Git-tracked Markdown work map, checkpoint
  only at step boundaries, so the repository doesn't fill with commits.
- **A checkpoint is evidence, not approval.** It never changes scope, authority or merge gates.
- **On resume, verify before trusting.** Re-read the branch and the PR state. If the record and reality disagree,
  reality wins and the record is corrected.

**Canonical example.** A session ends mid-way through `verify:all`. The next session reads `step 5/8 · last: npm run
verify:all · pending: none`, sees no results on the branch, and re-runs only that step.

**Entry-gate impact.** A row may not enter `In Progress` without an initial `in_flight_state`.
