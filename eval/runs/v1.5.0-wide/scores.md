# Deterministic scores: v1.5.0-wide

Generated 2026-08-05T17:30:05Z by `eval/aggregate.py` from 112 judged cells. Commit `7dbae71baa7bd43af54c345292b861046233af8c`, worktree clean, rubric penalty version 1.

Generated over 2 commits (`7dbae71baa7b`, `cf59e5f8a8c4`); the skill text was identical throughout.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.32 (54.0%) | 5.00 (62.5%) | +0.68 | +8.5 | +15.7% |
| Quality (as judged) /10 | 6.84 (68.4%) | 7.50 (75.0%) | +0.66 | +6.6 | +9.7% |
| Quality (after hard-failure penalty) /10 | 5.98 (59.8%) | 6.88 (68.8%) | +0.89 | +9.0 | +14.9% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 48.2% | 71.4% | +23.2 | 56 |
| `no_invented_facts` | 46.4% | 42.9% | -3.5 | 56 |
| `no_unacknowledged_source_loss` | 91.1% | 71.4% | -19.7 | 56 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 56 |
| `answer_first` | 76.2% | 76.2% | 0.0 | 42 |
| `first_level_count_within_limit` | 88.1% | 100.0% | +11.9 | 42 |
| `readers_question_literal` | 17.1% | 48.6% | +31.5 | 35 |
| `order_type_named` | 19.0% | 35.7% | +16.7 | 42 |
| `no_hard_failure` | 37.5% | 33.9% | -3.6 | 56 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 8 | 56.3% → 62.5% | 65.0% → 77.5% | +12.5 |
| gpt-oss-120b | 8 | 51.6% → 51.6% | 67.5% → 63.8% | -3.7 |
| haiku45 | 8 | 39.1% → 59.4% | 61.3% → 75.0% | +13.7 |
| kimi | 8 | 54.7% → 68.8% | 70.0% → 77.5% | +7.5 |
| opus5 | 8 | 65.6% → 76.6% | 75.0% → 81.3% | +6.3 |
| qwen3.6-35b-a3b | 8 | 60.9% → 59.4% | 71.3% → 72.5% | +1.2 |
| sonnet5 | 8 | 50.0% → 59.4% | 68.8% → 77.5% | +8.7 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 30 | 32 |
| `more_than_four_first_level` | 5 | 0 |
| `unacknowledged_source_loss` | 5 | 16 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 68% | 75% | +7 |
| `structure` | Structure, share of the judge's 8 points | 54% | 63% | +9 |
| `readers-question` | The reader's question is written down | 17% | 49% | +32 |
| `kind-matches` | First-level points are all the same kind | 48% | 71% | +23 |
| `answer-first` | Answer in the first sentence | 76% | 76% | +0 |
| `source-kept` | No source material lost without saying so | 91% | 71% | -20 |
