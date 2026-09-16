# Deterministic scores: v1.8.0

Generated 2026-09-16T13:25:38Z by `eval/aggregate.py` from 6 judged cells. Commit `d1bb1d02077958a5254497a455b25cbd88271d61`, worktree clean, rubric penalty version 1.

Generated at a single commit.

Every number here is computed from the json blocks in `verdicts/`. Quote them; do not recompute them.

## Pooled

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.33 (54.2%) | 6.00 (75.0%) | +1.67 | +20.8 | +38.5% |
| Quality (as judged) /10 | 6.67 (66.7%) | 7.33 (73.3%) | +0.67 | +6.6 | +10.0% |
| Quality (after hard-failure penalty) /10 | 5.33 (53.3%) | 7.33 (73.3%) | +2.00 | +20.0 | +37.5% |

## Behaviour pass rates

`n` is the number of cells the check applies to, per arm. A conditional check shows a smaller denominator by design.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 66.7% | 66.7% | 0.0 | 3 |
| `no_invented_facts` | 33.3% | 66.7% | +33.4 | 3 |
| `no_unacknowledged_source_loss` | 0.0% | 0.0% | 0.0 | 0 |
| `mode_respected` | 66.7% | 100.0% | +33.3 | 3 |
| `answer_first` | 100.0% | 100.0% | 0.0 | 3 |
| `first_level_count_within_limit` | 33.3% | 100.0% | +66.7 | 3 |
| `readers_question_literal` | 0.0% | 0.0% | 0.0 | 0 |
| `order_type_named` | 0.0% | 0.0% | 0.0 | 0 |
| `scq_intro_present` | 100.0% | 100.0% | 0.0 | 3 |
| `no_hard_failure` | 0.0% | 66.7% | +66.7 | 3 |

## By engine

| Engine | n per arm | Structure control → skill | Quality control → skill | Δ quality pp |
|---|---:|---|---|---:|
| codex | 1 | 62.5% → 100.0% | 80.0% → 100.0% | +20.0 |
| gpt-oss-120b | 1 | 25.0% → 62.5% | 40.0% → 60.0% | +20.0 |
| qwen3.6-fp8 | 1 | 75.0% → 62.5% | 80.0% → 60.0% | -20.0 |

## Hard failures by type

| Token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 2 | 1 |
| `more_than_four_first_level` | 2 | 0 |

## Landing-page figures

| Slug | Label | Control | With skill | Δ pp |
|---|---|---:|---:|---:|
| `quality` | Writing quality, share of the judge's 10 points | 67% | 73% | +6 |
| `structure` | Structure, share of the judge's 8 points | 54% | 75% | +21 |
| `readers-question` | The reader's question is written down | 0% | 0% | +0 |
| `kind-matches` | First-level points are all the same kind | 67% | 67% | +0 |
| `answer-first` | Answer in the first sentence | 100% | 100% | +0 |
| `source-kept` | No source material lost without saying so | 0% | 0% | +0 |
