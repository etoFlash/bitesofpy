import re


def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    result = {}
    for s in passwd.splitlines()[1:]:
        user = s.split(":")[0]
        name = re.sub(r",+", r" ", s.split(":")[4]).strip()
        result[user] = name or "unknown"

    return result
