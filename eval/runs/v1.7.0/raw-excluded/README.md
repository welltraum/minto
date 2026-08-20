The complete 02-ttv qwen3.8-27b pair, moved out of raw/ before blinding.

In the baseline run (v1.7.0-baseline) qwen3.8-27b never completed the 02-ttv
skill arm, so that pair is absent there. This run produced both arms, but a
pair present in one run and absent in the other would make the two pooled
deltas incomparable cell-for-cell. Composition is therefore pinned to the
intersection: both runs score the same 172 (fixture, engine, arm) cells.
10-rollout-review x qwen3.8-27b is absent from both runs for the same
reason (the hub closes the connection on both arms after ~20 minutes).
Recorded 2026-08-20.
