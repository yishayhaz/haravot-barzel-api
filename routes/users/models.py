from pydantic import BaseModel, Field
from helpers.types.fields import PasswordField, EmailField, PhoneField

class LoginPayload(BaseModel):
    username: str = Field(...)
    password: str  = Field(...)

class SignupPayload(BaseModel):
    username: str = Field(...)
    password: PasswordField = Field(...)
    email: EmailField = Field(...)
    phone: PhoneField = Field(...)
    first_name: str = Field(...)
    last_name: str = Field(...)