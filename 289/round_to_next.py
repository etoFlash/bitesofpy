from math import ceil


def round_to_next(number: int, multiple: int):
    if number == 0:
        return 0
    return ceil(number / multiple) * multiple
