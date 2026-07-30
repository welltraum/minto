#!/usr/bin/env bash
# Generate the concise public benchmark report from metadata, mappings, and verdicts.
# Usage: bash eval/build-report.sh <runs_dir> [report_file]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: build-report.sh <runs_dir> [report_file]}"
REPORT="${2:-$ROOT/eval/report-v1.5.0.md}"
REPORT_MODEL="${REPORT_MODEL:-claude-opus-5}"
REPORT_EFFORT="${REPORT_EFFORT:-medium}"

if command -v timeout >/dev/null 2>&1; then
  TIMEOUT_CMD="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
  TIMEOUT_CMD="gtimeout"
else
  echo "GNU timeout or gtimeout is required." >&2
  exit 1
fi

prompt="$(mktemp "${TMPDIR:-/tmp}/minto-report.XXXXXX")"
trap 'rm -f "$prompt"' EXIT

{
  cat "$ROOT/eval/report-prompt.md"
  echo
  echo "===== ENGINE METADATA ====="
  cat "$RUNS/engines.txt"
  echo
  cat "$RUNS/judge.txt"
  echo
  echo "===== BLIND MAPPING ====="
  cat "$RUNS/mapping.json"
  echo
  echo "===== VERDICTS ====="
  for verdict in "$RUNS/verdicts"/*.md; do
    echo
    echo "----- $(basename "$verdict") -----"
    cat "$verdict"
  done
} > "$prompt"

"$TIMEOUT_CMD" 900 claude -p \
  --model "$REPORT_MODEL" \
  --effort "$REPORT_EFFORT" \
  --tools "" \
  --safe-mode \
  --no-session-persistence \
  --output-format text < "$prompt" > "$REPORT"

test -s "$REPORT"
echo "wrote $REPORT ($(wc -c < "$REPORT" | tr -d ' ') bytes)"
