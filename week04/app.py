# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas", "requests", "streamlit"]
# ///

"""A Streamlit client for the FastAPI Worker example.

    uv run --with streamlit --with pandas --with requests streamlit run week04/app.py
"""

import calendar

import pandas as pd
import requests
import streamlit as st

from transform import select_day

API = (
    "https://sd5913-week04-tides.venetanji.workers.dev"
    "/tides"
)

st.title("Quarry Bay, one day at a time")
month = st.selectbox("Month", range(1, 13), format_func=lambda n: calendar.month_name[n])

try:
    response = requests.get(API, params={"month": month}, timeout=10)
    response.raise_for_status()
except requests.RequestException as exc:
    st.error("The tide API is not responding. Try again in a moment.")
    st.stop()

rows = response.json()
if not rows:
    st.info("There are no rows for that month.")
    st.stop()

day = st.selectbox("Day", [row["day"] for row in rows])
record = select_day(rows, day)
chart = pd.DataFrame({"Height (m)": record["heights"]}, index=range(1, 25))
chart.index.name = "Hour"
st.line_chart(chart)
st.caption(f"Hong Kong Observatory · Quarry Bay · 2026-{month:02}-{day:02}")
