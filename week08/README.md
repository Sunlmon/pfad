# Week 8 — plan one small piece and work on it together

> **Planning draft for 2026.** Adapted from the supplied 2025 Week 8 slides.
> Confirm lecture alignment and preflight the chosen tools before release.

## Team activity: one small, testable piece

1. Agree the user/player, one action and one response from your Week 7 idea.
2. List the small tasks needed for that interaction. Choose a short, realistic
   goal for the next work period, rather than promising the whole project.
3. Put the tasks in a simple backlog. For each selected task, name a person
   and say how the team will know it works.
4. Choose one task to work on in a feature branch. Have another person read
   the change and its result before combining it with the team's work.
5. At the end, show what works, what remains and the next small step.

This borrows the archive's sprint/backlog/increment language without asking
students to adopt a full professional Scrum process. Agree group scope with the
instructor by Week 8 under the existing course plan. Do not invent a team size,
new deadline or assessment requirement.

## Tutorial: same project, different environment

Use one existing project with known run instructions.

1. Identify its code, dependencies and data.
2. Draw which parts live on the host and which would live in a container.
   Distinguish an image (a template) from a running container.
3. With an instructor-prepared example, change a disposable sample value.
   Predict what survives stopping/restarting the container and what depends on
   a mounted folder or volume.
4. Record the observed result and the command that produced it. Keep the
   example small enough that another person can follow it.

**Working evidence:** a task list and one environment/persistence observation,
kept as team working notes. These are not extra assessed submissions.

## Setup and fallback

The exact Docker/Compose example and commands still need compatibility checks.
Do not install containers or start services from old slides without checking
their purpose and current instructions. Never mount secrets or broad personal
folders. A diagram and prepared output trace are a valid no-install route.

Computer vision was also in the old tutorial, but is an optional extension, not
a second required stack. A pointer or sample coordinate sequence can stand in
for a camera. Capture must be opt-in; no recording/upload by default and no
claims about a person's feelings or attention.

## Sources and release checklist

- Supplied “SD5913 - PFAD - Week 8.pdf”: pp19–23 Scrum and team workflow;
  pp24–29 Git branches; pp30–43 Docker/Compose/persistence; pp44–49 vision;
  pp51–61 tutorial. Page references use PDF page order.
- Current foundation: [Git reference](../reference/git.md) and existing weekly
  run instructions. Historical code: [2025 Week 8](https://github.com/sd5913/pfad/tree/2025/week08).
- The activities are proposed 2026 adaptations, not verbatim archival tasks.
- Pending: aligned lesson, chosen prepared example, tested start/stop and
  persistence behaviour, cross-platform notes and no-install fallback.
