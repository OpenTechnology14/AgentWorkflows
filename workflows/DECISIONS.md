# Decision gates: a plain question and a full reasoning

> **Status:** Maintained reusable policy (`AW-POLICY-DECISIONS-05`, third shape 2026-11-17) · Target-project rules retain authority

**Rule.** Every decision gate has two tiers, written together and kept in step. Tier 1 is one plain question and one suggested answer of one to three words, so it scans in a single dashboard row. Tier 2 holds everything the decision involves, so the owner can check it and anyone with no context can follow it later. Start from the [decision gate template](../templates/DECISION_GATE.md), which has both tiers pre-structured. A gate that is not in this shape is not ready to ask.

| Tier | Reader | What it holds | Where it lives |
|---|---|---|---|
| 1. The simple answer | The owner, in a status report, an index row or a prompt, with no project context | The question, and the suggested answer in one to three words. Nothing else | The gate's own row or question |
| 2. The full reasoning | The owner or a reviewer who is unsure; anyone later | For every option: what it is and what it unlocks, blocks, risks, costs and cannot go with; then a comparison, the knock-on effects, the cost of waiting and the worst case | A section headed `Reasoning for <gate ID>` in the same document as the gate |

## Tier 1: the simple answer

Exactly this, on one line in a table cell or as a standalone question:

`**Question:** <one short sentence?> **Suggested:** <one to three words>`

The rules, and who checks each:

1. **One plain question.** One sentence, at most 25 words, one question mark, starting with a capital. Write it for someone who has never opened the project: no gate IDs, file names, paths, links, code spans or table pipes, and no acronym or product term a new reader would have to look up. When the choice is between named things, the question names them, so the suggested answer makes sense on its own. The index generator checks what it can see: identifiers written in capitals (such as `P-067`), common file extensions, links, code spans and table pipes. The reviewer reads the question cold and checks the rest, including that it is a single sentence.
2. **One suggested answer of one to three words.** `**Suggested:** Yes`, `**Suggested:** Option B`, `**Suggested:** Force-push`, `**Suggested:** Keep private`, `**Suggested:** 90-day re-check`. It names the recommended choice, and it names exactly one option of tier 2: either by letter (`Option B`) or by that option's name. It is a name, not a sentence: no commas, no consequences, no reasons, no second suggestion. Nothing follows it but an optional full stop.
3. **Nothing else.** No options, no pointer and no explanation on the line, and nothing before the question: the cell holds the line and only the line. A table that used to say more in that cell moves the text into the Context of tier 2, where the options are too, and which the index links to.
4. **Answerable on its own.** The owner can reply `yes`, `no`, `Suggested`, a named alternative, free text or `later` from this line without opening tier 2. If the line cannot be answered without reading further, the question is too vague. The reviewer checks this.
5. **The recommendation is the owner's or the source's own.** Where the source records none, the suggestion is the author's: the Context line says so (see tier 2), and an index with a recommendation column shows the suggestion there as the author's, not as a recorded recommendation. A table with no recommendation column records none, so a gate written into one is marked as the author's: add a Default column when the recommendation is the owner's or the source's.

## Tier 2: the full reasoning

A section headed exactly `Reasoning for <gate ID>`, in the same document as the gate. The index finds it by that title, so the row carries no pointer. Its parts, in this order:

| Part | Holds |
|---|---|
| **Context** | What is being decided and why now; what is already decided, with links; the constraints that make it a real choice. Where the source records no recommendation, it says so and that the suggestion is the author's |
| **Prerequisites** | What must be true before this gate can be acted on at all, whichever option is chosen: an account, a review, a merged change, another answer |
| **Option A: name**, **Option B: name** and up to two more (one sub-heading each) | The eight lines below. Each name is one to three words, because the suggested answer may use it |
| **Trade-offs** (a sub-heading) | A table comparing the options on the axes that matter for this gate |
| **Downstream impact** | **Changes:** the files, rows, decisions, projects or public things that change with each answer. **Unblocks:** the work and decisions that can proceed afterwards |
| **Cost of deferring** | What stays stuck or breaks while the gate is open; what can proceed meanwhile and under what authority; any default applied; when waiting starts to cost something |
| **Worst case** | The worst realistic outcome if the suggested option is wrong, how it would show up, and how to undo it or limit the damage |

There are two to four options, lettered from A in order. The option the suggested answer names carries `(Suggested)` at the end of its heading, for example `#### Option B: Force-push (Suggested)`, and its column in the trade-offs table carries the same mark. No other option does.

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

The trade-offs table has one row per axis and one column per option, each column headed by the option's letter. Choose the axes that actually separate the options for this gate, at least two and usually three to six, for example the chance of exposing something public, work before release, whether it can be undone, cost, and what it asks of the owner.

**Never invent a figure.** Every line carries real content: at least two words. In Money and Effort a single figure such as `$0` or `$40 a month` is enough. When the source does not give a number, a date, a price or an effect, write `Unknown —` and what would settle it. When a line truly has nothing to add, write `None —` and why. A bare `none`, `n/a`, `tbd`, `see above` or an empty line is not an answer, and a line still holding a template placeholder (`[[...]]`) is not finished. An effort or timing figure that is an estimate says it is one.

**Agreement.** The suggested answer must name one option, that option's heading and its table column carry the mark, and the option letters run from A without gaps. A row that records its own default or recommendation, and names an option in it (by letter, as `Option B`, or by the option's name), names the same option the suggested answer does; free text that names no option is left alone. When the reasoning changes, the suggested answer changes in the same edit. The index shows the question and the suggested answer, and links the section; it never copies the reasoning.

**Small decisions.** A small gate keeps every part and every line, each as short as the truth allows. A line may say `None —` with its reason; it may not be left out.

**Where it goes.** The gate lives in the proposal or record that owns the choice, and tier 2 is a section in that same document. The [question template](../templates/QUESTION.md) carries the simple tier, the [proposal template](../templates/PROPOSAL.md) points at the gate template for each unresolved choice, and the [decision template](../templates/DECISION.md) records which reasoning the answer was given against, so a later reader sees what the owner knew.

## Review

A machine can reject a gate with a missing tier, a suggested answer that names no option, a missing option, line, table or part, or a leftover placeholder. It cannot judge clarity or truth, so the reviewer ([drive and review](DRIVE_REVIEW.md)) checks, and records that they checked:

1. The question can be answered by someone who has never seen the project, from the question and the suggested answer alone.
2. Each option is a real, distinct choice. The suggested answer is the owner's or the source's own recommendation, or, where the source records none, the Context line says it is the author's.
3. The full reasoning is complete and honest: no invented figures, every `Unknown —` says what would settle it, every estimate is labelled.
4. The two tiers agree.

A gate that fails review is not presented to the owner.

## Entry gate and older gates

**Entry gate.** A gate may not enter a question index, a status report or a prompt for the owner unless both tiers exist, the suggested answer names an option, and the section has every part above. This library supplies the rule; the project's index generator, reviewer or checks apply it.

**Older gates.** Gates written before the rule keep working while they are listed as missing it, and each gets the full shape the next time it is touched. A project may keep a list of such gates that can only shrink; when the list is empty, the rule applies to every gate. Back-filling an older gate changes its shape, not its meaning: the question and the owner's recommendation stay as the source has them, the Suggested words name that recommendation, the text the old cell held before the question moves into the Context, and the reviewer compares before and after. Whoever drafts the back-fill, the same review applies.

**Canonical example.** A proposal needs to know whether a generated dashboard may ship in a public export.

```markdown
**Question:** Should the public export include only this project's rows? **Suggested:** Yes

### Reasoning for D-12

- **Context:** The export is public, and the dashboard it ships merges rows from two projects today. Nothing has been exported yet.
- **Prerequisites:** The export script must know which project each row belongs to; it already does.

#### Option A: Yes (Suggested)

- **What it is:** The export keeps only the rows that belong to this project and drops the rest.
- **Unlocks:** A smaller export from one data source, with nothing from another project to check before publishing.
- **Blocks:** The combined cross-project view in the public dashboard.
- **Risks:** Readers lose the combined view. Low impact, and it can be added later.
- **Effort:** About one hour to filter and test (estimate).
- **Money:** None — a code change with no new service.
- **Incompatible with:** Option B, and any plan that needs the combined view in public.
- **Needs first:** None — the export script already knows each row's project.

#### Option B: No

- **What it is:** The export keeps this project's rows plus other projects' rows that carry a public mark.
- **Unlocks:** The combined cross-project view in public.
- **Blocks:** A quick release, because the mark must be built and trusted first.
- **Risks:** A wrong or missing mark publishes another project's row. High impact, and a published row cannot be fully recalled.
- **Effort:** About two days for the filter, its tests and a check of every project's marks (estimate).
- **Money:** None — no new service.
- **Incompatible with:** Option A, and exporting before every project has marked its rows.
- **Needs first:** A public or private mark on every row in every project, and someone who owns each project's marks.

#### Trade-offs

| Axis | A (Suggested) | B |
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

**Why.** A short question with a one-to-three-word suggestion gets answered in seconds and fits one row of a status view. A bare suggestion hides what the answer costs, so the reasoning sits one click away, and checking both tiers, mechanically and by a reviewer, stops either from being skipped or filled with something that only looks complete.
