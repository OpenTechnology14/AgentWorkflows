# Work row schema additions

> **Status:** Agent-filled template · Extends a project's existing work row; the Kind vocabulary, IDs and states stay the project's own

Add these fields to each tracked work row. In a Markdown table, keep them in a compact `fields:` block in the state cell
or in a linked row file. A runtime store holds them as structured data.

```text
assigned_role: claude | codex | qw | owner
origin:        claude | codex | chatgpt | owner
handoff:       claude_only | claude_ok          # see workflows/HANDOFF_ON_LIMIT.md
drive_model:   <exact model or route ID>
review_model:  <exact model or route ID>
review_state:  not_started | in_review | approved | rejected
blocks:        [<row-id>, ...]
blocked_by:    [<row-id>, ...]
in_flight_state:                              # mandatory while In Progress
  branch:           <branch name>
  step:             <current step> / <plan steps>
  last_command:     <last command run>
  pending_blockers: [<question or blocker>, ...]
  next_action:      <one line>
```

## Role and origin

`AW-SCHEMA-ROLE-ORIGIN-01`. `assigned_role` is who is expected to do the work now. `origin` is who created the row.
Without both, a later audit can't tell an owner request from an agent's own finding, or attribute work handed between
sessions and tools.

## Drive and review fields

`AW-SCHEMA-DRIVE-REVIEW-01`. These are set at registration ([drive/review](../workflows/DRIVE_REVIEW.md),
[model fit](../workflows/MODEL_FIT.md)). Only the named reviewer changes `review_state`. `approved` makes a PR eligible
to merge; it doesn't grant merge authority.

## Dependencies

`AW-SCHEMA-DEPENDENCIES-01`. Use `blocks` / `blocked_by` with row IDs instead of narrative references, and keep both
sides in step. Resolving a row **notifies** its dependents that they are unblocked. It doesn't start them; starting
still follows the project's approval rules.

## In-flight state

`AW-SCHEMA-INFLIGHT-01`. Required for any row in `In Progress` ([checkpoints](../workflows/CHECKPOINTS.md)). Clear it
when the row is delivered, held, or handed back.

**Example**

```text
T3-EXAMPLE-01 · simple change → add retry to the export job
assigned_role: qw · origin: owner · handoff: claude_ok
drive_model: qwen-coder-route · review_model: sonnet-route · review_state: in_review
blocked_by: [SCHEMA-EXAMPLE-01] · blocks: []
in_flight_state: branch fix/t3-example-01 · step 3/4 · last_command "npm test" · pending_blockers [] · next_action "open PR"
```
