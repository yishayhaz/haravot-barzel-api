from helpers.env import EnvVars
import jwt

class Tokens():
    @staticmethod
    def encode(user_id: str):
        return jwt.encode(
        { "user_id": user_id },
        EnvVars.TOKEN_SECRET,
        algorithm="HS256",
      )

    @staticmethod
    def decode(token: str):
        try:
            return jwt.decode(token, EnvVars.TOKEN_SECRET, algorithms=["HS256"])
        except:
            return None