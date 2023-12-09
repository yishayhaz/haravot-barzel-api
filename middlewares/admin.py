from fastapi import Request, HTTPException
from helpers.env import EnvVars

def is_admin(req: Request):

  if False and req.headers.get("x-admin-secret") != EnvVars.ADMIN_SECRET:
    raise HTTPException(
      status_code=401,
      detail="Unauthorized",
    )