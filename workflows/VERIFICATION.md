# Verification and acceptance evidence

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- Select checks from the actual change and target's required gates. Do not prescribe a full app build for every prose edit or invent commands that the project lacks.
- Verify user outcomes, not only clicks or process exit. Cover success, denied/failure, cleanup, count boundaries and applicable concurrency/replay/recovery cases.
- Use synthetic fixtures, isolated temporary storage and test-specific accounts/environments. Never silently touch production data, real resumes or paid APIs.
- Label each claim PASS, FAIL, BLOCKED or NOT RUN with revision, environment, command/check, artifact and limits. A mock/stub pass is not a real integration round trip.
- Separate source, unit/component, integration, browser/manual, real hardware/provider and live deployment acceptance. Do not claim native Windows, Unreal editor, GPU inference or publishing from a static source review.
- For visible changes, inspect rendered states, keyboard/focus and responsive variants under the target's UI rules. For migrations, use exact target/applied-state preflight and transactional postflight when permitted.
- Once appropriate required checks pass, repeat/broaden only for a new change, failure or unresolved concern. Preserve failing evidence honestly.
- Generate an acceptance prompt when only owner/device/live proof remains; name the exact action and target, not a vague request to test everything.
