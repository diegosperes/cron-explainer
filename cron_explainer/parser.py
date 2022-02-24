from typing import Set

from cron_explainer.constants import RANGES_BY_EXPRESSION_TYPE, DAY_WEEK


def _cast_to_int(digit: str, _type: str) -> int:
    try:
        return int(digit)

    except ValueError:
        raise ValueError(f"Invalid literal ({digit}) for {_type}.")


def parse_day_week_expression(expression: str, _type: str) -> Set[int]:
    """Parse a single unit from cron expression within the name of day week."""

    result = set()
    value = DAY_WEEK.index(expression)
    minimum_allowed, maximum_allowed = RANGES_BY_EXPRESSION_TYPE[_type]

    if minimum_allowed <= value < maximum_allowed:
        result.add(value)

    return result


def parse_integer_expression(expression: str, _type: str) -> Set[int]:
    """Parse a single integer unit from cron expression."""

    result = set()
    value = _cast_to_int(expression, _type)
    minimum_allowed, maximum_allowed = RANGES_BY_EXPRESSION_TYPE[_type]

    if minimum_allowed <= value < maximum_allowed:
        result.add(value)

    return result


def parse_star_expression(expression: str, _type: str) -> Set[int]:
    """Parse a single star unit from cron expression."""

    minimum_allowed, maximum_allowed = RANGES_BY_EXPRESSION_TYPE[_type]

    return set(range(minimum_allowed, maximum_allowed))


def parse_range_expression(expression: str, _type: str) -> Set[int]:
    """Parse a single unit from cron expression within dash."""

    minimum_allowed, maximum_allowed = RANGES_BY_EXPRESSION_TYPE[_type]
    range_from, range_to = expression.split("-")
    range_from = _cast_to_int(range_from, _type)
    range_to = _cast_to_int(range_to, _type) + 1

    return {
        value
        for value in range(range_from, range_to)
        if minimum_allowed <= value < maximum_allowed
    }


def parse_divisor_of_expression(expression: str, _type: str) -> Set[int]:
    """Parse a single unit from cron expression within slash."""

    minimum_allowed, maximum_allowed = RANGES_BY_EXPRESSION_TYPE[_type]
    _range, divisor = expression.split("/")
    divisor = _cast_to_int(divisor, _type)

    if "-" in _range:
        range_from, range_to = _range.split("-")
        range_from = _cast_to_int(range_from, _type)
        range_to = _cast_to_int(range_to, _type)

    elif "*" == _range:
        range_from = minimum_allowed
        range_to = maximum_allowed

    else:
        range_from = _cast_to_int(_range, _type)
        range_to = maximum_allowed

    return {
        value
        for value in range(range_from, range_to)
        if minimum_allowed <= value < maximum_allowed and value % divisor == 0
    }


def parse_multiple_expresions(expression: str, _type: str) -> Set[int]:
    """Parse a single unit from cron expression within comma."""

    result = set()
    nested_expresions = expression.split(",")

    for nested_expresion in nested_expresions:
        result.update(parse(nested_expresion, _type))

    return result


def parse(expression: str, _type: str) -> Set[int]:
    """Parse a single unit from cron expression."""

    expression = expression.lower()
    has_multiple_expresion = "," in expression

    if expression.isdigit():
        return parse_integer_expression(expression, _type)

    elif expression == "*":
        return parse_star_expression(expression, _type)

    elif has_multiple_expresion:
        return parse_multiple_expresions(expression, _type)

    elif "/" in expression:
        return parse_divisor_of_expression(expression, _type)

    elif "-" in expression:
        return parse_range_expression(expression, _type)

    elif _type == "day_week" and expression in DAY_WEEK:
        return parse_day_week_expression(expression, _type)

    raise ValueError(f"Cron expression ({expression}) does not match with an criteria.")
