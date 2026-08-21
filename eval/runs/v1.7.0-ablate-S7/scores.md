# Deterministic scores: v1.7.0-ablate-S7

Generated 2026-08-20T17:36:58Z by `eval/aggregate.py` from 24 judged cells. Commit `a5312821438a65c3b009a76992f4da732b0ffd03`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 2.67 (33.3%) | 3.83 (47.9%) | +1.17 | +14.6 | +43.7% |
| Quality (as judged) /10 | 6.92 (69.2%) | 6.75 (67.5%) | -0.17 | -1.7 | -2.4% |
| Quality (after hard-failure penalty) /10 | 6.33 (63.3%) | 6.25 (62.5%) | -0.08 | -0.8 | -1.3% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 16.7% | 33.3% | +16.6 | 12 |
| `no_invented_facts` | 41.7% | 33.3% | -8.4 | 12 |
| `no_unacknowledged_source_loss` | 58.3% | 66.7% | +8.4 | 12 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 12 |
| `answer_first` | 75.0% | 50.0% | -25.0 | 12 |
| `first_level_count_within_limit` | 91.7% | 100.0% | +8.3 | 12 |
| `readers_question_literal` | 16.7% | 41.7% | +25.0 | 12 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 8 |
| `scq_intro_present` | 25.0% | 87.5% | +62.5 | 8 |
| `no_hard_failure` | 25.0% | 16.7% | -8.3 | 12 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 3 | 29.2% → 41.7% | 73.3% → 60.0% | -13.3 |
| gpt-oss-120b | 3 | 25.0% → 45.8% | 56.7% → 60.0% | +3.3 |
| qwen3.6-fp8 | 3 | 33.3% → 50.0% | 70.0% → 73.3% | +3.3 |
| sonnet5 | 3 | 45.8% → 54.2% | 76.7% → 76.7% | 0.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 7 | 8 |
| `more_than_four_first_level` | 1 | 0 |
| `unacknowledged_source_loss` | 5 | 4 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 69% | 68% | -1 |
| `structure` | Structure, share of the judge's 8 points | 33% | 48% | +15 |
| `readers-question` | The reader's question is written down | 17% | 42% | +25 |
| `kind-matches` | First-level points are all the same kind | 17% | 33% | +16 |
| `answer-first` | Answer in the first sentence | 75% | 50% | -25 |
| `source-kept` | No source material lost without saying so | 58% | 67% | +9 |
