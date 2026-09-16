# Minto benchmark release report: v1.8.0-final

## Scope and methodology

`v1.8.0-final` is the release run for **1.8.0**: the shipped skill text (its
`skill_sha256` in `eval/runs/v1.8.0-final/engines.txt` matches
`plugins/minto/skills/minto/SKILL.md`) on fixture `12-talk-digest`, engines
codex, gpt-oss-120b, qwen3.6-fp8 and qwen3.6-35b-a3b, both arms, blind judge
gpt-5.6-sol at high effort. It measures one fixture only; the eleven older
fixtures and the site figures are unchanged from `v1.7.0-final`.

## Deterministic scores of the release run

PENDING_SCORES

---

## Appendix A — the two-round measurement behind the release decision (added by the maintainer)

The sections above describe `v1.8.0-final` in isolation, as the report model
sees only one run. The decision about which edits ship rests on the runs below:
the 1.7.0 text, the full four-edit candidate, and the candidate minus one edit
at a time, each in two rounds (three engines, then four). All figures come from
`eval/aggregate.py` over each run's `scores.json`, printed by a script that only
reads those files; nothing here is computed by hand or by a model. Control cells
of every removal test are copied byte-identically from the candidate run of the
same round, so the skill-minus-control column is comparable within a round.

| Run | text | n/arm | skill structure /8 | skill quality /10 | skill penalized /10 | skill − control (structure / quality / penalized) | skill `invented_facts` | control `invented_facts` | skill `more_than_four` |
|---|---|---:|---:|---:|---:|---|---:|---:|---:|
| `v1.8.0-baseline` | 1.7.0 | 3 | 6.33 | 8.00 | 8.00 | +1.00 / +1.00 / +1.67 | 1 | 2 | 0 |
| `v1.8.0` | candidate (D+C+R+S) | 3 | 6.00 | 7.33 | 7.33 | +1.67 / +0.67 / +2.00 | 1 | 2 | 0 |
| `v1.8.0-ablate-D` | candidate − D | 3 | 5.67 | 7.00 | 6.00 | -0.67 / +0.33 / +0.67 | 2 | 2 | 1 |
| `v1.8.0-ablate-C` | candidate − C | 3 | 6.33 | 8.00 | 7.67 | +0.67 / +1.67 / +2.33 | 1 | 2 | 0 |
| `v1.8.0-ablate-R` | candidate − R | 3 | 5.67 | 7.33 | 6.33 | +0.67 / +1.67 / +1.67 | 2 | 2 | 1 |
| `v1.8.0-ablate-S` | candidate − S | 3 | 6.67 | 7.67 | 7.00 | +1.33 / +1.00 / +1.00 | 2 | 2 | 0 |
| `v1.8.0-r2-baseline` | 1.7.0 | 4 | 6.00 | 8.00 | 8.00 | +0.25 / +1.75 / +3.25 | 0 | 3 | 0 |
| `v1.8.0-r2` | candidate (D+C+R+S) | 4 | 6.50 | 8.25 | 7.50 | +1.00 / +1.75 / +2.00 | 3 | 3 | 0 |
| `v1.8.0-r2-ablate-D` | candidate − D | 4 | 6.00 | 8.25 | 7.25 | +0.50 / +1.00 / +1.25 | 2 | 2 | 1 |
| `v1.8.0-r2-ablate-C` | candidate − C | 4 | 6.50 | 8.25 | 7.75 | +0.75 / +2.00 / +2.25 | 2 | 2 | 0 |
| `v1.8.0-r2-ablate-R` | candidate − R | 4 | 6.00 | 7.50 | 6.25 | -0.25 / +1.75 / +1.00 | 3 | 2 | 1 |
| `v1.8.0-r2-ablate-S` | candidate − S | 4 | 7.00 | 8.00 | 7.50 | +1.50 / +1.25 / +1.50 | 2 | 2 | 0 |

How to read it: the control arm answered identical prompts in every run, so its
movement between rounds is the judge-and-sampling noise floor — on this fixture
it is about one point of structure and one point of quality between two judge
passes over the same cells. Two independent rounds were run so that no decision
would rest on a single delta; the shipped text keeps the edits whose removal
moved the same way in both rounds, and drops the ones that did not.

## Appendix B — what shipped and what was rolled back

Four separable edits were written for the real case (`patch_skill.py` in the
maintainer's notes reproduces each; the shipped text is the 1.7.0 text plus D
and R):

- **D — depth follows the material.** Removal lowered skill-arm structure in both
  rounds (6.00 → 5.67, 6.50 → 6.00) and produced a `more_than_four_first_level`
  failure on codex in both rounds. **Ships.**
- **R — one long source in `digest`** (router row, "one or more sources", sizing
  bullets). Removal lowered structure (6.00 → 5.67, 6.50 → 6.00) and
  `mode_respected` (100 → 67, 75 → 50) in both rounds and produced the same
  fifth-branch failure. **Ships.**
- **C — supports keep the source's concreteness** (plus the noun-list top
  sentence). Removal left quality flat or higher in both rounds (7.33 → 8.00,
  8.25 → 8.25) and structure flat or higher (6.00 → 6.33, 6.50 → 6.50). The
  fixture's decisive question 4 asks which of nine planted figures survive; the
  judge's answers show the same range with and without the edit — codex keeps
  five or six, the hub models one to four. **Rolled back; the complaint stays
  open.**
- **S — the Situation is never made up for the reader.** Removal raised
  structure in both rounds (6.00 → 6.67, 6.50 → 7.00); its effect on
  `invented_facts` went one way in round 1 (1 → 2) and the other in round 2
  (3 → 2). **Rolled back.** The failure it aimed at is real and recurs in the
  shipped text — qwen3.6-fp8's `v1.8.0-final` skill cell opens with "We deployed
  coding agents expecting a tenfold acceleration", a Situation the request never
  gave it.

Two things the measurement did **not** show, recorded so the changelog cannot
overclaim: the 1.7.0 text already produced three levels with locators on every
engine here, so the flat single-sentence output of the real case (a 15,000-word
transcript, GPT-5.x in a Codex session writing to a file) was not reproduced by
this 3,700-word fixture; and no edit moved the survival of concrete figures.

## Appendix C — review and run-context notes the report model could not see

- Before any run, the candidate text, fixture and gold went through a Codex
  review (gpt-5.6, read-only). Its five must-fix items were applied before the
  runs: the depth edit lost its "more than three distinct themes" trigger and
  its universal locator requirement (both would have fired on the short `write`
  fixtures and on the plain-list fixture); the gold stopped admitting a fifth
  first-level branch; the digest definition was widened from "several sources"
  to "one or more"; two transcript sentences whose translation read as a
  reversed argument were retranslated against the Russian original.
- Claude engines are absent from every 1.8.0 run because the Claude CLI on the
  maintainer's machine was not authenticated, and the eval forbids in-session
  subagents as cells (they inherit the host prompt). They were not substituted;
  `engines.txt` in each run lists what ran.
- The Codex CLI hit its usage limit twice during the day; failed codex cells were
  re-run with the identical command (nonempty outputs are skipped, so no cell was
  regenerated), and the `v1.8.0-final` judge pass waited for the reset.
- The round-2 runs and the removal tests record the worktree as dirty because
  the text under test was written into a worktree whose HEAD carried a different
  text; `skill_sha256` in each `engines.txt` is the record of what was measured
  (1.7.0 text `baecb27d…`, full candidate `8022f2b0…`, shipped text
  `19e09efc…`).
- The site keeps the `v1.7.0-final` figures. They measure the 1.7.0 text on the
  eleven older fixtures, which were not re-run for this release.
