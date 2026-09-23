"""The refresh validator can be checked without contacting the Observatory."""

import json

import pytest

from week04.refresh_data import validate


def payload():
    return {
        "fields": ["MM", "DD", *(f"{hour:02}" for hour in range(1, 25))],
        "data": [["09", "17", *("1.25" for _ in range(24))] for _ in range(365)],
    }


def test_validate_accepts_a_full_year():
    result = validate(json.dumps(payload()).encode())

    assert len(result["data"]) == 365


def test_validate_rejects_a_short_file():
    raw = payload()
    raw["data"].pop()

    with pytest.raises(ValueError, match="expected 365 daily rows"):
        validate(json.dumps(raw).encode())


def test_validate_rejects_a_malformed_row():
    raw = payload()
    raw["data"][0].pop()

    with pytest.raises(ValueError, match="every daily row"):
        validate(json.dumps(raw).encode())
