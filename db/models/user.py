from pydantic import BaseModel, Field

class Users(BaseModel):
  username: str
  password: str
  email: str
  phone: str
  first_name: str
  last_name: str

  def __get_collection_name__():
    return "users"

