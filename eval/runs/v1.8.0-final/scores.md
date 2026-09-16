# Deterministic scores: v1.8.0-final

Generated 2026-09-16T18:23:08Z by `eval/aggregate.py` from 8 judged cells. Commit `58f3b0946a151b9b1d4ef5235df9484016e2d4b9`, worktree clean, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 7.00 (87.5%) | 6.00 (75.0%) | -1.00 | -12.5 | -14.3% |
| Quality (as judged) /10 | 7.75 (77.5%) | 7.75 (77.5%) | 0.00 | 0.0 | 0.0% |
| Quality (after hard-failure penalty) /10 | 7.00 (70.0%) | 7.25 (72.5%) | +0.25 | +2.5 | +3.6% |

## Behaviour pass rates

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

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 100.0% → 100.0% | 100.0% → 100.0% | 0.0 |
| gpt-oss-120b | 1 | 75.0% → 75.0% | 50.0% → 70.0% | +20.0 |
| qwen3.6-35b-a3b | 1 | 75.0% → 62.5% | 70.0% → 70.0% | 0.0 |
| qwen3.6-fp8 | 1 | 100.0% → 62.5% | 90.0% → 70.0% | -20.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 3 | 2 |
| `more_than_four_first_level` | 1 | 0 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 78% | 78% | +0 |
| `structure` | Structure, share of the judge's 8 points | 88% | 75% | -13 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 75% | 50% | -25 |
| `answer-first` | Answer in the first sentence | 75% | 75% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
