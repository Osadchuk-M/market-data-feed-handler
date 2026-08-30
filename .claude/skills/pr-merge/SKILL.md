---
name: pr-merge
description: "Use this skill when the user asks to merge the current pull request."
---

Steps:
1. Resolve all unresolved review conversations on the current PR (if any).
2. Mark the PR as ready for review.
3. Enable auto-merge with squash (`gh pr merge --auto --squash`).
4. Wait for merge by polling `gh pr checks --watch` until the PR is merged.
5. Check out `main`.
6. Pull latest changes.
