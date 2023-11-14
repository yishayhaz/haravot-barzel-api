from pydantic import BaseModel, Field
from datetime import datetime

class Users(BaseModel):
  created_at: datetime = Field(default_factory=datetime.utcnow) 
  username: str
  password: str
  email: str
  phone: str
  first_name: str
  last_name: str
  is_verified: bool = False
  date_of_birth: str = None

  def __get_collection_name__():
    return "users"

