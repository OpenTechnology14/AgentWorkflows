# Agent Workflows

Open-source workflows and templates that help people and AI agents turn ideas, bugs and decisions into reviewed, tracked work, while the people who own the project stay in charge.

It is a library of plain-language procedures. Nothing here runs: there is no server, no API key and no agent launcher. You load the instructions into the assistant you already use, and the assistant follows them.

## What you get

- **A facilitator workflow.** You bring an idea or a decision in one or two sentences. The assistant helps shape it, files it as one kind of work, and writes the next prompt. You get short bullets back: what changed, what needs your answer, what is next.
- **One intake, one list of Kinds:** idea, bug, simple change, proposal remainder, review finding, audit finding, housekeeping.
- **An entry gate:** register the work, then start it ([work types](workflows/WORK_TYPES.md), [entry gate](workflows/ENTRY_GATE.md)).
- **Routing and review rules.** Choose the model by fit, record which model drives and which one reviews, checkpoint long work, and hand off cleanly when a usage limit is hit.
- **Quality workflows** for proposals, design, implementation, verification, review and release, audits, bugs, security and data, documentation, and project logs. See the [workflow index](workflows/README.md).
- **Templates** the assistant fills in for you: intake, proposal, bug, design, question, decision, review, generated prompt, project adapter, row schema, content controls and a starter set of project logs. See the [template index](templates/README.md).
- **Direct project references and drift checks.** A small script records which library revision a project follows and reports when it has drifted ([how it works](docs/PROJECT_INTEGRATION.md)).
- **Repository management.** A duplicate-repository sync tracker and a public-migration playbook ([module](modules/repo-management/README.md)).

The same sources build three packages: an Agent Skill, a ChatGPT/Codex plugin, and a plain instruction pack for chat tools.

## Quick start

1. Choose a package in the [setup guide](docs/USAGE.md): the [Agent Skill](plugins/agent-workflows/skills/agent-workflows/SKILL.md), the plugin under `plugins/agent-workflows`, or the plain-chat instructions.
2. Start talking. For example: "Review my current proposals and show only the decisions I need to make." Or: "The save button does nothing." Or: "Smallest version, no notifications."
3. Read [how we work together](workflows/WORKING_TOGETHER.md) for starting, continuing and giving decisions.

A [worked example](examples/checkout-button.md) uses made-up data.

## Keep your records private

This repository holds procedures, blank templates and synthetic examples. Your real ideas, decisions, prompts, project mappings and credentials belong in a private workspace; see [private workspace setup](docs/PRIVATE_WORKSPACE.md). The packages are instruction-only: they do not connect to your projects, watch your chats, create agents or spend credits.

## Build and check

Python 3.10 or newer, standard library only; no API key or paid model call is needed.

```bash
python3 scripts/build.py                        # regenerate plugins/ and dist/
python3 scripts/verify.py                       # public-content and link checks
python3 -m unittest discover -s tests -v
```

Edit `workflows/`, `templates/` and `packaging/`; do not hand-edit generated files. The [build contract](docs/PACKAGING.md) explains the packages.

## Status

Pre-1.0: stable enough to use, and still changing. Behavior depends on the host assistant, so test realistic prompts before relying on a workflow.

## Community

[Contributing](CONTRIBUTING.md) · [Code of conduct](CODE_OF_CONDUCT.md) · [Security policy](SECURITY.md) · licensed under the [MIT License](LICENSE).
