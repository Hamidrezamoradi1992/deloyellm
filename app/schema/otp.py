from pydantic import BaseModel, Field, field_validator
from app.exption.exptionHTTP import InValidData
from app.utils.utils import Utils
import re





class OtpSchema(BaseModel):
    phone_number: str = Field(min_length=11,max_length=13)

    @field_validator("phone_number")
    @classmethod
    def validate_phone_number(cls, v):
        _=Utils.vilification_pattern_mobile(v)
        if not _:
            raise InValidData
        return v


class OtpLogingSchema(OtpSchema):
    code: str = Field(min_length=6, max_length=6)
