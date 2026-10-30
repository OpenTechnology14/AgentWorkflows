# Agent Workflows

Open-source workflows that turn human insights and decisions into useful AI work.

- **Start and finish ideas simply:** one or two sentences or a short list; the facilitator helps shape the idea and fills intake.
- **You bring ideas and decisions.** The agent investigates, writes prompts and carries authorized work forward.
- **One intake:** ideas, bugs, small changes, proposals, audits and review findings.
- **Simple conclusions drive each next prompt.** No technical forms for the owner.
- **Security and UI bug groups**, with other defects kept visible.
- **Short bulleted updates:** changed, needs your answer, next.
- **Usage-aware routing:** consider Hugging Face for bounded tasks and count review/rework costs.
- **Your project stays authoritative:** keep its queue, design rules, approvals and existing coordinator.

## Use it

Say: “Review my current proposals and show only the decisions you need from me.” Or: “The save button does nothing.” Or: “Smallest version, no notifications.” The facilitator translates each conclusion into the next complete task prompt.

- [Start, continue and give decisions](workflows/WORKING_TOGETHER.md)
- [Skill and ChatGPT setup](docs/USAGE.md)
- [Ready-to-use skill](plugins/agent-workflows/skills/agent-workflows/SKILL.md)
- [Workflow index](workflows/README.md) and [agent-filled templates](templates/README.md)
- [Synthetic worked example](examples/checkout-button.md)
- [Direct project references and drift checks](docs/PROJECT_INTEGRATION.md)
- [Private workspace setup](docs/PRIVATE_WORKSPACE.md)

## Build and validate

Python 3.10+; standard library only. No API key or paid model call needed.

```bash
python3 scripts/build.py
python3 scripts/verify.py
python3 -m unittest discover -s tests -v
```

One maintained library generates a portable Agent Skill, a ChatGPT/Codex plugin, and a plain instructions/knowledge pack for compatible chat experiences. ZIPs and the content-hash manifest are written to `dist/`. The generated plugin is committed so consumers can use it without building. See [packaging](docs/PACKAGING.md).

The packages are instruction-only. They do not connect your projects, monitor chats, create agents, spend credits or synchronize question cards automatically. Host tools and existing authorization determine what can run. Public GitHub distribution is separate from publishing a plugin to an app directory.

[MIT License](LICENSE) · [Contributing](CONTRIBUTING.md) · [Security and privacy](SECURITY.md)
