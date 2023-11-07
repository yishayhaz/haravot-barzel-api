from . import models
import db

def create_user(
  data: models.SignupPayload
):
  user = db.Users(
    username=data.username,
    password=data.password,
    email=data.email,
    phone=data.phone,
    first_name=data.first_name,
    last_name=data.last_name
  )

  return db.USER_COLLECTION.insert_one(
    user.model_dump()
  )
  