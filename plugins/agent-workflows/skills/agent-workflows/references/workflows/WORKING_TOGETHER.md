# How we work together

> **Status:** Owner interaction guide and facilitator response contract · **Reviewed:** 2026-10-30

Use ordinary language in the existing project coordinator or the current chat. A sentence or two or a short bulleted list is enough. These examples are suggestions, not required commands. The owner gives insights, priorities, limits and decisions; the facilitator handles investigation, intake, technical prompts and authorized follow-through.

## What you give and what the agent does

| You want to… | You can say… | Agent response and action |
|---|---|---|
| Start existing work | “Start the proposal review for this project. Show what remains and the choices you need from me.” | Read current sources, decisions, queue and PRs; summarize scope and next action; generate the review brief and perform authorized review. |
| Start a new outcome | “For the demo project, make saving clearer. Keep the current layout.” | Reflect outcome/limits, check existing work, fill intake and generate the appropriate next prompt. An explicit work request already authorizes its stated scope; apply the project's existing gates. |
| Explore an idea | “Saving feels confusing. Help me think it through.” | Help develop the idea, offer useful alternatives only when needed, and finish with a short outcome/scope/limits conclusion. Fill intake from that conclusion. |
| Continue work | “Continue the proposal review.” / “Continue this.” | Recover the latest canonical checkpoint, actual changes/PR state, prior decisions and blockers. Resume the next authorized step and regenerate a stale prompt. No need to retell the whole conversation. |
| Give a decision | “Q2: A, but no emails.” / “Use the smallest version and keep the current layout.” | Match the actual question/context, preserve exact words, read back the practical consequence and update scope/acceptance/next prompt. Continue without asking for the same decision again. |
| See pending choices | “What needs my decision?” | Show up to three relevant pending questions, each with its ID, concrete options, a recommendation and a short consequence; retain the rest. “Nothing right now” is a valid result. |
| Correct direction | “Change my last decision: keep the current layout.” | Preserve the earlier decision as superseded, update affected records/prompts, and verify any active assignment is steered before claiming it changed. |
| Park or stop | “Park this idea.” / “Stop work on this task for now.” | Record the requested hold, preserve unfinished work and pending questions, use an available authorized stop route where needed, and report the actual stop/delivery state. |
| Resume a hold | “Resume the save-feedback task; keep the previous limits.” | Resolve the named hold and refresh evidence before continuing within its authority. “Continue” on one task does not reopen unrelated held topics. |

## Minimum needed to align

- **Project or task**, if it is not already clear. A name, existing item/PR link or description is enough; the agent finds the canonical ID.
- **Desired outcome or insight**, in your words. A bug symptom, rough possibility or small change is valid input.
- **Limits or preferences you care about**, if any: “smallest version,” “no emails,” “keep the layout.” You do not have to invent constraints.

For continuing, just identify the work if context is unclear. For a decision, an option or plain answer is enough. Include the question ID when several questions/projects are in play; `1A, 2B` is valid only against the latest displayed set. The agent asks one concise clarification if the intended item, version or meaning cannot be inferred. It does not guess between conflicting choices or require technical forms, model names, acceptance checklists or copy/pasted agent prompts.

## What the agent returns

Use short bullets by default:

- **Changed:** Confirm the understood outcome and limits at kickoff; during work, report actual progress or the exact decision and practical consequence. Do not claim an unsaved record, unrun check or undelivered handoff.
- **Needs your answer:** Only meaningful unresolved choices, with a recommendation and consequence. State “Nothing right now” when the agent can proceed. Preserve unanswered IDs; silence supplies no answer.
- **Next:** One concrete action and its real state—working, prepared or blocked. Name the specific dependency if blocked, and continue independent authorized work.

Keep technical detail and the generated brief behind links unless requested. For a decision, the readback is: “You chose X. That means Y. Next: Z.” A clear answer does not need a second confirmation. Technical interpretation and routine choices remain agent work.

Example kickoff response:

- **Changed:** Goal is clear save feedback; the existing layout stays.
- **Needs your answer:** Nothing right now.
- **Next:** Inspect the current save flow and related work, then generate its triage prompt.

## One conversation, persistent work

The agent maintains canonical work, the idea/question/decision views, the current generated prompt and an evidence-backed next checkpoint in the configured private workspace. When resuming, it reads those sources rather than assuming chat memory or replaying finished stages. If access or persistence is unavailable, it states the gap and keeps a clearly temporary summary/prompt in the chat.

The [short idea process](IDEA_GENERATION.md) leads into [intake](INTAKE.md) and [prompt translation](PROMPT_TRANSLATION.md). Existing work enters at its current stage. Bugs are grouped by Security/UI, retaining other defects; reports, confirmed defects and desired changes remain distinct. Existing project rules, approvals and holds govern execution. Selection of behavior, implementation authority and release authority are recorded separately; do not invent permission for an unrelated merge, send or deployment.

## A complete small example

1. You: “Help me make saving clearer. Keep the layout.”
2. Agent: Briefly reflects the goal, investigates and offers only useful alternatives or a genuine unresolved choice.
3. You: “Use a small status message. No emails.”
4. Agent conclusion: “Show an inline success/error result after Save; keep the layout and exclude emails.”
5. Agent: Records that conclusion, fills intake, reuses any matching parent/PR and generates the next prompt. It continues within the actual work request/approval, reporting any genuine remaining boundary.
6. Later, you: “Continue the save-feedback work.” The agent refreshes its checkpoint and resumes; you do not rewrite the brief.
