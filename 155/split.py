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
    result = []
    while text:
        if text.startswith('"'):
            _, s, text = text.split('"', 2)
            text = text.lstrip(' ')
        elif not text.count(' '):
            s, text = text, None
        else:
            s, text = text.split(' ', 1)
        result.append(s)

    return result
