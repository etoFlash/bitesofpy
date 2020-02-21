import re


def has_timestamp(text):
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    pattern = r"INFO \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2} Shutdown initiated."
    if re.match(pattern, text):
        return True


def is_integer(number):
    """Return True if number is an integer"""
    pattern = r"^-?\d+$"
    if re.match(pattern, str(number)):
        return True


def has_word_with_dashes(text):
    """Returns True if text has one or more words with dashes"""
    pattern = r"\S-\S"
    if re.search(pattern, text):
        return True


def remove_all_parenthesis_words(text):
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""
    pattern = r"\s?\(.*?\)"
    return re.sub(pattern, "", text)


def split_string_on_punctuation(text):
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    split_chars = "?!.,;"
    text = text.strip(split_chars)
    return [s.strip() for s in re.split(r"[{}]".format(split_chars), text)]


def remove_duplicate_spacing(text):
    """Replace multiple spaces by one space"""
    pattern = r"\s{2,}"
    return re.sub(pattern, " ", text)


def has_three_consecutive_vowels(word):
    """Returns True if word has at least 3 consecutive vowels"""
    pattern = r"[aeioyu]{3,}"
    if re.search(pattern, word):
        return True


def convert_emea_date_to_amer_date(date):
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""
    pattern = r"(\d{2})/(\d{2})/(\d{4})"
    return re.sub(pattern, r"\2/\1/\3", date)
