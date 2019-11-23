def positive_divide(numerator, denominator):
    if denominator == 0:
        return 0

    if not (isinstance(numerator, (int, float)) and
            isinstance(denominator, (int, float))):
        raise TypeError

    result = numerator / denominator

    if result < 0:
        raise ValueError

    return result
