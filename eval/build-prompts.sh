#!/usr/bin/env bash
# Build the skill and control prompts from the canonical packaged skill.
# Generated prompt files are transient and excluded from Git.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$ROOT/plugins/minto/skills/minto"

for before in "$ROOT"/eval/fixtures/*/before.md; do
  fixture_dir="${before%/before.md}"
  name="$(basename "$fixture_dir")"
  language="$(awk -F'`' '/^\*\*Language:\*\*/ {print $2; exit}' "$before")"

  if [ "$language" != "en" ]; then
    echo "$name: expected **Language:** \`en\`, found '${language:-missing}'" >&2
    exit 1
  fi

  {
    echo "Below is a skill written as an instruction. Read it in full and apply it to the task at the end."
    echo
    echo "===== SKILL.md ====="
    cat "$SKILL_DIR/SKILL.md"
    echo
    echo "===== references/rules.md ====="
    cat "$SKILL_DIR/references/rules.md"
    echo
    echo "===== references/templates.md ====="
    cat "$SKILL_DIR/references/templates.md"
    echo
    echo "===== TASK ====="
    cat "$before"
    echo
    echo "Return only the result, with no explanation of how you produced it."
  } > "$fixture_dir/prompt-skill.md"

  {
    echo "You are working on a business document using the Minto Pyramid Principle."
    echo
    cat "$before"
    echo
    echo "Return only the result, with no explanation of how you produced it."
  } > "$fixture_dir/prompt-control.md"

  printf '%-30s skill %6s B  control %6s B\n' "$name" \
    "$(wc -c < "$fixture_dir/prompt-skill.md" | tr -d ' ')" \
    "$(wc -c < "$fixture_dir/prompt-control.md" | tr -d ' ')"
done
