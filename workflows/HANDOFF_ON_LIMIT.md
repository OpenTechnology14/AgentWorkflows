# Hand off when a session hits its usage limit

> **Status:** Maintained reusable policy (`AW-POLICY-HANDOFF-ON-LIMIT-01`) · Target-project rules retain authority

**Rule.** When a Claude session hits a 5-hour or weekly limit:

- **Unstarted rows flagged `claude_ok`** (Claude preferred, QW acceptable) become `pending_qw`, so a QW route can pick
  them up, for example with an agent CLI's unattended run mode.
- **Rows Claude was mid-way through** get a resume checkpoint ([checkpoints](CHECKPOINTS.md)). QW may resume only if
  every remaining step is [QW-appropriate](MODEL_FIT.md). Otherwise the row waits for Claude.
- **Claude-only rows** wait. They are never handed off.

**Guardrails carried over from [HF routing](HF_ROUTING.md):**

- Pickup runs only on a route the project has authorized for unattended work.
- A watchdog enforces time and step limits, rather than the prompt merely stating them.
- Each run gets one bounded attempt in an isolated branch or worktree. No fix-until-green loop.
- The row's `review_model` still reviews the result before merge.

Setting `pending_qw` is a routing state. It does not by itself authorize a launch.

**Canonical example.** At the limit, "regenerate API reference docs" (unstarted, `claude_ok`) flips to `pending_qw` and
QW runs it. "Decide the failover policy" (mid-way, raises a Question) keeps its checkpoint and waits.

**Entry-gate impact.** Rows carry a handoff flag (`claude_only` / `claude_ok`) at registration. Absent means
`claude_only`.
