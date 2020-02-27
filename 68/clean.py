def remove_punctuation(input_string):
    """Return a str with punctuation chars stripped out"""
    table = str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    return input_string.translate(table)
