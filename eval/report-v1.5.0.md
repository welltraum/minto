# Minto v1.5.0 release report

## Scope and methodology

This report covers all eight supplied fixtures across 32 evaluated cells: Codex and Kimi, each run once with the Minto skill and once as a control.

- Commit: `ccfe47cb1131f8d5c964b89e45f6d384e0c730c0`
- Codex: `gpt-5.6-terra`, low reasoning effort, Codex CLI 0.145.0
- Kimi: `kimi-code/k3-low`, low effort, Kimi CLI 0.30.0
- Blind judge: `gpt-5.6-sol`, high reasoning effort
- Run started: 2026-07-30 06:55:24 UTC

Blind output identifiers were decoded using the supplied mapping. Average structure and quality are unweighted arithmetic means across the eight fixtures. All verdicts contained numeric structure and quality totals, so exact averages were computable; no missing values were inferred. Hard failures were recorded separately and did not alter the supplied scores.

## Engine-level results

| Engine | Skill structure /8 | Control structure /8 | Δ | Skill quality /10 | Control quality /10 | Δ |
|---|---:|---:|---:|---:|---:|---:|
| Codex | 5.25 | 3.88 | +1.38 | 7.13 | 5.88 | +1.25 |
| Kimi | 4.50 | 4.88 | −0.38 | 6.38 | 5.38 | +1.00 |
| Both engines | 4.88 | 4.38 | +0.50 | 6.75 | 5.63 | +1.13 |

The skill arm raised average quality for both engines. Its structural effect was engine-dependent: positive for Codex and slightly negative for Kimi.

## Most decisive fixture-level results

`S/Q` denotes structure and quality. The listed result is the largest arm contrast within each fixture; ties and material reversals are shown explicitly.

| Fixture | Most decisive comparison | Result | Concrete evidence |
|---|---|---|---|
| 01 Big Chief | Codex: skill `6/7`, control `2/7` | Skill, primarily structural | Skill gave an explicit approval recommendation and subordinated most operating details; control promoted mechanics and stopped at feasibility. Both still lost source facts. |
| 02 TTV | Codex: skill `4/7`, control `3/6` | Slight skill advantage | Skill supplied a clearer establish–test–redesign sequence, although it still duplicated process branches and lost union pressure. Kimi was tied at `3/4`. |
| 03 Period graph books | Codex: `6/8` vs `4/5`; Kimi: `5/7` vs `4/3` | Skill for both engines | Skill outputs more clearly separated the absent corrective answer from the buried streamlining conclusion. Kimi control also invented inevitability and impossibility claims. |
| 04 Meeting note | Codex: skill `5/6` vs control `3/5`; Kimi: skill `3/4` vs control `5/5` | Exact engine reversal | Codex skill was more compact and better grouped; Kimi control demoted attendee constraints more successfully. No engine-independent arm winner exists. |
| 05 Role of Board | Kimi: skill `2/7`, control `1/3` | Skill, mainly quality | Skill retained all source topics and nested composition details more clearly, but still presented an agenda rather than concrete Board changes. Codex was tied at `2/4`. |
| 06 TTW visualization | Codex: skill `6/8`, control `7/8`; Kimi tied at `8/10` | No skill advantage | Both engines could produce the required two-action visualization. Codex skill lost several source supports, while its control retained them. |
| 07 Headings audit | Codex: skill `5/7`, control `4/5` | Skill, but not universal | Codex skill better diagnosed the topic-led hierarchy and excessive first-level set. Kimi skill had higher quality but lower structure than control (`5/7` vs `6/6`). |
| 08 Tech debt | Codex: skill `8/10`, control `6/7` | Strong skill result, with Kimi reversal | Codex skill produced three grounded business-loss branches and moved backlog growth into the complication. Kimi control exceeded Kimi skill (`8/7` vs `7/6`). |

## Recurring strengths

These strengths appeared in outputs from both engines:

- Direct, answer-first openings were common in the meeting-note, visualization, and technical-debt fixtures.
- Both engines could produce concise, finished English messages appropriate to the requested mode and scale.
- When the intended action structure was explicit, both engines could create a legible hierarchy with observations beneath actions. Fixture 06 was the clearest example.
- Both engines produced grounded outputs without invented evidence in multiple cells, particularly in the Board and visualization fixtures.
- Stronger outputs consistently separated the recommendation from supporting mechanics, constraints, or evidence.

## Recurring defects and v1.6.0 candidates

The following defects affected both engines and recur often enough to warrant attention in v1.6.0:

1. **Wrong first-level kind.** Topics, mechanics, constraints, diagnoses, or transition steps were frequently promoted where same-kind reasons or actions were required. This was central in fixtures 01, 02, 03, 04, 05, and 08.

2. **Weak MECE and nesting decisions.** Both engines retained duplicate branches, failed to nest related governance questions, or missed likely parent–child relationships. Fixtures 02, 05, and 07 provide repeated evidence.

3. **Unsupported strengthening and invented facts.** Both engines converted tentative evidence into certainty or added operational claims, predictions, timing, causality, or cost comparisons. This appeared prominently in fixtures 01, 02, 04, and 08.

4. **Source loss without acknowledgment.** Material facts or support layers were omitted in both engines, including account and settlement details, union pressure, governance context, visualization supports, and technical-debt evidence.

5. **Incomplete decision framing.** Outputs often stopped at feasibility, restated a question, or supplied a vague agenda rather than resolving the reader’s decision. The Board fixture was weak across all four cells.

6. **Literal reader questions were usually absent.** This defect affected both engines in fixtures where the frozen skill explicitly required the question, especially 01, 02, and 08.

7. **Mode apparatus was inconsistently applied.** Both engines sometimes omitted the default diagram or required audit markers, findings table, score, and prioritized fixes.

8. **Ordering principles were rarely explicit.** Even otherwise sound branches often lacked a clear causal, chronological, or priority rationale.

## Hard failures and incomplete cells

All 32 cells had complete numeric structure and quality scores. There were no incomplete score cells. The following cells had hard failures:

| Fixture | Engine/arm | Hard failure |
|---|---|---|
| 01 | Codex skill | Lost account 8306, the extraction-program commitment, and the accepted cash-receipt format. |
| 01 | Codex control | Lost account 8306 and the explicit replacement of individual-ticket settlement. |
| 01 | Kimi skill | Invented unchanged procedures, pre-balancing, unchanged processing, and contradictory responsibility for balancing. |
| 01 | Kimi control | Invented automatic processing. |
| 02 | Codex skill | Lost union pressure without acknowledgment. |
| 02 | Kimi skill | Invented conclusions that costs were excessive and operations were at a “breaking point.” |
| 02 | Kimi control | Invented likely excessive costs and a larger method opportunity. |
| 03 | Kimi control | Invented inevitable or guaranteed errors and impossible consistency checks; one quality axis was zero. |
| 04 | Codex skill | Invented “first time” and overstated tentative availability. |
| 04 | Kimi skill | Invented “earliest slot” and universal constraint clearance. |
| 04 | Kimi control | Unsupported certainty that the time worked for everyone. |
| 05 | Codex skill | Invented Board “oversight” responsibility and lost October timing and the years-long operational focus. |
| 05 | Codex control | Lost October timing and the years-long operational focus. |
| 06 | Codex skill | Lost the methods study, two departures, union pressure, and monitoring conditions without a note. |
| 08 | Codex control | Invented facts and lost source material, including Research and major-account specificity. |
| 08 | Kimi skill | Invented durations, projections, public status, and repeated worsening claims. |
| 08 | Kimi control | Strengthened churn causality and invented a cost comparison. |

Fixture 07 had no hard failures.

## Limitations

- The fixtures were paraphrased in English; results may reflect the paraphrase as well as the underlying structural task.
- There was only one run per engine–arm–fixture cell, so variance and repeatability are unknown.
- Scores depend on the selected generation models, effort settings, CLI versions, and the `gpt-5.6-sol` judge.
- Claude execution was unavailable for this release, leaving no Claude comparison.
- These English results are not directly comparable with historical Russian runs.
- The sample is small, and no statistical significance test is justified.

## Conclusion

Minto v1.5.0’s skill arm produced higher average quality for both engines and higher average structure for Codex. Kimi’s skill outputs improved quality but scored slightly below control on structure, and several fixtures showed ties or arm reversals. The evidence therefore supports a useful but inconsistent skill effect, not a blanket claim of improvement. The clearest v1.6.0 priorities are first-level grouping, MECE nesting, grounding and source preservation, decisive reader framing, and reliable mode compliance.