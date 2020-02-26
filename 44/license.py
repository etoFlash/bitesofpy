from string import ascii_uppercase, digits
import random

chars = ascii_uppercase + digits


def gen_key(parts=4, chars_per_part=8):
    return "-".join(
        "".join(random.choices(chars, k=chars_per_part))
        for _ in range(parts)
    )
