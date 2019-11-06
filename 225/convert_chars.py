PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    return "".join(c.swapcase() if c.lower() in PYBITES else c
                   for c in text)
