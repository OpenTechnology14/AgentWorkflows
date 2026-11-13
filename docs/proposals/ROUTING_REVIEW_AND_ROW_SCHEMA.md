# Routing by fit, drive/review, limit handoff, checkpoints and row schema

> **Status:** Owner-directed implementation · **Date:** 2026-11-10

The owner directed four routing and process policies, four row-schema additions and a consolidated best-practices list.
They are generic, so they live in this library, and projects point at them.

## Contract

| ID | File |
|---|---|
| `AW-POLICY-MODEL-FIT-01` | [`workflows/MODEL_FIT.md`](../../workflows/MODEL_FIT.md) |
| `AW-POLICY-DRIVE-REVIEW-01` | [`workflows/DRIVE_REVIEW.md`](../../workflows/DRIVE_REVIEW.md) |
| `AW-POLICY-HANDOFF-ON-LIMIT-01` | [`workflows/HANDOFF_ON_LIMIT.md`](../../workflows/HANDOFF_ON_LIMIT.md) |
| `AW-POLICY-CHECKPOINT-DISCIPLINE-01` | [`workflows/CHECKPOINTS.md`](../../workflows/CHECKPOINTS.md) |
| `AW-SCHEMA-INFLIGHT-01`, `-ROLE-ORIGIN-01`, `-DRIVE-REVIEW-01`, `-DEPENDENCIES-01` | [`templates/ROW_SCHEMA.md`](../../templates/ROW_SCHEMA.md) |
| `AW-BEST-PRACTICES-01` | [`workflows/BEST_PRACTICES.md`](../../workflows/BEST_PRACTICES.md) |

`MODEL_ROUTING.md` and `HF_ROUTING.md` now point at the fit rule instead of restating it. All files join the package
manifest.

## Where the new rules met existing ones

The owner's wording was kept, with the existing safety rules attached rather than replaced. Each choice below is a
default the owner can change.

- **Fit vs cost.** "Not by usage conservation" is read as: fit decides eligibility, and total cost still breaks ties
  between eligible routes, which keeps the existing HF cost comparison.
- **Dependency audits as QW work.** QW may drive an audit and a patch/minor fix. Majors, `--force` and failing checks
  go to Claude, and review is always capable. A minor validator bump in a real project changed user-facing behavior,
  which was caught only by review.
- **Unattended pickup.** `pending_qw` is a routing state, not a launch authorization. The existing rules still apply:
  an authorized route, an enforced watchdog, one bounded attempt, no fix-until-green.
- **Review approval and merging.** An approved review makes a PR eligible to merge. It doesn't replace a project's
  merge authority, for example a per-PR owner instruction for an admin-bypass.
- **Dependents.** Resolving a row notifies its dependents; it doesn't start them.

## Decision gates

| ID | Question | Default applied | Why it's a real choice |
|---|---|---|---|
| `AW-D01` | **Question:** When two routes both fit, should cost still pick between them? (yes, cost breaks ties / no, always prefer the stronger route) | Yes | "Not by usage conservation" could also mean "never let cost decide" |
| `AW-D02` | **Question:** May QW drive dependency fixes, with capable review? (patch/minor only / never / any bump) | Patch/minor only | The brief lists `npm audit fix` as QW work; existing policy routes security to the capable route |
| `AW-D03` | **Question:** Does marking a row `pending_qw` authorize an unattended launch? (no, a per-project standing authorization is needed / yes) | No | Existing rule: no agent launch without an authorized route |
| `AW-D04` | **Question:** Can an approved review authorize an admin-bypass merge without a per-PR owner instruction? (no / yes, per repository opt-in) | No | Projects record bypass merges as owner release decisions |
| `AW-D05` | **Question:** How often should rows checkpoint? (every 10 tool calls + step boundaries / step boundaries only / other N) | 10 + step boundaries | Frequent writes to a Git-tracked work map create commit churn |

## Rollout and rollback

Projects pinning this library refresh their source hashes after merge. Rollback: revert the change and rebuild. This
change doesn't depend on the open work-types/entry-gate PR, but it is written to fit it: the schema extends the row
rather than redefining Kinds.
