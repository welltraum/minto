#!/usr/bin/env bash
# Run the benchmark through the selected pinned engines.
# Usage: bash eval/run-cli.sh <runs_dir> [arms] [fixtures] [engines]
# Engines: codex kimi haiku45 fable5 sonnet5 opus5 gemma-4-31b gpt-oss-120b qwen3.6-35b-a3b
# Results: <runs_dir>/raw/<fixture>__<engine>__<arm>.md
# Set ALLOW_DIRTY=1 to run from a dirty worktree, CLAUDE_PREFLIGHT=1 to only prove
# Claude auth and isolation, FORCE_RUN=1 to re-run cells that already exist.
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
ALLOW_DIRTY="${ALLOW_DIRTY:-0}"
# Outputs of this size or smaller are treated as failures, never as cached cells.
MIN_OUTPUT_BYTES="${MIN_OUTPUT_BYTES:-10}"

CODEX_MODEL="${CODEX_MODEL:-gpt-5.6-terra}"
CODEX_EFFORT="${CODEX_EFFORT:-low}"
KIMI_MODEL="${KIMI_MODEL:-kimi-code/k3-low}"
KIMI_EFFORT="${KIMI_EFFORT:-low}"
CLAUDE_ENGINES="haiku45 fable5 sonnet5 opus5"
CLAUDE_EFFORT_LEVEL="${CLAUDE_EFFORT_LEVEL:-low}"
CLAUDE_TIMEOUT="${CLAUDE_TIMEOUT:-900}"
CLAUDE_CONCURRENCY="${CLAUDE_CONCURRENCY:-4}"
CLAUDE_PREFLIGHT="${CLAUDE_PREFLIGHT:-0}"
NEURALDEEP_MODELS="${NEURALDEEP_MODELS:-gemma-4-31b gpt-oss-120b qwen3.6-35b-a3b}"
NEURALDEEP_BASE_URL="${NEURALDEEP_BASE_URL:-https://api.neuraldeep.ru/v1}"
NEURALDEEP_CONCURRENCY="${NEURALDEEP_CONCURRENCY:-2}"

# Engine keys must not contain "__": shuffle.sh splits raw filenames on it.
claude_model_for() {
  case "$1" in
    haiku45) echo "haiku" ;;
    fable5) echo "fable" ;;
    sonnet5) echo "sonnet" ;;
    opus5) echo "opus" ;;
    *) return 1 ;;
  esac
}

is_claude_engine() {
  for claude_key in $CLAUDE_ENGINES; do
    [ "$claude_key" = "$1" ] && return 0
  done
  return 1
}

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

# A dirty worktree makes the recorded commit a lie: the cells cannot be
# reproduced from it. Refuse rather than record unusable provenance.
if [ "$WORKTREE_STATE" = "dirty" ] && [ "$ALLOW_DIRTY" != "1" ]; then
  {
    echo "Refusing to run: the worktree is dirty, so commit $TESTED_COMMIT would not"
    echo "reproduce these cells. Commit or stash first, or set ALLOW_DIRTY=1 to override."
    echo
    git -C "$ROOT" status --short
  } >&2
  exit 2
fi

# A resume must not rewrite the original run's provenance. Re-running a completed
# directory produces zero new cells, but the old code still stamped today's date,
# today's commit and today's CLI versions over the record of the cells that are
# actually on disk — quietly falsifying which commit and which CLI produced them.
# The first invocation owns engines.txt; later ones write a numbered resume file.
if [ -s "$RUNS/engines.txt" ]; then
  resume_index=1
  while [ -e "$RUNS/engines-resume-$resume_index.txt" ]; do
    resume_index=$((resume_index + 1))
  done
  PROVENANCE="$RUNS/engines-resume-$resume_index.txt"
  echo "engines.txt exists; recording this invocation in $(basename "$PROVENANCE")"
else
  PROVENANCE="$RUNS/engines.txt"
fi

{
  echo "started_utc: $STARTED_UTC"
  echo "commit: $TESTED_COMMIT"
  echo "worktree: $WORKTREE_STATE"
  echo "allow_dirty: $ALLOW_DIRTY"
  echo "min_output_bytes: $MIN_OUTPUT_BYTES"
  echo "skill_sha256: $(shasum -a 256 "$ROOT/plugins/minto/skills/minto/SKILL.md" | awk '{print $1}')"
  echo "rules_sha256: $(shasum -a 256 "$ROOT/plugins/minto/skills/minto/references/rules.md" | awk '{print $1}')"
  echo "templates_sha256: $(shasum -a 256 "$ROOT/plugins/minto/skills/minto/references/templates.md" | awk '{print $1}')"
  echo "codex: model=$CODEX_MODEL reasoning_effort=$CODEX_EFFORT"
  echo "codex_cli: $(codex --version 2>/dev/null || echo unavailable)"
  echo "kimi: model=$KIMI_MODEL effort=$KIMI_EFFORT"
  echo "kimi_cli: $(kimi --version 2>/dev/null || echo unavailable)"
  for claude_engine in $CLAUDE_ENGINES; do
    case " $ENGINES " in
      *" $claude_engine "*)
        echo "claude: engine=$claude_engine model=$(claude_model_for "$claude_engine") effort=$CLAUDE_EFFORT_LEVEL"
        ;;
    esac
  done
  echo "claude_cli: $(claude --version 2>/dev/null || echo unavailable)"
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
  echo "claude_command: cd ISOLATED_WORKSPACE && env -u CLAUDECODE -u CLAUDE_CODE_* -u CLAUDE_EFFORT -u CLAUDE_PID -u CLAUDE_PLUGIN_DATA -u CLAUDE_AGENT_SDK_VERSION claude -p --model MODEL --effort EFFORT --output-format json --tools \"\" --disable-slash-commands --strict-mcp-config --setting-sources \"\" --no-session-persistence --exclude-dynamic-system-prompt-sections < PROMPT"
  echo "neuraldeep_command: eval/run-neuraldeep.py MODEL PROMPT OUTPUT"
} > "$PROVENANCE"

# Every runner writes to a temp file and only mv's it into place on success, so a
# failed cell never leaves a poison pill that the resume check would treat as done.
run_codex() {
  codex_work="$(mktemp -d "${TMPDIR:-/tmp}/minto-codex-work.XXXXXX")"
  codex_tmp="$(mktemp "${TMPDIR:-/tmp}/minto-codex-out.XXXXXX")"
  if "$TIMEOUT_CMD" 900 codex exec \
    -C "$codex_work" \
    -m "$CODEX_MODEL" \
    -c model_reasoning_effort="$CODEX_EFFORT" \
    --ignore-user-config \
    --ignore-rules \
    --ephemeral --skip-git-repo-check -o "$codex_tmp" - < "$1" > /dev/null 2>>"$3"
  then
    run_status=0
    mv -f "$codex_tmp" "$2" 2>>"$3"
  else
    run_status=$?
  fi
  rm -rf "$codex_work"
  rm -f "$codex_tmp"
  return "$run_status"
}

run_kimi() {
  kimi_home="$(mktemp -d "${TMPDIR:-/tmp}/minto-kimi-home.XXXXXX")"
  kimi_tmp="$(mktemp "${TMPDIR:-/tmp}/minto-kimi-out.XXXXXX")"
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
' > "$kimi_tmp"
  then
    run_status=0
    mv -f "$kimi_tmp" "$2" 2>>"$3"
  else
    run_status=$?
  fi

  rm -rf "$kimi_home"
  rm -f "$kimi_tmp"
  return "$run_status"
}

# run_claude <prompt_file> <output_file> <log_file> <model_alias>
#
# Mirrors the codex isolation discipline: fresh cwd, no user config, no tools.
# Do NOT add --safe-mode (returns 401 here) or --bare (demands ANTHROPIC_API_KEY);
# both break auth in this setup. --setting-sources must stay "".
# --output-format json is load-bearing: under "text" the CLI prints auth errors to
# stdout, which is exactly the poison pill the temp-file discipline exists to stop.
# env -u CLAUDE_EFFORT is mandatory: this machine exports CLAUDE_EFFORT=xhigh, and a
# leaked xhigh would silently make Claude cells incomparable to the codex/kimi arms.
# The extractor keys on is_error, never on subtype: subtype reads "success" on a 401.
# Its resolved_models= line lands in logs/<cell>.log, so the model id that actually
# served the cell can be verified after the fact rather than merely asserted.
run_claude() {
  claude_prompt="$1"
  claude_dest="$2"
  claude_log="$3"
  claude_alias="$4"
  claude_work="$(mktemp -d "${TMPDIR:-/tmp}/minto-claude-work.XXXXXX")"
  claude_tmp="$(mktemp "${TMPDIR:-/tmp}/minto-claude-out.XXXXXX")"

  if (
    cd "$claude_work" &&
    env -u CLAUDECODE -u CLAUDE_CODE_CHILD_SESSION -u CLAUDE_CODE_ENTRYPOINT \
        -u CLAUDE_CODE_SESSION_ID -u CLAUDE_CODE_HOST_SESSION_ID \
        -u CLAUDE_CODE_OAUTH_SCOPES -u CLAUDE_CODE_SDK_HAS_OAUTH_REFRESH \
        -u CLAUDE_CODE_SDK_HAS_HOST_AUTH_REFRESH -u CLAUDE_AGENT_SDK_VERSION \
        -u CLAUDE_EFFORT -u CLAUDE_CODE_EXECPATH -u CLAUDE_PID -u CLAUDE_PLUGIN_DATA \
    "$TIMEOUT_CMD" "$CLAUDE_TIMEOUT" claude -p \
      --model "$claude_alias" \
      --effort "$CLAUDE_EFFORT_LEVEL" \
      --output-format json \
      --tools "" \
      --disable-slash-commands \
      --strict-mcp-config \
      --setting-sources "" \
      --no-session-persistence \
      --exclude-dynamic-system-prompt-sections \
      < "$claude_prompt" 2>>"$claude_log"
  ) \
    | python3 -c '
import json, sys
try:
    event = json.load(sys.stdin)
except ValueError:
    raise SystemExit(1)
if event.get("is_error") or event.get("api_error_status"):
    print(str(event.get("result", "unknown error"))[:500], file=sys.stderr)
    raise SystemExit(1)
text = (event.get("result") or "").strip()
if not text:
    raise SystemExit(1)
sys.stdout.write(text + "\n")
usage = event.get("modelUsage") or {}
print("resolved_models={} cost_usd={}".format(
    ",".join(sorted(usage)), event.get("total_cost_usd", "unknown")), file=sys.stderr)
' > "$claude_tmp" 2>>"$claude_log"
  then
    run_status=0
    mv -f "$claude_tmp" "$claude_dest" 2>>"$claude_log"
  else
    run_status=$?
  fi

  rm -rf "$claude_work"
  rm -f "$claude_tmp"
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
  neuraldeep_tmp="$(mktemp "${TMPDIR:-/tmp}/minto-neuraldeep-out.XXXXXX")"
  if NEURALDEEP_BASE_URL="$NEURALDEEP_BASE_URL" \
    "$TIMEOUT_CMD" -k 30 660 \
    python3 "$ROOT/eval/run-neuraldeep.py" "$model" "$2" "$neuraldeep_tmp" 2>>"$4"
  then
    run_status=0
    mv -f "$neuraldeep_tmp" "$3" 2>>"$4"
  else
    run_status=$?
  fi
  rm -f "$neuraldeep_tmp"
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
  if [ "$FORCE_RUN" != "1" ] && [ "$existing_bytes" -gt "$MIN_OUTPUT_BYTES" ]; then
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
    haiku45|fable5|sonnet5|opus5)
      run_claude "$fixture_dir/prompt-$arm.md" "$output" "$job_log" "$(claude_model_for "$engine")"
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
  if [ "$status" -eq 0 ] && [ "$output_bytes" -gt "$MIN_OUTPUT_BYTES" ]; then
    echo "ok   $name/$engine/$arm  $(wc -c < "$output" | tr -d ' ') B  ${elapsed}s"
    return 0
  fi

  # Never leave a failed cell on disk: it would survive the resume skip and then be
  # blinded and judged as if it were a real model output.
  #
  # Except when a valid cell was already there. The runners only move their temp
  # file into place on success, so what remains after a failure is the earlier good
  # output — and a FORCE_RUN retry that fails is no reason to destroy it.
  if [ "$existing_bytes" -gt "$MIN_OUTPUT_BYTES" ] && [ "$output_bytes" -eq "$existing_bytes" ]; then
    echo "FAIL $name/$engine/$arm  status=$status after ${elapsed}s (kept the earlier $existing_bytes B output; see logs/$(basename "$job_log"))"
    return 1
  fi

  rm -f "$output"
  echo "FAIL $name/$engine/$arm  status=$status after ${elapsed}s ($output_bytes B, removed; see logs/$(basename "$job_log"))"
  return 1
}

# Validate before truncating the log, so an unknown engine cannot wipe a prior run.
for engine in $ENGINES; do
  case "$engine" in
    codex|kimi|haiku45|fable5|sonnet5|opus5) ;;
    *)
      if ! is_neuraldeep_model "$engine"; then
        echo "Unknown engine '$engine'. Expected codex, kimi, one of: $CLAUDE_ENGINES, or one of: $NEURALDEEP_MODELS" >&2
        exit 2
      fi
      if [ -z "${NEURALDEEP_API_KEY:-}" ]; then
        echo "NEURALDEEP_API_KEY is required for engine '$engine'." >&2
        exit 2
      fi
      ;;
  esac
done

# Four sub-cent calls that prove auth, every isolation flag and the resolved model
# ids before any real cell is spent.
if [ "$CLAUDE_PREFLIGHT" = "1" ]; then
  preflight_status=0
  preflight_ran=0
  for engine in $ENGINES; do
    is_claude_engine "$engine" || continue
    preflight_ran=$((preflight_ran + 1))
    pf_alias="$(claude_model_for "$engine")"
    pf_prompt="$(mktemp "${TMPDIR:-/tmp}/minto-preflight-prompt.XXXXXX")"
    pf_out="$(mktemp "${TMPDIR:-/tmp}/minto-preflight-out.XXXXXX")"
    pf_log="$RUNS/logs/preflight-$engine.log"
    : > "$pf_log"
    echo "Reply with exactly: PREFLIGHT_OK" > "$pf_prompt"
    run_claude "$pf_prompt" "$pf_out" "$pf_log" "$pf_alias"
    pf_status=$?
    if grep -q 'PREFLIGHT_OK' "$pf_out" 2>/dev/null; then
      pf_ok="yes"
    else
      pf_ok="no"
    fi
    if [ "$pf_status" -eq 0 ] && [ "$pf_ok" = "yes" ]; then
      echo "preflight ok   engine=$engine model=$pf_alias preflight_ok=$pf_ok"
    else
      echo "preflight FAIL engine=$engine model=$pf_alias preflight_ok=$pf_ok status=$pf_status (see logs/preflight-$engine.log)"
      preflight_status=1
    fi
    echo "  $(grep -E 'resolved_models=' "$pf_log" | tail -n 1)"
    rm -f "$pf_prompt" "$pf_out"
  done
  if [ "$preflight_ran" -eq 0 ]; then
    echo "preflight: no Claude engines in '$ENGINES' (expected one of: $CLAUDE_ENGINES)"
  fi
  exit "$preflight_status"
fi

: > "$LOG"
overall_status=0

# Run one engine batch at a time. Codex and Kimi retain their full-batch behavior;
# Claude and NeuralDeep batches are capped to respect parallel-request limits.
for engine in $ENGINES; do
  pids=""
  batch_jobs=0
  jobs=0
  if is_neuraldeep_model "$engine"; then
    concurrency="$NEURALDEEP_CONCURRENCY"
  elif is_claude_engine "$engine"; then
    concurrency="$CLAUDE_CONCURRENCY"
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
