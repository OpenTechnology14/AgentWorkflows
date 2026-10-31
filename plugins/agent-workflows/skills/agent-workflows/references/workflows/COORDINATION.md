# T3, ordinary agents and standups

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- In T3, the existing coordinator actively facilitates idea generation: accept a short insight, help explore/refine it, and finish with one or two sentences or a short bulleted conclusion. The coordinator translates it into intake and the next prompt; see [idea generation](IDEA_GENERATION.md). Do not require an implementation-ready idea from the owner.
- Reuse one existing coordinator per project and current assignments. The facilitator translates owner insights/decisions into full worker/reviewer prompts and handles authorized handoffs; the owner does not copy prompts.
- Verify actual provider/model/tool availability and writing-worktree isolation before launch. Children receive the supplied brief; do not assume inherited context or shared permissions.
- Track prepared, queued, acknowledged, applied and uncertain separately. Inspect existing state before retrying a lost response; avoid duplicate workers and overlapping writers.
- Steer active work only through an authorized route; verify stop/acknowledgement before replacing ownership. Preserve unfinished edits.
- On standup, show changed, needs your answer and next, with at most three simple choices total across requested projects. Keep stable qualified IDs and exact answers.
- Prefer native question controls when available, plain-chat fallback otherwise. Markdown records do not automatically become T3 cards; runtime verification is separate from docs review.
- If configured separately, hourly finalization closes active intervals and preserves unanswered questions. It never grants approval, starts backlog work or keeps waking idle projects. Do not install a competing timer.
- This library includes no T3 server, provider connection or scheduler. Configure and verify any runtime separately; installing instructions does not create workers or services.
