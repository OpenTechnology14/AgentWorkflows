# Decision gates: a plain question and a full reasoning

> **Status:** Owner-directed implementation · **Date:** 2026-11-13, tightened 2026-11-16, third shape 2026-11-17

The owner directed that every decision gate carry both a short answer and a full reasoning. The rule is generic, so it lives in this library and projects point at it. On 2026-11-16 the owner raised the bar on both tiers. On 2026-11-17 the owner narrowed the simple tier: the recommendation is one to three words, so the simple tier is only the plain question and a `**Suggested:**` line, and everything else is in the full reasoning.

## Contract

| ID | File |
|---|---|
| `AW-POLICY-DECISIONS-05` | [`workflows/DECISIONS.md`](../../workflows/DECISIONS.md) |
| the templates | [`templates/DECISION_GATE.md`](../../templates/DECISION_GATE.md), [`templates/PROPOSAL.md`](../../templates/PROPOSAL.md), [`templates/QUESTION.md`](../../templates/QUESTION.md), [`templates/DECISION.md`](../../templates/DECISION.md), [`templates/REVIEW.md`](../../templates/REVIEW.md) |
| the reviewer's duty | [`workflows/DRIVE_REVIEW.md`](../../workflows/DRIVE_REVIEW.md) |

## Where the rule meets earlier shapes

The `**Question:**` line already existed in the question template and the [logs workflow](../../workflows/LOGS.md). The first version added a pointer and a four-part reasoning. The second, merged on 2026-11-16, put options A and B and a pointer on the same line and added prerequisites, eight lines per option, a comparison table and the worst case. The third replaces the line: the question and a suggested answer of one to three words, with nothing else. That retires three rules of the second shape, which no longer have a place to live: the 450-character cap, the mark on option A, and re-lettering options so the recommended one comes first. The full reasoning is unchanged except that the suggested option, whichever letter it has, carries the mark. The second shape also let a table cell keep an explanation before its question; the third does not, so that text moves into the Context. A gate written in an earlier shape is an older gate under the rule: it keeps working while a project lists it as missing the full shape, and it gets the new shape the next time it is touched.

## Decision gates

| ID | Question | Default applied | Why it is a real choice |
|---|---|---|---|
| `AW-D09` | **Question:** Must every gate carry the full reasoning, even a small one? **Suggested:** Yes | A | Skipping the reasoning for small gates is faster, but it makes "small" a judgment each author makes alone |
| `AW-D10` | **Question:** May a reasoning line say it does not know a figure and what would settle it? **Suggested:** Yes | A | Requiring every cost and date unblocks nothing when the source does not hold them, and pressure to fill the gap produces invented figures |
| `AW-D11` | **Question:** Should the suggested words name an option by its letter, by its name, or either? **Suggested:** Either | A | The owner's own examples use both, but a looser rule means a checker that has to reject a match that names two options |
| `AW-D12` | **Question:** When the author, not the owner, made the suggestion, where should that be shown? **Suggested:** Reasoning and index | C | The one-line tier has no room to say whose the suggestion is, so the choice is between the full reasoning alone, nowhere, and the reasoning plus the index row the owner actually scans |

### Reasoning for AW-D09

- **Context:** The rule asks for a plain question and a full reasoning on every gate. Some gates are small, such as a name or a default, and a full section for them can feel like paperwork. The rule is new, so the habit has not formed either way.
- **Prerequisites:** None — the rule and its template exist, and a small gate can use them as they are.

#### Option A: Yes (Suggested)

- **What it is:** Every gate keeps all parts and all eight lines per option. A small gate answers each in one short line, and a line with truly nothing to add says `None —` and why.
- **Unlocks:** One shape everywhere, so a reader and a checker never have to decide whether a gate was small enough to skip.
- **Blocks:** Skipping the reasoning on trivial gates.
- **Risks:** Small gates carry some padding. Low impact, and it is cheap to trim.
- **Effort:** About ten minutes for a small gate once the template is filled in (estimate).
- **Money:** None — a writing and checking rule, no new service.
- **Incompatible with:** Option B, and any checker that needs a size test to decide what to skip.
- **Needs first:** None — the template and the rule already exist.

#### Option B: Only big gates

- **What it is:** Gates outside the big kinds (scope, security, anything public) may keep the question and the suggested answer with no reasoning section.
- **Unlocks:** Less writing on trivial gates.
- **Blocks:** A single rule for the generator and the reviewer: each now has to classify a gate first.
- **Risks:** A gate that looked small turns out to matter and has no reasoning on record. Medium impact, and it is found only after the answer.
- **Effort:** Less per small gate, more for the classification step and its audit (estimate: a few minutes saved, an hour of rule work).
- **Money:** None — a writing rule, no new service.
- **Incompatible with:** Option A, and a generator that checks one rule everywhere.
- **Needs first:** A written test for which gates count as small, and a way to mark them.

#### Trade-offs

| Axis | A (Suggested) | B |
|---|---|---|
| Rules the checker applies | One | One plus a size test |
| Writing for a trivial gate | Ten short lines | Almost none |
| Chance a mattering gate has no reasoning | Very low | Real |
| Easy to change later | Yes, A can be relaxed | Hard to tighten once gates exist without reasoning |

- **Downstream impact:**
  - **Changes:** With A, an index generator checks one rule: every part exists. With B, it needs a way to mark a gate small, and every such marker is a bypass to audit.
  - **Unblocks:** Either answer unblocks writing gates. Older gates are listed as missing the full shape under both.
- **Cost of deferring:** Nothing blocks. The default applies, so projects write every part now. If the answer is B, the extra parts already written are harmless.
- **Worst case:** A is chosen and the padding on small gates slows the owner's review of long lists. It shows up as complaints about length, and the fix is to relax the rule for a named kind of gate.

### Reasoning for AW-D10

- **Context:** The full reasoning asks every option for its effort and its money, and for effects on other work. Many older gates come from sources that never recorded a cost or a date. The rule has to say what a line does when the figure does not exist.
- **Prerequisites:** None — the rule is wording only, and the generator accepts the form once projects adopt it.

#### Option A: Yes (Suggested)

- **What it is:** A line may read `Unknown —` followed by what would settle it, for example a quote or a measurement. A bare `unknown` is not accepted.
- **Unlocks:** Gates can be finished and asked now, with the gap shown honestly rather than guessed.
- **Blocks:** Nothing, except authors using Unknown to skip work, which the reviewer check catches.
- **Risks:** Unknown spreads across lines. Low to medium impact, because the reviewer rejects an Unknown that does not say what would settle it.
- **Effort:** None beyond the wording rule, which this change already adds.
- **Money:** None — wording only, no new service.
- **Incompatible with:** Option B.
- **Needs first:** The reviewer check in the drive and review workflow, which this change adds.

#### Option B: No

- **What it is:** A gate may not be presented until every cost, date and effect has a source.
- **Unlocks:** Complete figures on every gate that does get presented.
- **Blocks:** Most older gates, whose sources do not hold costs, until someone researches each one.
- **Risks:** Pressure to guess so a gate can move, which is the failure the rule exists to prevent. High impact on trust in the figures.
- **Effort:** Research for each gate, likely hours each (estimate).
- **Money:** Unknown — vendor quotes may be needed for some gates.
- **Incompatible with:** Option A, and any plan to back-fill a large set of older gates quickly.
- **Needs first:** A source for every figure.

#### Trade-offs

| Axis | A (Suggested) | B |
|---|---|---|
| Honesty of the figures | Gaps are shown | Complete or absent, pressure to guess |
| Gates that can be asked now | All | Only those with every figure |
| Reviewer effort | Check each Unknown names its fix | Check each figure's source |
| Back-fill speed | Fast | Stalls for research |

- **Downstream impact:**
  - **Changes:** With A, the template and the generator accept the `Unknown —` form. With B, the generator rejects it and the back-fill plans change.
  - **Unblocks:** A unblocks the back-fill of older gates in every project.
- **Cost of deferring:** The default applies and projects write `Unknown —` now. If the answer is B, gates with Unknown lines are reopened for research.
- **Worst case:** A is chosen and the owner decides on a gate whose money line said Unknown and the real cost is large. The Unknown names what would settle it, so the owner can reply `later` until it is known, and the reviewer check is the guard against a quiet gap.

### Reasoning for AW-D11

- **Context:** The suggested answer is one to three words and names the recommended choice. The owner's examples point at options in two ways: by letter (`Option B`) and by name (`Yes`, `Keep private`, `Force-push`, `90-day re-check`). The checker needs one rule for how the words find their option.
- **Prerequisites:** None — option names are already one to three words, so either way can be checked.

#### Option A: Either (Suggested)

- **What it is:** The suggested words are either `Option` and a letter, or exactly one option's name. A match that fits two options is rejected.
- **Unlocks:** Every one of the owner's examples works, and a yes or no gate can simply say `Yes`.
- **Blocks:** None — it rules nothing out.
- **Risks:** An option named like another option's letter, for example one called `Option B`, would be ambiguous. Low impact, because the checker rejects an ambiguous match.
- **Effort:** One rule in the checker and its tests (estimate: an hour).
- **Money:** None — a rule in a script, no new service.
- **Incompatible with:** Options B and C.
- **Needs first:** None — the options are already named.

#### Option B: Name only

- **What it is:** The suggested words must be exactly an option's name; a bare letter is not accepted.
- **Unlocks:** A suggested answer that reads well without the section open.
- **Blocks:** `Option B`, one of the owner's own examples.
- **Risks:** An author who wants to point at a letter must invent a name for it, which is noise.
- **Effort:** One rule in the checker and its tests (estimate: an hour).
- **Money:** None — a rule in a script, no new service.
- **Incompatible with:** Option A, and the owner's example `Option B`.
- **Needs first:** None — the options are already named.

#### Option C: Letter only

- **What it is:** The suggested words must be `Option` and a letter; names are not accepted.
- **Unlocks:** An unambiguous match every time.
- **Blocks:** `Yes`, `Keep private` and the other named examples.
- **Risks:** A suggested answer that says nothing without the section open, which defeats the one-row tier. Medium impact.
- **Effort:** One rule in the checker and its tests (estimate: an hour).
- **Money:** None — a rule in a script, no new service.
- **Incompatible with:** Options A and B, and the owner's named examples.
- **Needs first:** None — the options are already lettered.

#### Trade-offs

| Axis | A (Suggested) | B | C |
|---|---|---|---|
| Owner's examples accepted | All | Names only | `Option B` only |
| Reads well in one row | Yes | Yes | No |
| Ambiguity to reject | A name equal to another letter label | None | None |

- **Downstream impact:**
  - **Changes:** With A, the checker resolves a suggestion by letter or by name. With B or C it resolves by one of them, and the owner's other examples fail.
  - **Unblocks:** Any answer unblocks the checker and the back-fill; A matches the examples already given.
- **Cost of deferring:** The default applies, so the checker accepts either. If the answer is B or C, gates written with the other form are rewritten.
- **Worst case:** A is chosen and an author writes a name that happens to equal another option's label; the checker rejects it and the author renames the option.

### Reasoning for AW-D12

- **Context:** A suggestion should be the owner's or the source's own recommendation. Many older gates record none: they say "needs you" and ask for something only the owner can supply, so the suggestion is the author's own guess. The one-line tier has no room to say whose the suggestion is. That leaves the full reasoning, which the owner opens only when unsure, and the index row, which is what the owner scans.
- **Prerequisites:** None — the Context line already exists in every gate, and the index already has a column for the recommendation.

#### Option A: Reasoning only

- **What it is:** Where the source records no recommendation, the Context line says so and that the suggestion is the author's. The index shows the suggested words the same way for every gate.
- **Unlocks:** A reader of the section can tell a standing recommendation from a fresh author's guess, with no change to how an index is built.
- **Blocks:** A reader of the index row alone cannot tell the two apart.
- **Risks:** An owner who scans only the index takes an author's guess for a recorded position. Medium impact, and it is found only after the answer.
- **Effort:** One sentence of Context for each such gate; the reviewer confirms it (estimate: a minute each).
- **Money:** None — wording only, no new service.
- **Incompatible with:** Options B and C, which are the other answers to the same question.
- **Needs first:** None — the review check already asks the reviewer to confirm whose the suggestion is.

#### Option B: Nowhere

- **What it is:** Nothing says whose the suggestion is; a gate is simply suggested.
- **Unlocks:** Less writing, and one fewer check.
- **Blocks:** Telling a recommendation the source records from an author's guess, in the section or in the index.
- **Risks:** The owner takes an author's guess for a position the source already holds, and the index shows it as a standing recommendation. Medium impact, found only after the answer.
- **Effort:** None — nothing to write.
- **Money:** None — nothing changes.
- **Incompatible with:** Options A and C, and a reviewer check that the suggestion is the owner's or the source's.
- **Needs first:** None — it removes a rule.

#### Option C: Reasoning and index (Suggested)

- **What it is:** The Context line says it, as in A. The index's recommendation column also shows `None recorded; the author suggests: <words>` for those gates, instead of showing the suggestion as if it were recorded.
- **Unlocks:** The row the owner scans and the section agree: an author's guess is marked as one where it is read first.
- **Blocks:** None — the one-line tier stays a question and a suggestion; only the text the index shows beside it changes.
- **Risks:** An index that cannot tell a table with no recommendation column from one that records its recommendation under another heading marks a real recommendation as the author's. Low impact, and it shows up as a failing check on that table, fixed by naming the heading.
- **Effort:** One sentence of Context per gate, as in A, plus a one-time change to an index generator; the first index generator to adopt the rule already does it (estimate: an hour, with tests).
- **Money:** None — wording and code only.
- **Incompatible with:** Options A and B, which are the other answers to the same question.
- **Needs first:** An index generator that reads a table's recommendation column, which the first adopting generator already does.

#### Trade-offs

| Axis | A | B | C (Suggested) |
|---|---|---|---|
| Owner can tell whose the suggestion is in the section | Yes | No | Yes |
| Owner can tell whose the suggestion is in the index row | No | No | Yes |
| Writing per gate with no recorded recommendation | One sentence | None | One sentence |
| Checks an index generator runs | One, on the Context | None | Two, the Context and the text beside the suggestion |
| Chance an author's guess is taken for a standing recommendation | Real, in the index | Real | Low |

- **Downstream impact:**
  - **Changes:** With C, the policy says the index marks such a suggestion as the author's, and the first adopting generator already requires the Context to name the author and renders the marked text. With A, the index text is removed from the generator. With B, the Context check goes too.
  - **Unblocks:** Any answer unblocks the back-fill of gates that record no recommendation.
- **Cost of deferring:** The default applies, so authors write the sentence and the index marks the suggestion. If the answer is A or B, the index text is removed in one small change and the sentences already written are harmless.
- **Worst case:** C is chosen and the owner finds the marked text noisy; it is one text pattern in a generator and one sentence per gate, and removing it is one small change.

## Rollout and rollback

Projects add the template to their gate workflow and a check to their index generator. Older gates are listed as missing the full shape until they are touched. Rollback is removing the new requirements from the generator; the reasoning sections stay valid as ordinary documentation.
