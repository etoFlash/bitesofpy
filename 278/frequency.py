from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    mc = Counter(numbers).most_common()

    return mc[0][0], mc[-1][0]
