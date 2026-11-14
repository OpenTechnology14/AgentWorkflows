# Repository management

> **Status:** Maintained reusable module · Target-project rules retain authority

Two tools for projects that keep a private repository and a public one:

| File | What it is for |
|---|---|
| [`MIGRATION_PLAYBOOK.md`](MIGRATION_PLAYBOOK.md) | When to make a repository public, what blocks it, the fresh-repository procedure, three reference migrations, a compatibility matrix and a list of public considerations |
| [`SYNC_TRACKER.md`](SYNC_TRACKER.md) | How to track duplicate repositories (a private mirror, or a public snapshot of a private project) so neither side drifts unnoticed |
| [`sync_tracker.yaml`](sync_tracker.yaml) | The tracker file, with a synthetic example you replace in your private records |
| [`../../scripts/sync_tracker.py`](../../scripts/sync_tracker.py) | A stdlib-only check for the tracker file |

**Use it when** a project is about to go public, has just gone public, or keeps a second copy of itself somewhere.

**Entry gate.** A change that touches one side of a duplicate pair is made to both sides in the same operation, or the drift is recorded in the tracker with a reason and a date. This library supplies the rule; the project's pull request template, reviewer or checks apply it.

**What stays out of this repository.** The module is generic. Real repository names, revisions, owners and dates for your own pairs belong in a private workspace ([private workspace setup](../../docs/PRIVATE_WORKSPACE.md)), and the tracker file here holds only synthetic examples.
