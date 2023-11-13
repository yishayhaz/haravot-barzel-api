from fastapi import Request, HTTPException, Response
from helpers.tokens import Tokens
import db
from bson import ObjectId

def login_required(req: Request, res: Response):
  try:
    token = req.cookies.get("token")

    data = Tokens.decode(token)

    if not data.get('user_id'):
      raise Exception("Invalid token")
        
    user = db.USER_COLLECTION.find_one({
      "_id": ObjectId(data['user_id'])
    })

    if not user:
      raise Exception("User not found")
    
    del user['password']
        
    req.state.user = user
  except:
    raise HTTPException(
      status_code=401,
      detail="Unauthorized",
      headers={ "set-cookie": "token=; Path=/; HttpOnly; expires=Thu, 01 Jan 1970 00:00:00 GMT" }
    )