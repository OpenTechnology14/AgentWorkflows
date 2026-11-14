# Decision gates: a short answer and a full reasoning

> **Status:** Owner-directed implementation · **Date:** 2026-11-13

The owner directed that every decision gate carry both a one-line answer and a full reasoning. The rule is generic, so it lives in this library and projects point at it.

## Contract

| ID | File |
|---|---|
| `AW-POLICY-DECISIONS-05` | [`workflows/DECISIONS.md`](../../workflows/DECISIONS.md) |
| the templates | [`templates/PROPOSAL.md`](../../templates/PROPOSAL.md), [`templates/QUESTION.md`](../../templates/QUESTION.md), [`templates/DECISION.md`](../../templates/DECISION.md) |

## Where the new rule meets existing ones

The `**Question:**` line and the A/B options already existed in the question template and the [logs workflow](../../workflows/LOGS.md). This rule adds the pointer and the four-part reasoning and changes nothing else about how a question is asked. Gates written before the rule stay valid while a project lists them as missing their reasoning.

## Decision gates

| ID | Question | Default applied | Why it is a real choice |
|---|---|---|---|
| `AW-D09` | **Question:** Must every gate carry all four reasoning parts, even a small one? A (Recommended): yes, one line each. B: only gates that change scope, security or anything public. Reasoning: [below](#reasoning-for-aw-d09). | A | Skipping headings for small gates is faster, but it makes "small" a judgment each author makes alone |

### Reasoning for AW-D09

- **Context:** The rule asks for a short answer and a full reasoning on every gate. Some gates are small (a name, a default), and a four-part section for them can feel like paperwork. The rule is new, so the habit has not formed either way.
- **Trade-offs:** A keeps one shape everywhere, so a reader and a checker never have to decide whether a gate was small enough to skip, and `none, because …` costs one line. B saves effort on trivial gates but invites under-describing a gate that turns out to matter, and a checker would need a size test it cannot make reliably. A is easy to relax later; B is hard to tighten once gates exist without reasoning.
- **Downstream impact:** With A, an index generator checks one rule: the four parts exist. With B, it needs a way to mark a gate small, and every such marker is a bypass to audit. Existing projects list their older gates as missing reasoning under either answer.
- **Cost of deferring:** Nothing blocks. The default applies, so projects write all four parts now. If the answer is B, the extra parts already written are harmless.

## Rollout and rollback

Projects add the pointer to their question template and a check to their index generator. Rollback is removing the pointer requirement from the generator; the reasoning sections stay valid as ordinary documentation.
