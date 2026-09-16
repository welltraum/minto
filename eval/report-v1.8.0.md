# Minto benchmark release report: v1.8.0-final

## Scope and methodology

`v1.8.0-final` is the release run for **1.8.0**: the shipped skill text (its
`skill_sha256` in `eval/runs/v1.8.0-final/engines.txt` matches
`plugins/minto/skills/minto/SKILL.md`) on fixture `12-talk-digest`, engines
codex, gpt-oss-120b, qwen3.6-fp8 and qwen3.6-35b-a3b, both arms, blind judge
gpt-5.6-sol at high effort. It measures one fixture only; the eleven older
fixtures and the site figures are unchanged from `v1.7.0-final`.

## Deterministic scores of the release run

Generated 2026-09-16T18:23:08Z by `eval/aggregate.py` from 8 judged cells. Commit `58f3b0946a151b9b1d4ef5235df9484016e2d4b9`, worktree clean, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

### Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 7.00 (87.5%) | 6.00 (75.0%) | -1.00 | -12.5 | -14.3% |
| Quality (as judged) /10 | 7.75 (77.5%) | 7.75 (77.5%) | 0.00 | 0.0 | 0.0% |
| Quality (after hard-failure penalty) /10 | 7.00 (70.0%) | 7.25 (72.5%) | +0.25 | +2.5 | +3.6% |

### Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 75.0% | 50.0% | -25.0 | 4 |
| `no_invented_facts` | 25.0% | 50.0% | +25.0 | 4 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 75.0% | 100.0% | +25.0 | 4 |
| `answer_first` | 75.0% | 75.0% | 0.0 | 4 |
| `first_level_count_within_limit` | 75.0% | 100.0% | +25.0 | 4 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 4 |
| `no_hard_failure` | 25.0% | 50.0% | +25.0 | 4 |

### By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 100.0% → 100.0% | 100.0% → 100.0% | 0.0 |
| gpt-oss-120b | 1 | 75.0% → 75.0% | 50.0% → 70.0% | +20.0 |
| qwen3.6-35b-a3b | 1 | 75.0% → 62.5% | 70.0% → 70.0% | 0.0 |
| qwen3.6-fp8 | 1 | 100.0% → 62.5% | 90.0% → 70.0% | -20.0 |

### Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 3 | 2 |
| `more_than_four_first_level` | 1 | 0 |

### Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 78% | 78% | +0 |
| `structure` | Structure, share of the judge's 8 points | 88% | 75% | -13 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 75% | 50% | -25 |
| `answer-first` | Answer in the first sentence | 75% | 75% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |

### Reading the release run

Skill minus control in this run: structure −1.00, quality as judged 0.00,
quality after the hard-failure penalty +0.25; `invented_facts` 2 skill cells
against 3 control, `more_than_four_first_level` 0 against 1. The skill arm did
not beat control on structure here. Against the 1.7.0 text on the same fixture
and engines (`v1.8.0-r2-baseline`), the skill arm is flat: structure 6.00 →
6.00, quality 8.00 → 7.75, while the control arm of this run scored 1.25
structure points and 1.50 quality points above its own round-2 self on identical
prompts — that drift is the noise floor at four cells per arm. Cell-for-cell
output of `eval/compare-runs.py`:

```text
baseline:  v1.8.0-r2-baseline  commit 5092a71b580c  cells 8
candidate: v1.8.0-final  commit 58f3b0946a15  cells 8

== Pooled means per arm (delta = candidate - baseline) ==
measure                            arm       baseline  candidate   delta
structure /8                       skill        6.000      6.000  +0.000
quality_raw /10                    skill        8.000      7.750  -0.250
quality_penalized /10              skill        8.000      7.250  -0.750
structure /8                       control      5.750      7.000  +1.250
quality_raw /10                    control      6.250      7.750  +1.500
quality_penalized /10              control      4.750      7.000  +2.250

== Check pass rates per arm, pct (delta pp) ==
-- skill arm --
  answer_first                          75.0 ->  75.0  ( +0.0 pp, n=4)
  first_level_count_within_limit       100.0 -> 100.0  ( +0.0 pp, n=4)
  first_level_kind_matches             100.0 ->  50.0  (-50.0 pp, n=4)
  mode_respected                       100.0 -> 100.0  ( +0.0 pp, n=4)
  no_invented_facts                    100.0 ->  50.0  (-50.0 pp, n=4)
  scq_intro_present                    100.0 -> 100.0  ( +0.0 pp, n=4)
-- control arm --
  answer_first                         100.0 ->  75.0  (-25.0 pp, n=4)
  first_level_count_within_limit        25.0 ->  75.0  (+50.0 pp, n=4)
  first_level_kind_matches              50.0 ->  75.0  (+25.0 pp, n=4)
  mode_respected                        75.0 ->  75.0  ( +0.0 pp, n=4)
  no_invented_facts                     25.0 ->  25.0  ( +0.0 pp, n=4)
  scq_intro_present                    100.0 -> 100.0  ( +0.0 pp, n=4)

== Skill-arm quality_raw mean by engine ==
  codex              10.00 -> 10.00  (+0.00)
  gpt-oss-120b        7.00 ->  7.00  (+0.00)
  qwen3.6-35b-a3b     7.00 ->  7.00  (+0.00)
  qwen3.6-fp8         8.00 ->  7.00  (-1.00)

== Skill-arm structure+quality by fixture (mean over engines) ==
  12-talk-digest           structure 6.00 -> 6.00 (+0.00)   quality 8.00 -> 7.75 (-0.25)

== Hard failures per arm (token: baseline -> candidate) ==
  skill    invented_facts: 0->2
  control  invented_facts: 3->3, more_than_four_first_level: 3->1
```

The judge's per-cell answers for the skill arm: all four outputs show three
levels with minute markers on the supports (decisive questions 2 and 5); codex
keeps five of the nine planted figures, the hub models two or three (question 4);
qwen3.6-fp8 again opens with an invented reader position ("the reader's
organization deployed agents expecting 10×") and qwen3.6-35b-a3b turns "a month
without code" into "months" (question 7). The judge's own attribution table lists
"long-talk supports lose the figures and examples needed to judge the claim" as
the most frequent defect across both arms.


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
