# Bounded implementation

> **Status:** Maintained reusable procedure · Target-project rules retain authority


- Verify the selected canonical item, approval, readiness, active PR/branch and worktree ownership. Reuse existing work; preserve foreign changes and stop on overlapping ownership.
- The facilitator supplies the full prompt: conclusion, scope/allowed files, current evidence, dependencies, constraints, verification, model/HF decision, reviewer and checkpoint. Workers cannot assume inherited chat context.
- Make the smallest coherent change satisfying the accepted outcome. Do not add unrequested features, speculative abstractions or unrelated refactors.
- Follow the target's layer/type/storage/network/UI conventions and applicable skills. Keep secrets and real customer/profile data out of tests, logs and providers.
- Test the changed behavior and failure cases with relevant existing tools. Do not weaken types, remove guards or swap real data for static examples merely to make a build pass.
- Return actual diff, commands/results, remaining gaps and a plain conclusion. Generate the reviewer prompt against the actual changed revision; a worker summary is not independent proof.
- Scope growth, missing prerequisites or new product choices return to intake/decision with the minimum blocked slice. Existing authorized independent work can continue.
