from fastapi import Request, Response
from . import models, service
from helpers import responses

def login(req: Request, data: models.LoginPayload):
  return {
    "message": "Login"
  }

def signup(req: Request, data: models.SignupPayload):
  try:
    user = service.create_user(data)

    res = responses.ApiSuccess()

    res.set_cookie(
      key="token",
      value=str(user.inserted_id),
      httponly=True
    )

    return res
  except Exception as e:
    return responses.ApiError(
      code=400,
      error_code="SIGNUP_FAILED",
      message=str(e)
    )
