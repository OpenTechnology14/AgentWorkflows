# Contributing

Thank you for helping. Please read the [code of conduct](CODE_OF_CONDUCT.md) first, and report security problems privately as described in [SECURITY.md](SECURITY.md).

- Submit scoped changes through a branch and pull request. Keep workflows useful across projects and agents.
- Use synthetic examples; do not include live reporting or private upstream documents. Keep any project adapter and operational state in your own private workspace.
- Change maintained sources (`workflows/`, `templates/`, `packaging/`), rebuild with `python3 scripts/build.py`, and commit generated plugin changes. Run `python3 scripts/verify.py` and `python3 -m unittest discover -s tests -v`.
- Describe changed behavior, validation and limitations. Test realistic prompts in a host before claiming behavioral compatibility.
- Contribute only material you can provide under the repository's MIT license; contributions are accepted on the same terms, with no CLA or sign-off requirement. Preserve required third-party attribution.
- Use your Git host's noreply address for commits if it offers one; do not publish a personal email address in commit metadata.
- See [packaging](docs/PACKAGING.md) and [the release proposal](docs/proposals/PUBLIC_LIBRARY.md).
