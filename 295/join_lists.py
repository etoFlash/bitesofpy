from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:
    if not lst_of_lst:
        return None

    result = []

    for lst in lst_of_lst:
        if result:
            result.append(sep)

        result.extend(lst)

    return result
