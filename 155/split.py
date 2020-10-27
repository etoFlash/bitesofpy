from shlex import split


def split_words_and_quoted_text(text: str):
    """Split string text by space unless it is
       wrapped inside double quotes, returning a list
       of the elements.

       For example
       if text =
       'Should give "3 elements only"'

       the resulting list would be:
       ['Should', 'give', '3 elements only']
    """
    return split(text)
