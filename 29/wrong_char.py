from string import ascii_letters, digits


def get_index_different_char(chars):
    chars = list(map(str, chars))
    alnum = list(ascii_letters + digits)
    alnum_count = 0
    non_alnum_count = 0

    for c in chars:
        if c in alnum:
            alnum_count += 1
        else:
            non_alnum_count += 1

    for i, c in enumerate(chars):
        if alnum_count < non_alnum_count and c in alnum:
            return i

        if alnum_count > non_alnum_count and c not in alnum:
            return i
