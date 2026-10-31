# Agent Workflows contributor instructions

- Read README.md and the workflow relevant to the task. Target projects retain their own authority.
- Keep this public library generic. Never add live portfolio records, private source archives, local paths, credentials or runtime identifiers. Examples are synthetic.
- Idea conversations start and finish in one or two sentences or a short list; the facilitator helps refine them and fills intake.
- The owner supplies insights and decisions; agents generate complete current-stage prompts and brief bulleted summaries. Preserve scope, holds and unanswered questions.
- Edit workflows/, templates/ and packaging/; regenerate plugins/ and dist/ with `python3 scripts/build.py`. Do not hand-edit generated files.
- CLAUDE.md is maintained; AGENTS.md is its exact generated copy.
- Run `python3 scripts/verify.py` and `python3 -m unittest discover -s tests -v`. Build checks do not prove host installation or model behavior.
- Initial clean public bootstrap may create main. Subsequent changes use a task branch and PR; preserve foreign edits.
- Record material work in docs/proposals/. Do not infer product implementation, external sends, provider activation or merges from an instruction package.
- Keep one list of intake Kinds: workflows/WORK_TYPES.md is the source and `tests/test_work_types.py` fails when another file lists them differently. Register work before starting it (workflows/ENTRY_GATE.md).
- Keep distribution independent of private deployments. Respect license and attribution on contributions.
