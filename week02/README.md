# Week 02 — Predict, break, fix

Two hours. You will not write a program from a blank file today. You will be
handed programs that run, and asked three questions about them, over and over:

1. **What does it print?** — before you run it.
2. **Where is the fault?** — it runs, and it is wrong.
3. **Does it meet the spec?** — here is the brief, here are three attempts.

Those three questions are the job for the rest of the semester, because the code
you will be handed from now on is mostly going to be written by a machine, and
someone has to be able to tell whether it is any good.

The short drills are in the slides, and they run in your browser:
<https://sd5913.github.io/teaching/week02/>. This folder is the longer version,
on your own machine, with real windows.

---

## 0:00 — `uv run`, and nothing else

```bash
cd pfad          # your clone from week 1
git pull         # this folder arrives
cd week02
uv run schotter.py
```

A window opens with a Schotter in it. Press `space`. Press it again.

That is the only Python command you will type this semester: **`uv run <file>`**.
It finds a Python if you have none, installs what the file needs, and runs it.
The file says what it needs in the first four lines:

```python
# /// script
# requires-python = ">=3.10,<3.14"
# dependencies = ["pygame-ce"]
# ///
```

Read that as: *this program is not finished until it says what it needs.* Every
script you hand in from now on carries that block if it imports anything.

**Do not type `python`.** On a fresh Windows machine that word opens the Microsoft
Store. On a Mac it may be a Python from 2019. `uv run` sidesteps both.

No `uv` on this machine? Download and double-click
<https://github.com/ait4x/v915-setup/releases/latest/download/setup.bat> (Windows),
or `brew install uv` (Mac), then come back.

---

## 0:10 — Read first, run second

Three programs, each one rule from the lecture. Open the file **before** you run it.

| File | What it draws | Read this before running |
|---|---|---|
| `schotter.py` | Nees, *Schotter* — the week 1 sketch, live | `damage(row)`. Say in one sentence why the top stays calm. |
| `nake.py` | Nake, *Walk-through-Raster* — the rule from the slides, as lines | The `cap = ...` line. Say what combination it makes impossible. |
| `schotter3d.py` | Schotter, one dimension up — cubes instead of squares | `project()`, twenty lines at the bottom. Where does `distance` go? |

For each one: predict, then run, then change **one** knob at the top and predict
again. `S` saves a PNG. Keep one PNG per script — you will need them at the end.

`schotter3d.py` is the one to spend time on. There is no 3D library in it. A cube
is eight points; a point on screen is `x / depth` and `y / depth`; that is the
whole trick, and it has been the whole trick since 1435. Drag to orbit, and read
the function that makes the orbit happen.

---

## 0:40 — Tides: somebody else's data, your rule

```bash
cd tides
uv run tides.py
```

Twenty-four rings, one per quarter hour of a tidal forecast for Hong Kong waters,
each vertex on each ring shoved by the current at one point in the sea. This is a
Python translation of a two.js piece; it is the kind of thing assignment 2 asks for,
and week 3 is about getting data like this yourself.

- `tides.csv` is committed, so this runs without internet.
- `fetch_tides.py` is how the CSV was made: it asks the Hydrographic Office for a
  quarter-hour slot, caches the answer in `cache/`, and writes the CSV. Run it with
  `--now` if the room has wifi and you want today's water.
- The knobs are at the top of `tides.py`. `ORIENTATION`, `DISPLACEMENT` and `SPREAD`
  change the picture the most. Predict, then look.

Question to answer in your notes: `ring()` reads the arrows with `i % len(arrows)`.
What does the picture do if you change that to `i * len(arrows) // RESOLUTION`? Say
it before you flip `SPREAD`.

---

## 1:00 — Find the fault

```bash
cd ../faults
```

Four programs. **Every one of them runs without an error message, and every one is
wrong.** The spec is in the docstring at the top of each file.

| File | Spec |
|---|---|
| `01_average.py` | The mean of six readings. |
| `02_grid.py` | A 3 × 5 grid of zeros with exactly one `1` in it. |
| `03_ramp.py` | Ten opacity steps, `0.0` to `0.9`. |
| `04_nake.py` | Nake's raster — but half the picture is a wall. |

For each: run it, say what is wrong with the output, find the line, fix it, run it
again. Write the line number and the one-line fix in your notes. Three of the four
are things that will surprise you from the lecture; the fourth is one character.

---

## 1:25 — Does it meet the spec?

```bash
cd ../spec
```

`BRIEF.md` is a brief with five numbered rules. `candidate_a.py`, `candidate_b.py`
and `candidate_c.py` are three attempts at it. All three run. All three print a
plausible table. **Exactly one meets the brief.**

You are the one signing it off. Say which candidate passes, and for each of the
other two: which rule it breaks, which line, and the fix. `git diff --no-index a b`
will show you the differences faster than your eyes will.

One of the failures cannot be seen in the table. Read rule 4 again.

---

## 1:45 — Commit and push

Your answers go in **your own repository** — the one from week 1, or a new public one
called `sd5913-notes`. One markdown file, `week02-answers.md`, with:

- your predictions for the three readings, and whether you were right;
- the fault, line and fix for each of the four programs;
- the verdict on the three candidates, with the rule numbers;
- the PNGs you saved, in an `images/` folder, linked from the markdown.

```bash
git add week02-answers.md images/
git commit -m "Week 2: predictions, faults, verdicts"
git push
```

Then run the assignment 1 checker inside your **assignment** repo, because Sunday
is the deadline and this is the moment you have the terminal open:

```bash
cd ../your-assignment-repo
uv run https://raw.githubusercontent.com/sd5913/pfad/2026/assignments/check.py
```

Screenshot the green tick and upload it to the ClassPoint question on the last
slide. That is the attendance signal.

---

## When it goes wrong

**`uv: command not found`** — the installer did not run, or the terminal predates
it. New terminal first; then the setup link above.

**A window opens and closes at once** — read the terminal. The traceback names the
line. That is not a failure of the tutorial, that is the tutorial.

**`pygame` says it cannot open a display** — you are on a machine with no screen
(a remote server, or a lab image that boots headless). Every script here has
`--save out.png`, which draws one frame to a file without a window.

**The tides window is blank** — `tides.csv` is missing or empty. `git status` will
tell you if you deleted it; `git checkout tides.csv` brings it back.
