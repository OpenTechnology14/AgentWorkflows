# Duplicate-repository sync tracker

> **Status:** Maintained reusable procedure · Target-project rules retain authority

A project that publishes from a private repository ends up with two copies of the truth. This tracker records, for each pair, the last revision both sides agreed on and whether they have drifted since.

## Two kinds of pair

| Kind | What it is | How the public side is made | What drifts |
|---|---|---|---|
| `snapshot` | A private working repository and a public repository that holds a reviewed export of it | A script exports committed files from the private repository, and one new commit is published | The private side moves on; the public side stays at its last export |
| `mirror` | A private repository that holds a full copy of another repository, usually an archive of a retired one | Branches and tags are pushed; hidden pull-request refs cannot be, so the retired original keeps those | Rarely: a mirror is meant to be frozen, so any change is a finding |

## Fields

The file is `sync_tracker.yaml`: a `schema` number and a `pairs` list. Each pair has these keys, all required.

| Key | Meaning |
|---|---|
| `id` | A short name for the pair |
| `kind` | `snapshot` or `mirror` |
| `private_repo` | `owner/name` of the private side |
| `public_repo` | `owner/name` of the other side, which is public for a snapshot and private for a mirror |
| `method` | The exact command or procedure that syncs them, as a sentence (never a secret) |
| `last_synced_private_sha` | The 40-character private revision the other side was built from |
| `last_synced_other_sha` | The 40-character revision that was published or mirrored |
| `last_synced_at` | The date of that sync, `YYYY-MM-DD` |
| `drift` | `none`, `private-ahead`, `other-ahead`, `diverged` or `unknown` |
| `drift_reason` | Why, in one line. Required unless `drift` is `none` |
| `checked_at` | The date the drift was last measured, `YYYY-MM-DD` |
| `owner` | A role or team, not a personal address |

## Measuring drift

Compare the live heads with the recorded ones, then set `drift` and `checked_at`:

```bash
git ls-remote https://github.com/<private_repo>.git refs/heads/main
git ls-remote https://github.com/<public_repo>.git refs/heads/main
```

If the private head equals `last_synced_private_sha` and the other head equals `last_synced_other_sha`, the pair is `none`. If only the private head moved, it is `private-ahead`. If the other head moved, it is `other-ahead`. If both moved, it is `diverged`. If you could not read one side, it is `unknown`, which is a finding, not a pass.

## The entry gate

A change that touches one side of a pair is made to both sides in the same operation. If that is not possible, record `drift`, a `drift_reason` and the date before you stop; a drift with no reason is invalid. Before a snapshot is published, measure the pair first, so the export starts from a known state. The gate is a rule that people and reviewers apply; the checker below validates the tracker file, not anyone's behaviour.

## Checking the file

```bash
python3 scripts/sync_tracker.py check modules/repo-management/sync_tracker.yaml
```

The check validates the shape: required keys, 40-character revisions, dates, the allowed `kind` and `drift` values, and a reason whenever there is drift. It does not call the network; measuring drift is the step above.

## Why

Two copies drift silently: the public side keeps showing old behaviour, or someone fixes a bug on the public copy and the private source never learns of it. A one-line record per pair turns that into something a reviewer can see.
