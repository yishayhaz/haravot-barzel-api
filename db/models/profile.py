from pydantic import BaseModel, Field
from datetime import datetime
from .common import ApiFile
from enum import Enum
from helpers.types.fields import ObjectIdField

class ProfileSocialPlatform(str, Enum):
  INSTAGRAM = "instagram"
  FACEBOOK = "facebook"
  TWITTER = "twitter"
  LINKEDIN = "linkedin"
  YOUTUBE = "youtube"
  TIKTOK = "tiktok"
  SNAPCHAT = "snapchat"
  PINTEREST = "pinterest"
  REDDIT = "reddit"
  TELEGRAM = "telegram"
  

class ProfileSocial(BaseModel):
  url: str
  platform: ProfileSocialPlatform

class Profiles(BaseModel):
  created_at: datetime = Field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S"), alias="createdAt")
  username: str
  first_name: str
  last_name: str
  bio: str = None
  date_of_birth: str = None
  date_of_death: str = None

  image: ApiFile = None
  socials: list[ProfileSocial] = []

  manager: ObjectIdField

  def __get_collection_name__():
    return "profiles"

  