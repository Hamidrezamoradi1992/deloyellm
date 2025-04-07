import re
from beanie import Document, before_event, Insert, Before, Update, Replace
from datetime import datetime
from typing import Optional, List
from app.schema.enum import Gender
from pydantic import EmailStr, Field, IPvAnyAddress, HttpUrl
from app.utils.utils import Utils


class User(Document):
    email: Optional[EmailStr] = Field(default=None)
    phone_number: Optional[str] = Field(default=None, min_length=11, max_length=14)
    name: Optional[str] = Field(default=None, min_length=3, max_length=70)
    last_name: Optional[str] = Field(default=None, min_length=3, max_length=100)
    display_name: Optional[str] = Field(default=None, min_length=3, max_length=70)
    photo_url: Optional[HttpUrl] = Field(default=None, alias='url_photo')
    photo: Optional[str] = Field(default=None, alias='photo')
    gender: Optional[Gender] = Field(default=None, alias='gender')
    age: Optional[int] = Field(default=None, ge=12, alias='age')
    permissions: List = Field(default=['staff', 'user_free'])
    country: Optional[str] = Field(default=None, alias='country')
    ip_address_1: Optional[IPvAnyAddress] = Field(default=None, alias='ip_address')
    ip_address_2: Optional[IPvAnyAddress] = Field(default=None, alias='ip_address')
    ip_address_3: Optional[IPvAnyAddress] = Field(default=None, alias='ip_address')
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
    is_delete: bool = Field(False, alias='delete')
    is_active: bool = Field(True, alias='is_active')

    class Settings:
        is_root = True
        name = "users"
