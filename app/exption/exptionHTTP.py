from fastapi import HTTPException, status


class UserNotFound(HTTPException):
    def __init__(self):
        self.detail = 'User not found'
        self.status_code = status.HTTP_404_NOT_FOUND


class InvalidUser(HTTPException):
    def __init__(self):
        self.detail = 'username or password invalid'
        self.status_code = status.HTTP_401_UNAUTHORIZED


class InValidData(HTTPException):
    def __init__(self):
        self.detail = 'invalid data'
        self.status_code = status.HTTP_400_BAD_REQUEST


class InvalidToken(HTTPException):
    def __init__(self):
        self.detail = 'Token invalid'
        self.status_code = status.HTTP_401_UNAUTHORIZED


class InvalidTimeToken(HTTPException):
    def __init__(self):
        self.detail = 'Time token exp'
        self.status_code = status.HTTP_401_UNAUTHORIZED


class InvalidHeader(HTTPException):
    def __init__(self):
        self.detail = "auth header not found."
        self.status_code = status.HTTP_401_UNAUTHORIZED


class AlreadyRegistered(HTTPException):
    def __init__(self):
        self.detail = "Someone has already registered with this number."
        self.status_code = status.HTTP_406_NOT_ACCEPTABLE


class ExpireCode(HTTPException):
    def __init__(self):
        self.detail = "code time expire"
        self.status_code = status.HTTP_406_NOT_ACCEPTABLE
