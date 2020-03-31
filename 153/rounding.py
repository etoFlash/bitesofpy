from math import ceil, floor


def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) ronud up, else round down.
       Return a new list of rounded values
    """
    return [ceil(n) if up else floor(n)
            for n in transactions]
