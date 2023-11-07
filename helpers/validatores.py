import string, re

punctuation_regex = r"[" + re.escape(string.punctuation) + r"]"

def valid_password(password: str) -> bool:
    if not isinstance(password, str):
        return False

    if not 10 <= len(password) <= 64:
        return False

    if not re.search(r"[A-Z]", password):
        return False
    elif not re.search(r"[a-z]", password):
        return False
    elif not re.search(r"[0-9]", password):
        return False
    elif not re.search(punctuation_regex, password):
        return False

    return True