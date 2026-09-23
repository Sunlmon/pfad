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

## 1:00 — Test the API

In a second terminal, start the Worker locally:

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
