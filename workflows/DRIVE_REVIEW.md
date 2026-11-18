# Two-tier drive and review

> **Status:** Maintained reusable policy (`AW-POLICY-DRIVE-REVIEW-01`) · Target-project rules retain authority

**Rule.** Every row names a `drive_model` (who writes) and a `review_model` (who checks). The reviewer is always a
stronger-or-equal tier than the driver for that work.

| Work | Drive | Review |
|---|---|---|
| Mechanical ([QW-appropriate](MODEL_FIT.md)) | QW | Sonnet-class |
| Reasoning-adjacent | Sonnet-class | Sonnet-class; Opus-class only when high-stakes |
| High-stakes (security, auth, billing, data safety, migrations) | Opus-class or the project's capable route | Opus-class |

- **Review runs on the PR.** The reviewer reads the diff, the test results and the row's checkpoints
  ([checkpoints](CHECKPOINTS.md)), flags issues, and sets `review_state`.
- **Approval is a precondition, not a release.** An approved review makes a PR eligible to merge. Admin-bypass
  merges still need the authority the target project requires, which is often an explicit owner instruction per PR.
- **A change that adds or edits a decision gate** is also checked against the gate review in [decision gates](DECISIONS.md#review): the reviewer reads the question and the suggested answer cold, as someone with no project context, and confirms they can be answered from those words alone; confirms each option is real and the suggestion is the owner's or the source's (or the Context says it is the author's); and confirms the full reasoning is complete and honest and agrees with the suggested answer. The reviewer records that they did.
- **Attribution.** The PR body states `Drive: <model>` and `Review: <model> — <approved|rejected>`, plus the row ID.
- **One review pass per revision.** A rejection returns the row to its driver with the findings. Don't loop
  fix-until-green; escalate after a second rejection.

**Canonical example.** QW adds 40 tests from a spec. A Sonnet-class review finds two tests asserting the wrong boundary,
rejects, QW fixes those two, and the review approves. The PR body records both models.

**Entry-gate impact.** `drive_model` and `review_model` are set before work starts. `review_state` starts at
`not_started` ([row schema](../templates/ROW_SCHEMA.md#drive-and-review-fields)).
