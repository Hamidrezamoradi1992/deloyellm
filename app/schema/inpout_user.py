from typing import Optional
from pydantic import BaseModel, EmailStr, Field, HttpUrl

from app.schema.enum import Gender


class UserAuthEmailModel(BaseModel):
    email: EmailStr
    photo_url: HttpUrl
    display_name: str


class UserModelSchema(BaseModel):
    phone_number: Optional[str] = Field(default=None, min_length=11, max_length=13)
    name: Optional[str] = Field(default=None, min_length=3, max_length=70)
    last_name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    display_name: Optional[str] = Field(default=None, min_length=3, max_length=70)
    gender: Optional[Gender] = Field(default=None)
    age: Optional[int] = Field(default=None)
    country: Optional[str] = Field(default=None)

    class Config:
        json_schema_extra = {
            "example": {
                'phone_number': "0919---752 or +98919----752 / null",
                'name': 'str / null',
                'last_name': 'str / null',
                'display_name': 'str / ',
                'gender': 'male/female/other/not_given / null',
                'age': '15 < int < 120 / null',
                'country': 'str / null'
            }
        }
