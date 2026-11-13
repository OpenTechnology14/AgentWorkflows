# Agent work best practices

> **Status:** Maintained reusable summary (`AW-BEST-PRACTICES-01`) · Each item points to its source rule; target-project rules retain authority

1. **Register, then start.** A row with an ID, a Kind and a state exists before any branch or file changes. Owner
   instructions don't skip it.
2. **Branch name matches the row ID**, for example `fix/t3-example-01`. Anyone can find a row's branch, and a branch's
   row, without asking.
3. **Route by fit.** Pick the driver by what the work needs, then compare cost ([model fit](MODEL_FIT.md),
   [HF routing](HF_ROUTING.md)).
4. **Drive and review are different models.** A stronger-or-equal reviewer approves on the PR, and the PR body names
   both ([drive/review](DRIVE_REVIEW.md)).
5. **Checkpoint as you go,** so any session can recover the row ([checkpoints](CHECKPOINTS.md)).
6. **Hand off at the limit, not mid-judgment.** Only QW-appropriate work changes hands
   ([handoff](HANDOFF_ON_LIMIT.md)).
7. **Write dependencies as row IDs** (`blocks` / `blocked_by`), not prose ([row schema](../templates/ROW_SCHEMA.md)).
8. **Document every admin-bypass merge.** Record who authorized it, for which PR, what ran, and what was left unrun
   (for example, CI blocked by billing). An approved review alone is not that authorization.
9. **Private/public split.** Generic rules, taxonomy and patterns go in the public library. Rows, project names, people
   and environments go in the private workspace (see the library's private-workspace setup). Commit to public
   repositories only under a non-personal identity.
10. **Point, don't duplicate.** Link the one canonical rule or record. When two copies disagree, fix the source and
    replace the copy with a link.
