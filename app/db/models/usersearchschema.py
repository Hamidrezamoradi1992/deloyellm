from datetime import datetime
from typing import Optional
from bson import ObjectId
from pydantic import Field
from app.schema.schema_utils import UserSearchSchema
from beanie import Document, BeanieObjectId


class UserHistory(Document):
    user_id: BeanieObjectId
    title: str
    search: UserSearchSchema
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default=None)
    is_delete: bool = Field(False, alias='delete')
    is_active: bool = Field(True, alias='is_active')

    class Settings:
        name = "user_history"
