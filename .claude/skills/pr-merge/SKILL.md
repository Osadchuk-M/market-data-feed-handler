---
name: pr-merge
description: "Use this skill when the user asks to merge the current pull request."
---

Steps:
1. Resolve all unresolved review conversations on the current PR (if any).
2. Mark the PR as ready for review.
3. Enable auto-merge with squash (`gh pr merge --auto --squash`).
4. Wait for the actual merge by polling the PR state until it reports `MERGED`
   (`gh pr view --json state,mergedAt`); stop and report if it becomes `CLOSED` instead.
5. Check out `main`.
6. Pull latest changes.
