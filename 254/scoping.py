num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    result = sum(numbers)
    global num_hundreds
    num_hundreds += result // 100

    return result
