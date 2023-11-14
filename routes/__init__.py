from fastapi import APIRouter
from . import (
  users, admin
)

router = APIRouter()

router.include_router(users.router, prefix="/users", tags=["users"])
router.include_router(admin.router, prefix="/admin", tags=["admin"])