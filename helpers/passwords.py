import secrets, string
from argon2 import PasswordHasher
from argon2.exceptions import Argon2Error

ph = PasswordHasher()


def generate_password(length: int = 16) -> str:
  alphabet = string.ascii_letters + string.digits

  return "".join(secrets.choice(alphabet) for _ in range(length))


def hash_password(password: str) -> str:
  return ph.hash(password)


# compare a given password with a hashed password
def verify_password(hashed_password: str, password: str) -> bool:
  try:
    ph.verify(hashed_password, password)
    return True
  except Argon2Error:
    return False
