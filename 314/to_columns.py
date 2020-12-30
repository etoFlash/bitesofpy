from typing import List  # not needed when we upgrade to 3.9


def print_names_to_columns(names: List[str], cols: int = 2) -> None:
    result = []
    for idx, name in enumerate(names, 1):
        result.append(f'| {name:10}')
        if idx % cols == 0:
            result.append('\n')

    print(''.join(result))
