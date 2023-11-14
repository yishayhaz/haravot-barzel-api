from . import models, service
from helpers import responses

def create_profile(data: models.CreateProfilePayload):
  try:
    service.create_profile(data)

    return responses.ApiSuccess(message="Profile created successfully")
  except:
    return responses.ApiError(message="Profile creation failed")
  
def update_profile(data: models.UpdateProfilePayload):
  print(data)
  return responses.ApiSuccess(data=data)