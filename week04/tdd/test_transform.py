from transform import select_month


def test_select_month_keeps_only_matching_rows():
    rows = [
        {"month": 9, "day": 17},
        {"month": 10, "day": 1},
    ]

    assert select_month(rows, 9) == [rows[0]]
