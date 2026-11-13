# Proposal creation and refresh

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- A proposal is an evidence-backed implementation contract, not a brainstorm. Start with templates/PROPOSAL.md, then adapt to the target project's exact SOP/template and registry fields.
- Read current instructions, relevant skills, code, types, tests and existing proposals before drafting. Prefer an existing canonical parent; do not approve a pending proposal by generating it.
- State outcome, scope/non-goals, source intake, actual authority, assumptions, decisions and current evidence with revision/date.
- Name exact files, stable symbols/headings, dependencies, intended changes, representative contracts/examples and rollback. Prose field lists are insufficient for typed data/template work.
- Cover affected user/admin/API paths, actors/roles/tenants, integrations, persistence, cleanup and denied paths. Include click outcomes, empty/loading/error/success states and responsive/accessibility behavior when relevant.
- Cover repeated actions, counts 0/1/many/limit, concurrency, retry/replay, stale state, offline, interruption and recovery where the change makes them possible.
- Include schema ownership/types, migration order/applied state, compatibility, idempotency, RLS, pre/postflight and rollback for data work. Use workflows/SECURITY_DATA.md and the target's migration SOP.
- Distinguish local/source completion from real provider, device, live acceptance or release proof. State observability, rollout, rollback, dependencies, phased work and an exact first reviewable slice.
- Register/update the target queue, canonical registry, source backlink and navigation together. Keep model recommendation/rationale under the target policy and HF consideration under actual suitability.
- Mark genuinely inapplicable sections with a reason. Scale compact low-impact changes to the project's supported small-change contract; do not use reduced paperwork to omit security/data effects.
- Validate paths, links, claims, completeness and consistency, then generate the next design/implementation/review prompt from the conclusion and actual authority.
