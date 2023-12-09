from fastapi import Path
from helpers import responses
from . import service

def get_profile(profile_username: str = Path(...)):
  try:
    profile = service.get_profile_by_username(profile_username)

    if profile:
      return responses.ApiSuccess(data=profile)

  except:
    pass

  return responses.ApiError(message="Profile not found", code=404)