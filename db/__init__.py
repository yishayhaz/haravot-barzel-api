from pymongo import MongoClient
from helpers.env import EnvVars
from .models import (
  Users
)

mongo_client = MongoClient(EnvVars.DB_CONNECTION_STRING)
db = mongo_client[EnvVars.DB_NAME]

USER_COLLECTION = db[Users.__get_collection_name__()]

def create_indexes():
  print("Creating indexes 🕯️🕺")

  USER_COLLECTION.create_index("email", unique=True)