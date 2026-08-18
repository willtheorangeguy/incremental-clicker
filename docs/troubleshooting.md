# Incremental Clicker — Troubleshooting

## No window appears

Almost always missing tkinter. It ships with Python on Windows and macOS, but several Linux
distributions package it separately:

```bash
sudo apt install python3-tk       # Debian/Ubuntu
sudo dnf install python3-tkinter  # Fedora
sudo pacman -S tk                 # Arch
```

Confirm it directly:

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
```

An `ImportError` there is the whole explanation.

## It is not staying on top

Always-on-top is a hint to the window manager rather than something the program can enforce.

- **Some Linux window managers** ignore or override the hint. Many have a per-window
  "Always on Top" toggle in the title-bar menu that will work.
- **Full-screen applications** commonly take priority regardless, especially games.
- **macOS Spaces** can move the window rather than keeping it above.

Nothing in the program can change this.

## Running over SSH does nothing

It is a desktop application and needs a display. Use X forwarding, or run it on the machine
itself.

## The count reset itself

Nothing persists, so any restart begins at zero. If the window closed unexpectedly, the count
is gone.

## The window is too small, or in the way

It is an ordinary window — drag it anywhere. Position is not remembered between runs.

## `dist/clicker.exe` behaves differently from the source

Likely because it is stale. The committed binary is not tied to any particular commit, so it
can lag behind `clicker.py`. Run from source to be certain:

```bash
python clicker.py
```

## Tests fail with a display error

They should not — `test_clicker.py` exercises the counter methods directly rather than the
GUI. A display error there means something reached into the widget from the logic, which is
the separation worth preserving.
