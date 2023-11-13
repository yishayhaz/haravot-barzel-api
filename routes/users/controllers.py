from . import models, service
from helpers import responses, tokens
from fastapi import Request

def getme(req: Request):
  return responses.ApiSuccess(data=req.state.user)
  
def login(data: models.LoginPayload):
  try:
    user = service.login(data)

    token = tokens.Tokens.encode(str(user["_id"]))

    res = responses.ApiSuccess()

    res.set_cookie(
      key="token",
      value=token,
      httponly=True
    )

    return res

  except Exception as e:
    return responses.ApiError(
        code=400,
        error_code="LOGIN_FAILED",
        message=str(e)
      )

def signup(data: models.SignupPayload):
  try:
    user = service.create_user(data)

    token = tokens.Tokens.encode(str(user.inserted_id))

    res = responses.ApiSuccess()

    res.set_cookie(
      key="token",
      value=token,
      httponly=True
    )

    return res
  except Exception as e:
    return responses.ApiError(
      code=400,
      error_code="SIGNUP_FAILED",
      message=str(e)
    )
