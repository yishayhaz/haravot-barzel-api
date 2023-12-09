from . import models
import db
from bson import ObjectId

def create_profile(data: models.CreateProfilePayload):
  profile = db.Profiles(
    username=data.username,
    first_name=data.first_name,
    last_name=data.last_name
  ).model_dump()

  db.PROFILE_COLLECTION.insert_one(profile)

def update_profile(data: models.UpdateProfilePayload, profile_id: str):
  data = {k: v for k, v in data.model_dump().items() if v is not None}

  db.PROFILE_COLLECTION.update_one(
    {"_id": ObjectId(profile_id)},
    {"$set": data}
  )