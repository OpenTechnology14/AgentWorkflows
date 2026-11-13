# Audit and finding lifecycle

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- Define scope and evidence revision before scanning. Read canonical security records and current assignments; distinguish a read-only audit from authorized remediation.
- Inventory affected source, docs, routes/actions, tests and operational evidence. A missing test run, outdated doc and observed defect have different dispositions.
- Attribute every finding with evidence, impact, uncertainty and one candidate canonical parent. Deduplicate against existing bugs/proposals/PRs before allocating an ID.
- Use the project's finding lifecycle, reviewer/expiry rules and audit log. Never auto-close, accept risk or approve a pending proposal from an audit result.
- Cross-project checks compare both sides' actual contracts and revisions; no shared CI is assumed. Source ledgers are canonical; companion docs link rather than copy competing registries.
- Prepare approval-preview corrections where the target SOP requires them. Execute an authorized selected fix under its parent separately from the scan.
- A credible urgent security finding enters immediate safe triage under policy even if full reproduction is unavailable.
- Return concise findings and generated next prompts, not entire transcripts or a second permanent implementation backlog.
