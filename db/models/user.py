from pydantic import BaseModel, Field
from datetime import datetime

class Users(BaseModel):
  username: str
  password: str
  email: str
  phone: str
  first_name: str
  last_name: str
  is_verified: bool = False
  date_of_birth: str = None
  created_at: str = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"), alias="createdAt")

  def __get_collection_name__():
    return "users"

