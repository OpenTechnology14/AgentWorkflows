# Direct references and short idea facilitation

> **Status:** Owner-requested implementation · **Date:** 2026-10-27

Owner wants connected projects to directly reference the workflow source and detect drift, while T3 helps generate/refine ideas that start and finish with a sentence or two and/or short bullets.

## Injection and contract

- `workflows/IDEA_GENERATION.md`, intake/translation/coordination and templates: short opening → collaborative exploration → short conclusion → agent-filled canonical intake → next prompt. Project authority and idea-vs-approval distinctions persist.
- `workflows/PROJECT_REFERENCE.md`, `docs/PROJECT_INTEGRATION.md`, `scripts/project_reference.py`: immutable reference records, content hashes, explicit upstream drift/unavailability and a generated read-only CI adapter.
- Consuming project guides/locks/checks: source pointers and minimal fallback, without copying private inventory or generic workflows into this public repo.
- Packaging manifest/entrypoint/generated outputs: same procedure in skill, plugin and chat pack; version 0.2.0 candidate.

## Verification and release

Test current/changed/missing sources, invalid paths/records, different upstream, unavailable remote and unchanged generation. Project records must contain no local paths or secrets; all consumers use one accepted revision. A source commit awaiting merge is a visible dependency. CI/startup checks detect drift; they are not automatic model execution or universal file synchronization. No new scheduler, worker sends or product approvals.

Short owner examples and manual scenarios cover idea, bug, small change, existing parent, ambiguous choice, parked work and missing tools. Offline tests prove mechanics; fresh T3/host behavior remains separately evidenced. Preserve owner records on rollback and restore only the accepted workflow revision/pointers.

## Owner interaction guide — 2026-10-30

Owner asked how to kick off, continue and give decisions, and requested documentation of both their input and the agent response needed to align. `workflows/WORKING_TOGETHER.md` now supplies ordinary-language examples, minimum project/outcome/optional limits, checkpoint recovery, question matching, decision readback, corrections/holds and Changed / Needs your answer / Next responses. README, usage and packaged facilitator entrypoint point directly to it; the manifest includes the same guide in all compiled formats. Existing source/adoption references are refreshed together; no new coordinator, live dispatch or merge authority. Validation uses package/reference gates and manual conversation scenarios; no new prose-matching unit tests.
