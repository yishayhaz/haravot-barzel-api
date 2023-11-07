from fastapi import Request, Response
from . import models, service

def login(req: Request, data: models.LoginPayload):
  return {
    "message": "Login"
  }

def signup(req: Request, data: models.SignupPayload):
  try:
    user = service.create_user(data)

    res = Response()

    res.set_cookie(
      key="user_id",
      value=str(user.inserted_id),
      httponly=True
    )

    return res
  except Exception as e:
    return {
      "message": str(e)
    }
