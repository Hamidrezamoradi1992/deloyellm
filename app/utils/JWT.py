from typing import Annotated
import jwt
from fastapi import Header
from app.exption.exptionHTTP import InvalidToken, InvalidHeader, InvalidTimeToken
from app.schema.jwt import JWTPayload
from config.settings import setting
from datetime import datetime, timedelta
from app.utils.timezone import get_timezone


class JWTHandler:
    EXPER_TIME = setting.ACCESS_TOKEN_EXPIRE_MINUTES
    SECRET_KEY = setting.SECRET_KEY

    @staticmethod
    def token(id: str, exper_time: int) -> str:
        time = get_timezone()
        expires_delta = time + timedelta(minutes=exper_time)
        to_encode = {
            "exp": expires_delta,
            "id": id,
        }
        encoded_jwt = jwt.encode(to_encode, setting.SECRET_KEY, setting.ALGORITHM)

        return encoded_jwt

    @staticmethod
    def verify_token(auth_token: Annotated[str, Header()]) -> JWTPayload:
        time = get_timezone()
        jwt_token = auth_token
        if not jwt_token:
            raise InvalidHeader
        try:
            token_data = jwt.decode(jwt_token, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
            if datetime.fromtimestamp(token_data["exp"]) < time.now():
                raise InvalidTimeToken
        except jwt.exceptions.PyJWTError:
            raise InvalidToken

        return JWTPayload(**token_data)
