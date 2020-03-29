from words import sort_words_case_insensitively


def test_sort_words_case_insensitively():
    words = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()
    actual = sort_words_case_insensitively(words)
    expected = ['a', 'a', 'almost', 'and', 'and', 'Christmas',
                'Happy', 'Holidays', "It's", 'Merry', 'PyBites',
                'wishes', 'You', '2019']
    assert actual == expected


def test_sort_words_case_insensitively_another_phrase():
    words = ("Andrew Carnegie's 64-room chateau at 2 East 91st "
             "Street was converted into the Cooper-Hewitt National "
             "Design Museum of the Smithsonian Institution "
             "in the 1970's").split()
    actual = sort_words_case_insensitively(words)
    expected = ['Andrew', 'at', "Carnegie's", 'chateau', 'converted',
                'Cooper-Hewitt', 'Design', 'East', 'in', 'Institution',
                'into', 'Museum', 'National', 'of', 'Smithsonian',
                'Street', 'the', 'the', 'the', 'was', "1970's", '2',
                '64-room', '91st']
    assert actual == expected


def test_digit_inside_word_does_not_matter():
    """We only care about the first char being a number"""
    words = ("It was the twenty9th of October when it was questioned"
             "the meaning of nuMbers and weather hiding a number Inside"
             "tex56t should be treated as a word or another number").split()
    actual = sort_words_case_insensitively(words)
    expected = ['a', 'a', 'and', 'another', 'as', 'be', 'hiding',
                'Insidetex56t', 'It', 'it', 'meaning', 'number', 'number',
                'nuMbers', 'October', 'of', 'of', 'or', 'questionedthe',
                'should', 'the', 'treated', 'twenty9th', 'was',
                'was', 'weather', 'when', 'word']
    assert actual == expected


def test_words_with_mixed_chars_and_digits():
    words = ("Let's see how4 this 1sorts, hope it works 4 this "
             "B1te 22 55abc abc55").split()
    actual = sort_words_case_insensitively(words)
    expected = ['abc55', 'B1te', 'hope', 'how4', 'it', "Let's", 'see',
                'this', 'this', 'works', '1sorts,', '22', '4', '55abc']
    assert actual == expected