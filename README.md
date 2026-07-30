# Minto

Minto is an installable skill for Claude Code and Codex that applies the
[Minto Pyramid Principle](https://www.barbaraminto.com/) to business writing
and thinking.

**Website:** [welltraum.github.io/minto](https://welltraum.github.io/minto/)

It turns a topic into the reader's question, puts one answer at the top, groups
supporting ideas by kind, checks the logic for overlaps and gaps, and makes the
result easy to scan. The instructions are written in English, but the skill
answers in the language of the source material or request, including Russian.

## What it does

Minto routes a request into one of four modes:

- `intent`: interview the author and turn a vague goal into a reader question,
  one-sentence answer, and provisional key line.
- `audit`: diagnose pyramid-logic defects without rewriting the document.
- `write`: draft or restructure an answer-first memo, email, one-pager, decision
  note, chat update, or deck storyline.
- `viz`: render the pyramid and SCQ flow in Mermaid, with an optional
  self-contained HTML view when explicitly requested.

The skill preserves source facts, marks unsupported gaps instead of inventing
evidence, and adapts directness and context to the document's reader and genre.

## Install

### Claude Code

```bash
claude plugin marketplace add welltraum/minto
claude plugin install minto@minto
```

Restart Claude Code or run `/reload-plugins`, then invoke the skill explicitly:

```text
/minto:minto
```

Claude can also invoke the skill automatically when a request matches its
description. See the official
[Claude Code plugin](https://code.claude.com/docs/en/plugins) and
[marketplace](https://code.claude.com/docs/en/plugin-marketplaces)
documentation for scopes and update behavior.

### Codex

```bash
codex plugin marketplace add welltraum/minto
codex plugin add minto@minto
```

Start a new Codex session, then invoke:

```text
$minto
```

You can also open `/plugins` in Codex CLI and install Minto from the configured
marketplace. Plugins are not available in the Codex IDE extension; this
repository includes a `.agents/skills/minto` symlink so the skill is available
when developing the repository itself. See the official
[Codex plugin packaging guide](https://developers.openai.com/plugins/build/plugins).

## Example requests

```text
Use Minto intent mode to clarify what this board note must achieve.
```

```text
Audit this proposal for pyramid logic. Do not rewrite it.
```

```text
Rewrite these notes as a one-page decision memo, answer first.
```

```text
Show the resulting pyramid and SCQ flow in Mermaid.
```

For a deliberately unstructured input, use
[`messy-memo.md`](plugins/minto/skills/minto/assets/messy-memo.md).

## Repository layout

```text
.
├── .agents/plugins/marketplace.json
├── .claude-plugin/marketplace.json
├── plugins/minto/
│   ├── .claude-plugin/plugin.json
│   ├── .codex-plugin/plugin.json
│   └── skills/minto/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       ├── assets/
│       └── references/
└── eval/
```

`plugins/minto/skills/minto/SKILL.md` is the only copy of the skill. Both
plugin manifests package that same directory.

## Local development

Validate and test Claude Code directly from the checkout:

```bash
claude plugin validate --strict ./plugins/minto
claude plugin validate --strict .
claude --plugin-dir ./plugins/minto
```

Validate the Codex package:

```bash
python3 /path/to/plugin-creator/scripts/validate_plugin.py ./plugins/minto
python3 /path/to/skill-creator/scripts/quick_validate.py \
  ./plugins/minto/skills/minto
```

Build the evaluation prompts and run the pinned benchmark:

```bash
bash eval/build-prompts.sh
bash eval/run-cli.sh eval/runs/v1.5.0
bash eval/shuffle.sh eval/runs/v1.5.0
bash eval/run-judge.sh eval/runs/v1.5.0
bash eval/build-report.sh eval/runs/v1.5.0
```

The release benchmark uses eight English fixtures, two engines, and two arms
(`skill` and `control`) for 32 model outputs. Model identifiers, CLI versions,
effort settings, UTC time, and the commit SHA are recorded with the run.
Claude models were excluded because Claude execution was unavailable in the
release environment.

## Evaluation sources

The book-derived fixtures are faithful paraphrases of examples in Barbara
Minto's *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem
Solving* (2010), including Big Chief, TTV, Period Graph Books, the meeting note,
the board-role memo, and the project-team headings example.

The source book and online course are copyrighted and are not distributed with
this repository. Fixtures preserve the structural problem and evaluation target
without reproducing long source passages. The modern technical-debt fixture is
an original paraphrase inspired by a
[Planio article](https://plan.io/blog/pyramid-principle-pitching/).

## Updating

Claude Code:

```bash
claude plugin marketplace update minto
claude plugin update minto@minto
```

Codex:

```bash
codex plugin marketplace upgrade minto
codex plugin add minto@minto
```

Start a new session after an update so the host loads the new skill contents.

## License

The plugin code and original documentation are available under the
[MIT License](LICENSE). Minto Pyramid Principle source material remains the
property of its respective rights holders.
