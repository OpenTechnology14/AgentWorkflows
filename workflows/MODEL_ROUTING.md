# Model routing and usage

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- Read the target's model/skill policy and actual available provider catalog. Do not hardcode a universal model tier, infer credentials from a catalog, or quote current prices from memory.
- For each assignment, record HF considered, suitability, actual availability, reason, data boundaries, finite limits, reviewer and fallback. Use workflows/HF_ROUTING.md as the shared detailed contract.
- Bounded extraction, classification and pattern-based drafts may suit HF when review/rework cost justifies them. Security, architecture, cross-project judgment and acceptance use the project's capable route.
- Never fragment a complex task to bypass routing rules. Development-assistant routing does not change the product's own model or “no AI” behavior.
- Default to one bounded HF draft attempt with tool/time/output limits and capable review. No HF/Ollama fix-until-green loops; preserve work and escalate on failure/timeout/empty output/scope growth.
- Compare whole-task effort including setup, retries, review and rework. Label estimates vs measured usage; no promised savings or free/unlimited claim without evidence.
- Refresh only selected context and regenerate only materially changed prompts. Unchanged snapshots, dormant backlog pre-generation and repeated idle wakes consume usage without progress.
