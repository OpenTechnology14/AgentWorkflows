# Decision gate

> **Status:** Agent-filled template · Both tiers are required ([decision gates](../workflows/DECISIONS.md)). Replace every `[[...]]`; a gate that still holds one is rejected. Delete option C if there is no third real choice.

## Tier 1: the simple answer

Put this on one line in the gate's table row (or one option per line in a standalone question). Write it for someone who has never seen the project: no gate IDs, file names, paths, links or code spans, and no term a new reader would have to look up.

**Question:** [[one sentence, at most 25 words, ending in a question mark]] A (Recommended): [[what happens, in a short phrase and what it leads to]]. B: [[what happens]]. C: [[only for a third real choice]]. Reasoning: [below](#reasoning-for-[[gate-id-in-lower-case]])

Nothing follows the pointer. A is the owner's or the source's recommendation; if the source records none, say so in the Context line below and that A is the author's suggestion.

## Tier 2: the full reasoning

Put this in the same document as the gate. The options keep the letters, order and names used above.

### Reasoning for [[Gate ID]]

- **Context:** [[what is being decided and why now; what is already decided, with links; what makes it a real choice; and, if the source records no recommendation, that A is the author's suggestion]]
- **Prerequisites:** [[what must be true before this can be acted on at all, whichever option is chosen; or `None —` and why]]

#### Option A (Recommended): [[short name]]

- **What it is:** [[what would actually be done, in two or three plain sentences]]
- **Unlocks:** [[what becomes possible, cheaper or safer]]
- **Blocks:** [[what it rules out or makes harder]]
- **Risks:** [[what could go wrong, how likely, how bad, and whether it can be undone]]
- **Effort:** [[who does what, and roughly how long; say when it is an estimate]]
- **Money:** [[the cost in dollars, or `None —` and why there is no spend]]
- **Incompatible with:** [[other options, decisions, tools or limits it cannot sit beside; or `None —` and why]]
- **Needs first:** [[what must be true or done before this option can be carried out]]

#### Option B: [[short name]]

- **What it is:** [[...]]
- **Unlocks:** [[...]]
- **Blocks:** [[...]]
- **Risks:** [[...]]
- **Effort:** [[...]]
- **Money:** [[...]]
- **Incompatible with:** [[...]]
- **Needs first:** [[...]]

#### Option C: [[short name; delete this option if there is no third real choice]]

- **What it is:** [[...]]
- **Unlocks:** [[...]]
- **Blocks:** [[...]]
- **Risks:** [[...]]
- **Effort:** [[...]]
- **Money:** [[...]]
- **Incompatible with:** [[...]]
- **Needs first:** [[...]]

#### Trade-offs

At least two axes, usually three to six, that actually separate these options. One column per option, each headed by its letter, the recommended one marked.

| Axis | A (Recommended) | B | C |
|---|---|---|---|
| [[axis]] | [[short phrase]] | [[short phrase]] | [[short phrase]] |
| [[axis]] | [[short phrase]] | [[short phrase]] | [[short phrase]] |
| [[axis]] | [[short phrase]] | [[short phrase]] | [[short phrase]] |

- **Downstream impact:**
  - **Changes:** [[files, rows, decisions, projects or public things that change with each answer; name them]]
  - **Unblocks:** [[the work and decisions that can proceed afterwards; name them]]
- **Cost of deferring:** [[what stays stuck or breaks while the gate is open; what can proceed meanwhile and under what authority; any default applied; when waiting starts to cost something]]
- **Worst case:** [[the worst realistic outcome if the recommended option is wrong, how it would show up, and how to undo it or limit the damage]]

Never invent a figure. Where the source does not give one, write `Unknown —` and what would settle it. A bare `none`, `n/a` or `tbd` is not an answer.
