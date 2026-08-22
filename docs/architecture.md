# Incremental Clicker — Architecture

## The whole application

```text
clicker.py        41 lines — the window and the counter
test_clicker.py   95 lines — tests for the counter logic
```

The test file is more than twice the size of the application, which is a reasonable ratio for
something this small.

## The counter class

A single class holding the count, with three methods:

| Method | Does |
|---|---|
| `increment` | Count up |
| `decrement` | Count down |
| `reset` | Back to zero |

State is one integer in memory. There is no persistence layer because there is no persistence.

## Always-on-top

The window sets the toolkit's topmost hint, so the window manager keeps it above others.

This is a **hint**, not a guarantee. Behaviour varies by platform and window manager, and some
Linux setups override or ignore it. That is the one place this program depends on something it
does not control — see [Troubleshooting](./troubleshooting.md).

## No dependencies

Pure standard-library tkinter. No third-party packages at runtime, nothing to install beyond
Python, and nothing that can break from an upstream release.

For a 41-line utility that is the right shape: it will still run in five years.

## Testing without a display

`test_clicker.py` covers the counter methods directly rather than driving the GUI, which is why
the suite runs in CI where no window can be opened.

The separation is implicit rather than enforced — the logic simply does not reach into the
widget — and it is worth preserving if the program grows.

## Packaging

There is none. No `pyproject.toml`, no console script; `clicker.py` is run directly.

A PyInstaller build exists as `dist/clicker.exe`, along with its intermediates in `build/`.
Both are tracked in git despite `.gitignore` excluding them — see
[`internal/known-issues.md`](./internal/known-issues.md).

## CI

`tests.yml` runs the test suite on push and pull request.
