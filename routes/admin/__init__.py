from fastapi import APIRouter, Depends
from . import controllers
import middlewares

router = APIRouter()

router.add_api_route("/profile", controllers.create_profile, methods=["POST"])
router.add_api_route("/profile/{profile_id}", controllers.update_profile, methods=["PUT"])