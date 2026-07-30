#!/usr/bin/env bash
# Judge each fixture from a leakage-free prompt with a pinned Codex model.
# Usage: bash eval/run-judge.sh <runs_dir>
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
RUNS="${1:?usage: run-judge.sh <runs_dir>}"
case "$RUNS" in
  /*) ;;
  *) RUNS="$ROOT/$RUNS" ;;
esac
JUDGE_MODEL="${JUDGE_MODEL:-gpt-5.6-sol}"
JUDGE_EFFORT="${JUDGE_EFFORT:-high}"
SKILL_DIR="$ROOT/plugins/minto/skills/minto"

if command -v timeout >/dev/null 2>&1; then
  TIMEOUT_CMD="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
  TIMEOUT_CMD="gtimeout"
else
  echo "GNU timeout or gtimeout is required." >&2
  exit 1
fi

mkdir -p "$RUNS/verdicts" "$RUNS/logs"
{
  echo "judge_model: $JUDGE_MODEL"
  echo "judge_effort: $JUDGE_EFFORT"
  echo "codex_cli: $(codex --version 2>/dev/null || echo unavailable)"
  echo "command: codex exec -C ISOLATED_WORKSPACE -m MODEL -c model_reasoning_effort=EFFORT --ignore-user-config --ignore-rules --ephemeral --skip-git-repo-check -o OUTPUT -"
} > "$RUNS/judge.txt"

judge_one() {
  before="$1"
  fixture_dir="${before%/before.md}"
  name="$(basename "$fixture_dir")"
  output="$RUNS/verdicts/$name.md"
  log="$RUNS/logs/judge-$name.log"

  if [ -s "$output" ]; then
    echo "skip $name (verdict exists)"
    return 0
  fi

  prompt="$(mktemp "${TMPDIR:-/tmp}/minto-judge.XXXXXX")"
  {
    cat "$ROOT/eval/judge-prompt.md"
    echo
    echo "===== FIXTURE: $name ====="
    cat "$before"
    echo
    echo "===== GOLD STRUCTURE ====="
    cat "$fixture_dir/gold.md"
    echo
    echo "===== RUBRIC ====="
    cat "$ROOT/eval/rubric.md"
    echo
    echo "===== DECISIVE QUESTIONS ====="
    awk -v heading="## $name" '
      $0 == heading {active=1}
      active && $0 != heading && /^## / {exit}
      active {print}
    ' "$ROOT/eval/decisive-questions.md"
    echo
    echo "===== SKILL SNAPSHOT ====="
    cat "$SKILL_DIR/SKILL.md"
    echo
    cat "$SKILL_DIR/references/rules.md"
    echo
    echo "===== BLINDED OUTPUTS ====="
    for blinded in "$RUNS/blind/$name"/out-*.md; do
      echo
      echo "----- $(basename "$blinded") -----"
      cat "$blinded"
    done
  } > "$prompt"

  count="$(find "$RUNS/blind/$name" -name 'out-*.md' -type f | wc -l | tr -d ' ')"
  if [ "$count" -ne 4 ]; then
    echo "FAIL $name expected 4 blinded outputs, found $count"
    rm -f "$prompt"
    return 1
  fi

  started=$SECONDS
  judge_work="$(mktemp -d "${TMPDIR:-/tmp}/minto-judge-work.XXXXXX")"
  if "$TIMEOUT_CMD" 900 codex exec \
    -C "$judge_work" \
    -m "$JUDGE_MODEL" \
    -c model_reasoning_effort="$JUDGE_EFFORT" \
    --ignore-user-config \
    --ignore-rules \
    --ephemeral \
    --skip-git-repo-check \
    -o "$output" - < "$prompt" > /dev/null 2>>"$log"; then
    status=0
  else
    status=$?
  fi
  rm -rf "$judge_work"
  rm -f "$prompt"
  elapsed=$((SECONDS - started))

  if [ "$status" -eq 0 ] && [ -s "$output" ]; then
    echo "ok   $name  $(wc -c < "$output" | tr -d ' ') B  ${elapsed}s"
    return 0
  fi

  echo "FAIL $name status=$status after ${elapsed}s (see logs/$(basename "$log"))"
  return 1
}

pids=""
for before in "$ROOT"/eval/fixtures/*/before.md; do
  judge_one "$before" &
  pids="$pids $!"
done

status=0
for pid in $pids; do
  if ! wait "$pid"; then
    status=1
  fi
done
exit "$status"
