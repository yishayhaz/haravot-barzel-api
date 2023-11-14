from . import models
import db

def create_profile(data: models.CreateProfilePayload):
  profile = db.Profiles(
    username=data.username,
    first_name=data.first_name,
    last_name=data.last_name
  ).model_dump()

  db.PROFILE_COLLECTION.insert_one(profile)