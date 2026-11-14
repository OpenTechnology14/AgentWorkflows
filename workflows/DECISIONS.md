# Decision gates: a short answer and a full reasoning

> **Status:** Maintained reusable policy (`AW-POLICY-DECISIONS-05`) · Target-project rules retain authority

**Rule.** Every decision gate has two tiers, written together and kept in step.

1. **The simple answer.** What the owner reads in the questions index or a status report: one `**Question:**` line of one short sentence, then the options `A`, `B` and, if needed, `C`, one line each, the recommended option first and marked `(Recommended)`, and a `Reasoning:` pointer to the second tier. The owner can answer from this alone: `A`, `B`, `C`, free text or `later`.
2. **The full reasoning.** What the reader opens when unsure. It lives in the proposal or record that owns the gate, as a section named `Reasoning for <gate ID>` with exactly four headings, in this order: **Context**, **Trade-offs**, **Downstream impact**, **Cost of deferring**.

| Heading | Holds |
|---|---|
| Context | what is being decided and why now; what is already decided, with links; the constraints that make it a real choice |
| Trade-offs | each option's upside, downside, cost and reversibility, and why the recommended one wins |
| Downstream impact | what changes after each answer: files, work rows, other projects, anything public; what it unblocks and what it closes off |
| Cost of deferring | what waits if the gate stays open, what can proceed meanwhile and under what authority, any default applied, and when waiting starts to cost something |

**Agreement.** The options, their order and the recommendation on the simple line must match the reasoning. When the reasoning changes, the line changes in the same edit. The index shows the line and the pointer, never a copy of the reasoning.

**Small decisions.** A small gate keeps all four headings with one line each. A heading may say `none`, with the reason, when it truly has nothing to add (`Downstream impact: none beyond this file`). A gate with a missing heading is not ready to ask.

**Where it goes.** The gate lives in the proposal or record that owns the choice; the [proposal template](../templates/PROPOSAL.md) has the block. The [question template](../templates/QUESTION.md) carries the line and the pointer, and the [decision template](../templates/DECISION.md) records which reasoning the answer was given against, so a later reader sees what the owner knew.

**Entry gate.** A gate may not enter a question index, a status report or a prompt for the owner unless both tiers exist and the pointer resolves to a section with the four headings. This library supplies the rule; the project's index generator, reviewer or checks apply it. Gates written before this rule keep working while they are listed as missing their reasoning, and each gets one the next time it is touched.

**Canonical example.** A proposal needs to know whether a generated dashboard may ship in a public export.

- The simple line, in the index: `**Question:** Should the exported dashboard include only this project's rows? A (Recommended): yes, this project only. B: also other projects, filtered to public ones. Reasoning: docs/proposals/EXPORT.md#reasoning-for-d-12`.
- The full reasoning, in the proposal. Context: the export is public and the dashboard currently merges two projects. Trade-offs: A cannot leak another project's rows but loses the cross-project view; B keeps the view but needs a per-row visibility filter that must itself be trusted. Downstream impact: A means one data source and a smaller export; B means a filter to build, test and audit. Cost of deferring: the export stays blocked, and no default may ship another project's rows.

**Why.** A one-line question gets answered fast, but a bare question hides what the answer costs. A long reasoning attached to every question buries the question. Two tiers keep the question answerable in seconds and the reasoning one click away, and checking both stops either from being skipped.
