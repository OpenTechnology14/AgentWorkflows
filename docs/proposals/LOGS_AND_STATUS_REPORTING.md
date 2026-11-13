# Logs and status reporting

> **Status:** Owner-directed implementation · **Date:** 2026-11-12

The owner directed the four-logs policy and status reporting rules. They are generic, so they live in this library, and projects point at them.

## Contract

| ID | File |
|---|---|
| `AW-POLICY-LOGS-04` | [`workflows/LOGS.md`](../../workflows/LOGS.md) |
| the starter directory | `templates/project-log-starter/` |

## Where the new rules met existing ones

The logs are distinct from the [bug workflow](../../workflows/BUGS.md) and the project bug tracker. The entry-gate file is not in this library yet, so the `Logs:` rule lives in `workflows/LOGS.md` and moves to the entry gate when that lands. The reporting rule changes what a summary contains, not what is logged.

## Decision gates

| ID | Question | Default applied | Why it is a real choice |
|---|---|---|---|
| `AW-D06` | **Question:** Keep `CHANGELOG.md` at the root and the other three under `docs/`, or put all four in one `logs/` folder? | root plus `docs/` | A flat logs/ folder is cleaner but breaks existing tooling that expects CHANGELOG.md at root |
| `AW-D07` | **Question:** Use `BUG-nnn` and `GAP-nnn` IDs with a three-level severity? | yes | Simpler schemes lose information; more complex ones add overhead |
| `AW-D08` | **Question:** Should a pull request that touches no log still carry `Logs: none.`? | yes | A missing line is a gap; `Logs: none.` is explicit |

The defaults stay provisional in `workflows/LOGS.md` until these gates are answered.

## Rollout and rollback

Projects add the logs and the footer line in one pull request each. Rollback is deleting the files and the footer line.
