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
# Empty means "take the count shuffle.sh recorded per fixture". Set it to a number
# to assert one global count instead — which only holds when every engine produced
# every cell.
EXPECTED_OUTPUTS="${EXPECTED_OUTPUTS:-}"
JUDGE_ATTEMPTS="${JUDGE_ATTEMPTS:-2}"
JUDGE_FORCE="${JUDGE_FORCE:-0}"
SKILL_DIR="$ROOT/plugins/minto/skills/minto"

if command -v timeout >/dev/null 2>&1; then
  TIMEOUT_CMD="timeout"
elif command -v gtimeout >/dev/null 2>&1; then
  TIMEOUT_CMD="gtimeout"
else
  echo "GNU timeout or gtimeout is required." >&2
  exit 1
fi

sha() { shasum -a 256 "$1" | awk '{print $1}'; }

mkdir -p "$RUNS/verdicts" "$RUNS/logs"
{
  echo "judge_model: $JUDGE_MODEL"
  echo "judge_effort: $JUDGE_EFFORT"
  echo "expected_outputs_per_fixture: ${EXPECTED_OUTPUTS:-from shuffle.txt}"
  echo "judge_attempts: $JUDGE_ATTEMPTS"
  echo "judge_prompt_sha256: $(sha "$ROOT/eval/judge-prompt.md")"
  echo "rubric_sha256: $(sha "$ROOT/eval/rubric.md")"
  echo "universal_checks_sha256: $(sha "$ROOT/eval/universal-checks.md")"
  echo "codex_cli: $(codex --version 2>/dev/null || echo unavailable)"
  echo "command: codex exec -C ISOLATED_WORKSPACE -m MODEL -c model_reasoning_effort=EFFORT --ignore-user-config --ignore-rules --ephemeral --skip-git-repo-check -o OUTPUT -"
} > "$RUNS/judge.txt"

# The judge is a measuring instrument now, so its own definition is provenance:
# a verdict attributed against a different rubric or check set is not comparable.

expected_for() {
  # Per-fixture count from shuffle.txt, unless a global override is set.
  if [ -n "$EXPECTED_OUTPUTS" ]; then
    echo "$EXPECTED_OUTPUTS"
    return 0
  fi
  if [ -f "$RUNS/shuffle.txt" ]; then
    awk -v f="$1" '$1 == "outputs" && $2 == f { print $3; found = 1 } END { if (!found) print "" }' "$RUNS/shuffle.txt"
    return 0
  fi
  echo ""
}

judge_one() {
  before="$1"
  fixture_dir="${before%/before.md}"
  name="$(basename "$fixture_dir")"
  output="$RUNS/verdicts/$name.md"
  log="$RUNS/logs/judge-$name.log"

  if [ -s "$output" ] && [ "$JUDGE_FORCE" != "1" ]; then
    echo "skip $name (verdict exists)"
    return 0
  fi

  mode="$(awk -F'`' '/^\*\*Mode:\*\*/ { print $2; exit }' "$before")"
  if [ -z "$mode" ]; then
    echo "FAIL $name has no '**Mode:** \`x\`' line"
    return 1
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
    echo "===== UNIVERSAL CHECKS ====="
    python3 "$ROOT/eval/checks.py" "$name" "$mode"
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
  expected="$(expected_for "$name")"
  if [ -z "$expected" ]; then
    echo "FAIL $name has no expected output count (run shuffle.sh, or set EXPECTED_OUTPUTS)"
    rm -f "$prompt"
    return 1
  fi
  if [ "$count" -ne "$expected" ]; then
    echo "FAIL $name expected $expected blinded outputs, found $count"
    rm -f "$prompt"
    return 1
  fi

  names="$(cd "$RUNS/blind/$name" && ls out-*.md | sed 's/\.md$//' | paste -sd, -)"

  started=$SECONDS
  attempt=1
  status=1
  while [ "$attempt" -le "$JUDGE_ATTEMPTS" ]; do
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

    # A verdict that is merely non-empty is not usable. Validating here, while a
    # retry still costs one call, is far cheaper than discovering it at aggregation
    # and re-judging the fixture by hand.
    if [ "$status" -eq 0 ] && [ -s "$output" ]; then
      if python3 "$ROOT/eval/verdict.py" "$output" "$name" "$mode" "$names" 2>>"$log"; then
        break
      fi
      echo "attempt $attempt: verdict failed validation" >> "$log"
      status=65
      rm -f "$output"
    fi
    attempt=$((attempt + 1))
  done
  rm -f "$prompt"
  elapsed=$((SECONDS - started))

  if [ "$status" -eq 0 ] && [ -s "$output" ]; then
    echo "ok   $name  $(wc -c < "$output" | tr -d ' ') B  ${elapsed}s  attempt=$attempt"
    return 0
  fi

  echo "FAIL $name status=$status after ${elapsed}s over $((attempt - 1)) attempt(s) (see logs/$(basename "$log"))"
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
