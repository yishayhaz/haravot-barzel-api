from . import models, service
from helpers import responses
from fastapi import Path

def create_profile(data: models.CreateProfilePayload):
  try:
    service.create_profile(data)

    return responses.ApiSuccess(message="Profile created successfully")
  except:
    return responses.ApiError(message="Profile creation failed")
  
def update_profile(data: models.UpdateProfilePayload, profile_id: str = Path(...)):
  try:
    service.update_profile(data, profile_id)

    return responses.ApiSuccess(message="Profile updated successfully")
  except:
    return responses.ApiError(message="Profile update failed")
  
def add_profile_social(data: models.AddProfileSocialPayload, profile_id: str = Path(...)):
  try:
    service.add_profile_social(data, profile_id)

    return responses.ApiSuccess(message="Profile social added successfully")
  except Exception as e:
    print(e)
    return responses.ApiError(message="Profile social add failed")

def delete_profile_social(profile_id: str = Path(...), social_platform: str = Path(...)):
  try:
    service.delete_profile_social(profile_id, social_platform)

    return responses.ApiSuccess(message="Profile social deleted successfully")
  except:
    return responses.ApiError(message="Profile social delete failed")