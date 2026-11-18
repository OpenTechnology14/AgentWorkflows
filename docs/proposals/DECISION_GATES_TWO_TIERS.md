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

The `**Question:**` line already existed in the question template and the [logs workflow](../../workflows/LOGS.md). The first version added a pointer and a four-part reasoning. The second, merged on 2026-11-16, put options A and B and a pointer on the same line and added prerequisites, eight lines per option, a comparison table and the worst case. The third replaces the line: the question and a suggested answer of one to three words, with nothing else. That retires three rules of the second shape, which no longer have a place to live: the 450-character cap, the mark on option A, and re-lettering options so the recommended one comes first. The full reasoning is unchanged except that the suggested option, whichever letter it has, carries the mark. A gate written in an earlier shape is an older gate under the rule: it keeps working while a project lists it as missing the full shape, and it gets the new shape the next time it is touched.

## Decision gates

| ID | Question | Default applied | Why it is a real choice |
|---|---|---|---|
| `AW-D09` | **Question:** Must every gate carry the full reasoning, even a small one? **Suggested:** Yes | A | Skipping the reasoning for small gates is faster, but it makes "small" a judgment each author makes alone |
| `AW-D10` | **Question:** May a reasoning line say it does not know a figure and what would settle it? **Suggested:** Yes | A | Requiring every cost and date unblocks nothing when the source does not hold them, and pressure to fill the gap produces invented figures |
| `AW-D11` | **Question:** Should the suggested words name an option by its letter, by its name, or either? **Suggested:** Either | A | The owner's own examples use both, but a looser rule means a checker that has to reject a match that names two options |
| `AW-D12` | **Question:** Where the source records no recommendation, must the Context say the suggestion is the author's? **Suggested:** Yes | A | The one-line tier has no room to say whose the suggestion is, so the full reasoning is the only place left |

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

- **Context:** A suggestion should be the owner's or the source's own recommendation. Many older gates record none: they say "needs you" and ask for something only the owner can supply. The one-line tier has no room to say whose the suggestion is, so the rule needs somewhere else to say it.
- **Prerequisites:** None — the Context line already exists in every gate.

#### Option A: Yes (Suggested)

- **What it is:** Where the source records no recommendation, the Context line says so and that the suggestion is the author's. The generator enforces it for a row whose own default column says none or is blank.
- **Unlocks:** A reader of the section can tell a standing recommendation from a fresh author's guess, without cluttering the one-line tier.
- **Blocks:** None — it rules nothing out.
- **Risks:** An owner who reads only the one-line tier does not see whose suggestion it is. Low to medium impact, and the shape leaves no room for a marker on the line.
- **Effort:** One sentence of Context for each such gate; the reviewer confirms it (estimate: a minute each).
- **Money:** None — wording only, no new service.
- **Incompatible with:** Option B.
- **Needs first:** None — the review check already asks the reviewer to confirm whose the suggestion is.

#### Option B: No

- **What it is:** The Context line does not have to say whose the suggestion is; a gate is simply suggested.
- **Unlocks:** Less writing, and one fewer check.
- **Blocks:** Telling a recommendation the source records from an author's guess.
- **Risks:** The owner takes an author's guess for a position the source already holds, and the index shows it as a standing recommendation. Medium impact, found only after the answer.
- **Effort:** None — nothing to write.
- **Money:** None — nothing changes.
- **Incompatible with:** Option A, and a reviewer check that the suggestion is the owner's or the source's.
- **Needs first:** None — it removes a rule.

#### Trade-offs

| Axis | A (Suggested) | B |
|---|---|---|
| Owner can tell whose the suggestion is | In the section | No |
| Writing per gate with no recorded recommendation | One sentence | None |
| Chance an author's guess is taken for a standing recommendation | Low | Real |
| Checks the generator runs | One more, for rows with a default column | None |

- **Downstream impact:**
  - **Changes:** With A, the generator requires the Context to name the author for a row whose default says none, and the review check says the same. With B, both are removed.
  - **Unblocks:** Either answer unblocks the back-fill of gates that record no recommendation.
- **Cost of deferring:** The default applies, so authors write the sentence now. If the answer is B, the sentences already written are harmless.
- **Worst case:** A is chosen and the owner would rather not know whose suggestion it is; the sentence is one line in a section, and removing it is trivial.

## Rollout and rollback

Projects add the template to their gate workflow and a check to their index generator. Older gates are listed as missing the full shape until they are touched. Rollback is removing the new requirements from the generator; the reasoning sections stay valid as ordinary documentation.
