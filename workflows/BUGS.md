# Bug creation, Security and UI

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- Group bugs primarily by Security and UI. Use Security for auth, permissions, tenant isolation, secrets, exposure and vulnerabilities; UI for interaction, layout, accessibility and visible presentation. Preserve both tags when needed, Security primary for a security boundary.
- Retain reliability/data/build defects in Other/needs-classification. Category does not set severity, approval or queue order. A UI symptom can have a server or security root cause.
- Capture expected/actual behavior, revision/build, environment, preconditions, safe reproduction, affected roles/resources, frequency, impact, severity rationale and source. Keep unverified reports clearly labeled.
- Search canonical bug, security, audit and proposal records plus current PRs. Keep existing legacy IDs stable; allocate new IDs only under the target's rules. Add stable anchors when its tracker supports them.
- Distinguish product defect, bad fixture, missing configuration, stale documentation, enhancement and missing test execution. Only a product defect is a bug: stale documentation, a missing test run or a bad fixture is housekeeping (an audit finding when a scan found it), and an enhancement is a simple change ([work types](WORK_TYPES.md)). Fixed historical entries are regression references, not new open bugs.
- A small fix still needs a canonical parent and observable acceptance. Security/data/migration/integration impact may require the full proposal depth despite a short diff.
- Generate triage, repair, review or acceptance prompts from actual findings. No new owner question for a routine repair already within authority; ask only an unresolved behavior/risk/operational choice.
- Close only when implementation, reproduction/regression evidence, queue and tracker agree. Source patch, green CI and deployed safety are distinct; preserve residual gaps and mitigation status.
