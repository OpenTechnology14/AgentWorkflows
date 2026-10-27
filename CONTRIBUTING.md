# Contributing

- Submit scoped changes through a branch and pull request. Keep workflows useful across projects and agents.
- Use synthetic examples; do not include live reporting or private upstream documents. Keep any project adapter and operational state in your own private workspace.
- Change maintained sources, rebuild with `python3 scripts/build.py`, and commit generated plugin changes. Run `python3 scripts/verify.py` and `python3 -m unittest discover -s tests -v`.
- Describe changed behavior, validation and limitations. Test realistic prompts in a host before claiming behavioral compatibility.
- Contribute only material you can provide under the repository's MIT license. Preserve required third-party attribution.
- See [packaging](docs/PACKAGING.md) and [the release proposal](docs/proposals/PUBLIC_LIBRARY.md).
