# Week 04 — One control, one clear response

Two hours. Build a chart from local tide data, then compare it with a separate
browser-and-API example. Protect one API rule with a test.

The promise for the whole session is:

> When I choose a day, the chart shows that day's 24 hourly tide heights.

The Streamlit example reads the committed Hong Kong Observatory snapshot in
[`tides-QUB-2026.json`](tides-QUB-2026.json). It loads a local file and creates
the page; it does not make an API request. The separate API example serves the
same snapshot from a Python Worker.

```bash
cd pfad
git pull
```

## 0:00 — Run the complete interaction

Start the interface from the repository root:

```bash
uv run --with streamlit --with pandas streamlit run week04/app.py
```

Choose September, then change the day. The chart should always contain 24
heights. Streamlit reads the bundled JSON file directly, then generates the
page and chart.

The interaction has three parts:

| Part | In this app |
|---|---|
| Input | The month and day selectors |
| State | The currently selected month and day |
| Response | The chart and its date caption |

## 0:30 — Trace one choice

Read [`app.py`](app.py) from the data-file load to `st.line_chart`:

1. Python reads `tides-QUB-2026.json` from the same folder.
2. `parse_rows` turns its records into usable values.
3. The month selector filters those local rows.
4. The day selector and `select_day` choose one day's record.
5. Streamlit draws that record's 24 heights.

This is a single app: the Python code reads a file and Streamlit generates the
HTML page. The FastAPI Worker is a separate example. Open
<https://sd5913-week04-tides.venetanji.workers.dev/docs>, try `GET /tides` with
month `9`, and inspect one returned record.

The browser version keeps the frontend and backend separate. A static HTML and
JavaScript page can be published on GitHub Pages; JavaScript uses `fetch()` to
request JSON from the FastAPI Worker and a chart library such as Recharts
renders the data. The Week 4 slides show this browser request. The Streamlit
example does not call that API.

The Worker runs Python through Pyodide on Cloudflare. Its `Default` entrypoint
adapts the same FastAPI app to an incoming Worker request:

```python
from workers import asgi

Default = asgi.entrypoint(app)
```

The Worker reads its bundled snapshot. It does not fetch from the Observatory
while someone is using the app. [`transform.py`](transform.py) holds the small
data rules shared by the API, the Streamlit app and the tests.

To run the Worker locally, install Node.js and use:

```bash
uv run pywrangler dev
```

[`../wrangler.jsonc`](../wrangler.jsonc) names the Worker, selects Python 3.13,
includes the JSON snapshot, and enables observability. A maintainer deploys the
same bundle with `uv run pywrangler deploy`. Cloudflare documents the runtime
in [Python Workers](https://developers.cloudflare.com/workers/languages/python/)
and its [FastAPI adapter](https://developers.cloudflare.com/workers/languages/python/packages/fastapi/).

## 1:00 — Test the API

For the API example, start the Worker locally in a second terminal:

```bash
uv run pywrangler dev
```

The first test is in one file, [`tdd/test_api.py`](tdd/test_api.py). It asks
for September and checks that the API responds with daily records in the
expected format:

```bash
uv run --with pytest python -m pytest week04/tdd/test_api.py
```

The development loop is just two colors: write the test first and see it fail;
add the `/tides` route; run the same test and see it pass. The test checks for
HTTP 200, the first date, and 24 numeric heights in a record.

## 1:30 — Explain the check

Pair up. Run the test again and explain one assertion to your partner: which
part of the response does it check? Before closing, stop Streamlit with
`Ctrl+C`.

The repository also has extra checks for maintainers. For today, focus on the
single test file and the red-to-green change.
