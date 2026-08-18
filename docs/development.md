# Incremental Clicker — Development

## Setup

```bash
git clone https://github.com/willtheorangeguy/incremental-clicker.git
cd incremental-clicker
```

Nothing to install beyond Python with tkinter.

## Run

```bash
python clicker.py
```

## Tests

```bash
pytest test_clicker.py
```

`test_clicker.py` covers the counter methods directly rather than driving the GUI, which is
what lets the suite run in CI where no window can be opened.

Keep it that way: logic that reaches into the widget stops being testable headlessly, and the
separation here is convention rather than something enforced.

## Where to make changes

| Change | Where |
|---|---|
| Counter behaviour | The counter class in `clicker.py` |
| Window appearance or layout | `clicker.py` |
| Test coverage | `test_clicker.py` |

At 41 lines there is only one file, so the real discipline is keeping the counter logic
separable from the widget that displays it.

## Build artifacts do not belong in git

`build/` and `dist/` are both in `.gitignore`, and both are still tracked — they were
committed before the rule existed, and `.gitignore` does not untrack retroactively.

Before adding more build output, run:

```bash
git rm -r --cached build dist
```

See [`internal/known-issues.md`](./internal/known-issues.md).

## CI

`tests.yml` runs the suite on push and pull request.
