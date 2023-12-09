from fastapi import APIRouter, Depends
from . import (
  users, admin, profile
)
import middlewares

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(profile.router, prefix="/profile", tags=["profile"])
router.include_router(admin.router, prefix="/admin", tags=["admin"], dependencies=[Depends(middlewares.is_admin)])