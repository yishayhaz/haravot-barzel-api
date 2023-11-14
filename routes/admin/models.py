from pydantic import BaseModel, Field, validator
from db.models.profile import ProfileSocial

class CreateProfilePayload(BaseModel):
  username: str = Field(...)
  first_name: str = Field(...)
  last_name: str = Field(...)


class UpdateProfilePayload(BaseModel):
  username: str = None
  first_name: str = None
  last_name: str = None
  date_of_birth: str = None
  date_of_death: str = None
  bio: str = None
  image: str = None