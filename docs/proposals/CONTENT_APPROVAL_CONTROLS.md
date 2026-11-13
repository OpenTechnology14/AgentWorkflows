# Content approval and reporting controls

**Kind:** simple change · **State:** Local implementation verified; release/adoption open · **Date:** 2026-10-31

The owner requested social content controls connected to this workflow library and private
Agent reporting. This public library supplies a generic procedure and adapter contract;
the target application owns channel/account state, concept revisions and execution.
Live portfolio details remain in the private deployment and target project.

First slice: a source-backed concept workflow, an agent-filled adapter template, discovery
from the entrypoint/index and regenerated packages. No credentials, scheduler, account
service, automatic dispatch or second canonical queue. Existing project-reference PR work
is preserved; this branch starts from main `b70913d`.

Acceptance: discover target controls, submit a draft, present it, apply an explicit
revision-bound owner decision, read it back, prepare production and report actual progress.
Concept approval must not become publication approval; source instructions stay inert;
disconnected tools must produce an honest prepared/blocked state. Synthetic scenarios
cover these transitions. Target CLI execution evidence belongs in its own proposal.

Validation: package build, verifier, unit suite and synthetic scenario review. No host
installation, account connection, public publishing or audience results are claimed.
Rollback the workflow/template/package references together; preserve private decisions.
HF considered: bounded source summaries may fit with capable review; approval, routing
and release judgment do not. Availability unverified; no paid call or dispatch.
Next prompt: review the concrete workflow/package diff against these boundaries and the
target adapter's actual CLI results, then record missing host/provider acceptance.


Verification (2026-10-31): `python3 scripts/build.py` passed (42 generated files), `python3 scripts/verify.py` passed (111 local links), and `python3 -m unittest discover -s tests -v` passed all 14 packaging tests. The target adapter completed a real isolated CLI submit/approve/brief/edit/stale-rejection cycle. Synthetic workflow scenarios were checked against those controls; model behavior, host installation, account access and publishing were not exercised.
