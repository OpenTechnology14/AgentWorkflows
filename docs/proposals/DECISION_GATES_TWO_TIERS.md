# Decision gates: a plain answer and a full reasoning

> **Status:** Owner-directed implementation · **Date:** 2026-11-13, tightened 2026-11-16

The owner directed that every decision gate carry both a one-line answer and a full reasoning. The rule is generic, so it lives in this library and projects point at it. On 2026-11-16 the owner raised the bar on both tiers: the simple answer must be plain enough for someone with no project context, and the reasoning must cover every option in full.

## Contract

| ID | File |
|---|---|
| `AW-POLICY-DECISIONS-05` | [`workflows/DECISIONS.md`](../../workflows/DECISIONS.md) |
| the templates | [`templates/DECISION_GATE.md`](../../templates/DECISION_GATE.md), [`templates/PROPOSAL.md`](../../templates/PROPOSAL.md), [`templates/QUESTION.md`](../../templates/QUESTION.md), [`templates/DECISION.md`](../../templates/DECISION.md), [`templates/REVIEW.md`](../../templates/REVIEW.md) |
| the reviewer's duty | [`workflows/DRIVE_REVIEW.md`](../../workflows/DRIVE_REVIEW.md) |

## Where the new rule meets existing ones

The `**Question:**` line and the A/B options already existed in the question template and the [logs workflow](../../workflows/LOGS.md). The first version of this rule added a pointer and a four-part reasoning (context, trade-offs, downstream impact, cost of deferring). The tightening replaces that reasoning with the full shape: prerequisites, eight lines for every option, a comparison table and the worst case. A gate written in the four-part form is an older gate under the new rule: it keeps working while a project lists it as missing the full shape, and it gets the full shape the next time it is touched.

## Decision gates

| ID | Question | Default applied | Why it is a real choice |
|---|---|---|---|
| `AW-D09` | **Question:** Must every gate carry the full reasoning, even a small one? A (Recommended): yes, one short line per part. B: only gates that change scope, security or anything public. Reasoning: [below](#reasoning-for-aw-d09) | A | Skipping the reasoning for small gates is faster, but it makes "small" a judgment each author makes alone |
| `AW-D10` | **Question:** May a reasoning line say it does not know a figure and what would settle it? A (Recommended): yes, written as Unknown and what would settle it. B: no, a gate waits until every figure is found. Reasoning: [below](#reasoning-for-aw-d10) | A | Requiring every cost and date unblocks nothing when the source does not hold them, and pressure to fill the gap produces invented figures |
| `AW-D11` | **Question:** Should the simple line be capped at 450 characters? A (Recommended): yes, so it fits one status row. B: no cap, the reviewer judges length. Reasoning: [below](#reasoning-for-aw-d11) | A | A cap is mechanical and checkable, but the number is a judgment and a rich gate may need splitting to fit |

### Reasoning for AW-D09

- **Context:** The rule asks for a plain answer and a full reasoning on every gate. Some gates are small, such as a name or a default, and a full section for them can feel like paperwork. The rule is new, so the habit has not formed either way.
- **Prerequisites:** None — the rule and its template exist, and a small gate can use them as they are.

#### Option A (Recommended): every gate, one short line per part

- **What it is:** Every gate keeps all parts and all eight lines per option. A small gate answers each in one short line, and a line with truly nothing to add says `None —` and why.
- **Unlocks:** One shape everywhere, so a reader and a checker never have to decide whether a gate was small enough to skip.
- **Blocks:** Skipping the reasoning on trivial gates.
- **Risks:** Small gates carry some padding. Low impact, and it is cheap to trim.
- **Effort:** About ten minutes for a small gate once the template is filled in (estimate).
- **Money:** None — a writing and checking rule, no new service.
- **Incompatible with:** Option B, and any checker that needs a size test to decide what to skip.
- **Needs first:** None — the template and the rule already exist.

#### Option B: only gates that change scope, security or anything public

- **What it is:** Gates outside those three kinds may keep a one-line question with no reasoning section.
- **Unlocks:** Less writing on trivial gates.
- **Blocks:** A single rule for the generator and the reviewer: each now has to classify a gate first.
- **Risks:** A gate that looked small turns out to matter and has no reasoning on record. Medium impact, and it is found only after the answer.
- **Effort:** Less per small gate, more for the classification step and its audit (estimate: a few minutes saved, an hour of rule work).
- **Money:** None — a writing rule, no new service.
- **Incompatible with:** Option A, and a generator that checks one rule everywhere.
- **Needs first:** A written test for which gates count as small, and a way to mark them.

#### Trade-offs

| Axis | A (Recommended) | B |
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

#### Option A (Recommended): allow Unknown, with what would settle it

- **What it is:** A line may read `Unknown —` followed by what would settle it, for example a quote or a measurement. A bare `unknown` is not accepted.
- **Unlocks:** Gates can be finished and asked now, with the gap shown honestly rather than guessed.
- **Blocks:** Nothing, except authors using Unknown to skip work, which the reviewer check catches.
- **Risks:** Unknown spreads across lines. Low to medium impact, because the reviewer rejects an Unknown that does not say what would settle it.
- **Effort:** None beyond the wording rule, which this change already adds.
- **Money:** None — wording only, no new service.
- **Incompatible with:** Option B.
- **Needs first:** The reviewer check in the drive and review workflow, which this change adds.

#### Option B: no, the gate waits until every figure is found

- **What it is:** A gate may not be presented until every cost, date and effect has a source.
- **Unlocks:** Complete figures on every gate that does get presented.
- **Blocks:** Most older gates, whose sources do not hold costs, until someone researches each one.
- **Risks:** Pressure to guess so a gate can move, which is the failure the rule exists to prevent. High impact on trust in the figures.
- **Effort:** Research for each gate, likely hours each (estimate).
- **Money:** Unknown — vendor quotes may be needed for some gates.
- **Incompatible with:** Option A, and any plan to back-fill a large set of older gates quickly.
- **Needs first:** A source for every figure.

#### Trade-offs

| Axis | A (Recommended) | B |
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

- **Context:** The simple line has to fit one row of a status view or an index. The owner asked for it to be short enough for a dashboard row but gave no number. The index currently shortens long cells, which can cut an option in half.
- **Prerequisites:** None — the cap is a number the generator reads.

#### Option A (Recommended): cap at 450 characters

- **What it is:** The simple line, not counting its pointer, may be at most 450 characters. A longer line is rejected and the gate is shortened or split.
- **Unlocks:** A line that always fits one row, so an index never cuts an option, and a limit a machine can check.
- **Blocks:** Long conditions on the line, which move to the reasoning.
- **Risks:** A rich gate is squeezed until its options turn vague. Low impact, because the reviewer's check that the line can be answered alone catches it, and the remedy is to split the gate.
- **Effort:** About two minutes to trim a line (estimate).
- **Money:** None — a number in a check, no new service.
- **Incompatible with:** Option B.
- **Needs first:** None — the generator reads the number.

#### Option B: no cap, the reviewer judges length

- **What it is:** No number. The reviewer decides whether a line is short enough.
- **Unlocks:** Lines with fuller options.
- **Blocks:** A mechanical length check, and a guaranteed fit in a one-row view.
- **Risks:** Lines grow until the owner has to read them closely, which defeats the first tier. Medium impact, and it builds up gradually.
- **Effort:** None — no change to the generator is needed.
- **Money:** None — nothing is built.
- **Incompatible with:** Option A, and any index that shows the full line without shortening.
- **Needs first:** None — nothing needs to change.

#### Trade-offs

| Axis | A (Recommended) | B |
|---|---|---|
| Fits one status row | Always | Not guaranteed |
| Checked by a machine | Yes | No |
| Room for detail on the line | Little, so detail goes to the reasoning | More |
| Risk of a vague option from squeezing | Some, caught in review | None |

- **Downstream impact:**
  - **Changes:** With A, the generator rejects longer lines in new gates and the index shows the whole line. With B, neither changes.
  - **Unblocks:** Neither answer blocks anything.
- **Cost of deferring:** The default applies, so new gates are held to 450 characters now. Older gates are not affected.
- **Worst case:** A is chosen and a good gate is rejected for being twenty characters over. It shows up as a failed check, and trimming or splitting fixes it in minutes.

## Rollout and rollback

Projects add the template to their gate workflow and a check to their index generator. Older gates are listed as missing the full shape until they are touched. Rollback is removing the new requirements from the generator; the reasoning sections stay valid as ordinary documentation.
