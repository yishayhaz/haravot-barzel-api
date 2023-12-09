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