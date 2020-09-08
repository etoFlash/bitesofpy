from string import ascii_uppercase, digits


BASE_CHARS = digits + ascii_uppercase


def convert(number: int, base: int = 2) -> str:
    """Converts an integer into any base between 2 and 36 inclusive

    Args:
        number (int): Integer to convert
        base (int, optional): The base to convert the integer to. Defaults to 2.

    Raises:
        Exception (ValueError): If base is less than 2 or greater than 36

    Returns:
        str: The returned value as a string
    """
    if not 2 <= base <= 36:
        raise ValueError("Base should be between 2 and 36")

    result = []

    while number > 0:
        result.insert(0, BASE_CHARS[number % base])
        number = number // base

        if number < base:
            result.insert(0, BASE_CHARS[number])
            number = 0

    return "".join(result)
