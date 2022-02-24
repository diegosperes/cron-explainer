import pytest

from cron_explainer.parser import parse


def test_parse_star_minute():
    assert parse("*", "minute") == {
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
    }


def test_parse_star_hour():
    assert parse("*", "hour") == {
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
    }


def test_parse_star_day():
    assert parse("*", "day") == {
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
    }


def test_parse_star_month():
    assert parse("*", "month") == {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}


def test_parse_star_day_week():
    assert parse("*", "day_week") == {0, 1, 2, 3, 4, 5, 6}


def test_parse_digit():
    assert parse("1", "minute") == {1}


def test_parse_multiple_expressions():
    assert parse("3-5,2", "hour") == {3, 4, 5, 2}


def test_parse_divisor_of_expression():
    assert parse("5/10", "day") == {10, 20, 30}


def test_parse_divisor_of_expression_with_star():
    assert parse("*/2", "day_week") == {0, 2, 4, 6}


def test_parse_divisor_of_expression_with_range_expression():
    assert parse("3-7/2", "month") == {4, 6}


def test_parse_monday_day_week_expression():
    assert parse("mon", "day_week") == {1}


def test_parse_tuesday_day_week_expression():
    assert parse("tue", "day_week") == {2}


def test_parse_wednesday_day_week_expression():
    assert parse("wed", "day_week") == {3}


def test_parse_thurday_day_week_expression():
    assert parse("thu", "day_week") == {4}


def test_parse_friday_day_week_expression():
    assert parse("fri", "day_week") == {5}


def test_parse_saturday_day_week_expression():
    assert parse("sat", "day_week") == {6}


def test_parse_sunday_day_week_expression():
    assert parse("sun", "day_week") == {0}


def test_parse_wrong_day_week_expression():
    with pytest.raises(ValueError) as excinfo:
        parse("suk", "day_week")
    assert (
        str(excinfo.value) == "Cron expression (suk) does not match with an criteria."
    )


def test_parse_wrong_range_expression():
    with pytest.raises(ValueError) as excinfo:
        parse("5-a", "month")
    assert str(excinfo.value) == "Invalid literal (a) for month."


def test_parse_wrong_integer_expression():
    with pytest.raises(ValueError) as excinfo:
        parse("z", "day")
    assert str(excinfo.value) == "Cron expression (z) does not match with an criteria."


def test_parse_wrong_divisor_of_expression():
    with pytest.raises(ValueError) as excinfo:
        parse("z/2", "day")
    assert str(excinfo.value) == "Invalid literal (z) for day."


def test_parse_wrong_divisor_of_expression_with_range():
    with pytest.raises(ValueError) as excinfo:
        parse("z-1/2", "day")
    assert str(excinfo.value) == "Invalid literal (z) for day."
