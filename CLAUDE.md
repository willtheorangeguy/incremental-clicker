# CLAUDE.md

## Project Overview

Incremental Clicker is a Python/Tkinter GUI counter application. Users can increment, decrement, and reset a numeric counter displayed in an always-on-top window.

## Tech Stack

- **Language:** Python 3.11+
- **GUI:** Tkinter
- **Testing:** unittest (with xvfb for headless GUI testing in CI)
- **Linting:** Ruff
- **Build:** PyInstaller (produces `dist/clicker.exe`)
- **CI:** GitHub Actions

## Project Structure

```
clicker.py            # Main application (ClickerApp class)
test_clicker.py       # Unit tests (unittest)
.github/
  workflows/tests.yml # CI: runs tests on push/PR to main/master
  agents/             # AI agent role configurations
docs/app.png          # App screenshot
```

## Commands

```bash
# Run the app
python3 clicker.py

# Run tests (same as CI)
xvfb-run -a python3 -m unittest test_clicker -v

# Lint
ruff check . --fix
```

## Conventions

- **Naming:** `snake_case` for functions/variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants
- **Testing:** Test file is `test_clicker.py` using unittest. Tests must handle Tkinter window lifecycle (setUp creates root window, tearDown destroys it).
- **CI requires xvfb** for headless Tkinter testing — use `xvfb-run -a` prefix locally on Linux if no display is available.

## Architecture

`clicker.py` contains a single `ClickerApp` class:
- `self.count` — integer counter state
- `increment()` / `decrement()` / `reset()` — modify counter
- Label displays count, three buttons provide controls
- Window is 200x150, always-on-top
