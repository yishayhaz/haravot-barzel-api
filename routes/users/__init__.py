from fastapi import APIRouter, Depends
from . import controllers
import middlewares

router = APIRouter()

router.add_api_route("/login", controllers.login, methods=["POST"])
router.add_api_route("/signup", controllers.signup, methods=["POST"])
router.add_api_route("/me", controllers.getme, methods=["GET"], dependencies=[Depends(middlewares.login_required)])