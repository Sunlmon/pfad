from transform import select_day


def test_select_day_returns_the_matching_record():
    rows = [
        {"month": 9, "day": 17},
        {"month": 9, "day": 18},
    ]

    assert select_day(rows, 17) == rows[0]
