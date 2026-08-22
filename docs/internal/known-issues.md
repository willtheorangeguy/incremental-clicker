# Known Issues — incremental-clicker

Concrete defects and gaps found while writing this repository's documentation in
August 2026. **Nothing here was changed** — each one needs a code, configuration, or
licensing decision rather than a documentation one.

Ordered by severity. See [`docs/roadmap.md`](../roadmap.md) for the narrative version,
which also covers deliberate non-goals.

**2 open:** 1 medium, 1 low.

## 1. 25 MB of build output is tracked despite .gitignore already excluding it

**Severity:** Medium
**Where:** `build/` (17 files), `dist/clicker.exe`

**What:** `.gitignore` lists both `build/` and `dist/`, but 18 files under them are still tracked — PyInstaller intermediates (`Analysis-00.toc`, `PYZ-00.pyz`, `base_library.zip`, tree manifests) totalling ~14 MB, plus an ~11 MB `clicker.exe`.

**Why it matters:** They were committed before the ignore rule was added, and `.gitignore` does not untrack files retroactively — so the rule looks like it is working and is not. The repository carries 25 MB of build output for 41 lines of source, every clone pays for it, and the committed `.exe` is an unreviewable binary that will silently go stale against the code.

**Suggested fix:** `git rm -r --cached build dist` and commit. The ignore rules are already correct, so nothing else is needed. Publish the executable through GitHub Releases, where it is versioned and its provenance is the release workflow. Note the history still contains the blobs; only a history rewrite reclaims that space.

## 2. The README was a single sentence

**Severity:** Low
**Where:** `README.md`

**What:** Two lines including the heading.

**Why it matters:** Nothing described how to run it, that a prebuilt executable exists, or that the window is always-on-top by design.

**Suggested fix:** Addressed by the documentation added in this sweep.

---

## Also, across every repository

**`.bandit` is present on disk but untracked in git.** Verified in PyWorkout, treklogger,
skyscanner-cli, booking-cli, piggy, and aibot — the config file exists locally in each but
`git ls-files` does not know about it, so none of it reached GitHub.

The August 2026 security sweep therefore looks complete locally and landed nowhere. Worth
checking across all 44 repositories it covered.
