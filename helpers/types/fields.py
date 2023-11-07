from helpers import validators
from pydantic import BaseModel, validator

class PasswordField(BaseModel):
    password: str

    @validator("password")
    def validate_email(cls, value):
        if not validators.valid_password(value):
            raise ValueError("Invalid password format")
        
        return value