# Consider Hugging Face before assigning work

> **Status:** Required consideration in this workflow; project policy controls execution · **Reviewed:** 2026-10-26

Choose the least costly route likely to produce an acceptable result, including review and rework. HF suitability is a question for the facilitator to resolve from evidence, not a recurring technical question for the owner.

| Task shape | Starting choice | Boundary |
|---|---|---|
| Reformat supplied text, extract facts, list test cases, draft a short description | Consider a bounded HF draft | Inputs and output are explicit; a capable agent checks meaning and omissions. |
| Small documentation edit or repetitive change matching an existing pattern | Consider HF if project policy permits | Exact writable files, acceptance checks and review are known. |
| Feature work with several interacting behaviors | Normal project coding route | HF may handle a genuinely separable low-risk draft. Do not split artificially to bypass policy. |
| Architecture, conflicting decisions, cross-project coordination, security, auth, billing or data safety | Capable project-approved route | HF does not own these decisions or sign off release. |

Target-project model assignments, data restrictions and spending limits govern execution.

## Required routing note

```text
HF considered: yes
Suitable slice: <specific bounded draft, or none>
Decision: use | skip | unavailable | unknown
Why: <task fit + project policy + expected review/rework>
Provider/model: <exact ID from current available catalog; not memory>
Qualification: <recent comparable task proof; catalog-only is not proof>
Limits: <one draft attempt; finite output, time and tool/step budget>
Reviewer/checks: <owner of diff/behavior review and relevant checks>
Fallback: <stop on timeout, empty output, failure or scope growth; preserve work>
Usage: <estimate / measured tokens, elapsed time, cost if available, review time>
```

Default to one bounded draft attempt. On failure, stop and let the responsible capable agent diagnose; a specific corrective attempt may be authorized within the task's budget. Never run an HF/Ollama fix-until-green loop. A watchdog must actually enforce elapsed time and tool/step limits; a prompt or ignored `steps` setting is not enforcement. Use an isolated branch/worktree for any writing agent and preserve unrelated edits.

Compare total cost/effort: draft + reviewer + likely correction + dispatch overhead. A tiny task may cost less done directly. Use already available context, small outputs and incremental status reads. Do not claim percentage savings without comparable measured runs. Unknown usage is `unknown`, not zero. Do not silently fall back to a paid provider or bypass per-request approval rules. HF credits and charges depend on billing route; check the current [HF billing documentation](https://huggingface.co/docs/inference-providers/pricing) rather than assuming unlimited free usage.
