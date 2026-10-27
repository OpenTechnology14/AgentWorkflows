# Build contract

Maintained inputs are enumerated in `packaging/manifest.json`: generic workflows, templates, entrypoint and metadata. The compiler never recursively imports arbitrary project docs or private deployment records.

```bash
python3 scripts/build.py          # regenerate plugin and distribution artifacts
python3 scripts/build.py --check  # detect drift without writing
python3 scripts/verify.py         # links, source boundaries, generated parity
python3 -m unittest discover -s tests -v
```

Outputs:

- `plugins/agent-workflows/`: portable plugin with one self-contained skill and progressive references.
- `dist/agent-workflows-skill.zip`: skill folder for compatible hosts.
- `dist/agent-workflows-plugin.zip`: plugin root with manifest.
- `dist/agent-workflows-chatgpt.zip`: portable copy of the manual chat pack.
- `dist/chatgpt/`: instructions, knowledge and starters for manual import.
- `dist/manifest.json`: source/output SHA-256 hashes and package version.

The same canonical text feeds all formats. ZIP ordering/timestamps and manifest serialization are deterministic. Missing input, path escape, symlink, duplicate input or unknown generated files stop the build. `--check` compares exact bytes; it does not contact providers.

Only public source material belongs here. Private deployment records and any predecessor Git history are deliberately excluded from the public baseline. Do not introduce raw source archives as a convenience.

Format references: [Agent Skills](https://learn.chatgpt.com/docs/build-skills), [portable plugin packaging](https://developers.openai.com/plugins/build/plugins). Plugin schema validation and host behavioral acceptance are distinct from repository tests.
