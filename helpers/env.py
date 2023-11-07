from pydantic_settings import BaseSettings

class EnvVariabels(BaseSettings):
  DB_CONNECTION_STRING: str = ""
  DB_NAME: str = ""

  class Config:
      env_file = ".env"
      env_file_encoding = "utf-8"


EnvVars = EnvVariabels()