import os
from fastapi import APIRouter, UploadFile, Depends, Body,Response
from app.schema.inpout_user import UserAuthEmailModel, UserModelSchema
from app.schema.jwt import JWTResponsePayload, JWTPayload
from app.db.query.user import UserQuery
from app.schema.output_user import UserModelOutputSchema
from config.settings import setting
from app.utils.utils import Utils
from app.utils.JWT import JWTHandler
from app.exption.exptionHTTP import InvalidToken

router = APIRouter()


@router.post("/loging/", tags=["user"], response_model=JWTResponsePayload)
async def signup( response:Response,data: UserAuthEmailModel = Body(..., embed=True)):
    """
        This api for signup a user whit GOOGLE authorization

            - Response
                - status code 200: create user successfully
                    {
                          "access": "ey___Scw",
                          "refresh": "ey___uo"
                    }
                - status code 422: Unprocessable Content
                    Invalid data input
                - status code 406 : Someone has already registered with this number.
                        {detail: Someone has already registered with this number}
    """
    user = await UserQuery.create_user_email(data)
    access_token = JWTHandler.token(id=str(user.id), exper_time=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    refresh_token = JWTHandler.token(id=str(user.id), exper_time=setting.REFRESH_TOKEN_EXPIRE_MINUTES)
    response.set_cookie(key='access_token', value=access_token,max_age=setting.ACCESS_TOKEN_EXPIRE_MINUTES*60)
    response.set_cookie(key='refresh_token', value=refresh_token,max_age=setting.REFRESH_TOKEN_EXPIRE_MINUTES*60
                        )
    return JWTResponsePayload(access=access_token, refresh=refresh_token)


@router.get("/profile/", tags=["user"])
async def get_user(verifi: JWTPayload = Depends(JWTHandler.verify_token)):
    if verifi:
        user = await UserQuery.get(verifi)
        data = UserModelOutputSchema(**user.model_dump())
        return data
    raise InvalidToken


@router.post("/upload/image/", tags=["user"])
async def create_upload_file(file: UploadFile, verifi: JWTPayload = Depends(JWTHandler.verify_token)):
    if verifi:
        unique_filename = Utils.generate_unique_filename(setting.STATIC_DIR, file.filename)
        file_path = os.path.join(setting.STATIC_DIR, unique_filename)
        with open(file_path, "wb") as f:
            f.write(file.file.read())
        user = await UserQuery.update_image_user(verifi.id, file_path)

        return {"status": user}
    raise InvalidToken


@router.post("/update/", tags=['user'], response_model=UserModelSchema)
async def create_update_profile(data: UserModelSchema,  # noqa
                                verifi: JWTPayload = Depends(JWTHandler.verify_token)) -> UserModelSchema:
    if verifi:
        user = await UserQuery.update_user_profile(verifi.id, data)
        return user
    raise InvalidToken
