# Incremental Clicker — Usage

## Running it

```bash
python clicker.py
```

A small window opens and stays above every other window.

## Controls

| Action | Effect |
|---|---|
| Increment | Count up by one |
| Decrement | Count down by one |
| Reset | Back to zero |

Decrement is not floored at zero — see [FAQ](./faq.md).

## Why always-on-top matters

It is the whole feature. A counter you have to alt-tab to is worse than a piece of paper,
because switching windows is exactly the moment you lose count.

The window is small and stays out of the way, so it can sit in a corner while you work in
something else.

## What it is good for

Anything counted while doing something else — reps, laps, tally marks, stock takes, passing
cars. Short sessions where a running total matters and the history does not.

## Nothing persists

Closing the window discards the count. There is no state file, no history, and no export.

That suits a session-length counter and rules out anything longer. If you need the number
later, write it down before closing.

## Moving the window

It is an ordinary window — drag it wherever suits. Position is not remembered between runs.
