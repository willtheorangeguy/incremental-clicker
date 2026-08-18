# Incremental Clicker — Installation

## Requirements

Python with tkinter. No third-party packages.

tkinter ships with Python on Windows and macOS. Several Linux distributions package it
separately:

```bash
sudo apt install python3-tk       # Debian/Ubuntu
sudo dnf install python3-tkinter  # Fedora
sudo pacman -S tk                 # Arch
```

## From source

```bash
git clone https://github.com/willtheorangeguy/incremental-clicker.git
cd incremental-clicker
python clicker.py
```

There is no install step, no packaging, and no console script — the file is run directly.

## Prebuilt Windows executable

`dist/clicker.exe` is committed to the repository and runs without Python.

Two caveats worth knowing:

- **It is not versioned.** Nothing ties it to a particular commit, so it can silently drift
  from `clicker.py`.
- **It is why the clone is large.** `build/` and `dist/` account for roughly 25 MB. See
  [`internal/known-issues.md`](./internal/known-issues.md).

Prefer a [GitHub release](https://github.com/willtheorangeguy/incremental-clicker/releases)
if one exists.

## Verify

```bash
python clicker.py
```

A small always-on-top window. If nothing appears, tkinter is the usual cause.

## Next

[Quickstart](./quickstart.md), or [Usage](./usage.md).
