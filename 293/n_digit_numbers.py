from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    if n < 1:
        raise ValueError("'n' should be >= 1")

    factor = int('1' + '0' * (n - 1))

    return [int(str(number * factor)[:n + (1 if number < 0 else 0)])
            for number in numbers]
