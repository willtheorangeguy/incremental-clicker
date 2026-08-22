# Incremental Clicker — FAQ

## Does it save my count?

No. Closing the window discards it. There is no state file, no history, and no export — the
program is scoped to a single session.

## Why does it stay on top of everything?

That is the point. A counter you have to alt-tab to is worse than a piece of paper, because
switching windows is exactly when you lose count.

## It is not staying on top

Always-on-top is a **hint** to the window manager, not a guarantee. Some Linux window managers
override or ignore it, and some full-screen applications take priority regardless. See
[Troubleshooting](./troubleshooting.md).

## Can I go below zero?

Yes. Decrement is not floored at zero, which is deliberate for tally-style counting where a
correction may cross it.

## Do I need to install anything?

Python with tkinter, and nothing else. On Windows and macOS tkinter comes with Python; some
Linux distributions package it separately.

## Can I run it without Python?

On Windows, yes — `dist/clicker.exe` is committed to the repository. Prefer a
[release](https://github.com/willtheorangeguy/incremental-clicker/releases) if one exists,
since the committed binary is not versioned and can drift from the source.

## Why is the clone so large for such a small program?

Because `build/` and `dist/` are tracked — roughly 25 MB of PyInstaller output for 41 lines of
source. `.gitignore` excludes them, but they were committed before that rule existed. See
[`internal/known-issues.md`](./internal/known-issues.md).

## Why is the test file bigger than the program?

A reasonable ratio at this size. The counter logic is exactly the kind of thing that is cheap
to test and easy to break.

## Can I count more than one thing at once?

No — one window, one counter. Running the program twice gives you two independent windows,
which is the available workaround.

## Does it remember where I put the window?

No. Position resets each run.
