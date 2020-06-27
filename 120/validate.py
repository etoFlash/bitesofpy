from functools import wraps


def int_args(func):
    @wraps(func)
    def wrapped(*args):
        for a in args:
            if not isinstance(a, int):
                raise TypeError("Allowed only int")
            if a < 0:
                raise ValueError("Allowed only int greater than 0")
        return func(*args)
    return wrapped
