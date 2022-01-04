from pprint import pformat
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    return pformat(obj, indent=1, width=60, depth=2)
