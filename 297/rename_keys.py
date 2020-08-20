from typing import List, Dict, Any


def _rename_str_key(key: Any) -> Any:
    if isinstance(key, str):
        return key.lstrip("@")
    return key


def _rename_values(value: Any) -> Any:
    if isinstance(value, Dict):
        return rename_keys(value)
    elif isinstance(value, List):
        return [
            rename_keys(v) for v in value
        ]
    return value


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    return {
        _rename_str_key(k): _rename_values(v)
        for k, v in data.items()
    }
