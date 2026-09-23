"""A small read-only API over week 3's committed HKO tide data.

    uv run --with fastapi --with uvicorn uvicorn week04.api:app --reload
"""

import json
from pathlib import Path

from fastapi import FastAPI, Query

from week04.transform import parse_rows, select_month

DATA = Path(__file__).resolve().parent.parent / "week03" / "data" / "tides-QUB-2026.json"
app = FastAPI(title="Quarry Bay tides")


def load_rows():
    """Read the committed source file; never fetch from inside a request."""
    raw = json.loads(DATA.read_text(encoding="utf-8"))
    return parse_rows(raw["data"])


@app.get("/tides")
def tides(month: int = Query(ge=1, le=12)):
    """Return one month's daily records as JSON."""
    return select_month(load_rows(), month)
