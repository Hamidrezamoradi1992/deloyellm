from pydantic import BaseModel



class JWTResponsePayload(BaseModel):
    access: str
    refresh: str


class JWTPayload(BaseModel):
    id: str
    exp: int


class JWTResponseRefreshToken(BaseModel):
    access: str
