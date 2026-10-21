# Week 8 — one piece that works (Thu 29 Oct 2026)

Bring your Week 7 idea and mock-up. Today you will turn one interaction into a
small, testable next step, give a teammate a way to review it, and explain how
someone else could repeat a run. These are team working notes, **not another
assessed submission**. Check with your instructor how your group agrees its
project scope under the existing Week 8 course plan.

## Try a tiny class first

The [Tile example](tile_demo.py) is a **text-only model**, not a clickable
interface or audio player. A class describes a kind of object; `blue` and `red`
are two separate objects made from it. Each starts unselected. Calling
`blue.choose()` changes only blue's `selected` value from `False` to `True`.
The program prints their states so you can check that prediction without a
browser, a speaker or extra Python packages.

From the `pfad` repository root, with Python 3 installed, run:

```bash
python -B week08/tile_demo.py
```

On a machine where `python` is not Python 3, use
`python3 -B week08/tile_demo.py` instead (or
`py -3 -B week08/tile_demo.py` on Windows).
Expect these two lines:

```text
Before: blue=False, red=False
After:  blue=True, red=False
```

Predict before running: if you replace `blue.choose()` with `red.choose()`,
what changes in the second line? Try it, then restore the original. A visible
tile on a screen would still need interface code to display this state; a tone
would need separate sound code. Neither is promised by this Python example.
To check the example's state and its printed result, from the same folder run:

```bash
python -B -m unittest discover -s week08 -p "test_*.py"
```

You should see `OK`. `-B` avoids writing Python cache files in this folder.
The tests use only the Python standard library.

## Turn your idea into one test

1. From your Week 7 mock-up, name a person, **one action** they take and **one
   response** they can notice. Example: a visitor taps a blue tile and sees it
   highlighted. A sound is optional; visible feedback also works without
   speakers.
2. Write a sentence another person can test: "When a visitor chooses blue,
   blue becomes selected and red does not." Ask what would count as evidence
   rather than promising a complete installation. The Python example checks
   state only; a real interface needs a person to try its visible response.
3. Put a few tasks in order: respond to a tap, show selection, test with a
   person, then consider other sounds/tiles. Choose a short next goal such as
   "one tile gives visible feedback"; leave the rest in the backlog. Borrow
   goal/backlog/increment vocabulary from Scrum without adopting formal roles.
   An **increment** is a usable change, not just a list of tasks.
4. For the chosen task, note who will try it and what result they expect. If
   nothing runs yet, label the expectation as untested rather than claiming it
   works. Show what works, what remains and the next small test.

## Make the change reviewable

Use your team's working version as the starting point. Work on one small
feature branch; commit a change that has a clear purpose and open a pull
request to the team project. In its description, say what should happen, how
to run it and what you actually checked. A second person reads the change and
tries the interaction before the team combines it. If both people edit the
same line, resolve the conflict together; even a conflict-free merge needs a
test of the combined project. A pull request is a request for review, not
proof that a change works. See the [Git reference](../reference/git.md) for
branches and the everyday commands.

## Can another person repeat your result?

Swap run instructions with a teammate. Point to the entry command and working
folder, needed code and packages, and a safe sample input. For this demo the
entry command is `python -B week08/tile_demo.py`, there are no third-party
packages, and the two colour names are built into the file. What would a
new person see? What might fail on another machine? Improve one instruction
in your own project's README, then ask the teammate to try it. Do not share
credentials or private data to make a run work.

**Optional paper trace, no container install required:** An image is a
template; a container is an instance with a writable layer. Imagine a program
writes `choice.txt` inside that layer. Predict what happens when you (a) stop
and restart the *same* container and (b) remove it and create a new one from
the image. In (a) the file remains; in (b) the unmounted file is lost. If the
file instead lives in a bind-mounted host folder or named volume, it can
survive removal **when the new container reconnects the same mount**. A named
volume does not need a running container to exist, but deleting that volume
explicitly destroys its data. This is a conceptual trace, not measured output
or an instruction to install Docker/Compose. Keep secrets and personal folders
out of mounts.

Camera/gesture input and AI agent tools are optional connections, not required
project stacks. A coordinate sequence can replace a camera; capture is opt-in,
with no recording or upload by default. A tool suggestion does not grant an
agent permission to use the tool.

## Sources

- Historical “SD5913 - PFAD - Week 8.pdf”: pp19–23 Scrum/team workflow;
  pp24–29 branches; pp30–43 containers/persistence; pp44–49 vision;
  pp51–61 tutorial (PDF page order). These are background, not 2026 deadlines,
  team arrangements or mandatory software instructions.
- Current foundation: [Git reference](../reference/git.md) and the earlier
  weekly run guides. Historical code: [2025 Week 8](https://github.com/sd5913/pfad/tree/2025/week08).
- This 2026 activity and the two-object example adapt the Week 8 teaching
  sequence; they are not verbatim archival tasks.

## Verification scope

Independent verification (21 October 2026): the two standard-library tests passed on Linux x86_64 with Python 3.12.14. The Docker section is a conceptual paper trace, not a claimed container run.

The PR workflow checks every available Week 8–12 companion on an Ubuntu 24.04 runner, including the real local MCP smoke when Week 12 is present. It does not deploy or publish the course.
