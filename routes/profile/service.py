import db

def get_profile_by_username(
  username: str
):
  return db.PROFILE_COLLECTION.find_one({
    "username": username
  })