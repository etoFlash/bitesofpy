def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    return len(text) - len(text.lstrip(" "))
