# Idea generation with the facilitator

> **Status:** Maintained workflow · Human-facing start and finish are brief

Start with one or two ordinary sentences or a short bulleted list. A rough insight, bug symptom or small improvement is enough. The facilitator can help discover and refine the idea; the owner does not need a finished solution or technical intake form.

- In T3, use the existing project coordinator as the facilitator. Read the current project reference and selected source records before exploring; retain the project's holds and actual authorization. The same conversation process works in another capable agent.
- Reflect the desired outcome briefly, label agent suggestions, and offer up to three useful possibilities only when alternatives help. Ground suggestions in available project context. Ask the smallest question that changes direction; do not turn every suggestion into a pending decision.
- Improve the idea together through short replies. Investigate routine technical unknowns independently. Distinguish the owner's choice from the agent's evidence conclusion. Keep unselected ideas available without filling the work queue.
- Finish with one or two sentences or a short bulleted list: intended outcome, smallest useful scope, explicit limits and any real unresolved choice. Mirror the owner's wording; preserve corrections. This is the idea conclusion, not a long proposal.
- The agent then fills the [intake record](../templates/INTAKE.md): original insight, project/source, kind, evidence, duplicate/parent check, conclusion, limits/authority and next prompt. Expand technical detail behind the link. Route a bug under Security/UI/Other and the project's intake rules.
- Attach existing work if it already covers the outcome. Generate the current next-stage prompt through [translation](PROMPT_TRANSLATION.md). A conclusion can lead to exploration, triage, an existing PR review, a proposal or a hold; it does not automatically approve implementation or release.
- Preserve unanswered questions and parked ideas. If files/tools are unavailable, provide the short conclusion and complete prepared prompt in chat, and state the persistence gap. No new background service or speculative backlog generation is needed.

Example start: “Saving feels confusing. I want to know whether my change worked.”

Example finish:

- Show a clear success or failure result after Save.
- Keep the existing layout; no new notifications.

The facilitator translates that conclusion into intake, deduplicates existing work and prepares the appropriate investigation/design prompt. The owner does not write the technical brief.
