# Review, proposal wrap-up and release

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- Start with owner-selected proposal wrap-up. Compare approved outcome, actual main and PR head, diff, tests and acceptance. Return: ready for review, remaining implementation, owner proof needed, held or unknown.
- PR titles and mergeability are evidence pointers, not proof of completion. Check conflicts, actual checks, reviews and source revisions. Do not duplicate work already in an open PR.
- Inspect behavior, security/data boundaries, regressions, scope and observability. Required tests prove written assertions; review checks missing logic and assumptions.
- A finding generates a bounded repair prompt under existing authority. A behavior change outside scope becomes a decision/proposal refresh, not an unannounced fix.
- Update bug/proposal/source/queue evidence consistently. Keep implemented, accepted and released distinct. Complete only when the governing definition of done is met.
- Use task branches and PRs under each project's rules; open the PR by its required first-push boundary. Never reset/rebase/clean another agent's worktree or force-push as a shortcut.
- A named owner merge/override instruction applies only to that action and does not turn failed checks into passes. General workflow adoption is not blanket merge permission.
- PR descriptions name concrete behavior and evidence for a reviewer without chat history. Preserve rollback, live gates, known limitations and canonical bookkeeping.
- After wrap-up, route the selected next bug/reliability item under existing priority; decisions occur alongside actual blockers, not as a mandatory approval for every fix.
