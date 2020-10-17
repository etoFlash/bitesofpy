def _sort_chars(word):
    chars = list(word.lower().replace(' ', ''))
    return sorted(chars)


def is_anagram(word1, word2):
    """Receives two words and returns True/False (boolean) if word2 is
       an anagram of word1, ignore case and spacing.
       About anagrams: https://en.wikipedia.org/wiki/Anagram"""
    return _sort_chars(word1) == _sort_chars(word2)
