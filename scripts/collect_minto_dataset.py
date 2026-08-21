#!/usr/bin/env python3
"""Collect a dataset of Claude Code dialogs where the /minto skill was invoked.

Scans every session transcript under ~/.claude/projects (main transcripts and
their subagent files). A session qualifies when an assistant turn actually
invoked the skill — a `Skill` tool_use whose `input.skill` contains "minto" —
or when the user typed the command directly (`<command-name>` containing
"minto"). Plain text mentions of the word do not qualify.

Output (regenerated from scratch on every run):
  dataset/sessions.jsonl — one record per session: metadata + ordered messages
  dataset/summary.md     — counts by project and by day, all computed here

The dataset holds client project content and is gitignored; run locally.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "dataset"
PROJECTS_DIR = Path.home() / ".claude" / "projects"

COMMAND_RE = re.compile(r"<command-name>[^<]*minto[^<]*</command-name>", re.IGNORECASE)


def iter_records(path: Path):
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError:
                continue


def minto_skill_uses(record: dict) -> list[dict]:
    """Skill tool_use blocks targeting minto within an assistant record."""
    if record.get("type") != "assistant":
        return []
    content = (record.get("message") or {}).get("content")
    if not isinstance(content, list):
        return []
    uses = []
    for block in content:
        if (
            isinstance(block, dict)
            and block.get("type") == "tool_use"
            and block.get("name") == "Skill"
            and "minto" in str((block.get("input") or {}).get("skill", "")).lower()
        ):
            uses.append(block)
    return uses


def user_text(record: dict) -> str:
    content = (record.get("message") or {}).get("content")
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = [
            b.get("text", "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        ]
        return "\n".join(p for p in parts if p)
    return ""


def has_minto_command(record: dict) -> bool:
    return record.get("type") == "user" and bool(COMMAND_RE.search(user_text(record)))


def session_qualifies(main_file: Path) -> bool:
    files = [main_file]
    subagent_dir = main_file.with_suffix("") / "subagents"
    if subagent_dir.is_dir():
        files.extend(sorted(subagent_dir.glob("agent-*.jsonl")))
    for path in files:
        for record in iter_records(path):
            if minto_skill_uses(record) or has_minto_command(record):
                return True
    return False


def extract_session(main_file: Path) -> dict:
    project_slug = main_file.parent.name
    messages: list[dict] = []
    meta = {
        "session_id": main_file.stem,
        "project_slug": project_slug,
        "transcript_path": str(main_file),
        "cwd": None,
        "git_branch": None,
        "cc_version": None,
        "model": None,
    }
    invocation_args: list[str] = []
    timestamps: list[str] = []

    for record in iter_records(main_file):
        rtype = record.get("type")
        if rtype not in ("user", "assistant") or record.get("isSidechain"):
            continue
        ts = record.get("timestamp")
        if ts:
            timestamps.append(ts)
        meta["cwd"] = meta["cwd"] or record.get("cwd")
        meta["git_branch"] = meta["git_branch"] or record.get("gitBranch")
        meta["cc_version"] = meta["cc_version"] or record.get("version")

        if rtype == "user":
            text = user_text(record)
            content = (record.get("message") or {}).get("content")
            is_tool_result = isinstance(content, list) and any(
                isinstance(b, dict) and b.get("type") == "tool_result" for b in content
            )
            if text and not is_tool_result:
                # The harness injects the skill's own instructions as a user
                # turn right after a Skill invocation; keep it, but not as if
                # the human wrote it.
                role = (
                    "skill_content"
                    if text.startswith("Base directory for this skill:")
                    else "user"
                )
                messages.append(
                    {"role": role, "text": text, "timestamp": ts, "uuid": record.get("uuid")}
                )
            continue

        meta["model"] = meta["model"] or (record.get("message") or {}).get("model")
        content = (record.get("message") or {}).get("content")
        if not isinstance(content, list):
            continue
        text_parts = [
            b.get("text", "")
            for b in content
            if isinstance(b, dict) and b.get("type") == "text"
        ]
        text = "\n".join(p for p in text_parts if p)
        if text:
            messages.append(
                {"role": "assistant", "text": text, "timestamp": ts, "uuid": record.get("uuid")}
            )
        for use in minto_skill_uses(record):
            args = (use.get("input") or {}).get("args", "")
            invocation_args.append(args)
            messages.append(
                {
                    "role": "skill_invocation",
                    "skill": (use.get("input") or {}).get("skill"),
                    "args": args,
                    "timestamp": ts,
                    "uuid": record.get("uuid"),
                }
            )

    meta.update(
        first_ts=min(timestamps) if timestamps else None,
        last_ts=max(timestamps) if timestamps else None,
        minto_invocations=sum(1 for m in messages if m["role"] == "skill_invocation"),
        invocation_args=invocation_args,
        message_count=len(messages),
    )
    return {**meta, "messages": messages}


def write_summary(sessions: list[dict]) -> None:
    by_project = Counter(s["project_slug"] for s in sessions)
    by_day = Counter((s["first_ts"] or "")[:10] for s in sessions if s["first_ts"])
    total_invocations = sum(s["minto_invocations"] for s in sessions)

    lines = [
        "# Датасет сессий с /minto",
        "",
        "Сгенерировано `scripts/collect_minto_dataset.py`; не редактировать руками.",
        "Данные: `dataset/sessions.jsonl` (одна строка = одна сессия).",
        "",
        f"- Сессий: {len(sessions)}",
        f"- Вызовов /minto: {total_invocations}",
        f"- Сообщений всего: {sum(s['message_count'] for s in sessions)}",
        "",
        "## По проектам",
        "",
    ]
    lines += [f"- `{slug}`: {n}" for slug, n in by_project.most_common()]
    lines += ["", "## По дате первой активности", ""]
    lines += [f"- {day}: {n}" for day, n in sorted(by_day.items())]
    lines.append("")
    (OUT_DIR / "summary.md").write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    main_files = sorted(
        p
        for p in PROJECTS_DIR.glob("*/*.jsonl")
        if p.is_file()
    )
    sessions = []
    for main_file in main_files:
        if session_qualifies(main_file):
            sessions.append(extract_session(main_file))
    sessions.sort(key=lambda s: s["first_ts"] or "")

    OUT_DIR.mkdir(exist_ok=True)
    with (OUT_DIR / "sessions.jsonl").open("w", encoding="utf-8") as fh:
        for session in sessions:
            fh.write(json.dumps(session, ensure_ascii=False) + "\n")
    write_summary(sessions)

    print(f"sessions: {len(sessions)}")
    print(f"invocations: {sum(s['minto_invocations'] for s in sessions)}")
    for s in sessions:
        print(f"  {s['first_ts']}  {s['project_slug']}/{s['session_id']}  calls={s['minto_invocations']}")


if __name__ == "__main__":
    main()
