import string
import re

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if 6 <= len(password) <= 12 and \
      re.search(r"[0-9]", password) and \
      len(re.findall(r"[a-z]", password)) > 1 and \
      re.search(r"[A-Z]", password) and \
      re.search(rf"[{string.punctuation}]", password) and \
      password not in used_passwords:
        used_passwords.add(password)
        return True
    return False
