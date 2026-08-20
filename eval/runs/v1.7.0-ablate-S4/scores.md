# Deterministic scores: v1.7.0-ablate-S4

Generated 2026-08-20T17:23:13Z by `eval/aggregate.py` from 32 judged cells. Commit `a5312821438a65c3b009a76992f4da732b0ffd03`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 3.69 (46.1%) | 4.38 (54.7%) | +0.69 | +8.6 | +18.6% |
| Quality (as judged) /10 | 7.25 (72.5%) | 7.81 (78.1%) | +0.56 | +5.6 | +7.8% |
| Quality (after hard-failure penalty) /10 | 6.63 (66.3%) | 6.94 (69.4%) | +0.31 | +3.1 | +4.7% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 12.5% | 37.5% | +25.0 | 16 |
| `no_invented_facts` | 62.5% | 25.0% | -37.5 | 16 |
| `no_unacknowledged_source_loss` | 75.0% | 66.7% | -8.3 | 12 |
| `mode_respected` | 93.8% | 100.0% | +6.2 | 16 |
| `answer_first` | 75.0% | 56.3% | -18.7 | 16 |
| `first_level_count_within_limit` | 87.5% | 100.0% | +12.5 | 16 |
| `readers_question_literal` | 0.0% | 16.7% | +16.7 | 12 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 12 |
| `scq_intro_present` | 62.5% | 100.0% | +37.5 | 16 |
| `no_hard_failure` | 50.0% | 25.0% | -25.0 | 16 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 4 | 56.3% → 68.8% | 77.5% → 90.0% | +12.5 |
| gpt-oss-120b | 4 | 50.0% → 43.8% | 72.5% → 62.5% | -10.0 |
| qwen3.6-fp8 | 4 | 34.4% → 59.4% | 70.0% → 82.5% | +12.5 |
| sonnet5 | 4 | 43.8% → 46.9% | 70.0% → 77.5% | +7.5 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 6 | 12 |
| `more_than_four_first_level` | 2 | 0 |
| `unacknowledged_source_loss` | 3 | 4 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 73% | 78% | +5 |
| `structure` | Structure, share of the judge's 8 points | 46% | 55% | +9 |
| `readers-question` | The reader's question is written down | 0% | 17% | +17 |
| `kind-matches` | First-level points are all the same kind | 13% | 38% | +25 |
| `answer-first` | Answer in the first sentence | 75% | 56% | -19 |
| `source-kept` | No source material lost without saying so | 75% | 67% | -8 |
