from fastapi import APIRouter
from . import controllers

router = APIRouter()

router.add_api_route("/login", controllers.login, methods=["POST"])
router.add_api_route("/signup", controllers.signup, methods=["POST"])