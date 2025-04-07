from bson.errors import InvalidId
from app.exption.exptionHTTP import UserNotFound, InValidData, AlreadyRegistered
from app.db.models.user import User
from app.schema.inpout_user import UserAuthEmailModel, UserModelSchema
from bson.objectid import ObjectId
from app.utils.utils import Utils
from app.schema.jwt import JWTPayload
from app.schema.output_user import UserModelOutputSchema
from config.settings import setting


class UserQuery:
    @staticmethod
    async def create_user_email(data: UserAuthEmailModel) -> User:
        user = await User.find_one({"email": data.email})
        if not user:
            user = User(**data.model_dump())
            await user.insert()  # noqa
        return user

    @staticmethod
    async def create_phone(data: str) -> User:
        normalized_phone = Utils.normalize_phone_number(data)
        _ = await User.find_one({"phone_number": normalized_phone}).exists()
        if _:
            return await User.find_one({"phone_number": normalized_phone})
        user = User(phone_number=normalized_phone)
        await user.insert()  # noqa
        return user

    # @staticmethod
    # async def create_phone(phone_number: str) -> User:
    #     normalized_phone = UserQuery.normalize_phone_number(phone_number)
    #     existing_user =  User.find_one({"phone_number": normalized_phone})
    #
    #     if existing_user and await existing_user.exists():
    #         return  User.find_one({"phone_number": normalized_phone})
    #
    #     new_user = User(phone_number=normalized_phone)
    #     await new_user.insert()  # Insert the new user into the database
    #     return new_user


    @staticmethod
    async def get(data: JWTPayload) -> User:
        try:

            user = await User.find_one({'_id': ObjectId(data.id)})
            if not user:
                raise UserNotFound
            return user
        except InvalidId:
            raise InValidData

    @staticmethod
    async def update_image_user(user_id: str, path_file: str) -> bool:
        user = await User.find_one({'_id': ObjectId(user_id)})
        if not user:
            raise AlreadyRegistered
        await user.update({"$set": {"photo": path_file}})
        return True

    @staticmethod
    async def update_user_profile(user_id: str, data: UserModelSchema) -> UserModelSchema:
        user = await User.find_one({'_id': ObjectId(user_id)})
        if not user:
            raise AlreadyRegistered

        user = await user.update({"$set": {**data.model_dump()}})
        return user
