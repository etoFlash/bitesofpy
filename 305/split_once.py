from typing import List
from string import whitespace


def split_once(text: str, separators: str = None) -> List[str]:
    result = [text]
    seps = list(separators or whitespace)

    while seps:
        sep = max(seps, key=lambda x: result[0].find(x))
        result[:1] = result[0].split(sep, 1)
        seps.remove(sep)

    return result
