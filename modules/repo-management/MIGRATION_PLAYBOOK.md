# Public migration playbook

> **Status:** Maintained reusable procedure · Target-project rules retain authority

How to take a private project public without publishing what should stay private. It is written from three real migrations; section 5 summarizes them.

## 1. When to migrate, and when to stay private

| Situation | Do this |
|---|---|
| Every ref is clean: no personal identity, no secret, nothing private in any file | Flip the existing repository to public. It is the cheapest path |
| History or pull-request refs carry identities or data you cannot remove | Create a fresh repository (section 4). A history rewrite cleans branches and tags, but GitHub owns the hidden `refs/pull/*` refs and a rewrite cannot reach them |
| The tree mixes public and private material (a private matrix, deployment records, generated dashboards) | Keep the working repository private and publish a reviewed snapshot as a second repository, tracked as a [snapshot pair](SYNC_TRACKER.md) |
| Nobody outside needs it, or its value is the private data or process | Stay private, and still fix the hygiene findings so a later flip is cheap |
| The project is finished | Archive it |

## 2. What blocks a public flip

- Any ref (branches, tags, pull-request refs) with a personal commit identity you do not want public, or with a secret.
- A flip also exposes issues, pull requests, Actions runs and artifacts. Anything private in them blocks the flip.
- Private names, links or tracker ids in files, and generated artifacts that embed another project's rows (section 6).
- No license, or a dependency or asset whose license does not allow redistribution under yours (section 7).
- No private channel for security reports, and CI that needs private secrets to pass.

Not blockers, but do them in the same change: a README written for a public reader, a code of conduct, a contributing guide, and repository protections.

## 3. OSS-readiness checklist

- [ ] **History and identity.** Commits counted by identity class (never print an address); every ref checked, including mirror-cloned pull-request refs; a secret scan over all refs.
- [ ] **Content.** No personal literals, home paths, private repository names, internal tracker ids or private links in any tracked file.
- [ ] **Generated artifacts.** Every generated file (HTML exports, JSON receipts, manifests, snapshots, indexes) opened and scanned for identifiers that belong to another project.
- [ ] **Licenses.** A license file; dependency and asset licenses checked against it.
- [ ] **Community files.** `LICENSE`, `CODE_OF_CONDUCT.md` with a working contact, `SECURITY.md` with a private channel, `CONTRIBUTING.md`, a README for outsiders.
- [ ] **Settings.** Private vulnerability reporting, secret scanning and push protection, Dependabot alerts and security updates, squash-only merges, a read-only default Actions token, branch protection.
- [ ] **Consumers.** Every project that pinned the old location is listed and repointed.

## 4. The fresh-repository procedure

Do the irreversible steps (5 to 7) in one short window, with the tree already built and checked.

1. **Audit first, report only.** Count commits by identity class, mirror-clone to see `refs/pull/*`, scan all refs for secrets, scan content for private names, read the current settings.
2. **Build and check the tree in scratch.** Merge any open work you want to ship, write the community files and a public README, run the project's own checks, then scan for personal literals, home paths and private names.
3. **Make one commit with the noreply identity.** Set `user.name` and `user.email` locally; a machine's global email may not be a noreply address. Create an orphan branch, commit, then fetch only that commit into a fresh `git init` and check the author and committer classes there.
4. **Get an independent go/no-go** on the tree and on this command list.
5. **Create the private mirror.** A new private repository. Push branches and tags, and push the old pull-request heads as ordinary branches (`refs/pull/*:refs/heads/pr/*`), because GitHub refuses pushes to the hidden refs. Compare the refs on both sides.
6. **Retire the original.** Rename it to `<name>-archive`, make it private, archive it. It keeps the hidden pull-request refs and is the full-fidelity copy.
7. **Create the empty public repository** under the original name, with no README, license or gitignore. Turn on private vulnerability reporting, secret scanning and push protection before the first push, then push the single commit to `main`.
8. **Apply the other settings:** squash-only merges, delete branch on merge, a read-only default Actions token that cannot approve pull requests, Dependabot alerts and security updates.
9. **After the first CI run,** protect `main`: pull request required, no required approvals if you are the only maintainer, the CI job name read from the actual run as the required check, linear history, no force-push or deletion, an administrator bypass left available.
10. **Verify from a fresh clone:** exactly one commit, noreply identities, CI green, every setting read back.
11. **Close the mirror.** Delete any temporary candidate branch from it, then archive it.
12. **Repoint consumers.** Links to the old pinned revisions stop resolving for everyone else at step 6, when the original goes private, and stay broken after step 7, because the new repository does not contain those commits. For each pinned file compare its blob at the old and the new revision: identical means replace the revision; different means review the sentence that quotes it. Re-record each project's reference and open one pull request per project.
13. **Record the pair** in the [sync tracker](SYNC_TRACKER.md) and the decisions in your private records.

**Gotchas.** In zsh, `$SHA:refs/heads/main` is a modifier, not a refspec: write `${SHA}:refs/heads/main`. Dependabot opens a pull request on the new repository within minutes. Squash merges are safe for identity only when the account keeps its email private: check the first merge commit. Between steps 6 and 7 the old URL redirects to the private archive and 404s for everyone but you; step 7 ends that redirect, and the old name then resolves to the new repository.

## 5. Reference migrations

Figures are from each audit at the time it ran.

- **Job Hunter.** The audit found a personal address reachable through pull-request refs, which a history rewrite cannot clean. The project was re-created with a clean history: a new public repository, the original renamed, made private and archived, and a private sibling repository.
- **The Agent Workflows library** (the predecessor of this repository). 9 of 15 commits across 11 refs carried a personal identity, 3 of them only behind pull-request refs. Content, secrets and private identifiers were clean, every repository control was off, there was no code of conduct, and the security policy had no private channel. The procedure above was followed: a private mirror, the original archived, one clean commit that also carried the content of two open pull requests, and a repoint of every pinned consumer. Choices worth copying: the conduct contact is the repository's private reporting form until a project mailbox exists; no tag or release was re-created; a short independent review ran before the irreversible steps.
- **MyFeed.** 49 of 65 commits and every one of its 24 pull-request refs carried a real address. It had no license, code of conduct, security policy or contributing guide, a README written for internal contributors that named a private sibling, and none of the repository controls. It took the same shape as the others.

## 6. Cautionary tale: generated artifacts

A migration's public first commit can still carry another project's content. In one migration, a generated dashboard page and its snapshot receipt embedded **dozens of rows from a different, private project's queue**, and the receipt named that project's source file and its hash. The audit had counted addresses, scanned for secrets and searched for names, and all of those passed. Only opening the generated files and looking for another project's identifiers finds this.

- **A fresh repository removes old history, not content.** Whatever is in the first commit is public.
- List every generated file and read it, not just the source that produced it.
- Scan the tree for identifier patterns that belong to other projects: their tracker ids, their repository names, their private file paths and hashes.
- Regenerate each artifact from the public project's own data only, then scan again.
- Keep an allow-list of identifier patterns per repository and fail the export when one appears that is not on it.

## 7. OSS compatibility matrix

| Area | What to check | Blocks a flip? |
|---|---|---|
| Commit identities | Author and committer classes on every ref | Yes, unless you accept them as public |
| Secrets | Secret scan on all refs, Actions logs and artifacts | Yes |
| Project license | A license file; the choice is yours (MIT, Apache-2.0 and so on) | Yes, none means "all rights reserved" |
| Dependency licenses | GPL, AGPL, non-commercial and share-alike terms against your license | Yes when incompatible |
| Assets (fonts, images, audio, models, datasets) | Redistribution rights and attribution | Yes for anything you cannot redistribute |
| Private references | Names, links, tracker ids, paths in files and generated artifacts | Yes |
| Issues, pull requests, Actions | Content a flip would expose | Yes for private content |
| Community files | Code of conduct contact, security channel, contributing guide | No, but do them with the flip |
| Repository settings | Protections, scanning, token permissions | No, but do them with the flip |
| Consumers | Projects that pin the old location | No, but repoint at once |

## 8. Public considerations

Beyond what to remove, decide these on purpose:

- **Visibility is permanent in practice.** Archives, mirrors and search caches copy a public repository within minutes. A later private flip hides it on GitHub only.
- **Support.** Say what you do not promise: response times, supported versions, feature requests.
- **Names and marks.** Check project and product names, logos and screenshots for third-party marks.
- **Contributor privacy.** Contributors should commit with a noreply address; the account setting that blocks pushes exposing an email is worth turning on for maintainers.
- **Maintenance load.** Dependabot, security reports and pull requests arrive once you are public; decide who triages and how often.
- **Inbound equals outbound.** Contributions are under the repository license unless you say otherwise; do not add a contributor agreement by accident.
- **Announcement and deprecation.** Decide when to announce, and leave a note in the archived original saying where the project moved.
- **What the world will read.** Public pull request descriptions, commit messages and issue text become part of the record; keep real names, internal ids and private links out of them from the first day.

## 9. After the flip

Watch the first week: triage the Dependabot pull request, confirm the security form works by reading it as a reporter would, check that CI stays green on `main`, and rescan the tree after any large merge. Re-run the generated-artifact scan whenever an export or dashboard is regenerated.

## 10. What a migration does not do

It does not recall copies that already exist: public archives, caches, search indexes and other people's clones keep the old history. It does not change the past for anyone who pinned a commit and cached it. Treat anything that was public as having been seen, and rotate secrets that ever appeared in any ref.
