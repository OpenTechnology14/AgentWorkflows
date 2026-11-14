#!/usr/bin/env python3
"""Validate the shape of a duplicate-repository sync tracker (see modules/repo-management/SYNC_TRACKER.md).

Stdlib only. The tracker uses a small YAML subset: `schema: 1`, then `pairs:` with `- key: value` items.
It checks the file, never the network.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path

REQUIRED = ["id", "kind", "private_repo", "public_repo", "method", "last_synced_private_sha",
            "last_synced_other_sha", "last_synced_at", "drift", "drift_reason", "checked_at", "owner"]
KINDS = {"snapshot", "mirror"}
DRIFTS = {"none", "private-ahead", "other-ahead", "diverged", "unknown"}
SHA = re.compile(r"^[0-9a-f]{40}$")
REPO = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")


def parse(text: str) -> tuple[dict, list[dict]]:
    top: dict[str, str] = {}
    pairs: list[dict] = []
    current: dict | None = None
    for number, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        item = re.match(r"^  - (\w+):\s*(.*)$", raw)
        field = re.match(r"^    (\w+):\s*(.*)$", raw)
        if item:
            current = {item.group(1): clean(item.group(2)), "_line": number}
            pairs.append(current)
        elif field and current is not None:
            current[field.group(1)] = clean(field.group(2))
        elif re.match(r"^\w+:", raw):
            key, _, value = raw.partition(":")
            top[key.strip()] = clean(value)
            current = None
        else:
            raise ValueError(f"line {number}: unsupported syntax")
    return top, pairs


def clean(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def problems(top: dict, pairs: list[dict]) -> list[str]:
    found: list[str] = []
    if top.get("schema") != "1":
        found.append("schema must be 1")
    if "pairs" not in top and not pairs:
        found.append("no pairs")
    seen: set[str] = set()
    for pair in pairs:
        where = f"pair at line {pair.get('_line')}"
        for key in REQUIRED:
            if key not in pair:
                found.append(f"{where}: missing {key}")
        name = pair.get("id", "")
        if name in seen:
            found.append(f"{where}: duplicate id {name}")
        seen.add(name)
        if pair.get("kind") not in KINDS:
            found.append(f"{where}: kind must be one of {sorted(KINDS)}")
        if pair.get("drift") not in DRIFTS:
            found.append(f"{where}: drift must be one of {sorted(DRIFTS)}")
        for key in ("private_repo", "public_repo"):
            if key in pair and not REPO.match(pair[key]):
                found.append(f"{where}: {key} must look like owner/name")
        for key in ("last_synced_private_sha", "last_synced_other_sha"):
            if key in pair and not SHA.match(pair[key]):
                found.append(f"{where}: {key} must be 40 lowercase hex characters")
        for key in ("last_synced_at", "checked_at"):
            if key in pair:
                try:
                    date.fromisoformat(pair[key])
                except ValueError:
                    found.append(f"{where}: {key} must be YYYY-MM-DD")
        if pair.get("drift") not in (None, "none") and not pair.get("drift_reason"):
            found.append(f"{where}: drift needs a drift_reason")
        if "@" in pair.get("owner", ""):
            found.append(f"{where}: owner must be a role or team, not an address")
    return found


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("command", choices=["check"])
    parser.add_argument("path", type=Path)
    args = parser.parse_args(argv)
    try:
        top, pairs = parse(args.path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        print(f"FAIL: {error}")
        return 1
    found = problems(top, pairs)
    if found:
        print("FAIL:")
        for line in found:
            print(f"- {line}")
        return 1
    print(f"PASS: {len(pairs)} pair(s) valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
