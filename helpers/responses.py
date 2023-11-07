from fastapi.responses import JSONResponse, Response
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Any
from bson import ObjectId
from pymongo.errors import DuplicateKeyError
from io import BytesIO


class _Response(JSONResponse):
    def __init__(
        self,
        code: int,
        success: bool,
        data: dict = None,
        message: str = None,
        error_code: str = None,
        *args,
        **kwargs,
    ):
        self.content = {"success": success}

        if data is not None:
            self.content["content"] = jsonable_encoder(
                data, custom_encoder={ObjectId: str}
            )
        if message is not None:
            self.content["message"] = message

        if error_code is not None:
            self.content["error_code"] = error_code

        super().__init__(self.content, status_code=code, *args, **kwargs)


class ApiError(_Response):
    def __init__(self, code: int = 400, error_code: str = None, *args, **kwargs):
        super().__init__(code, False, error_code=error_code, *args, **kwargs)


class ApiSuccess(_Response):
    def __init__(self, code: int = 200, success: bool = True, *args, **kwargs):
        super().__init__(code, success, *args, **kwargs)