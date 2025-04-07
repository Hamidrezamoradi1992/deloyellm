from fastapi import APIRouter, Depends
from app.exption.exptionHTTP import InvalidToken
from app.schema.jwt import JWTPayload,JWTResponseRefreshToken
from app.utils.JWT import JWTHandler
from config.settings import setting

router = APIRouter()


@router.post("/registerJwt",tags=["jwt"])
async def registerJwt(verifi: JWTPayload = Depends(JWTHandler.verify_token)):
    if verifi:
        token = JWTHandler.token(verifi.id, setting.ACCESS_TOKEN_EXPIRE_MINUTES)
        return JWTResponseRefreshToken(access=token)
    raise InvalidToken
