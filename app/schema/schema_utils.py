from datetime import datetime
from pydantic import BaseModel, Field


class UserSearchSchema(BaseModel):
    question: str
    answer: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime
    is_delete: bool = Field(False, alias='delete')
    is_active: bool = Field(True, alias='is_active')
