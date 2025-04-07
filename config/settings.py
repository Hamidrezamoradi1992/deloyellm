from pydantic_settings import BaseSettings
from config import BASE_DIR


class Settings(BaseSettings):
    DB_CONNECTION_STRING: str
    DB_NAME: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    REDIS_HOST: str
    REDIS_PORT: int
    TIME_CHASH_OTP: int
    OTP_APIKEY: str
    OTP_PATTERN_CODE: str
    OTP_PHONE: str
    OTP_UTL: str
    STATIC_PATH: str
    STATIC_DIR: str

    class Config:
        env_file = BASE_DIR.joinpath(".env")


setting = Settings()
