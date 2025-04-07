from app.db.query.user import UserQuery
from config.settings import setting
from app.schema.jwt import JWTResponsePayload
from app.schema.otp import OtpLogingSchema, OtpSchema
from fastapi import APIRouter
from app.utils.JWT import JWTHandler
from app.utils.utils import Utils
import redis
from app.servise.sendsms import SendMassage
from app.exption.exptionHTTP import ExpireCode, InValidData

redis_pool = redis.ConnectionPool(host=setting.REDIS_HOST, port=setting.REDIS_PORT, db=15)
redis_client = redis.Redis(connection_pool=redis_pool)
router = APIRouter()


@router.post("/signup/", tags=["otp"], response_model=OtpSchema)
async def signup(phone: OtpSchema):
    """
        If phone number client verify send code otp

            - Response

                - status code 200 : ok send code otp
                - status code 400 : invalid data input
    """
    code = redis_client.get(phone.phone_number)
    if not code:
        code = Utils.code_generator()
        redis_client.set(phone.phone_number, code)  # noqa
        redis_client.expire(phone.phone_number, setting.TIME_CHASH_OTP)# noqa
    else:
        code = code.decode("utf-8")  # noqa
    SendMassage(massage=code, phone=phone.phone_number).send()
    return phone


@router.post("/loging_phone/", tags=["otp"], response_model=JWTResponsePayload)
async def loging_phone(data: OtpLogingSchema):
    """
          If phone number client verify and verify code otp bot create user

                - Response
                    - status code 200 : ok send code otp
                        {
                          "access": "ey___Scw",
                          "refresh": "ey___uo"
                        }

                    - status code 406 : Someone has already registered with this number.
                        {detail: Someone has already registered with this number}
                    - status code 422 : invalid data input
                    - status code 400 : code or phone number is invalid
                        - {detail: invalid data}
                    - status code 406 : invalid data input
                        - {detail: code time expire}

      """
    try:
        code = redis_client.get(data.phone_number).decode("utf-8")
    except AttributeError:
        raise InValidData
    if not code:
        raise ExpireCode
    if not code == data.code:
        raise InValidData

    user = await UserQuery.create_phone(data.phone_number)
    access_token = JWTHandler.token(id=str(user.id), exper_time=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token = JWTHandler.token(id=str(user.id), exper_time=setting.REFRESH_TOKEN_EXPIRE_MINUTES)
    return JWTResponsePayload(access=access_token, refresh=refresh_token)
