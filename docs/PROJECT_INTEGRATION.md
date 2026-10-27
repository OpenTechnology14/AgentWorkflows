# Direct project references and drift checks

> **Status:** Maintained process · A link alone is not a synchronization check

Each consuming project keeps one small `.agent-workflows.json` reference record and a pointer in its existing agent guide. The library owns generic workflows; projects own their product rules and private records. Do not copy generic workflow paragraphs into every project as competing maintained sources. A short fallback keeps ideas usable when the library cannot be read.

## Adoption

From a clean reviewed AgentWorkflows checkout, record the accepted revision in the target project:

```bash
python3 scripts/project_reference.py record --library /path/to/AgentWorkflows --project /path/to/project --guide docs/AGENT_GUIDE.md
```

The agent supplies real paths. The record stores the public repository, immutable revision, source SHA-256 hashes and the project's relative guide path. It contains no workstation paths, coordinator IDs or private project content. Link it from the existing root → guide startup path; use the target's generator for generated root instructions.

## Every relevant session and project PR

```bash
python3 /path/to/AgentWorkflows/scripts/project_reference.py check --library /path/to/AgentWorkflows --project /path/to/project --upstream
```

- Verify the exact accepted revision and hashes before using its workflow. Read STARTUP, IDEA_GENERATION, INTAKE, PROMPT_TRANSLATION and the relevant stage directly from that checkout or its revision-pinned public source.
- The upstream check compares the accepted revision with public main. Different upstream, changed source, missing record/source or an unavailable network check is explicit. It never silently rewrites the accepted version or claims the check passed.
- Offline checks omit `--upstream`: they prove the pinned local source, not freshness against main. Use `ci` to write a focused GitHub workflow that repeats the reference check on push/PR/manual runs. No scheduler or model call is added.
- If library access is unavailable, preserve existing project rules and the short idea/intake fallback, label the gap, and hold only work that depends on the missing evidence. Never invent approval or replace a project's product authority.

A pending library PR may be pinned while preparing coordinated adoption. Its commit is readable, but the upstream check correctly reports a difference until that accepted revision reaches main. Adoption PRs should state this dependency.

## Update without drift

1. Edit generic behavior in AgentWorkflows first. Rebuild the skill/plugin/chat outputs and pass tests; open the library PR. A project-specific override stays in that project's guide with its reason.
2. Review the library diff against each project's current authority. Select a clean revision, run `record`, then `ci` for each affected project and update only its thin pointer or necessary local override. Keep product queues and decisions intact.
3. Re-run checks across all consumers. Keep adoption and source PRs linked in private reporting; do not publish a private project inventory here. Source, generated packages and all accepted references must agree before calling adoption current.
4. Merge/release through the existing project gates. Then repeat the upstream check. Different, unavailable and current are separate states. New installed package versions must also be installed/reloaded in the host; repository parity is not proof of a refreshed session.

Use `python3 scripts/project_reference.py ci --library /path/to/AgentWorkflows --project /path/to/project` to generate the version-pinned check. The workflow is a generated adapter; refresh it together with the record. It reads only public library content and uses read-only repository permissions. Projects without Git/CI use the same local check.

Rollback: preserve private reporting and owner answers, select the previous accepted library revision, regenerate the reference/check and run verification. Do not reset foreign worktrees or roll back product decisions with workflow instructions.
