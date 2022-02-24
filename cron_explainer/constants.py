from typing import Tuple


DAY_WEEK = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]


RANGES_BY_EXPRESSION_TYPE: Tuple[int, int] = {
    "minute": (0, 60),
    "hour": (0, 24),
    "day": (1, 32),
    "month": (1, 13),
    "day_week": (0, 7),
}
