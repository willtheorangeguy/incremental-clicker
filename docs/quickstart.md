# Incremental Clicker — Quickstart

## Run it

```bash
git clone https://github.com/willtheorangeguy/incremental-clicker.git
cd incremental-clicker
python clicker.py
```

A small window appears and stays above everything else.

## Or skip Python entirely

The repository includes a prebuilt Windows executable at `dist/clicker.exe`, so a machine
without Python can run it directly.

That said, prefer a [release](https://github.com/willtheorangeguy/incremental-clicker/releases)
if one is available — the committed binary is not versioned and can drift from the source.

## Use it

| Action | Effect |
|---|---|
| Increment | Count up |
| Decrement | Count down |
| Reset | Back to zero |

## Nothing is saved

Closing the window loses the count. There is no state file — see [FAQ](./faq.md).

## If no window appears

Almost always missing tkinter, which some Linux distributions package separately:

```bash
sudo apt install python3-tk      # Debian/Ubuntu
```

See [Troubleshooting](./troubleshooting.md).
