# Use one directly referenced workflow library

> **Status:** Maintained workflow

- A consuming project records its accepted library revision and source hashes in `.agent-workflows.json`; its existing root/guide points there. Generic workflow behavior is maintained in the public library rather than copied into project guides.
- At a relevant session, verify the record against the accepted library checkout and compare public main when available. Use the repository's `scripts/project_reference.py check` or the equivalent revision-pinned source evidence. Changed, stale, missing and unavailable are explicit; offline equality does not prove upstream freshness.
- Follow the checked source directly for startup, short idea generation, intake, prompt translation and the selected work stage. Keep private project reporting and coordinator configuration outside the public library.
- Update generic behavior at source, rebuild packages, review the change, then refresh each affected project's record and generated CI adapter together. Never silently change acceptance from a moving main link.
- Project PR/startup checks expose drift. A source/adoption PR dependency stays visible until accepted commits reach the governed branch; new host sessions/packages require their own reload.
- If evidence is unavailable, preserve actual project authority and the short idea/intake fallback. Hold only dependent work. Do not create a duplicate queue, coordinator or timer to repair a reference.
