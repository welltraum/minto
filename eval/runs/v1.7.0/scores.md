# Deterministic scores: v1.7.0

Generated 2026-08-20T16:46:43Z by `eval/aggregate.py` from 172 judged cells. Commit `03975451e3c979d733f5e2053a239bac29c7cea9`, worktree clean, rubric penalty version 1.

Generated over 2 commits (`03975451e3c9`, `03975451e3c9`); the skill text was identical throughout.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.36 (54.5%) | 4.78 (59.7%) | +0.42 | +5.2 | +9.6% |
| Quality (as judged) /10 | 6.91 (69.1%) | 7.28 (72.8%) | +0.37 | +3.7 | +5.4% |
| Quality (after hard-failure penalty) /10 | 6.15 (61.5%) | 6.71 (67.1%) | +0.56 | +5.6 | +9.1% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 52.3% | 60.5% | +8.2 | 86 |
| `no_invented_facts` | 46.5% | 52.3% | +5.8 | 86 |
| `no_unacknowledged_source_loss` | 64.1% | 59.0% | -5.1 | 78 |
| `mode_respected` | 97.7% | 100.0% | +2.3 | 86 |
| `answer_first` | 81.4% | 74.3% | -7.1 | 70 |
| `first_level_count_within_limit` | 85.7% | 95.7% | +10.0 | 70 |
| `readers_question_literal` | 8.7% | 32.6% | +23.9 | 46 |
| `order_type_named` | 20.4% | 25.9% | +5.5 | 54 |
| `scq_intro_present` | 58.7% | 93.5% | +34.8 | 46 |
| `no_hard_failure` | 33.7% | 37.2% | +3.5 | 86 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 11 | 58.0% → 64.8% | 72.7% → 78.2% | +5.5 |
| gpt-oss-120b | 11 | 51.1% → 43.2% | 61.8% → 56.4% | -5.4 |
| haiku45 | 11 | 47.7% → 62.5% | 63.6% → 74.5% | +10.9 |
| opus5 | 11 | 62.5% → 72.7% | 75.5% → 80.9% | +5.4 |
| qwen3.6-35b-a3b | 11 | 55.7% → 60.2% | 70.9% → 71.8% | +0.9 |
| qwen3.6-fp8 | 11 | 52.3% → 59.1% | 68.2% → 74.5% | +6.3 |
| qwen3.8-27b | 9 | 55.6% → 61.1% | 71.1% → 81.1% | +10.0 |
| sonnet5 | 11 | 53.4% → 54.5% | 69.1% → 66.4% | -2.7 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 46 | 41 |
| `more_than_four_first_level` | 10 | 3 |
| `unacknowledged_source_loss` | 28 | 32 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 69% | 73% | +4 |
| `structure` | Structure, share of the judge's 8 points | 55% | 60% | +5 |
| `readers-question` | The reader's question is written down | 9% | 33% | +24 |
| `kind-matches` | First-level points are all the same kind | 52% | 61% | +9 |
| `answer-first` | Answer in the first sentence | 81% | 74% | -7 |
| `source-kept` | No source material lost without saying so | 64% | 59% | -5 |
