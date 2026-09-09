"""
Candidate B for the brief in BRIEF.md.

    uv run candidate_b.py

Prints one row per row of the grid and writes candidate_b.svg.
Nothing to install — this uses only what ships with Python.
"""

import random

COLS, ROWS = 12, 22
SEED = 5913
CHAOS = 1.0
SQUARE = 30
MARGIN = 45
STROKE = "#111111"
BACKGROUND = "#faf8f4"


def damage(row):
    """How disordered row `row` is."""
    return CHAOS * (row / (ROWS - 1)) ** 2


def place(rng, row):
    """One square: how far it turns, and how far it slides, in x and in y."""
    hurt = damage(row)
    angle = rng.uniform(-1, 1) * hurt * 45
    dx = rng.uniform(-1, 1) * hurt * SQUARE * 0.5
    dy = rng.uniform(-1, 1) * hurt * SQUARE * 0.5
    return angle, dx, dy


def square(x, y, angle, dx, dy):
    cx, cy = x + SQUARE / 2, y + SQUARE / 2
    return (f'  <rect x="{x:.2f}" y="{y:.2f}" width="{SQUARE}" height="{SQUARE}" '
            f'transform="translate({dx:.2f} {dy:.2f}) '
            f'rotate({angle:.2f} {cx:.2f} {cy:.2f})" />')


def main():
    rng = random.Random(SEED)
    parts = []

    print("row   damage   max move")
    for row in range(ROWS):
        moved = 0.0
        for col in range(COLS):
            angle, dx, dy = place(rng, row)
            moved = max(moved, abs(dx), abs(dy))
            parts.append(square(MARGIN + col * SQUARE, MARGIN + row * SQUARE,
                                angle, dx, dy))
        print(f"{row:3d}   {damage(row):6.3f}   {moved:8.2f}")

    width = COLS * SQUARE + MARGIN * 2
    height = ROWS * SQUARE + MARGIN * 2
    svg = "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">',
        f'  <rect width="100%" height="100%" fill="{BACKGROUND}" />',
        f'  <g fill="none" stroke="{STROKE}" stroke-width="1.4">',
        *parts,
        "  </g>",
        "</svg>",
    ])

    with open("candidate_b.svg", "w", encoding="utf-8") as handle:
        handle.write(svg)
    print("wrote candidate_b.svg")


if __name__ == "__main__":
    main()
