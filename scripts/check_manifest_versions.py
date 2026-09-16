#!/usr/bin/env python3
"""Keep the plugin version consistent across every manifest a host reads.

Both hosts treat the version string as the update trigger: Codex caches a plugin
under `<name>/<version>/` and Claude Code records the installed version, so skill
text that changes without a bump never reaches an installed user. The version is
spelled out in three files, and 1.7.0 shipped with only two of them updated.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_PAYLOAD = "plugins/minto"
CHANGELOG = ROOT / "CHANGELOG.md"


def marketplace_version(document: dict) -> str:
    for entry in document.get("plugins", []):
        if entry.get("name") == "minto":
            return entry.get("version", "")
    raise KeyError("no plugin named 'minto' in the marketplace manifest")


MANIFESTS = (
    (Path(".claude-plugin/marketplace.json"), marketplace_version),
    (Path("plugins/minto/.claude-plugin/plugin.json"), lambda d: d.get("version", "")),
    (Path("plugins/minto/.codex-plugin/plugin.json"), lambda d: d.get("version", "")),
)


def read_versions() -> tuple[dict[str, str], list[str]]:
    versions: dict[str, str] = {}
    errors: list[str] = []
    for relative, extract in MANIFESTS:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"{relative}: missing")
            continue
        try:
            versions[str(relative)] = extract(json.loads(path.read_text()))
        except (json.JSONDecodeError, KeyError) as error:
            errors.append(f"{relative}: {error}")
    return versions, errors


def git(*arguments: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ("git", *arguments), cwd=ROOT, capture_output=True, text=True
    )


def latest_tag() -> str | None:
    result = git("tag", "-l", "v*", "--sort=-v:refname")
    if result.returncode != 0:
        return None
    tags = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return tags[0] if tags else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--tag",
        help="release tag (e.g. v1.8.0) the manifests must match",
    )
    arguments = parser.parse_args()

    versions, errors = read_versions()

    distinct = set(versions.values())
    if len(distinct) > 1:
        errors.append(
            "manifests disagree on the version: "
            + ", ".join(f"{path} = {version}" for path, version in versions.items())
        )

    version = next(iter(distinct)) if len(distinct) == 1 else None

    if version and not any(
        line.startswith(f"## {version} - ") for line in CHANGELOG.read_text().splitlines()
    ):
        errors.append(f"CHANGELOG.md: no '## {version} - <date>' section")

    if arguments.tag:
        expected = arguments.tag.removeprefix("v")
        if version != expected:
            errors.append(f"tag {arguments.tag} does not match manifest version {version}")

    tag = latest_tag()
    if version and tag and tag.removeprefix("v") == version:
        changed = git("diff", "--quiet", f"refs/tags/{tag}", "--", PLUGIN_PAYLOAD)
        if changed.returncode == 1:
            errors.append(
                f"{PLUGIN_PAYLOAD} changed since {tag} but the version is still "
                f"{version}; installed users keep the old text until it is bumped"
            )

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1

    print(f"Manifests agree on version {version}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
