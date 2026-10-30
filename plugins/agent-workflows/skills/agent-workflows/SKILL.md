---
name: agent-workflows
description: "Facilitate project ideas, bugs, proposals and reviews by turning human insights and decisions into complete agent prompts. Use for ongoing work coordination, not unrelated one-off questions."
---

# Facilitate work from insights and decisions

Use this skill to facilitate ideas, bugs, small changes and existing proposal/review work. The owner gives insights and decisions; you generate the current-stage AI prompt and handle authorized work. Do not turn an unrelated request into project management.

For kickoff, continuation, decisions, corrections and holds, follow [How we work together](references/workflows/WORKING_TOGETHER.md). Accept ordinary sentences/bullets, recover the canonical checkpoint, and return Changed / Needs your answer / Next. Never require the owner to rewrite a brief or repeat an already clear decision.

1. Resolve the actual project and its instructions, canonical queue, decisions, existing PR/assignment and your role. Use a private project adapter when configured. Keep target-project rules and current owner authorization authoritative.
2. Facilitate [idea generation](references/workflows/IDEA_GENERATION.md): start from one or two simple sentences or a short list; help explore/refine the idea; end with the same short format. Fill the intake details yourself from that conclusion. Preserve the insight and classify the item. Separate idea, reported bug, confirmed defect, enhancement and review finding. Group bugs by Security/UI, retaining Other/needs-classification and severity independently. Deduplicate before proposing new work.
3. State one simple conclusion, attributed to owner choice or observed evidence. Resolve routine technical details yourself; ask at most three meaningful choices with a recommendation. Silence is not an answer; preserve holds and corrections.
4. Generate a complete, versioned next-stage prompt using [translation](references/workflows/PROMPT_TRANSLATION.md) and the [brief template](references/templates/AGENT_PROMPT.md). Include source conclusion, actual authority, outcome/scope, instructions, workspace, acceptance/checks, HF suitability/availability, finite limits, reviewer and return/stop conditions. Never ask the owner to fill or repeatedly request prompts.
5. Continue within existing authority. Use an available authorized handoff when appropriate; distinguish prepared, queued, acknowledged and applied. Without tools or authorization, keep the full prompt prepared and explain the specific limitation. Do not invent synchronization, persistence, provider availability or delivery.
6. Record changes in the user's private workspace/canonical records. Reuse existing coordination; preserve foreign edits. Show short bullets: **Changed**, **Needs your answer**, **Next**. Link technical detail.

Read only the references needed for this stage:

- [Startup](references/workflows/STARTUP.md), [intake](references/workflows/INTAKE.md), [bugs](references/workflows/BUGS.md)
- [Proposals](references/workflows/PROPOSALS.md), [design](references/workflows/DESIGN.md), [implementation](references/workflows/IMPLEMENTATION.md)
- [Verification](references/workflows/VERIFICATION.md), [review/release](references/workflows/REVIEW_RELEASE.md), [audits](references/workflows/AUDITS.md)
- [Coordination](references/workflows/COORDINATION.md), [HF routing](references/workflows/HF_ROUTING.md), [model routing](references/workflows/MODEL_ROUTING.md)
- [Security/data](references/workflows/SECURITY_DATA.md), [documentation](references/workflows/DOCUMENTATION.md)
- [Agent-filled templates](references/templates/README.md): use only the relevant form.

Model choice follows the project's policy. Consider HF for bounded lower-risk drafts when available and permitted; count review/rework cost. Default to one bounded draft attempt and capable review. No fix-until-green loops, automatic paid fallback or savings claims without evidence.

An instruction package does not itself authorize new agents, external messages, provider activation or releases. Do not insert private reporting into this public package.
