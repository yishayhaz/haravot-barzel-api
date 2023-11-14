from pydantic import BaseModel, Field, validator
from db.models.profile import ProfileSocial
from typing import Optional

class CreateProfilePayload(BaseModel):
  username: str = Field(...)
  first_name: str = Field(...)
  last_name: str = Field(...)


class UpdateProfilePayload(BaseModel):
  username: Optional[str] = Field(None)
  first_name: Optional[str] = Field(None)
  last_name: Optional[str] = Field(None)
  date_of_birth: Optional[str] = Field(None)
  date_of_death: Optional[str] = Field(None)
  bio: Optional[str] = Field(None)
  image: Optional[str] = Field(None)