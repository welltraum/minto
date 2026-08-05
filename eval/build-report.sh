#!/usr/bin/env bash
# Generate the concise public benchmark report from metadata, mappings, and verdicts.
# Usage: bash eval/build-report.sh <runs_dir> [report_file]
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: build-report.sh <runs_dir> [report_file]}"
case "$RUNS" in
  /*) ;;
  *) RUNS="$ROOT/$RUNS" ;;
esac
REPORT="${2:-$RUNS/report.md}"
case "$REPORT" in
  /*) ;;
  *) REPORT="$ROOT/$REPORT" ;;
esac
REPORT_MODEL="${REPORT_MODEL:-gpt-5.6-sol}"
REPORT_EFFORT="${REPORT_EFFORT:-high}"

if command -v timeout >/dev/null 2>&1; then
  TIMEOUT_CMD="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
  TIMEOUT_CMD="gtimeout"
else
  echo "GNU timeout or gtimeout is required." >&2
  exit 1
fi

if [ ! -s "$RUNS/scores.md" ]; then
  echo "$RUNS/scores.md is missing. Run: python3 eval/aggregate.py $RUNS" >&2
  echo "Every published figure comes from the aggregator, so the report cannot be" >&2
  echo "built before it has run." >&2
  exit 2
fi

prompt="$(mktemp "${TMPDIR:-/tmp}/minto-report.XXXXXX")"
trap 'rm -f "$prompt"' EXIT

{
  cat "$ROOT/eval/report-prompt.md"
  echo
  echo "===== DETERMINISTIC SCORES ====="
  cat "$RUNS/scores.md"
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

report_work="$(mktemp -d "${TMPDIR:-/tmp}/minto-report-work.XXXXXX")"
if "$TIMEOUT_CMD" 900 codex exec \
  -C "$report_work" \
  -m "$REPORT_MODEL" \
  -c model_reasoning_effort="$REPORT_EFFORT" \
  --ignore-user-config \
  --ignore-rules \
  --ephemeral \
  --skip-git-repo-check \
  -o "$REPORT" - < "$prompt" > /dev/null
then
  report_status=0
else
  report_status=$?
fi
rm -rf "$report_work"
if [ "$report_status" -ne 0 ]; then
  exit "$report_status"
fi

test -s "$REPORT"
echo "wrote $REPORT ($(wc -c < "$REPORT" | tr -d ' ') bytes)"
