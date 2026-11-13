# Route by model-capability fit

> **Status:** Maintained reusable policy (`AW-POLICY-MODEL-FIT-01`) · Target-project rules retain authority

**Rule.** Decide which route may drive a work item by what the work needs, not by how much usage a route would save.
"QW" below means a qualified open-weight coding route (for example, a Qwen-class model driven by an agent CLI) that
has passed a comparable bounded task. "Claude" means the project's capable reasoning route.

| QW-appropriate (may drive) | Claude-appropriate (must drive) |
|---|---|
| Bulk or scripted refactors with a stated pattern | Architecture and scope decisions |
| Adding tests to existing, specified behavior | Security-sensitive code and its review |
| Mechanical documentation updates | Ambiguous or conflicting requirements |
| Code generation from a clear, complete spec | Cross-cutting or cross-project coordination |
| Dependency audits and a patch/minor `npm audit fix` (review stays capable, see below) | Anything that surfaces a `**Question:**` for the owner |

- **Fit decides eligibility; cost breaks ties.** When both routes fit, [HF routing](HF_ROUTING.md)'s total-cost
  comparison (draft + review + likely rework) still chooses between them.
- **Owner override per row.** The owner may pin any row to a route. Record the words and date on the row.
- **Reclassify on discovery.** If a QW row turns up a security impact, a behavior change or a `**Question:**`, stop and
  hand it to Claude. Don't let QW finish it.
- **Dependency updates:** QW may run the audit and a patch/minor fix. Any major bump, `--force`, or failing check goes to
  Claude. The review is always capable, because release notes can change behavior (for example, a validator that starts
  counting string length differently).

**Canonical example.** "Add unit tests for the existing date parser" → QW drives. "Should hourly schedules be paid-only?"
→ Claude drives and surfaces a Question.

**Entry-gate impact.** At registration each row records its fit class and `drive_model`
([row schema](../templates/ROW_SCHEMA.md#drive-and-review-fields)). A row with no fit class can't start.
