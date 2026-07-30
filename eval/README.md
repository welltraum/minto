# Evaluation

The evaluation asks two questions:

1. Does the skill produce the structural result expected by the Minto examples?
2. Does it improve on a control prompt that only names the Pyramid Principle?

The suite contains eight English fixtures:

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

Book-derived inputs are faithful paraphrases of Barbara Minto's 2010 English
edition. They preserve the business facts and structural defect without
reproducing long copyrighted passages. The source PDF is not part of the
repository.

## Arms and engines

- `skill`: canonical `SKILL.md` plus both references and the task.
- `control`: one sentence naming the Minto Pyramid Principle plus the same task.

The pinned release matrix is:

- `gpt-5.6-terra`, low reasoning, through Codex CLI.
- `kimi-code/k3-low` through Kimi Code CLI.

Eight fixtures x two arms x two engines = 32 outputs. Claude execution was
unavailable in the release environment and was excluded rather than silently
substituted. Judging and report synthesis use `gpt-5.6-sol` with high reasoning
in isolated Codex workspaces.

## Run

```bash
bash eval/build-prompts.sh
bash eval/run-cli.sh eval/runs/v1.5.0
bash eval/shuffle.sh eval/runs/v1.5.0
bash eval/run-judge.sh eval/runs/v1.5.0
bash eval/build-report.sh eval/runs/v1.5.0
```

Each engine is run as a batch of 16 parallel jobs. Nonempty outputs are skipped,
so rerunning the same directory safely fills only failed or missing cells.

`engines.txt` records model IDs, effort, CLI versions, UTC time, fixture and arm
selection, and the tested Git commit. Never compare runs whose engine metadata
or fixture wording differs without stating that limitation.

## Isolation

The judge sees only:

- the fixture input and gold structure;
- the shared rubric;
- that fixture's decisive questions;
- a frozen copy of the skill and rules;
- four blinded outputs.

It does not receive the output mapping, changelog, other fixtures, previous
reports, or other verdicts. The report step sees verdicts and mapping only after
all fixture judgments are complete.

## Interpretation

Scores are supporting evidence. The decisive questions are the primary signal
because they identify concrete behaviors such as wrong key-line kind, duplicate
branches, invented evidence, and mode violations.

The release benchmark is descriptive. Do not tune the tested skill against the
same outputs and call the result a clean measurement. Recurring defects become
candidates for the next version and require a new run.
