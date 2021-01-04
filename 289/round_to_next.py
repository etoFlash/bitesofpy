from math import ceil


def round_to_next(number: int, multiple: int):
    return ceil(number / multiple) * multiple
