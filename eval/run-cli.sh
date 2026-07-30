#!/usr/bin/env bash
# Run the benchmark through the selected pinned engines.
# Usage: bash eval/run-cli.sh <runs_dir> [arms] [fixtures] [engines]
# Results: <runs_dir>/raw/<fixture>__<engine>__<arm>.md
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: run-cli.sh <runs_dir> [arms] [fixtures] [engines]}"
case "$RUNS" in
  /*) ;;
  *) RUNS="$ROOT/$RUNS" ;;
esac
ARMS="${2:-skill control}"
FIXTURES="${3:-}"
ENGINES="${4:-codex kimi}"
FORCE_RUN="${FORCE_RUN:-0}"

CODEX_MODEL="${CODEX_MODEL:-gpt-5.6-terra}"
CODEX_EFFORT="${CODEX_EFFORT:-low}"
KIMI_MODEL="${KIMI_MODEL:-kimi-code/k3-low}"
KIMI_EFFORT="${KIMI_EFFORT:-low}"
NEURALDEEP_MODELS="${NEURALDEEP_MODELS:-gemma-4-31b gpt-oss-120b qwen3.6-35b-a3b}"
NEURALDEEP_BASE_URL="${NEURALDEEP_BASE_URL:-https://api.neuraldeep.ru/v1}"
NEURALDEEP_CONCURRENCY="${NEURALDEEP_CONCURRENCY:-2}"

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
if [ -n "$(git -C "$ROOT" status --short 2>/dev/null)" ]; then
  WORKTREE_STATE="dirty"
else
  WORKTREE_STATE="clean"
fi

{
  echo "started_utc: $STARTED_UTC"
  echo "commit: $TESTED_COMMIT"
  echo "worktree: $WORKTREE_STATE"
  echo "skill_sha256: $(shasum -a 256 "$ROOT/plugins/minto/skills/minto/SKILL.md" | awk '{print $1}')"
  echo "rules_sha256: $(shasum -a 256 "$ROOT/plugins/minto/skills/minto/references/rules.md" | awk '{print $1}')"
  echo "templates_sha256: $(shasum -a 256 "$ROOT/plugins/minto/skills/minto/references/templates.md" | awk '{print $1}')"
  echo "codex: model=$CODEX_MODEL reasoning_effort=$CODEX_EFFORT"
  echo "codex_cli: $(codex --version 2>/dev/null || echo unavailable)"
  echo "kimi: model=$KIMI_MODEL effort=$KIMI_EFFORT"
  echo "kimi_cli: $(kimi --version 2>/dev/null || echo unavailable)"
  for model in $NEURALDEEP_MODELS; do
    case " $ENGINES " in
      *" $model "*)
        echo "neuraldeep: model=$model base_url=$NEURALDEEP_BASE_URL temperature=${NEURALDEEP_TEMPERATURE:-0.1} max_tokens=${NEURALDEEP_MAX_TOKENS:-8192} timeout=${NEURALDEEP_TIMEOUT:-300} attempts=${NEURALDEEP_ATTEMPTS:-2} concurrency=$NEURALDEEP_CONCURRENCY"
        ;;
    esac
  done
  echo "arms: $ARMS"
  echo "fixtures: ${FIXTURES:-all}"
  echo "engines: $ENGINES"
  echo "codex_command: codex exec -C ISOLATED_WORKSPACE -m MODEL -c model_reasoning_effort=EFFORT --ignore-user-config --ignore-rules --ephemeral --skip-git-repo-check -o OUTPUT -"
  echo "kimi_command: cd ISOLATED_HOME && KIMI_CODE_HOME=ISOLATED_HOME kimi --skills-dir EMPTY_SKILLS -p PROMPT -m MODEL --output-format stream-json"
  echo "neuraldeep_command: eval/run-neuraldeep.py MODEL PROMPT OUTPUT"
} > "$RUNS/engines.txt"

run_codex() {
  codex_work="$(mktemp -d "${TMPDIR:-/tmp}/minto-codex-work.XXXXXX")"
  if "$TIMEOUT_CMD" 900 codex exec \
    -C "$codex_work" \
    -m "$CODEX_MODEL" \
    -c model_reasoning_effort="$CODEX_EFFORT" \
    --ignore-user-config \
    --ignore-rules \
    --ephemeral --skip-git-repo-check -o "$2" - < "$1" > /dev/null 2>>"$3"
  then
    run_status=0
  else
    run_status=$?
  fi
  rm -rf "$codex_work"
  return "$run_status"
}

run_kimi() {
  kimi_home="$(mktemp -d "${TMPDIR:-/tmp}/minto-kimi-home.XXXXXX")"
  mkdir -p "$kimi_home/skills"
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

  if (
    cd "$kimi_home" &&
    KIMI_CODE_HOME="$kimi_home" "$TIMEOUT_CMD" 900 \
    kimi --skills-dir "$kimi_home/skills" -p "$(cat "$1")" \
      -m "$KIMI_MODEL" --output-format stream-json 2>>"$3"
  ) \
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

is_neuraldeep_model() {
  for model in $NEURALDEEP_MODELS; do
    [ "$model" = "$1" ] && return 0
  done
  return 1
}

run_neuraldeep() {
  model="$1"
  if NEURALDEEP_BASE_URL="$NEURALDEEP_BASE_URL" \
    "$TIMEOUT_CMD" -k 30 660 \
    python3 "$ROOT/eval/run-neuraldeep.py" "$model" "$2" "$3" 2>>"$4"
  then
    run_status=0
  else
    run_status=$?
  fi
  return "$run_status"
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
  if [ "$FORCE_RUN" != "1" ] && [ "$existing_bytes" -gt 10 ]; then
    echo "skip $name/$engine/$arm (exists)"
    return 0
  fi

  started=$SECONDS
  case "$engine" in
    codex)
      run_codex "$fixture_dir/prompt-$arm.md" "$output" "$job_log"
      status=$?
      ;;
    kimi)
      run_kimi "$fixture_dir/prompt-$arm.md" "$output" "$job_log"
      status=$?
      ;;
    *)
      if is_neuraldeep_model "$engine"; then
        run_neuraldeep "$engine" "$fixture_dir/prompt-$arm.md" "$output" "$job_log"
        status=$?
      else
        echo "unknown engine: $engine" >> "$job_log"
        status=2
      fi
      ;;
  esac
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

for engine in $ENGINES; do
  case "$engine" in
    codex|kimi) ;;
    *)
      if ! is_neuraldeep_model "$engine"; then
        echo "Unknown engine '$engine'. Expected codex, kimi, or one of: $NEURALDEEP_MODELS" >&2
        exit 2
      fi
      if [ -z "${NEURALDEEP_API_KEY:-}" ]; then
        echo "NEURALDEEP_API_KEY is required for engine '$engine'." >&2
        exit 2
      fi
      ;;
  esac
done

# Run one engine batch at a time. Codex and Kimi retain their full-batch behavior;
# NeuralDeep batches are capped to respect account parallel-request limits.
for engine in $ENGINES; do
  if ! selected "$engine" "$ENGINES"; then
    continue
  fi

  pids=""
  batch_jobs=0
  jobs=0
  if is_neuraldeep_model "$engine"; then
    concurrency="$NEURALDEEP_CONCURRENCY"
  else
    concurrency=999
  fi
  echo "[$(date -u '+%H:%M:%SZ')] starting engine=$engine" | tee -a "$LOG"
  for before in "$ROOT"/eval/fixtures/*/before.md; do
    fixture_dir="${before%/before.md}"
    name="$(basename "$fixture_dir")"
    selected "$name" "$FIXTURES" || continue
    for arm in $ARMS; do
      job "$fixture_dir" "$name" "$arm" "$engine" >> "$LOG" 2>&1 &
      pids="$pids $!"
      jobs=$((jobs + 1))
      batch_jobs=$((batch_jobs + 1))
      if [ "$batch_jobs" -ge "$concurrency" ]; then
        for pid in $pids; do
          if ! wait "$pid"; then
            overall_status=1
          fi
        done
        pids=""
        batch_jobs=0
      fi
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
