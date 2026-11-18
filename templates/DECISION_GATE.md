# Decision gate

> **Status:** Agent-filled template · Both tiers are required ([decision gates](../workflows/DECISIONS.md)). Replace every `[[...]]`; a gate that still holds one is rejected. Use two to four options and delete the ones you do not need.

## Tier 1: the simple answer

Put this on one line in the gate's table row, or as a standalone question. Nothing else goes in it: no options, no pointer, no explanation. Write it for someone who has never seen the project: no gate IDs, file names, paths, links or code spans, and no term a new reader would have to look up.

**Question:** [[one sentence, at most 25 words, ending in a question mark]] **Suggested:** [[one to three words]]

The suggested words name the recommended choice and name exactly one option below, either by letter (`Option B`) or by that option's name. If the source records no recommendation, the suggestion is the author's: say so in the Context line below.

## Tier 2: the full reasoning

Put this in the same document as the gate. The heading text is exactly `Reasoning for` and the gate's ID, because the index finds the section by it. Each option name is one to three words. Add `(Suggested)` to the heading of the option the suggested words name, and to its column in the Trade-offs table; no other option carries it.

### Reasoning for [[Gate ID]]

- **Context:** [[what is being decided and why now; what is already decided, with links; what makes it a real choice; and, if the source records no recommendation, that the suggestion is the author's]]
- **Prerequisites:** [[what must be true before this can be acted on at all, whichever option is chosen; or `None —` and why]]

#### Option A: [[name, one to three words]]

- **What it is:** [[what would actually be done, in two or three plain sentences]]
- **Unlocks:** [[what becomes possible, cheaper or safer]]
- **Blocks:** [[what it rules out or makes harder]]
- **Risks:** [[what could go wrong, how likely, how bad, and whether it can be undone]]
- **Effort:** [[who does what, and roughly how long; say when it is an estimate]]
- **Money:** [[the cost in dollars, or `None —` and why there is no spend]]
- **Incompatible with:** [[other options, decisions, tools or limits it cannot sit beside; or `None —` and why]]
- **Needs first:** [[what must be true or done before this option can be carried out]]

#### Option B: [[name, one to three words]]

- **What it is:** [[...]]
- **Unlocks:** [[...]]
- **Blocks:** [[...]]
- **Risks:** [[...]]
- **Effort:** [[...]]
- **Money:** [[...]]
- **Incompatible with:** [[...]]
- **Needs first:** [[...]]

#### Option C: [[name, one to three words; delete this option if there is no third real choice]]

- **What it is:** [[...]]
- **Unlocks:** [[...]]
- **Blocks:** [[...]]
- **Risks:** [[...]]
- **Effort:** [[...]]
- **Money:** [[...]]
- **Incompatible with:** [[...]]
- **Needs first:** [[...]]

#### Trade-offs

At least two axes, usually three to six, that actually separate these options. One column per option, each headed by its letter, the suggested one marked.

| Axis | A | B | C |
|---|---|---|---|
| [[axis]] | [[short phrase]] | [[short phrase]] | [[short phrase]] |
| [[axis]] | [[short phrase]] | [[short phrase]] | [[short phrase]] |
| [[axis]] | [[short phrase]] | [[short phrase]] | [[short phrase]] |

- **Downstream impact:**
  - **Changes:** [[files, rows, decisions, projects or public things that change with each answer; name them]]
  - **Unblocks:** [[the work and decisions that can proceed afterwards; name them]]
- **Cost of deferring:** [[what stays stuck or breaks while the gate is open; what can proceed meanwhile and under what authority; any default applied; when waiting starts to cost something]]
- **Worst case:** [[the worst realistic outcome if the suggested option is wrong, how it would show up, and how to undo it or limit the damage]]

Never invent a figure. Where the source does not give one, write `Unknown —` and what would settle it. A bare `none`, `n/a` or `tbd` is not an answer.
