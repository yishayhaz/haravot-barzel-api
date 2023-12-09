from fastapi import APIRouter
from . import controllers

router = APIRouter()

router.add_api_route("/profile", controllers.create_profile, methods=["POST"])
router.add_api_route("/profile/{profile_id}", controllers.update_profile, methods=["PUT"])
router.add_api_route("/profile/{profile_id}/social", controllers.add_profile_social, methods=["POST"])
router.add_api_route("/profile/{profile_id}/social/{social_platform}", controllers.delete_profile_social, methods=["DELETE"])