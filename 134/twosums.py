def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    result_list = []
    for i, v in enumerate(numbers):
        try:
            second_idx = numbers.index(target - v, i + 1)
            if v < numbers[second_idx]:
                result_list.append((i, second_idx))
        except ValueError:
            pass

    if not result_list:
        return None
    else:
        return min(result_list, key=lambda x: numbers[x[0]])
