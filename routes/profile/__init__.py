from fastapi import APIRouter
from . import controllers

router = APIRouter()

router.add_api_route("/{profile_username}", controllers.get_profile, methods=["GET"])
