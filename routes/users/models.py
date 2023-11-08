from pydantic import BaseModel, Field, validator
from helpers.types.fields import PasswordField

class LoginPayload(BaseModel):
    username: str = Field(...)
    password: str  = Field(...)

class SignupPayload(BaseModel):
    username: str = Field(...)
    password: str = Field(...)
    email: str = Field(...)
    phone: str = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)
    date_of_birth: str = Field(...)

    @validator("password")
    def validate_password(cls, value):
        return PasswordField(password=value).password

