# Proposal — <outcome>

> **Status:** Agent-filled template · Use the target project's SOP and canonical IDs

## 1. Outcome and authority

Source intake, canonical parent, actual approval/readiness, expected measurable result.

## 2. Scope and decisions

In/out of scope; exact owner conclusions, assumptions, unresolved choices and holds.

Each unresolved choice is a decision gate with both tiers, copied from the [decision gate template](DECISION_GATE.md) and governed by `workflows/DECISIONS.md`:

- Tier 1, on one line in the gate's row: **Question:** one short plain sentence. A (Recommended): ... B: ... C only if needed. Reasoning: link to the section below.
- Tier 2, a section `### Reasoning for <gate ID>` here: Context, Prerequisites, then for every option what it is, unlocks, blocks, risks, effort, money, what it is incompatible with and what it needs first; a trade-offs table; downstream impact (changes, unblocks); cost of deferring; and the worst case if the recommendation is wrong.
- Default applied until answered, and its authority (exploration or drafting only).

## 3. Verified current state

Claim / classification / revision and evidence / consequence. Separate source and live proof.

## 4. User and system paths

Actor / trigger / entry / success / denied/failure/recovery / cleanup.

## 5. Design and architecture

Ownership, interfaces, states, trust boundaries and appropriate diagram/contracts.

## 6. Exact injection map

File / stable symbol or heading / create-update-remove / dependencies / example / verification / rollback.

## 7. Contracts and examples

Representative types/API/schema/config/UI and realistic fixtures; buildable typed structures where required.

## 8. Security, data and integrations

Roles/tenants/privacy; exact live target, setup, round trip, disconnect/cleanup; migration/preflight/ledger where applicable.

## 9. Outcomes and pressure

Scenario IDs, expected outcome, test/evidence location; count/retry/concurrency/stale/offline/interruption paths.

## 10. Rollout and rollback

Compatibility, migration/backfill, flags, observability, cleanup and failure stop conditions.

## 11. Phases and first slice

Dependencies, one bounded first outcome, exact allowed paths, assigned owner and existing PR.

## 12. Release gates and proof

Local/source/live distinctions, required checks, reviewer, actual status and completion criteria.

## 13. Generated next prompt

Conclusion, stage/version, HF suitability/availability, finite usage, reviewer, delivery state and stop condition.

For every inapplicable section, state why. Agent fills this; owner does not.
