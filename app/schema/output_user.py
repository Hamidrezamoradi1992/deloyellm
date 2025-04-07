from typing import Dict, List, Optional

from pydantic import BaseModel, Field,HttpUrl


class ModelOutputSchema(BaseModel):
    status: int = Field(default=200, alias='status')
    massage: List = Field(default=["code accepted"], alias='massage')
    data: Dict





class UserModelOutputSchema(BaseModel):
    email: Optional[str]
    phone_number: Optional[str]
    name: Optional[str]
    last_name: Optional[str]
    display_name: Optional[str]
    photo_url: Optional[HttpUrl]
    photo: Optional[str]
    gender: Optional[str]
    age: Optional[int]
    country: Optional[str]


