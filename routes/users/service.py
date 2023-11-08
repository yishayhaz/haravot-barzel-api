from . import models
import db
from helpers import passwords
from datetime import datetime

def login(
  data: models.LoginPayload
):
  user = db.USER_COLLECTION.find_one({
    "username": data.username
  })

  if not user:
    raise Exception("User not found")
  
  if not passwords.verify_password(user["password"], data.password):
    raise Exception("Invalid password")
  
  return user

def create_user(
  data: models.SignupPayload
):
  hashed_password = passwords.hash_password(data.password)

  user = db.Users(
    username=data.username,
    password=hashed_password,
    email=data.email,
    phone=data.phone,
    first_name=data.first_name,
    last_name=data.last_name,
    createdAt=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    date_of_birth=data.date_of_birth
  ).model_dump()

  return db.USER_COLLECTION.insert_one(user)
  