# Incremental Clicker — Roadmap

Known gaps, observed from the code. Limitations, not a schedule. Concrete defects with
suggested fixes are in [`internal/known-issues.md`](./internal/known-issues.md).

## Gaps

**Nothing persists.** The count exists only while the window is open. Fine for a session
counter, and it means an accidental close loses the number with no recovery.

**One counter per window.** Counting two things means running the program twice.

**No labels.** The counter is a bare number, so remembering what it counts is on you.

**No keyboard shortcuts.** Everything is a click, which is awkward for the counting-while-busy
case the program exists for.

**Window position is not remembered**, so it needs repositioning each run.

**Always-on-top is not guaranteed.** It is a window-manager hint, and some environments
ignore it. Nothing in the program can change that.

## Repository

**Build output is tracked**, and the clone is roughly 25 MB for 41 lines of source. `.gitignore`
already excludes `build/` and `dist/`, so the fix is untracking rather than a rule change —
see [`internal/known-issues.md`](./internal/known-issues.md).

## Non-goals

- **A full incremental game.** The name says clicker; the program is a counter. Upgrades,
  currencies, and idle mechanics would be a different project.
- **Persistence or sync.** A counter that outlives the window is a different program.
- **Third-party dependencies.** Standard-library only is why it will still run in five years.
