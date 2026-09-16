# Removal test: candidate minus edit C

Skill arm regenerated from the 1.8.0 candidate text with edit C removed
(`patch_skill.py --without C`). Control arm copied byte-identically from
`eval/runs/v1.8.0/raw`, so the skill-minus-control delta is comparable
cell-for-cell with the candidate run. Worktree recorded as dirty by design:
the ablated text is not a committed state.
