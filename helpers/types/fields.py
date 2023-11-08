from helpers import validators
from pydantic import BaseModel, validator
from bson import ObjectId

class PasswordField(BaseModel):
    password: str

    @validator("password")
    def validate_email(cls, value):
        if not validators.valid_password(value):
            raise ValueError("Invalid password format")
        
        return value
    
class ObjectIdField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid id")

        return ObjectId(value)

    @classmethod
    def __get_pydantic_json_schema__(cls, field_schema):
        field_schema.update(type="string")