# Week 04 — Interfaces, APIs, and tests

Two hours. Put a surface on last week's data, then make a promise the computer
can check.

This folder is the long version of the week 4 lecture. It reuses the committed
Hong Kong Observatory tide file from [`week03/data/`](../week03/data/), so the
examples and tests do not need the internet. The API is a small FastAPI server;
the page is a Streamlit client that asks it for one month and one day.

```bash
cd pfad          # your clone
git pull
```

## 0:00 — Say what the interface should do

The control is the input, the selected month and day are state, and the chart is
the response. The sentence for this example is:

> When I choose a day, the page shows that day's 24 hourly tide heights.

Read [`app.py`](app.py) and [`api.py`](api.py). The Streamlit page does not read
the raw file. It asks `GET /tides?month=9` and draws the JSON response. This keeps
the person-facing surface on the client and the data route on the server.

## 0:15 — Run the tests

From the repository root, run the completed tests:

```bash
uv run --with pytest python -m pytest week04/tests
```

The tests use a tiny in-memory fixture. They check the rule without fetching the
live API, so the same input produces the same answer every time.

Try the test-first sequence in [`tdd/`](tdd/):

1. Run `uv run --with pytest python -m pytest week04/tdd/test_transform.py`. It should fail:
   `select_month` is still a stub.
2. Read the assertion. It says that selecting September returns the September row
   and leaves October out.
3. Implement `select_month` with the smallest rule that makes the test pass.
4. Add an empty-month test, run again, then refactor only while the tests stay green.

That is red → green → refactor. A passing test is evidence that this example
matches its test; check that the test itself matches the intended behavior.

## 0:30 — Read the cached data

[`transform.py`](transform.py) turns the Observatory's list of rows into records
with numeric heights, then selects a month. The raw file is still the source of
truth. The API reads it; neither the API nor the tests silently fetch a new copy.

## 0:45 — Start the API

In a terminal at the repository root:

```bash
uv run --with fastapi --with uvicorn uvicorn week04.api:app --reload
```

Open <http://127.0.0.1:8000/docs>. FastAPI made the interactive page from the
endpoint definition. Try `GET /tides`, enter month `9`, and inspect one returned
record. Each record has a month, a day, and 24 heights in metres.

## 1:05 — Start the interface

In a second terminal, also at the repository root:

```bash
uv run --with streamlit --with pandas --with requests streamlit run week04/app.py
```

Choose a month, then a day. Streamlit reruns the script when a widget changes;
the script asks the API again and redraws the chart. Stop both programs with
`Ctrl+C` when you are done.

## 1:25 — Let GitHub run the checks

[`../.github/workflows/week04-tests.yml`](../.github/workflows/week04-tests.yml)
runs the completed fixture tests on every push and pull request to `2026`. Read it
top to bottom: the event starts a job, the job checks out the repo, installs
`uv`, then runs the tests. The workflow uses read-only repository permission.

[`../.github/workflows/refresh-tides.yml`](../.github/workflows/refresh-tides.yml)
is manual. In the course repo it refreshes the Week 3 HKO example file; maintainers
can run it here. Read it as a model for your assignment repo: adapt the fetch script
and file path, then trigger your own workflow. It validates the file, runs tests,
and commits the replacement only if all checks pass. It needs `contents: write`
because it pushes refreshed data. The old copy stays in Git history. Start with a
manual refresh; add a schedule only when the source should keep changing.

The refresher writes a temporary file first. If the request fails or the file
does not have 365 rows with 26 fields, it leaves the committed data untouched.
The tests stay offline; the refresh job has one separate check for the returned
file's shape.

## Try next

- Change the query to return one day, or add an endpoint for the month's high
  and low water.
- Add one test before implementing the new behavior.
- Change the Streamlit control and say what state the app must remember.
- Ask a partner to use the page without explaining it. What did they expect?

The 2025 version spent this week on `input()`, pygame polling, local language
models, and screenshots of PATH setup. The interaction sequence survives here;
the runnable examples now connect it to an API, a browser surface, fixture tests,
and the data already used in week 3.
