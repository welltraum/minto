# Removal test: candidate minus edit R

Skill arm regenerated from the 1.8.0 candidate text with edit R removed
(`patch_skill.py --without R`). Control arm copied byte-identically from
`eval/runs/v1.8.0/raw`, so the skill-minus-control delta is comparable
cell-for-cell with the candidate run. Worktree recorded as dirty by design:
the ablated text is not a committed state.
