# Security and privacy

## Report a vulnerability

Report suspected vulnerabilities **privately** through this repository's [private vulnerability reporting form](https://github.com/OpenTechnology14/AgentWorkflows/security/advisories/new). Please do not open a public issue, and do not post credentials or operational data anywhere public. Say what you found, where, and how to reproduce it with synthetic data. This is a small, volunteer-maintained project: reports are read and answered on a best-effort basis.

## What this repository is, and is not

The compiler uses an explicit source list and checks path containment. It makes no network requests, installs no runtime and dispatches no agent work. A package is instructions, not authorization.

## Keep your data out of it

Secrets, runtime configuration and live project reporting belong outside this public repository and its packages, in your own [private workspace](docs/PRIVATE_WORKSPACE.md). Use synthetic fixtures for issues and examples.

Automated scans are limited indicators, not proof that arbitrary new content is safe to publish.
