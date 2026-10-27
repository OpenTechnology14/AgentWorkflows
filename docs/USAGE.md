# Use as a skill, plugin or chat instructions

## Agent Skill

The complete self-contained skill is `plugins/agent-workflows/skills/agent-workflows/`. Copy that directory, including references and license, into a skill location supported by your host. Current Codex documentation lists `.agents/skills/` for repository skills and `~/.agents/skills/` for user skills. Invoke `$agent-workflows` in Codex, or select the installed skill in the host. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

This is the standard SKILL.md folder format. Other compatible agents can consume it, but their installation and tool behavior must be verified separately.

## ChatGPT / Codex plugin

`plugins/agent-workflows/plugin.json` packages the same skill. The repository's `.agents/plugins/marketplace.json` points to it for supported local clients. Follow the [official plugin installation instructions](https://developers.openai.com/plugins/build/plugins#install-a-local-plugin-manually), choose the local marketplace and install/test it in your supported host. The repository does not automatically enable the plugin or alter your settings.

Generated `dist/agent-workflows-plugin.zip` contains the portable manifest and skill. A GitHub repository or ZIP is not a directory listing or a workspace installation. Publishing to a plugin directory, workspace sharing and account permissions remain separate steps.

## Plain chat / custom instruction fallback

Run the build. `dist/chatgpt/INSTRUCTIONS.md` is the concise instruction text, `KNOWLEDGE.md` contains the workflow/template references, and `STARTERS.md` provides examples. Use these in an instruction/knowledge surface your account supports, or provide them to a chat. This is a manual import pack, not a GPT creation API or an automatic uploader.

Prefer the skill/plugin path where supported. OpenAI's [custom GPT migration guide](https://learn.chatgpt.com/docs/migrate-custom-gpts) describes workflows moving to skills/plugins; available legacy GPT surfaces vary. No custom actions, connectors or background jobs are included.

## First conversation

“Use Agent Workflows to facilitate this project. I provide insights and decisions; you generate the prompts. Start by reviewing existing proposal work. Show short bullets and ask only the choices that need me.”

The agent finds existing instructions and canonical records, captures the current conclusion and generates the appropriate next prompt. Native question controls are optional; chat questions are the fallback. Without connected files/tools, it must explain the missing access instead of claiming to update or send anything.

Packaging was validated offline. Run the [behavioral scenarios](../tests/SCENARIOS.md) in your intended host before claiming end-to-end compatibility.
