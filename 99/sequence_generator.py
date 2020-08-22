from itertools import cycle
from string import ascii_uppercase


def sequence_generator():
    nums = cycle(range(1, 27))
    chars = cycle(ascii_uppercase)

    while True:
        yield next(nums)
        yield next(chars)
