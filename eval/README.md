# Evaluation

The evaluation asks two questions:

1. Does the skill produce the structural result expected by the Minto examples?
2. Does it improve on a control prompt that only names the Pyramid Principle?

The suite contains eleven English fixtures:

| Fixture | Mode | Primary behavior |
|---|---|---|
| `01-big-chief` | write | benefits instead of system mechanics |
| `02-ttv` | write | merge a duplicate branch and promote the wage action |
| `03-period-graph-books` | audit | identify that the required changes are absent |
| `04-meeting-note` | write | two honest branches and proportional output |
| `05-role-of-board` | write | turn topics into actions |
| `06-ttw-viz` | viz | expose an existing two-branch pyramid |
| `07-headings-audit` | audit | distinguish topics from ideas without false positives |
| `08-techdebt` | write | move a buried recommendation to the top |
| `09-sources-digest` | digest | answer-first source report with cross-source synthesis |
| `10-rollout-review` | write | large sectioned document: cross-section MECE, honest geometry |
| `11-plain-list` | write | plain pasteable output without audit apparatus |

Book-derived inputs are faithful paraphrases of Barbara Minto's 2010 English
edition. They preserve the business facts and structural defect without
reproducing long copyrighted passages. The source PDF is not part of the
repository. Fixtures 09–11 are modeled on real usage sessions with every
company, product, person, system and number invented for the benchmark; the
raw session data never leaves the maintainer's machine (`dataset/` is
gitignored).

## Arms and engines

- `skill`: canonical `SKILL.md` plus both references and the task.
- `control`: one sentence naming the Minto Pyramid Principle plus the same task.

The v1.5.0 release matrix was two engines: `gpt-5.6-terra` at low reasoning
through Codex CLI, and `kimi-code/k3-low` through Kimi Code CLI. Eight fixtures x
two arms x two engines = 32 outputs. Claude was unavailable in that environment
and was excluded rather than silently substituted.

The wide matrix adds four Claude models and two NeuralDeep models, all generating
at low effort:

| Engine key | Model | Transport |
|---|---|---|
| `codex` | `gpt-5.6-terra` | Codex CLI |
| `kimi` | `kimi-code/k3-low` | Kimi Code CLI |
| `haiku45` `sonnet5` `opus5` | Claude aliases `haiku` `sonnet` `opus` | Claude Code CLI |
| `gpt-oss-120b` `qwen3.6-35b-a3b` | as named | NeuralDeep OpenAI-compatible API |

Seven engines x two arms x eight fixtures = 112 cells. Generation runs at low
effort throughout so the comparison is between arms, not between reasoning
budgets. Judging and report synthesis stay at high reasoning: the judge is the
measuring instrument, not a subject of the experiment.

`fable5` is defined in `CLAUDE_ENGINES` but excluded from the matrix. On the
account used for this run both `--model fable` and the explicit
`--model claude-fable-5` resolve to `claude-opus-5`, verified from the CLI's own
`modelUsage` field. Running it would have put sixteen Opus-generated cells in the
table under another engine's name, double-weighting Opus in the pooled average and
claiming a comparison that does not exist. This is what the `resolved_models=` line
in each cell log is for: an alias that silently falls back is indistinguishable from
a working one until you read what actually answered.

`gemma-4-31b` is a selectable engine but is excluded from the matrix: it times out
on the 26 KB skill prompt at both 300 and 550 seconds while completing short
fixtures, so it would contribute only the fixtures it finds easy. See
`neuraldeep-availability-2026-08-05.md`. A uniformly absent engine reduces `n`; an
engine absent from exactly the hard fixtures is a bias.

Credentials come only from `NEURALDEEP_API_KEY` in the environment. Never write a
key into repository files or command metadata.

### Claude transport

The Claude engines shell out to `claude -p` with every customization disabled:

```
--tools "" --disable-slash-commands --strict-mcp-config --setting-sources ""
--no-session-persistence --exclude-dynamic-system-prompt-sections --effort low
--output-format json
```

Four details are load-bearing:

- `--disable-slash-commands` is what keeps the minto skill out of the control arm.
  Without it the control is not a control.
- The wrapper runs under `env -u CLAUDE_EFFORT` and unsets the other inherited
  `CLAUDE_*` variables. A developer machine running Claude Code exports
  `CLAUDE_EFFORT`, and if it ever won over the flag the run would claim low effort
  while producing something else.
- `--output-format json`, never `text`. Under `text` the CLI prints authentication
  errors to stdout, which would land in `raw/` and be judged as a model output.
  The extractor keys on `is_error`, because `subtype` reads `"success"` even on a
  401.
- Not `--safe-mode` and not `--bare`. Both break authentication here; `--bare`
  refuses OAuth entirely and requires `ANTHROPIC_API_KEY`.

If Claude cells fail with `401 OAuth access token has been revoked` while
`claude auth status` reports `loggedIn: true`, the stored keychain credential is
stale — that command reports the blob's presence, not its validity. Run
`claude auth login` in a plain terminal, outside any Claude Code session so no
host environment is inherited, then re-run the preflight.

Claude cells must be produced by this CLI path, not by in-session subagents. A
subagent inherits the host system prompt, the user's `CLAUDE.md`, the installed
plugin set, and the session's effort, so its control arm is contaminated and its
effort is not the one recorded in `engines.txt`.

### Preflight

Two stages, both before any real spend. The first proves authentication and the
flag set; the second proves the long skill prompt actually survives the round
trip, which is the failure the first stage cannot see:

```bash
bash eval/build-prompts.sh
CLAUDE_PREFLIGHT=1 bash eval/run-cli.sh eval/runs/wide-preflight \
  "skill" "04-meeting-note" "haiku45 sonnet5 opus5"
NEURALDEEP_API_KEY=... NEURALDEEP_ATTEMPTS=1 \
  bash eval/run-cli.sh eval/runs/wide-preflight \
  "skill control" "04-meeting-note 03-period-graph-books" \
  "haiku45 sonnet5 opus5 gpt-oss-120b qwen3.6-35b-a3b"
```

The two fixtures bracket the workload deliberately: `04-meeting-note` produces the
shortest outputs and tests proportionality, `03-period-graph-books` produces the
longest and is `audit` mode.

Record unavailable models instead of silently substituting another engine. An
engine that is uniformly absent only reduces `n`; one that is absent for some
cells and present for others biases the delta, which is why `shuffle.sh` and
`aggregate.py` both refuse an unpaired cell.

## Run

The v1.7.0 release matrix (see `neuraldeep-availability-2026-08-20.md` for the
engine admissions of that round):

```bash
bash eval/build-prompts.sh
PARALLEL_ENGINES=1 \
NEURALDEEP_API_KEY=... NEURALDEEP_MODELS="gpt-oss-120b qwen3.6-35b-a3b qwen3.6-fp8 qwen3.8-27b" \
NEURALDEEP_MAX_TOKENS=24576 NEURALDEEP_TIMEOUT=550 bash eval/run-cli.sh eval/runs/v1.7.0-final \
  "skill control" "" \
  "gpt-oss-120b qwen3.6-35b-a3b qwen3.6-fp8 qwen3.8-27b codex haiku45 sonnet5 opus5"
SHUFFLE_SEED=v1.7.0-final bash eval/shuffle.sh eval/runs/v1.7.0-final
bash eval/run-judge.sh eval/runs/v1.7.0-final
python3 eval/aggregate.py eval/runs/v1.7.0-final --allow-partial
bash eval/build-report.sh eval/runs/v1.7.0-final eval/report-v1.7.0.md
```

To compare two aggregated runs cell-for-cell (a baseline skill text against a
candidate), run `python3 eval/compare-runs.py <baseline_dir> <candidate_dir>`.
The control arms of the two runs answered identical prompts, so their drift is
the noise floor against which skill-arm movement must be read. The runs must
score the same cell set; pin composition by moving orphaned cells to a
`raw-excluded/` directory with a README before blinding, as the v1.7.0 runs do.

Engine order matters in the default sequential mode: `run-cli.sh` runs one
engine batch at a time, so listing the cheap models first surfaces a systemic
problem before the expensive ones are spent. `PARALLEL_ENGINES=1` instead runs
each transport in its own concurrent lane, with all NeuralDeep models sharing
one sequential lane because the hub enforces account-wide parallel limits.

List every engine in **one** invocation. `engines.txt` is written by the first
invocation and never rewritten — a later invocation records itself in
`engines-resume-N.txt` instead, so the provenance of cells already on disk cannot
be restamped. Since `shuffle.sh` filters on the `engines:` line in `engines.txt`,
an engine introduced by a second invocation would be silently left out of the
blinding. Name them all up front; failed cells are picked up by re-running the
identical command.

`shuffle.sh` derives the expected output count per fixture and writes it to
`shuffle.txt`, which `run-judge.sh` then reads. Passing a global
`EXPECTED_OUTPUTS` asserts one count for every fixture instead, which only holds
when every engine produced every cell. Set `SHUFFLE_SEED` per run: the blinding is
deterministic by design, so without a per-run seed the identities learned from one
run's verdicts carry into the next.

`run-cli.sh` refuses to start on a dirty worktree, because the commit it records in
`engines.txt` would not reproduce the cells. Override with `ALLOW_DIRTY=1` only for
throwaway runs.

Codex and Kimi run as batches of 16 parallel jobs. NeuralDeep defaults to two
concurrent requests because its API enforces parallel and requests-per-minute
limits; override this with `NEURALDEEP_CONCURRENCY` only when the account tier
supports it. Retryable `408`, `429`, `500`, and `502` responses are retried.
Each API attempt has a five-minute read timeout, with two attempts and a hard
process deadline so a stalled upstream cannot block the full run indefinitely.
Nonempty outputs are skipped, so rerunning the same directory safely fills only
failed or missing cells.

`engines.txt` records model IDs, effort, CLI versions, UTC time, fixture and arm
selection, and the tested Git commit. Never compare runs whose engine metadata
or fixture wording differs without stating that limitation.

## Isolation

The judge sees only:

- the fixture input and gold structure;
- the shared rubric;
- that fixture's decisive questions;
- that fixture's slice of the universal checks, with applicability already
  resolved, produced by `eval/checks.py`;
- a frozen copy of the skill and rules;
- the expected set of blinded outputs.

It does not receive the output mapping, changelog, other fixtures, previous
reports, or other verdicts. The report step sees verdicts and mapping only after
all fixture judgments are complete. `eval/test-eval.py` asserts that no fixture's
check slice names any other fixture.

## Which release a run belongs to

A run directory is named after the skill text it tested, not the release it ships
with. `v1.5.0-wide` is the release benchmark for **1.6.0**, because 1.6.0 ships
`SKILL.md`, `rules.md` and `templates.md` byte-identical to 1.5.0 — the
`skill_sha256` in `engines.txt` is the check, and it matches.

The 1.7.0 release ships three run directories: `v1.7.0-baseline` (the 1.6.0
skill text on the eleven-fixture matrix), `v1.7.0` (an intermediate candidate,
two of whose sections later failed their removal tests — see
`eval/runs/v1.7.0-ablate-*` and Appendix B of `report-v1.7.0.md`), and
`v1.7.0-final`, the release benchmark for **1.7.0**: its `skill_sha256`
matches the shipped text.

Do not rename a run to match a release. The name records what was measured and
when; renaming it would restate both, and it would break `scores.json`'s `run`
field, the `--run` argument in the Pages workflow, and every committed artifact path.

## Deterministic scores

Every published percentage comes from `eval/aggregate.py`, which reads the fenced
`json` block each verdict ends with, joins it to `mapping.json`, and writes
`scores.json` and `scores.md` into the run directory. Nothing downstream is allowed
to recompute: `build-report.sh` refuses to run before the aggregator has, and the
report prompt instructs the model to quote and calculate nothing.

This exists because the arithmetic used to be done by a language model. The v1.5.0
figures happened to be right, but nobody could reproduce them from the artifacts.

Two properties are worth knowing before quoting a number:

- **Quality is reported twice.** `quality_raw` is the axes as the judge scored
  them. `quality_penalized` applies the hard-failure map in `rubric.md`, in code,
  identically in every cell. The judge does not apply penalties itself; it reports
  raw axes and a failure list, which is what makes the deduction reproducible.
- **Every rate carries its denominator.** Six universal checks apply to all eight
  fixtures. `readers_question_literal` applies only to the five `write` fixtures
  and `order_type_named` to six, so they show smaller `n` by design and never
  belong in a pooled headline.

The aggregator fails loudly. It collects every problem, prints them all, and
computes nothing until the list is empty — a missing verdict, a total that does not
equal its axes, a check answered where the matrix says `na`, or a `(fixture,
engine)` pair with only one arm. `--allow-partial` downgrades the pairing error to
dropping the pair, recorded in `scores.json` with its reason. Use it when engines
genuinely timed out; do not use it to make a broken run report a number.

`eval/test-eval.py` covers the validator, the penalty map, the applicability matrix
and the aggregator's refusals. Run it after touching any of them.

## Interpretation

Scores are supporting evidence. The decisive questions are the primary signal
because they identify concrete behaviors such as wrong key-line kind, duplicate
branches, invented evidence, and mode violations. The universal checks sit between
the two: aggregable, but a narrower question than the decisive ones ask.

The release benchmark is descriptive. Do not tune the tested skill against the
same outputs and call the result a clean measurement. Recurring defects become
candidates for the next version and require a new run.
