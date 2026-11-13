# Public library and portable packages

> **Status:** Owner-requested implementation · **Date:** 2026-10-27

## Outcome and scope

Publish reusable Agent Workflows as open source, with a compiler for a standard Agent Skill, ChatGPT/Codex plugin and plain instruction/knowledge pack. Preserve idea-to-conclusion-to-prompt behavior, Security/UI bug organization and usage-aware routing.

## Boundaries and injection

- `workflows/`, `templates/`: maintained generic contracts; private deployment state remains separate.
- `packaging/manifest.json`, `packaging/ENTRYPOINT.md`, metadata: explicit package inputs and concise discovery.
- `scripts/build.py`: deterministic local compilation into a skill/plugin and chat pack; no network, provider calls or automatic installation.
- `scripts/verify.py`, `tests/`: source containment, generated parity, links, deterministic archives and failure-path checks.
- `docs/USAGE.md`, `.agents/plugins/marketplace.json`: portable distribution and supported installation guidance.
- `LICENSE`, `CONTRIBUTING.md`, `SECURITY.md`: public contribution and privacy boundaries.

## Acceptance and failure paths

Build from only declared inputs; every bundled reference resolves without this source checkout. Repeated builds match byte-for-byte. Undeclared files are excluded; missing/duplicate/traversal/symlink inputs and unknown generated files fail visibly. Check mode writes nothing. No private deployment records or predecessor commits enter public history. Owner-facing prompts remain simple and preserve actual authority; test behavioral cases separately in a host.

## Release and rollback

Inspect the clean Git tree/history before making the repository public. Preserve predecessor private data independently. Offline tests and package validation are required; hosted CI and live host acceptance are reported separately. Initial publication does not submit to a plugin directory or enable providers. Future releases use branches/PRs; rollback a package by selecting the prior version, preserving private reporting.
