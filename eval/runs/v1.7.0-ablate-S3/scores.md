# Deterministic scores: v1.7.0-ablate-S3

Generated 2026-08-20T17:11:50Z by `eval/aggregate.py` from 8 judged cells. Commit `a5312821438a65c3b009a76992f4da732b0ffd03`, worktree dirty, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 5.50 (68.8%) | 5.25 (65.6%) | -0.25 | -3.2 | -4.5% |
| Quality (as judged) /10 | 6.75 (67.5%) | 7.50 (75.0%) | +0.75 | +7.5 | +11.1% |
| Quality (after hard-failure penalty) /10 | 5.75 (57.5%) | 6.75 (67.5%) | +1.00 | +10.0 | +17.4% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 25.0% | 100.0% | +75.0 | 4 |
| `no_invented_facts` | 25.0% | 0.0% | -25.0 | 4 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 4 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 4 |
| `answer_first` | 100.0% | 75.0% | -25.0 | 4 |
| `first_level_count_within_limit` | 75.0% | 100.0% | +25.0 | 4 |
| `readers_question_literal` | 0.0% | 50.0% | +50.0 | 4 |
| `order_type_named` | 0.0% | 25.0% | +25.0 | 4 |
| `scq_intro_present` | 75.0% | 100.0% | +25.0 | 4 |
| `no_hard_failure` | 0.0% | 0.0% | 0.0 | 4 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 100.0% → 100.0% | 100.0% → 100.0% | 0.0 |
| gpt-oss-120b | 1 | 62.5% → 37.5% | 60.0% → 50.0% | -10.0 |
| qwen3.6-fp8 | 1 | 62.5% → 62.5% | 60.0% → 80.0% | +20.0 |
| sonnet5 | 1 | 50.0% → 62.5% | 50.0% → 70.0% | +20.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 3 | 4 |
| `more_than_four_first_level` | 1 | 0 |
| `unacknowledged_source_loss` | 4 | 4 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 68% | 75% | +7 |
| `structure` | Structure, share of the judge's 8 points | 69% | 66% | -3 |
| `readers-question` | The reader's question is written down | 0% | 50% | +50 |
| `kind-matches` | First-level points are all the same kind | 25% | 100% | +75 |
| `answer-first` | Answer in the first sentence | 100% | 75% | -25 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
