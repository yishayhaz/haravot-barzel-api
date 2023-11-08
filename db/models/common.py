from pydantic import BaseModel

class ApiFile(BaseModel):
  name: str
  meme_type: str
  url: str