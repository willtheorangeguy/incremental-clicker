# Incremental Clicker — Documentation

A 41-line tkinter counter that stays above every other window. There is not much to it, which
is the point.

```
incremental-clicker/
├── docs/
│   ├── README.md          this page
│   ├── quickstart.md      run it
│   ├── installation.md    Python, or the prebuilt executable
│   ├── usage.md           the controls
│   ├── architecture.md    how always-on-top works, and the class
│   ├── development.md     tests and CI
│   ├── faq.md             persistence, platforms, the executable
│   ├── troubleshooting.md no window, not staying on top
│   └── roadmap.md         known gaps and non-goals
├── clicker.py             the whole application
└── test_clicker.py        counter logic tests
```

## Pages

- [Quickstart](./quickstart.md) — clone and run
- [Installation](./installation.md) — Python with tkinter, or the Windows build
- [Usage](./usage.md) — increment, decrement, reset
- [Architecture](./architecture.md) — the counter class and the always-on-top hint
- [Development](./development.md) — the test suite and CI
- [FAQ](./faq.md) — does it save, which platforms, why so small
- [Troubleshooting](./troubleshooting.md) — no window, not staying on top
- [Roadmap](./roadmap.md) — known gaps and non-goals

## What it is for

Counting things while doing something else — reps, laps, tally marks, passing cars. The
always-on-top behaviour is the entire feature; a counter you have to alt-tab to is a worse
counter than a piece of paper.

## Note on repository size

`build/` and `dist/` are tracked despite `.gitignore` excluding them, so a clone pulls about
25 MB for 41 lines of source. See [`internal/known-issues.md`](./internal/known-issues.md).
