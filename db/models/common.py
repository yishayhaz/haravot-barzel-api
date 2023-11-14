from pydantic import BaseModel, Field
from datetime import datetime

class ApiFile(BaseModel):
  created_at: datetime = Field(default_factory=datetime.utcnow) 
  name: str
  meme_type: str
  url: str