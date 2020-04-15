import re

IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    result = []
    for name in names:
        if name.startswith(IGNORE_CHAR) or re.match(r".*\d+.*", name):
            continue
        if QUIT_CHAR in name or len(result) >= MAX_NAMES:
            break
        result.append(name)
    
    return result
