# Week 7 — from an idea to one interaction

**22 October 2026.** The midterm is 10:00–10:30 HKT. This page is for the
group work after the quiz and the optional tutorial that follows it.
Follow the instructor's quiz instructions; this activity does not change them.

## First, form your team

Use the Canvas group-registration route demonstrated in class. If you do not
have a group, ask for help. Follow the instructor's existing team arrangements;
this page does not set a team size.

Build something you want to use: an ambitious useful app, a creative tool or a
game mashup. AI can help you develop it, but AI does not have to be inside the
finished product. Reinvent an interaction, not somebody else's code or assets.
Use original or licensed material.

## Activity 1: tell us what happens — 20 minutes

Include team formation and registration in this time. Pick one representative
and one team name. Submit **one ClassPoint text response** with:

- Team name.
- Intended user or player.
- What that person does.
- How the program responds.
- What you are reinventing or combining.
- The first interaction you want to test.

Keep it concrete. “The player presses this button, and this changes” gives you
something to discuss and test. A list of technologies does not yet describe an
experience.

## Activity 2: show one moment — 20 minutes

Make **one image mock-up** of a screen or moment of use. Show the action and the
response from Activity 1. Add arrows or short labels if that makes it clearer.

A photograph of a paper sketch is enough. The same representative submits the
image on ClassPoint using the same team name. Do not spend this time making a
logo or setting up a new image-generation account.

These are today's two idea-development submissions. There is no extra
prototype, video, pitch deck or critique submission. Use remaining class time
for feedback and helping people find a group.

## Tutorial: try one small change (optional practice)

After the two group activities, use an example you already know. This is a
proposed practice route, not an additional assessed deliverable or a promise to
finish a group prototype today.

1. Choose the smallest interaction related to your idea. Use
   [Week 4's control and response](../week04/README.md),
   [Week 5's images and frames](../week05/README.md), or
   [Week 6's sound and browser sketches](../week06/README.md).
   Keep its existing setup instructions open.
2. Before editing, write what one input should do. Predict the result.
3. Change one value, mapping or function. Run it. Compare the result with your
   prediction. Keep API calls, paid models and model downloads out of the core
   exercise.
4. Try an edge case: the smallest/largest accepted value, no input, a repeated
   click, or Stop followed by Start. Pick one that makes sense for your example.
5. Swap roles. Have another person explain the input, the response and the line
   responsible for the change. Keep a short note of what worked and what did
   not, for your own next step.

If setup is not ready, trace the existing example together on paper and mark
the change you would test. You can still explain the interaction without
installing a new stack. If working in your own repository, keep changes small
and attributable; do not commit credentials or private recordings.

### Optional extension: give one thing its own state

Try the small, self-contained [two-ball example](ball.py). From the repository
root, run `python week07/ball.py` (or `python3` where that is your Python
command). It needs no installs, internet, API key or graphics framework.
Predict the output before running: red starts at 2 and moves 3 units per
second; blue starts at 10 and moves -1 unit per second. Which ball moves after
`red.update(1)`? What changes after `blue.update(1)`? Try changing one velocity
or calling `red.update(0)`, then compare the printed positions.

The supplied Week 7 PDF, p52, offers a more involved Ball example. This version
keeps explicit position/velocity arguments instead of the archive's `**kwargs`
or Processing-specific vector setup. It models one dimension so you can see
that each object owns its position, while both share the same `update` rule.
Sketch the two objects and trace them on paper if Python is unavailable.

This is optional practice, not an advanced asyncio exercise or an assessed
object-oriented prototype. A diagram and value trace are sufficient today.

### If AI helps with the change

Ask for one small change, then read and test it. A plausible explanation is not
evidence that the code behaves correctly. Compare the ordinary input and the
edge case. Note the tool/model if known, attempts needed, and elapsed time to a
working result. Do not compare output-token speed with total task completion
time, or treat a single attempt as a benchmark.

## Optional current examples — checked 21 October 2026

These are discussion prompts, not required tools. See the
[companion lecture news brief](https://github.com/sd5913/teaching/blob/2fe0d30d4dcdc7c19665be0e10b568220b53f15f/lessons/week07-news-20261021.md)
for the release context. Performance descriptions come from the vendors;
we have not reproduced their benchmarks.

- **19 October 2026:** [OpenAI's MultiLangBench announcement](https://openai.com/index/low-resource-programming-languages/)
  and [evaluation repository](https://github.com/openai/MultiLangBench)
  concern testing programming tasks across languages. Open evaluation code is
  not the same thing as open model weights. For our exercise: what test would
  show that your changed function works?
- **15 October 2026, fast-mode general availability:** [Anthropic's release notes](https://platform.claude.com/docs/en/release-notes/overview)
  and [fast-mode documentation](https://platform.claude.com/docs/en/build-with-claude/fast-mode)
  describe a faster output mode. Generating tokens faster does not measure
  setup, failed attempts or debugging. For our exercise: measure time to a
  working interaction, including retries.
- **19 October 2026:** [MiniMax's M3.1 Flash announcement](https://www.minimax.io/blog/minimax-m31f)
  describes hosted availability and a later weights release. Do not call it
  open-weight before the weights are released. No signup or paid API is needed
  to take part in this tutorial.

## Keep the two projects separate

The group project is 40%: a shared GitHub repository, everyone's commits,
original/licensed material and scope agreed by Week 8. Follow the actual brief;
this page does not add final deliverables or assessment rules.

Individual Assignment 3 is separate: 15%, due **1 November 2026, 23:59 HKT**.
Use its own brief and Canvas submission instructions.

## Instructor review and sources

This README is proposed in a draft PR. The two 20-minute activities follow the
[Week 7 lesson plan](https://github.com/sd5913/teaching/blob/31c675b4085f771da6340878f3a54d7018f1015d/lessons/week07-lesson-plan.md)
in teaching PR #10. The optional tutorial adapts existing 2026 Weeks 4–6;
it is not an activity recovered from last year's slides. The supplied 2025 PDF, “SD5913 - PFAD - Week 7.pdf”, pp15–28 and
41–54, covers agents, state, global variables and creative-code tutorials.
Its old Blackboard, deadline, team-size and preinstalled-software assumptions
are not carried forward. The core class activities still follow the current
2026 plan, not the old assessment logistics.
Before class, check the actual Canvas group route and ClassPoint text/image
activities. Do not reuse last year's response links.
