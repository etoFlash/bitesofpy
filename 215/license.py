import re


def validate_license(key: str) -> bool:
    """Write a regex that matches a PyBites license key
       (e.g. PB-U8N435EH-PG65PW87-IXPWQG5T-898XSZI4)
    """
    r = re.match(r"^PB(-[0-9A-Z]{8}){4}$", key)

    return bool(r)
