# Prompt translation — the facilitator does the writing


The owner supplies insights and decisions. The facilitator generates and maintains the AI instructions for each item as it moves through the work. Never require the owner to fill a template, choose a tool/model, copy a brief between agents, or say “turn this into a prompt” at each step. Technical interpretation, source gathering, canonical routing, task decomposition and prompt writing are agent work.

## Short idea conversation → complete intake

Start and finish exploration with one or two simple sentences or a short bulleted list. The facilitator helps generate/refine the idea, then expands that conclusion into the agent-filled intake and next prompt. Keep technical details behind links; do not ask the owner to complete a form. See [idea generation](IDEA_GENERATION.md).

## One intake, different kinds of work

Capture ideas, bug reports, simple changes, proposal remainders, review findings, audit findings and housekeeping (one Kind each; see [work types](WORK_TYPES.md)) from any **available, authorized** source: this conversation, a project coordinator, an existing issue/PR or project documents. “Anywhere” does not grant access to an unconnected app, start monitoring, or authorize sending private content elsewhere. If the project/source is ambiguous, keep an unassigned intake note and ask only what cannot be inferred.

Idea generation includes improving broken behavior and small adjustments. Keep the original report distinct from a proposed solution: “button fails” is a reported bug; “use a dropdown” is a change idea until evidence establishes a defect. Reuse an existing item when the outcome matches. If an item's proposal already exists, enter at its actual stage instead of restarting idea generation. the private idea inbox is the intake view, the private bug view groups defects, and the project's existing queue retains implementation authority.

## The conclusion drives the next prompt

For each active item, maintain this small translation record beside its canonical record or in the private generated-prompt index:

```text
Item: project + canonical ID/source key (temporary source key if intake is not allocated)
Kind: idea | bug | simple change | proposal remainder | review finding | audit finding | housekeeping
Bug group: Security | UI | Other/needs classification | not a bug (file under another Kind)
Bug state: reported | confirmed | n/a
Insight: exact safe owner words or attributed source; date/revision
Evidence: observed facts, documented claims and unknowns kept separate
Conclusion: one plain sentence, attributed to owner or agent evidence
Authority: existing approved scope; any unresolved boundary; source link
Stage: intake | explore/triage | decide | plan | implement | review | acceptance | close
Next prompt: stable item/stage/version + actual complete prompt path
State: prepared | blocked | queued | acknowledged | applied | superseded
Replaces: prior prompt version and reason, or none
```

An owner conclusion such as “smallest version, no notifications” becomes explicit scope and acceptance criteria. An agent's evidence conclusion such as “this already has a PR” changes the next prompt to review that PR; it is not an owner product decision. “Later” parks dependent work. Silence supplies no conclusion. Existing approval covers routine choices within its scope; avoid asking the owner to approve each technical step.

## Generate the right prompt at each transition

The facilitator fills the [complete brief contract](../templates/AGENT_PROMPT.md), then adds the appropriate instructions below. These are **agent obligations**, not a form for the owner.

| Current item / event | Generated AI prompt must ask for | Next output / transition |
|---|---|---|
| New idea or simple change | Read surrounding behavior and sources; deduplicate; describe intended outcome and smallest useful options; identify actual constraints | Evidence-backed recommendation; ask a product choice only if necessary |
| Reported bug | Record actual/expected behavior and reproduction context; determine Security/UI/other; investigate safely; find canonical bug/parent; do not assume the suggested cause | Confirmed defect, duplicate, already fixed, needs evidence, or change request; preserve severity and gates |
| Proposal/PR encountered | Compare canonical scope, main, current PR and acceptance evidence; identify remaining work and existing answers | Reuse work; generate review/remaining-slice/acceptance prompt, not a duplicate build |
| Choice genuinely needed | Present at most three portfolio questions with concrete options/recommendation; source/ID and specific blocked slice | Owner's plain answer → exact recorded conclusion → revised prompt; no repeated approval |
| Direction settled | Expand conclusion into project SOP/template, allowed paths, dependencies, done conditions, tests, rollout/rollback and existing authority | Bounded implementation prompt if authorized; otherwise a prepared plan with the precise missing boundary |
| Implementation authorized | Execute one scoped slice using existing assignment/worktree; preserve constraints; test relevant behavior; return evidence and residual failures | Generate a reviewer prompt against the actual diff and owner conclusion |
| Review finding | Classify bug vs scope change, severity and existing parent; generate repair prompt only within authority | Verified fix then targeted re-review; bounded iteration, no HF fix-until-green |
| Housekeeping item | Read the records, tests or tooling involved; confirm nothing changes behavior, access, data or a public contract (otherwise reclassify); name the check that proves it done; keep to the stated records | Done with named evidence, or reclassified. Never a way around review or security gates |
| Review passed but live/manual proof absent | Prepare the exact acceptance checklist, target and prerequisites; show the owner only their necessary action/choice | Local/source completion remains distinct from release/production acceptance |
| Acceptance complete | Reconcile proposal/bug/queue evidence together; summarize outcome; generate next authorized item's prompt | Close only with proof; retain pending questions/holds and release gates |

On **every material answer, finding, result or source revision**, refresh the item and write its next concrete prompt without waiting for the owner to request translation. Do not generate speculative future-stage prompts for the whole dormant backlog. Every handled item gets a current prompt or a precise blocked/held record; unchanged input does not generate another version or consume another model call.

## Carry the work forward

The facilitator can execute authorized work in the current chat. If an existing authorized T3 handoff is available, deliver the complete prompt, record the receipt and check acknowledgement. Do not make the owner copy it. If external/coordinator messaging is not authorized or unavailable, leave the prompt prepared and report the exact delivery limitation once; prompt generation still completes. This workflow instruction alone does not authorize new workers, external messages, paid calls or merges. Never claim a file write means a coordinator received it.

Workers return findings and proposed record updates to the same coordinator. One facilitator serializes shared writes. Before changing a prompt for a running assignment, inspect its state and use an authorized steer/stop path; do not launch a second writer. Retain prior versions in Git or the canonical history, and preserve superseded owner conclusions. A stale or conflicting source blocks only its dependent slice.

Every generated prompt includes HF consideration, actual availability, data limits, finite effort/attempt limits, fallback and a capable reviewer. A source-extraction draft may qualify; security judgment, owner decisions and final acceptance do not move to HF merely to save usage. [HF routing](HF_ROUTING.md) remains authoritative with each project's policy.

## What the owner sees

```text
You said: <short insight or answer>.
Conclusion: <plain result and scope>.
Next: <one action the agent will take; prepared/working/blocked accurately>.
Need you: <one genuine choice, or nothing>.
```

Keep prompt mechanics behind links unless requested. Prefer T3's native question controls when supported; otherwise ask the same plain question in chat. Pending questions stay in the running list. No automatic synchronization from Markdown into T3 question cards is claimed.

## Examples of translation (hypothetical)

- “The save button does nothing.” → bug intake, UI symptom; generate reproduction/triage prompt. Do not invent a cause or request redesign approval. If investigation finds a tenant authorization defect, Security becomes primary and UI remains a tag.
- “Make labels a dropdown; keep everything else.” → simple change, minimal scope; deduplicate against label PRs, then generate the appropriate review/implementation prompt under actual authority.
- “Yes, smallest version, no emails.” → save that exact conclusion; generate the next scoped prompt with email sends excluded. Do not ask the owner to write it.
- “Add boundary tests; no behavior change.” → housekeeping: no feature and no defect; name the test run that proves it, and reclassify if a test exposes a defect.
- “Reword every open decision as one question.” → housekeeping (a format pass over records); check that no decision text was removed.
- “This is already fixed.” → verify linked proof; generate closure reconciliation, not another implementation task.
