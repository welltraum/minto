#!/usr/bin/env bash
# Run the benchmark through four pinned engines.
# Usage: bash eval/run-cli.sh <runs_dir> [arms] [fixtures] [engines]
# Results: <runs_dir>/raw/<fixture>__<engine>__<arm>.md
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: run-cli.sh <runs_dir> [arms] [fixtures] [engines]}"
ARMS="${2:-skill control}"
FIXTURES="${3:-}"
ENGINES="${4:-codex kimi sonnet haiku}"

CODEX_MODEL="${CODEX_MODEL:-gpt-5.6-terra}"
CODEX_EFFORT="${CODEX_EFFORT:-low}"
KIMI_MODEL="${KIMI_MODEL:-kimi-code/k3-low}"
KIMI_EFFORT="${KIMI_EFFORT:-low}"
CLAUDE_SONNET_MODEL="${CLAUDE_SONNET_MODEL:-claude-sonnet-5}"
CLAUDE_HAIKU_MODEL="${CLAUDE_HAIKU_MODEL:-claude-haiku-4-5-20251001}"
CLAUDE_EFFORT="${CLAUDE_EFFORT:-medium}"

if command -v timeout >/dev/null 2>&1; then
  TIMEOUT_CMD="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
  TIMEOUT_CMD="gtimeout"
else
  echo "GNU timeout or gtimeout is required." >&2
  exit 1
fi

mkdir -p "$RUNS/raw" "$RUNS/logs"
LOG="$RUNS/log.txt"
TESTED_COMMIT="$(git -C "$ROOT" rev-parse HEAD 2>/dev/null || echo uncommitted)"
STARTED_UTC="$(date -u '+%Y-%m-%dT%H:%M:%SZ')"

{
  echo "started_utc: $STARTED_UTC"
  echo "commit: $TESTED_COMMIT"
  echo "codex: model=$CODEX_MODEL reasoning_effort=$CODEX_EFFORT"
  echo "codex_cli: $(codex --version 2>/dev/null || echo unavailable)"
  echo "kimi: model=$KIMI_MODEL effort=$KIMI_EFFORT"
  echo "kimi_cli: $(kimi --version 2>/dev/null || echo unavailable)"
  echo "claude_sonnet: model=$CLAUDE_SONNET_MODEL effort=$CLAUDE_EFFORT"
  echo "claude_haiku: model=$CLAUDE_HAIKU_MODEL effort=$CLAUDE_EFFORT"
  echo "claude_cli: $(claude --version 2>/dev/null || echo unavailable)"
  echo "arms: $ARMS"
  echo "fixtures: ${FIXTURES:-all}"
  echo "engines: $ENGINES"
  echo "codex_command: codex exec -m MODEL -c model_reasoning_effort=EFFORT --ephemeral --skip-git-repo-check -o OUTPUT -"
  echo "kimi_command: KIMI_CODE_HOME=ISOLATED_HOME kimi -p PROMPT -m MODEL --output-format stream-json"
  echo "claude_command: claude -p --model MODEL --effort EFFORT --tools '' --safe-mode --no-session-persistence --output-format text"
} > "$RUNS/engines.txt"

run_codex() {
  "$TIMEOUT_CMD" 900 codex exec \
    -m "$CODEX_MODEL" \
    -c model_reasoning_effort="$CODEX_EFFORT" \
    --ephemeral --skip-git-repo-check -o "$2" - < "$1" > /dev/null 2>>"$3"
}

run_kimi() {
  kimi_home="$(mktemp -d "${TMPDIR:-/tmp}/minto-kimi-home.XXXXXX")"
  cp "$HOME/.kimi-code/config.toml" "$kimi_home/config.toml"
  cp -R "$HOME/.kimi-code/credentials" "$kimi_home/credentials"
  {
    echo
    echo "[models.\"$KIMI_MODEL\"]"
    echo 'provider = "managed:kimi-code"'
    echo 'model = "k3"'
    echo 'max_context_size = 1048576'
    echo 'capabilities = [ "thinking", "always_thinking", "image_in", "video_in", "tool_use" ]'
    echo 'display_name = "K3 Low"'
    echo 'support_efforts = [ "low", "high", "max" ]'
    echo "default_effort = \"$KIMI_EFFORT\""
  } >> "$kimi_home/config.toml"

  if KIMI_CODE_HOME="$kimi_home" "$TIMEOUT_CMD" 900 \
    kimi -p "$(cat "$1")" -m "$KIMI_MODEL" --output-format stream-json 2>>"$3" \
    | python3 -c '
import json
import sys

last = ""
for line in sys.stdin:
    try:
        event = json.loads(line)
    except ValueError:
        continue
    if event.get("role") == "assistant" and event.get("content"):
        last = event["content"]
if not last:
    raise SystemExit(1)
sys.stdout.write(last.rstrip() + "\n")
' > "$2"
  then
    run_status=0
  else
    run_status=$?
  fi

  rm -rf "$kimi_home"
  return "$run_status"
}

run_sonnet() {
  run_claude "$CLAUDE_SONNET_MODEL" "$1" "$2" "$3"
}

run_haiku() {
  run_claude "$CLAUDE_HAIKU_MODEL" "$1" "$2" "$3"
}

run_claude() {
  "$TIMEOUT_CMD" 900 claude -p \
    --model "$1" \
    --effort "$CLAUDE_EFFORT" \
    --tools "" \
    --safe-mode \
    --no-session-persistence \
    --output-format text < "$2" > "$3" 2>>"$4"
}

selected() {
  [ -z "$2" ] && return 0
  for wanted in $2; do
    [ "$wanted" = "$1" ] && return 0
  done
  return 1
}

file_bytes() {
  if [ -f "$1" ]; then
    wc -c < "$1" | tr -d ' '
  else
    echo 0
  fi
}

job() {
  fixture_dir="$1"
  name="$2"
  arm="$3"
  engine="$4"
  output="$RUNS/raw/${name}__${engine}__${arm}.md"
  job_log="$RUNS/logs/${name}__${engine}__${arm}.log"

  existing_bytes="$(file_bytes "$output")"
  if [ "$existing_bytes" -gt 10 ]; then
    echo "skip $name/$engine/$arm (exists)"
    return 0
  fi

  started=$SECONDS
  if "run_$engine" "$fixture_dir/prompt-$arm.md" "$output" "$job_log"; then
    status=0
  else
    status=$?
  fi
  elapsed=$((SECONDS - started))

  output_bytes="$(file_bytes "$output")"
  if [ "$status" -eq 0 ] && [ "$output_bytes" -gt 10 ]; then
    echo "ok   $name/$engine/$arm  $(wc -c < "$output" | tr -d ' ') B  ${elapsed}s"
    return 0
  fi

  echo "FAIL $name/$engine/$arm  status=$status after ${elapsed}s (see logs/$(basename "$job_log"))"
  return 1
}

: > "$LOG"
overall_status=0

# Run one engine batch at a time. Each batch contains all selected fixtures and
# both arms, which balances throughput without launching all 64 processes at once.
for engine in $ENGINES; do
  if ! selected "$engine" "$ENGINES"; then
    continue
  fi

  pids=""
  jobs=0
  echo "[$(date -u '+%H:%M:%SZ')] starting engine=$engine" | tee -a "$LOG"
  for before in "$ROOT"/eval/fixtures/*/before.md; do
    fixture_dir="${before%/before.md}"
    name="$(basename "$fixture_dir")"
    selected "$name" "$FIXTURES" || continue
    for arm in $ARMS; do
      job "$fixture_dir" "$name" "$arm" "$engine" >> "$LOG" 2>&1 &
      pids="$pids $!"
      jobs=$((jobs + 1))
    done
  done

  echo "launched $jobs jobs for $engine" | tee -a "$LOG"
  for pid in $pids; do
    if ! wait "$pid"; then
      overall_status=1
    fi
  done
  grep -E "^(ok|FAIL|skip) .*/$engine/" "$LOG" | tail -n "$jobs"
done

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] finished status=$overall_status" | tee -a "$LOG"
exit "$overall_status"
