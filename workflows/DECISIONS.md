# Decision gates: a plain answer and a full reasoning

> **Status:** Maintained reusable policy (`AW-POLICY-DECISIONS-05`, tightened 2026-11-16) · Target-project rules retain authority

**Rule.** Every decision gate has two tiers, written together and kept in step. Tier 1 lets the owner decide. Tier 2 shows everything the decision involves, so the owner can check it and anyone with no context can follow it later. Start from the [decision gate template](../templates/DECISION_GATE.md), which has both tiers pre-structured. A gate that is not in this shape is not ready to ask.

| Tier | Reader | What it holds | Where it lives |
|---|---|---|---|
| 1. The simple answer | The owner, in a status report, an index row or a prompt, with no project context | One question, two or three lettered options, one recommendation, a pointer | The gate's own row or question, on one line |
| 2. The full reasoning | The owner or a reviewer who is unsure; anyone later | For every option: what it is and what it unlocks, blocks, risks, costs and cannot go with; then a comparison, the knock-on effects, the cost of waiting and the worst case | A section headed `Reasoning for <gate ID>` in the document that owns the gate |

## Tier 1: the simple answer

One line, in this order:

`**Question:** <one short sentence?> A (Recommended): <what happens>. B: <what happens>. C: <only if a third real choice exists>. Reasoning: [below](#reasoning-for-<gate-id>)`

In a table cell it stays on one line; in a standalone question each option goes on its own line. The rules, and who checks each:

1. **One question.** One sentence, at most 25 words, one question mark, starting with a capital. The index generator checks this.
2. **Plain words.** Write for someone who has never opened the project. No gate IDs, file names, paths, links, code spans or table pipes in the question or the options, and no acronym or product term a new reader would have to look up. The generator checks what it can see: identifiers written in capitals (such as `P-067`), common file extensions, links, code spans and table pipes. The reviewer reads the line cold and checks the rest.
3. **Two or three options, lettered in order.** `A` and `B`, and `C` only for a third real choice. More options than that means more than one gate: split it. Each option is a short phrase and what it leads to, at least two words, so a bare `yes` or `no` does not count.
4. **One recommendation, and it is A.** The recommended option comes first and carries `(Recommended)`. No other option does. The recommendation is the owner's or the source's own. Where the source records none, the author writes A as the smallest step that keeps the gate answerable (for example, give the missing answer now) and B as leaving it open, and says in the Context line that the source records no recommendation and A is the author's suggestion.
5. **Short enough for one status row.** The line, not counting the pointer, is at most 450 characters.
6. **Answerable on its own.** The owner can reply `A`, `B`, `C`, yes, no, free text or `later` without opening tier 2. If the line cannot be answered without reading further, the question or the options are too vague. The reviewer checks this.
7. **The pointer ends the line.** `Reasoning:` and a link to the anchor of the gate's own tier 2 section in the same document, `#reasoning-for-<gate-id>`. Nothing follows it.

## Tier 2: the full reasoning

A section headed `Reasoning for <gate ID>`, in the document that owns the gate, with these parts in this order. The options use the same letters, order and names as tier 1.

| Part | Holds |
|---|---|
| **Context** | What is being decided and why now; what is already decided, with links; the constraints that make it a real choice |
| **Prerequisites** | What must be true before this gate can be acted on at all, whichever option is chosen: an account, a review, a merged change, another answer |
| **Option A (Recommended): name**, then **Option B: name** and any **Option C: name** (one sub-heading each) | The eight lines below |
| **Trade-offs** (a sub-heading) | A table comparing the options on the axes that matter for this gate |
| **Downstream impact** | **Changes:** the files, rows, decisions, projects or public things that change with each answer. **Unblocks:** the work and decisions that can proceed afterwards |
| **Cost of deferring** | What stays stuck or breaks while the gate is open; what can proceed meanwhile and under what authority; any default applied; when waiting starts to cost something |
| **Worst case** | The worst realistic outcome if the recommended option is wrong, how it would show up, and how to undo it or limit the damage |

Each option carries these eight lines, in this order:

| Line | Holds |
|---|---|
| **What it is** | What would actually be done, in two or three plain sentences |
| **Unlocks** | What becomes possible, cheaper or safer |
| **Blocks** | What it rules out or makes harder |
| **Risks** | What could go wrong, how likely and how bad, and whether it can be undone |
| **Effort** | Who does what, and roughly how long; an estimate says it is one |
| **Money** | The cost in dollars, or `None —` and why there is no spend |
| **Incompatible with** | The other options, decisions, tools or limits it cannot sit beside, or `None —` and why |
| **Needs first** | What must be true or done before this option can be carried out |

The trade-offs table has one row per axis and one column per option, each column headed by the option's letter (the recommended one marked). Choose the axes that actually separate the options for this gate, at least two and usually three to six, for example the chance of exposing something public, work before release, whether it can be undone, cost, and what it asks of the owner.

**Never invent a figure.** Every line carries real content: at least two words, or a figure such as `$0` or `$40 a month`. When the source does not give a number, a date, a price or an effect, write `Unknown —` and what would settle it. When a line truly has nothing to add, write `None —` and why. A bare `none`, `n/a`, `tbd`, `see above` or an empty line is not an answer, and a line still holding a template placeholder (`[[...]]`) is not finished. An effort or timing figure that is an estimate says so.

**Agreement.** The letters, order, names and recommendation on the simple line must match the section's option sub-headings and the trade-offs columns. When the reasoning changes, the simple line changes in the same edit. The index shows the line and the pointer, never a copy of the reasoning.

**Small decisions.** A small gate keeps every part and every line, each as short as the truth allows. A line may say `None —` with its reason; it may not be left out.

**Where it goes.** The gate lives in the proposal or record that owns the choice, and its pointer resolves to a section in that same document. The [question template](../templates/QUESTION.md) carries the simple line, the [proposal template](../templates/PROPOSAL.md) points at the gate template for each unresolved choice, and the [decision template](../templates/DECISION.md) records which reasoning the answer was given against, so a later reader sees what the owner knew.

## Review

A machine can reject a gate with a missing tier, option, line, pointer or table, or a leftover placeholder. It cannot judge clarity or truth, so the reviewer ([drive and review](DRIVE_REVIEW.md)) checks, and records that they checked:

1. The simple line can be answered by someone who has never seen the project, from that line alone.
2. Each option is a real, distinct choice, and the recommendation is the owner's or the source's own, or is labelled in the Context line as the author's suggestion because the source records none.
3. The full reasoning is complete and honest: no invented figures, every `Unknown —` says what would settle it, every estimate is labelled.
4. The two tiers agree.

A gate that fails review is not presented to the owner.

## Entry gate and older gates

**Entry gate.** A gate may not enter a question index, a status report or a prompt for the owner unless both tiers exist, the pointer resolves to that gate's own section, and the section has every part above. This library supplies the rule; the project's index generator, reviewer or checks apply it.

**Older gates.** Gates written before the rule keep working while they are listed as missing it, and each gets the full shape the next time it is touched. A project may keep a list of such gates that can only shrink; when the list is empty, the rule applies to every gate. Back-filling an older gate changes its shape, not its meaning: the question and the owner's recommendation stay as the source has them, the options are lettered so the recommended one is A (re-lettered if the source recommended another), and the reviewer compares before and after. Whoever drafts the back-fill, the same review applies.

**Canonical example.** A proposal needs to know whether a generated dashboard may ship in a public export.

```markdown
**Question:** Should the public export include only this project's rows? A (Recommended): yes, this project only. B: also other projects' rows, but only the ones marked public. Reasoning: [below](#reasoning-for-d-12)

### Reasoning for D-12

- **Context:** The export is public, and the dashboard it ships merges rows from two projects today. Nothing has been exported yet.
- **Prerequisites:** The export script must know which project each row belongs to; it already does.

#### Option A (Recommended): this project only

- **What it is:** The export keeps only the rows that belong to this project and drops the rest.
- **Unlocks:** A smaller export from one data source, with nothing from another project to check before publishing.
- **Blocks:** The combined cross-project view in the public dashboard.
- **Risks:** Readers lose the combined view. Low impact, and it can be added later.
- **Effort:** About one hour to filter and test (estimate).
- **Money:** None — a code change with no new service.
- **Incompatible with:** Option B, and any plan that needs the combined view in public.
- **Needs first:** None — the export script already knows each row's project.

#### Option B: also other projects' public rows

- **What it is:** The export keeps this project's rows plus other projects' rows that carry a public mark.
- **Unlocks:** The combined cross-project view in public.
- **Blocks:** A quick release, because the mark must be built and trusted first.
- **Risks:** A wrong or missing mark publishes another project's row. High impact, and a published row cannot be fully recalled.
- **Effort:** About two days for the filter, its tests and a check of every project's marks (estimate).
- **Money:** None — no new service.
- **Incompatible with:** Option A, and exporting before every project has marked its rows.
- **Needs first:** A public or private mark on every row in every project, and someone who owns each project's marks.

#### Trade-offs

| Axis | A (Recommended) | B |
|---|---|---|
| Chance of publishing another project's row | None | Real, if one mark is wrong |
| Work before release | About one hour | About two days |
| Combined view in public | No | Yes |
| Can it be changed later | Yes, B can be added | A published row cannot be recalled |

- **Downstream impact:**
  - **Changes:** A changes the export script only. B also changes every project's row format.
  - **Unblocks:** Either answer unblocks the public export.
- **Cost of deferring:** The export stays blocked, and no default may ship another project's rows.
- **Worst case:** A is chosen and the combined view turns out to be needed at launch, so the release slips by the two days B would have taken. Nothing is lost or exposed, and B can still be added later.
```

**Why.** A one-line question gets answered fast, but a bare question hides what the answer costs. A long reasoning attached to every question buries the question. Two tiers keep the question answerable in seconds and the full reasoning one click away, and checking both, mechanically and by a reviewer, stops either from being skipped or filled with something that only looks complete.
