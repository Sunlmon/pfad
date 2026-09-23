# Week 04 — One control, one clear response

Two hours. Put a surface on last week's tide data, trace one action through the
program, then protect its rule with a test.

The promise for the whole session is:

> When I choose a day, the chart shows that day's 24 hourly tide heights.

The example reuses the committed Hong Kong Observatory file in
[`week03/data/`](../week03/data/). A copy is bundled with a Python Worker, so
class does not depend on the Observatory being online.

```bash
cd pfad
git pull
```

## 0:00 — Run the complete interaction

Start the interface from the repository root:

```bash
uv run --with streamlit --with pandas --with requests streamlit run week04/app.py
```

Choose September, then change the day. The chart should always contain 24
heights. The Streamlit script asks the deployed Python Worker at
<https://sd5913-week04-tides.venetanji.workers.dev> for its data.

The interaction has three parts:

| Part | In this app |
|---|---|
| Input | The month and day selectors |
| State | The currently selected month and day |
| Response | The chart and its date caption |

## 0:30 — Trace one choice

Read [`app.py`](app.py) from the first `selectbox` to `st.line_chart`:

1. The month selector supplies a number.
2. `requests.get` asks `GET /tides?month=9` for that month's rows.
3. The day selector supplies a day found in the response.
4. `select_day(rows, day)` returns one record.
5. The chart draws that record's 24 heights.

Open <https://sd5913-week04-tides.venetanji.workers.dev/docs>. FastAPI builds this page from
[`api.py`](api.py). Try `GET /tides` with month `9` and inspect one returned
record. The Streamlit page is the person-facing client; the FastAPI Worker is
the service it asks for data.

The Worker runs Python through Pyodide on Cloudflare. Its `Default` entrypoint
adapts the same FastAPI app to an incoming Worker request:

```python
from workers import asgi

Default = asgi.entrypoint(app)
```

The Worker reads its bundled snapshot. It does not fetch from the Observatory
while someone is using the app. [`transform.py`](transform.py) holds the small
data rules that the service, the app and the tests share.

To run the Worker locally, install Node.js and use:

```bash
uv run pywrangler dev
```

[`../wrangler.jsonc`](../wrangler.jsonc) names the Worker, selects Python 3.13,
includes the JSON snapshot, and enables observability. A maintainer deploys the
same bundle with `uv run pywrangler deploy`. Cloudflare documents the runtime
in [Python Workers](https://developers.cloudflare.com/workers/languages/python/)
and its [FastAPI adapter](https://developers.cloudflare.com/workers/languages/python/packages/fastapi/).

## 1:00 — Test the promise first

The completed tests use tiny fixtures rather than the full file or a live
network request:

```bash
uv run --with pytest python -m pytest week04/tests
```

Now work through the deliberately unfinished version in [`tdd/`](tdd/):

```bash
uv run --with pytest python -m pytest week04/tdd/test_transform.py
```

It should fail because `select_day` is still a stub. Read the assertion as a
sentence: when the rows contain days 17 and 18, choosing 17 returns the first
record.

Implement the smallest rule that passes:

```python
def select_day(rows, day):
    return next((row for row in rows if row["day"] == day), None)
```

Run the same test again. Add a second test for a missing day, then improve the
code only while both tests stay green. That is the red, green, refactor cycle.

## 1:30 — Change one visible behavior

Choose one small change:

- Show the day's highest and lowest heights beneath the chart.
- Make the hour labels start at `01:00` rather than `1`.
- Add a test before adding an endpoint that returns one day.

Write the interaction before changing the code:

> When I ___, the interface ___.

Ask a partner to use the result without explaining it. Show them the test that
checks its data rule. Before closing, stop Streamlit with `Ctrl+C`.

## What GitHub checks

[`../.github/workflows/week04-tests.yml`](../.github/workflows/week04-tests.yml)
runs the completed fixture tests on pushes and pull requests to `2026`. Read it
after the local test makes sense: the workflow repeats the same command on a
GitHub machine and shows the result beside the commit.

## Optional: refresh the snapshot

[`../.github/workflows/refresh-tides.yml`](../.github/workflows/refresh-tides.yml)
is a maintainer example, not a required workshop step. It runs manually, fetches
the 2026 file, checks that every date and hourly value is present, updates both
committed copies, runs the offline tests, and commits the replacement only if
every check passes. The old snapshot remains in Git history.

Start with a manual refresh in your own project. Add a schedule only when the
source should keep changing and you understand what a failed fetch should do.
