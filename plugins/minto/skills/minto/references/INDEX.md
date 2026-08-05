# Working materials for Minto and MECE

This index is the source register for developing the Minto skill. It separates
the method's canon from interpretations, applications, and project evidence so
that a useful example or an isolated model failure does not silently become a
general rule.

This file is for maintainers. It does not change runtime behavior. Operational
instructions belong in `SKILL.md`; exact tests and the scoring rubric belong in
`rules.md`.

## Authority and use

Use sources in this order when they conflict:

1. **Normative canon** defines the method.
2. **First-party interpretation** clarifies the canon without replacing it.
3. **Applied guidance and examples** show how related practices work in context.
4. **Project evidence** shows where this skill succeeds or fails.

An applied source may suggest a test, and project evidence may justify adding
one, but neither may override the canon. Before promoting a project hypothesis
into the skill, check that it is consistent with the canon and useful across
more than one case.

The entries below describe copyrighted and paid materials bibliographically.
Do not copy or distribute source text beyond short quotations allowed for
analysis and attribution.

## 1. Normative canon

| Status | Material | Contribution | Intended use | Limitations |
|---|---|---|---|---|
| Primary | [Barbara Minto, *The Minto Pyramid Principle: Logic in Writing, Thinking and Problem Solving* (1996)](https://www.barbaraminto.com/textbook) | Defines the pyramid rules, vertical and horizontal logic, introductions, ordering, and structured problem solving. | Resolve questions about what the method requires and check whether a proposed skill rule is faithful to it. | Copyrighted and not distributed with this repository. The local fixtures are paraphrases, not substitutes for the book. |

## 2. First-party interpretation

| Status | Material | Contribution | Intended use | Limitations |
|---|---|---|---|---|
| Author's overview | [The Minto Pyramid Principle course](https://www.barbaraminto.com/course) | Emphasizes identifying the reader's question, organizing the points needed to answer it, and examining whether a grouping contains the right ideas and supports a useful insight. | Clarify how critically to examine groupings rather than accepting a tidy list at face value. | A course overview, not a complete statement of the method. |
| Author interview | [Barbara Minto: “MECE: I invented it, so I get to say how to pronounce it”](https://www.mckinsey.com/alumni/news-and-events/global-news/alumni-news/barbara-minto-mece-i-invented-it-so-i-get-to-say-how-to-pronounce-it.) | Restates three core rules: a parent summarizes its children; grouped ideas are logically alike; and grouped ideas follow a logical order. It also defines MECE relative to the whole being divided. | Interpret the relationship between vertical summarization, same-kind grouping, order, and MECE. | Retrospective interview rather than a procedural manual. |

## 3. Applied guidance and examples

| Status | Material | Contribution | Intended use | Limitations |
|---|---|---|---|---|
| Writing guidance | [Richard Bierck, “How to Structure What You Write,” *Harvard Business Review* (1998)](https://store.hbr.org/product/how-to-structure-what-you-write/C9812B) | Provides an applied refresher on the Pyramid Principle and places it beside alternative structuring approaches. | Compare the skill's writing workflow with adjacent business-writing practice. | Paid two-page article; the product description alone does not establish new MECE rules. |
| Problem-solving guidance | [“How to master the seven-step problem-solving process,” McKinsey](https://www.mckinsey.com/capabilities/strategy-and-corporate-finance/our-insights/how-to-master-the-seven-step-problem-solving-process) | Connects precise problem definition, logic-tree decomposition, prioritization, analysis, and synthesis into a decision story. | Inform pre-draft decomposition and the transition from analysis to a reader-facing answer. | Broader than business writing and not a replacement for Minto's grouping rules. |
| Application example | [“Taking the next leap forward in semiconductor yield improvement,” McKinsey](https://www.mckinsey.com/industries/semiconductors/our-insights/taking-the-next-leap-forward-in-semiconductor-yield-improvement) | Shows MECE used to improve reporting coverage and reduce double counting in an operational setting. | Test whether a proposed MECE check remains meaningful outside prose outlines. | Domain-specific case; its reporting design should not be generalized into a universal document structure. |

## 4. Project evidence

| Status | Material | Contribution | Intended use | Limitations |
|---|---|---|---|---|
| Volatile case | [Shared conversation: “Acceptance Protocol Format”](https://chatgpt.com/share/6a6b0e44-953c-83eb-ad7e-3fc0db102097) | Shows one function—helping an expert understand the result without reproducing the agent's work—reappearing in the introduction, key line, branches, and examples. | Study semantic duplication across levels and distinguish a branch from an example or mechanism that supports it. | External share links may expire or change; treat the case as an observation, not as a reproducible fixture or authority. |
| Evaluation summary | [`eval/report-v1.5.0-wide.md`](../../../../../eval/report-v1.5.0-wide.md) | Confirms weak first-level grouping as the recurring defect, and shows source material being dropped without acknowledgment more often with the skill than without it. | Establish whether a failure recurs often enough to justify a skill change. | 112 cells over seven engines, still one run per engine-arm-fixture cell, so variance is unmeasured. Figures are computed by `eval/aggregate.py`, not summarised by a model. |
| Gold fixture | [`02-ttv`](../../../../../eval/fixtures/02-ttv/gold.md) | Demonstrates duplicate action branches: simplifying a process and changing its method describe the same intervention, while the missing wage action is buried in observations. | Test branch merging, claim ownership, and promotion of a genuinely independent action. | A faithful paraphrase of one book example, not a universal decomposition template. |
| Gold fixture | [`05-role-of-board`](../../../../../eval/fixtures/05-role-of-board/gold.md) | Demonstrates incorrect abstraction and nesting: source topics must become evidence beneath three concrete actions. | Test whether topics, evidence, and whole-document labels are kept out of the key line. | Evaluates an action-answer case; it does not define the correct branch kind for other questions. |
| Gold fixture | [`07-headings-audit`](../../../../../eval/fixtures/07-headings-audit/gold.md) | Demonstrates false grouping, mixed abstraction levels, and likely parent-child relationships among headings. | Test audit precision without inventing unseen body content. | The fixture exposes headings only, so conclusions about missing evidence or detailed coverage are out of scope. |

## Project hypotheses — not canon

These hypotheses capture the current direction for strengthening MECE. They
must be tested before they are moved into `SKILL.md` or `rules.md`.

1. **Define the universe and answer kind first.** State what whole is being
   divided and whether its elements must be reasons, actions, parts, options,
   criteria, risks, or another single kind.
2. **Atomize the source before grouping.** Reduce the material to distinct
   claims and assign each claim one primary owner. Preserve source material
   without promoting every claim to the first level.
3. **Give each branch a boundary.** State what the branch includes and excludes.
   If one claim fits two sibling boundaries equally well, change the split,
   merge the branches, or nest one beneath the other.
4. **Test both overlap and coverage.** Compare sibling pairs for double
   placement, then inspect unassigned claims and the named universe for relevant
   gaps.
5. **Nest support instead of promoting it.** An example, mechanism, constraint,
   or item of evidence belongs under the branch it supports unless it
   independently answers the reader's question.
6. **Separate summarization from semantic echo.** A parent may compress the
   meaning of its children. A child must add a distinct reason, action, part, or
   piece of evidence; merely restating the parent's outcome at greater length is
   duplication.
7. **Use different construction checks for editing and drafting.** When editing,
   reverse-outline one claim per paragraph and cluster paraphrases before
   rebuilding the hierarchy. When drafting, create the claim-ownership map
   before writing prose.

## Maintenance checklist

- Give every new source one primary role in this index.
- Prefer direct, first-party links and record access or copyright constraints.
- Explain what a source contributes and what it cannot establish.
- Keep local evidence reproducible; label volatile external cases explicitly.
- Recheck external links and local paths when preparing a release.
- Audit this index itself for overlap among roles and gaps in the evidence base.
