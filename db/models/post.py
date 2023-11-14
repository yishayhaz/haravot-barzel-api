from pydantic import BaseModel, Field
from datetime import datetime
from helpers.types.fields import ObjectIdField
from .common import ApiFile
from enum import Enum

class PostContentType(str, Enum):
  IMAGE = "image"
  VIDEO = "video"

class PostContent():
  type: PostContentType
  file: ApiFile

class Posts(BaseModel):

  created_at: datetime = Field(default_factory=datetime.utcnow) 
  created_by: ObjectIdField
  profile: ObjectIdField

  content: list
  text: str = None

  # candels_count: int = 0

  def __get_collection_name__():
    return "posts"