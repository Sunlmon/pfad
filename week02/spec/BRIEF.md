# Brief — the fall of a grid

You are the person who has to sign this off, not the person who wrote it.

## What was asked for

A program that lays out a **Schotter** grid — `COLS` × `ROWS` squares, ordered at the
top, coming apart towards the bottom — and, for each row, prints

```
row   damage   max move
```

where **damage** is how disordered that row is, and **max move** is the largest
distance (in pixels, in x or in y) that any square in that row is pushed off its slot.
It also writes an SVG of the grid so you can look at it.

## The rules it has to meet

Constants, fixed for all three: `COLS = 12`, `ROWS = 22`, `SEED = 5913`,
`CHAOS = 1.0`, `SQUARE = 30`.

1. **The first row is untouched.** Row 0 has damage `0.00`.
2. **The last row is fully damaged.** Row `ROWS - 1` has damage exactly `CHAOS`.
3. **Damage grows with the square of the depth.** It is
   `CHAOS × (fraction of the way down)²`, where the fraction is `0` at the first row
   and `1` at the last. Not a straight line — the top has to stay calm.
4. **It is reproducible.** Run it twice, get the same numbers and the same picture.
   Forever, on any machine.
5. **Nothing wanders more than half a square.** No square is moved by more than
   `SQUARE / 2` — that is 15.0 pixels — in x or in y.

## Your job

Three people handed in `candidate_a.py`, `candidate_b.py`, `candidate_c.py`.
All three run. All three print a table. All three produce a picture that looks
plausible on a first glance.

**Exactly one meets the brief.**

Say which, and for each of the other two: **which numbered rule it breaks, which
line breaks it, and the one-line fix.** One of the two cannot be caught by reading
the table once — you have to think about what "reproducible" means and do something
about it.

Reading three near-identical files is much easier if you let a machine do the
comparison:

```bash
git diff --no-index candidate_a.py candidate_b.py
git diff --no-index candidate_b.py candidate_c.py
```

That is the same view GitHub shows you on a commit, pointed at two files instead
of two versions.
