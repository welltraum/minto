# Minto benchmark release report — v1.5.0-wide

## Scope and methodology

This report covers the `skill` and `control` arms for 64 judged cells generated from the supplied fixture set. The deterministic scores were produced on 2026-08-05T16:20:05Z by `eval/aggregate.py` at commit `7dbae71baa7bd43af54c345292b861046233af8c`, with a clean worktree and rubric penalty version 1.

Outputs were blindly mapped to their engines and arms, then assessed by `gpt-5.6-sol` at high judge effort. Structure was judged on an eight-point rubric and quality on a ten-point rubric. Hard-failure penalties and behaviour checks were applied by the aggregator. All figures below are quoted from the deterministic scores; no additional statistics were calculated.

## Overall result

| Measure | Control | With skill | Δ | Δ pp | Relative |
|---|---:|---:|---:|---:|---:|
| Structure /8 | 4.28 (53.5%) | 4.75 (59.4%) | +0.47 | +5.9 | +10.9% |
| Quality as judged /10 | 6.91 (69.1%) | 7.38 (73.8%) | +0.47 | +4.7 | +6.8% |
| Quality after hard-failure penalty /10 | 5.94 (59.4%) | 6.88 (68.8%) | +0.94 | +9.4 | +15.8% |

## Results by engine

| Engine | n per arm | Structure: control → skill | Quality: control → skill | Δ quality pp |
|---|---:|---:|---:|---:|
| codex | 8 | 54.7% → 67.2% | 68.8% → 76.3% | +7.5 |
| gpt-oss-120b | 8 | 46.9% → 51.6% | 67.5% → 70.0% | +2.5 |
| kimi | 8 | 53.1% → 59.4% | 72.5% → 75.0% | +2.5 |
| qwen3.6-35b-a3b | 8 | 59.4% → 59.4% | 67.5% → 73.8% | +6.3 |

Quality moved in favour of the skill for every scored engine. Structure improved for codex, gpt-oss-120b, and kimi, while qwen3.6-35b-a3b was unchanged rather than improved.

## Behaviour pass rates

The denominator is the number of applicable cells in each arm. Conditional checks therefore have smaller denominators.

| Check | Control | With skill | Δ pp | n per arm |
|---|---:|---:|---:|---:|
| `first_level_kind_matches` | 50.0% | 68.8% | +18.8 | 32 |
| `no_invented_facts` | 43.8% | 53.1% | +9.3 | 32 |
| `no_unacknowledged_source_loss` | 87.5% | 65.6% | -21.9 | 32 |
| `mode_respected` | 100.0% | 100.0% | 0.0 | 32 |
| `answer_first` | 83.3% | 75.0% | -8.3 | 24 |
| `first_level_count_within_limit` | 87.5% | 100.0% | +12.5 | 24 |
| `readers_question_literal` | 15.0% | 65.0% | +50.0 | 20 |
| `order_type_named` | 16.7% | 37.5% | +20.8 | 24 |
| `no_hard_failure` | 34.4% | 40.6% | +6.2 | 32 |

The rates that moved against the skill were `no_unacknowledged_source_loss` at -21.9 percentage points and `answer_first` at -8.3 percentage points. `mode_respected` was unchanged at 100.0%.

## Most decisive fixture-level result

The deterministic section does not provide fixture-level aggregate deltas, so the clearest verdict-level contrast is reported qualitatively without calculating a score.

| Fixture | Engine | Control verdict | Skill verdict | Decisive distinction |
|---|---|---|---|---|
| Big Chief | codex | Answered feasibility rather than whether management should accept; kept mechanics at the first level; omitted source detail and incurred `unacknowledged_source_loss` | Converted the mechanics into grounded acceptance reasons, subordinated operational evidence correctly, and had no hard failure | The skill changed both the governing answer and the hierarchy while preserving the evidence |

## Recurring strengths

The following strengths recur across multiple engines:

- Better first-level grouping. The aggregate `first_level_kind_matches` rate rose from 50.0% to 68.8%. The fixture verdicts repeatedly show skill outputs organizing support as actions, benefits, or other consistent categories, especially in the visualization and governance tasks.

- More explicit reader orientation. `readers_question_literal` rose from 15.0% to 65.0%, with successful examples across gpt-oss-120b, kimi, codex, and qwen3.6-35b-a3b.

- Better control of group size. `first_level_count_within_limit` rose from 87.5% to 100.0%, and `more_than_four_first_level` hard failures changed from 3 to 0.

- Stronger visible action pyramids. Across the engines, the visualization fixture commonly placed a controlling claim above action branches and subordinated observations beneath the relevant action.

- Better judged quality. Quality rose for every scored engine, while pooled quality as judged moved from 6.91 (69.1%) to 7.38 (73.8%).

## Recurring defects and revision candidates

The following defects recur across multiple engines and should be candidates for the next skill revision:

- Source preservation regressed. `no_unacknowledged_source_loss` fell from 87.5% to 65.6%, while `unacknowledged_source_loss` hard failures changed from 4 to 11. The skill needs a stricter final inventory check and an explicit omission note when compression removes material.

- Unsupported specificity remains common. `invented_facts` hard failures changed from 18 to 15, and `no_invented_facts` reached only 53.1%. Verdicts across all scored engines identify invented certainty, causal claims, dates, metrics, plurality, or implementation detail. The next revision should distinguish paraphrase from inference and preserve tentative wording.

- Answer-first behaviour weakened. `answer_first` fell from 83.3% to 75.0%. SCQ framing, headings, and explanatory setup should not delay the requested recommendation.

- Ordering remains under-specified. Although `order_type_named` rose from 16.7% to 37.5%, the verdicts repeatedly note that ordering was visible but not explicitly explained.

- Compression sometimes destroys hierarchy or evidence. Codex, gpt-oss-120b, and qwen3.6-35b-a3b examples lost source details; other outputs promoted constraints or context to the first level. The revision should require every retained fact to have a clear parent before shortening.

- Formatting can become disproportionate. Several engines added SCQ apparatus, diagrams, or extensive audit scaffolding to short messages. The skill should scale visible structure to the size and mode of the requested deliverable.

## Hard failures, incomplete cells, and exclusions

| Hard-failure token | Control | With skill |
|---|---:|---:|
| `invented_facts` | 18 | 15 |
| `more_than_four_first_level` | 3 | 0 |
| `unacknowledged_source_loss` | 4 | 11 |

No incomplete judged cells are reported: every mapped verdict cell is marked completed. The deterministic scores do not report any excluded judged pair or give any pair-level exclusion reason.

The metadata configures Codex, Kimi, Neuraldeep, and Claude execution paths. Only codex, kimi, gpt-oss-120b, and qwen3.6-35b-a3b appear in the blind mapping and deterministic engine table. The configured Claude-family engines are absent from both. Their provider or engine availability outcome—and the reason they did not enter the judged set—is not available in the supplied aggregator output, so no exclusion cause can be assigned.

## Limitations

- The fixtures are paraphrased English versions, so linguistic and structural behaviour may differ from the original material.

- There was one run per cell; the report therefore does not measure run-to-run variance.

- Results depend on the selected models, reasoning settings, provider implementations, and the `gpt-5.6-sol` judge.

- Provider and engine availability is only partially observable from the metadata. Configured Claude-family engines are absent from the mapped and scored outputs, without a supplied reason.

- The benchmark uses the current rubric, checks, templates, and hard-failure penalty. Results may change with any of those components.

- These English results are not directly comparable with historical Russian runs.

## Conclusion

The supplied scores support a qualified improvement claim: pooled structure, judged quality, penalty-adjusted quality, and quality for every scored engine moved in favour of the skill. There was no engine-level quality reversal, although qwen3.6-35b-a3b showed no structure gain.

The result is not uniformly positive. Source preservation reversed sharply against the skill at -21.9 percentage points, and answer-first behaviour reversed at -8.3 percentage points. The next revision should retain the stronger grouping and explicit reader-question behaviour while tightening source retention, factual grounding, tentative language, and placement of the answer.