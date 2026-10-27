# Synthetic example: a save button

> **Status:** Fictional example; no live project or execution

Owner: “The save button does nothing. Keep the existing design.”

- **Changed:** Captured a reported UI bug; cause unverified. Existing design stays.
- **Needs your answer:** Nothing yet.
- **Next:** Inspect the existing bug/PR and reproduce with synthetic data.

Generated triage prompt:

```text
Item: Demo project / temporary save-button report; UI symptom, not yet a confirmed bug.
Conclusion: Investigate failed saves without redesigning the page.
Authority: Read-only triage under the user's request; follow actual project rules.
Read: project instructions, relevant save flow, bug records and current PRs.
Work: compare expected/actual behavior and safely reproduce with synthetic data.
If the cause crosses an authorization boundary, classify Security primary and UI secondary.
Acceptance: reproduction evidence or a specific remaining evidence gap; no invented cause.
HF: bounded log classification may fit if permitted; availability unknown; do not dispatch.
Review: capable agent checks evidence; one investigation pass, report new blockers.
Return: short conclusion, genuine owner choice if needed, complete next-stage prompt.
Delivery: prepared; no worker or external message sent.
```

A result such as “an existing PR fixes this, but keyboard acceptance is missing” produces a review/acceptance prompt, not another implementation. A new owner answer updates scope and the prompt version. Silence leaves questions pending.
