# Work types — one Kind per item

> **Status:** Maintained reusable procedure · Target-project rules retain authority

Every item that enters [intake](INTAKE.md) gets exactly one **Kind**. Kind says what the work *is*. It does not set priority, severity or approval, and it is separate from the bug group, the item's state and its stage. Register the item under its Kind before work starts ([entry gate](ENTRY_GATE.md)).

Kinds: idea, bug, simple change, proposal remainder, review finding, audit finding, housekeeping.

| Kind | Use it when | Not this |
|---|---|---|
| idea | A rough insight or possibility. Nothing is requested yet and nothing is known to be broken | A request to change something specific is a simple change |
| bug | Observed behavior differs from expected behavior. State is *reported* until evidence confirms it, then *confirmed*. Group it Security, UI or Other/needs-classification ([bugs](BUGS.md)) | A wanted change ("use a dropdown"), stale documentation or a missing test run is not a defect |
| simple change | A small, bounded change the owner wants, with an observable result. An enhancement is a simple change | A change that needs its own design or approval path is a proposal |
| proposal remainder | The remaining or next slice of work that already has a canonical proposal or parent | New work with no parent starts as an idea, then becomes a proposal ([proposals](PROPOSALS.md)) |
| review finding | A finding raised on a specific pull request or diff | A finding from a scan or a test run is an audit finding |
| audit finding | A finding from an audit, scan, coverage run or a failed test or acceptance run ([audits](AUDITS.md)) | Wrong behavior that a person observed is a bug |
| housekeeping | Upkeep that adds no feature and fixes no defect: records, repositories, tests, tooling, process, or the reporting system itself. Also the catch-all: anything that fits no other Kind after one stated attempt | Anything that changes behavior, access, data or a public contract |

## Housekeeping

**Trigger.** The item's product is the health of the project's records, repositories, tests, tooling or process rather than product behavior, or, after one stated attempt, no other Kind fits.

**Typical shapes** (synthetic): a tests-only slice that changes no behavior; rewording a set of decision records into one plain question each; clearing stale rows from a ledger after the work merged; refreshing a pinned reference to a shared library; moving or re-creating a repository and re-pointing its references; closure bookkeeping for merged work; changing the workflows themselves.

**Rules.**

- It still needs a row and a one-line reason why no other Kind fits. A true catch-all item is written `housekeeping (unclassified: <why>)`.
- It is not a bypass. If the work changes behavior, access, data or a public contract, reclassify it as a bug, simple change or proposal remainder and apply that Kind's gates. A security-relevant finding is triaged under [security and data](SECURITY_DATA.md) whatever its Kind.
- It needs no owner approval beyond the project's own rules, but it names the check that shows it is done: a test run, a link check, or a diff showing nothing else changed.
- The facilitator reviews unclassified housekeeping at each standup. When three items share a shape, propose a new Kind or a sharper rule in this library once, rather than letting each project invent a local variant.

## Older wording

Earlier files listed the Kinds in different ways. Use the right-hand term.

| Older wording | Use |
|---|---|
| reported bug, confirmed bug, confirmed defect | bug, with state reported or confirmed |
| enhancement, small change | simple change |
| proposal, proposal remnant | proposal remainder |
| review comment, PR review finding | review finding |
| audit or test failure, acceptance failure found by a run | audit finding |
| owner or operator request | not a Kind. It is a source: classify what it asks for |
| other / needs-classification | a bug group, for defects only. For other work use housekeeping (unclassified) |

## Examples (synthetic)

| Input | Kind |
|---|---|
| “The save button does nothing.” | bug (reported), UI group |
| “Make labels a dropdown.” | simple change |
| “Do the second slice of the approved import proposal.” | proposal remainder |
| “The reviewer says PR 12 misses a null check.” | review finding |
| “The coverage scan lists three untested modules.” | audit finding |
| “Add boundary tests; no behavior change.” | housekeeping |
| “Reword every open decision as one question.” | housekeeping |
| “Move the repository and re-point its references.” | housekeeping |
