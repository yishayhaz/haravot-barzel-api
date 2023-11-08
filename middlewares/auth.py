from fastapi import Request, HTTPException
from helpers.tokens import Tokens
from helpers.responses import ApiError
import db
from bson import ObjectId

def login_required(req: Request):
  try:
    token = req.cookies.get("token")

    data = Tokens.decode(token)

    if not data['user_id']:
      raise Exception("Invalid token")
        
    user = db.USER_COLLECTION.find_one({
      "_id": ObjectId(data['user_id'])
    })

    if not user:
      raise Exception("User not found")
        
    req.state.user = user
  except:
    res = ApiError(
      code=401,
      error_code="UNAUTHORIZED",
    )

    res.delete_cookie(
      key="token"
    )

    return res