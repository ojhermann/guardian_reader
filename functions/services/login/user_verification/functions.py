from os import getenv

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from functions.passwords.user_password_reference import UserPasswordReference
from functions.services.login.user_verification.exceptions import CredentialsException
from static_data.login import LOGIN, GUARDIAN_JWT_KEY, HS256

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=LOGIN)


def validate_token(token: str = Depends(oauth2_scheme)) -> None:
    try:
        payload = jwt.decode(token, getenv(GUARDIAN_JWT_KEY), [HS256])
    except JWTError:
        # todo add logging
        print("jwt problem")
        raise CredentialsException()

    username: str = payload.get("sub")  # https://tools.ietf.org/html/rfc7519#section-4.1.2
    if username is None:
        # todo add logging
        print("payload problem")
        raise CredentialsException()

    if getenv(UserPasswordReference(username)) is None:
        # todo add logging
        print("env variable problem")
        raise CredentialsException()
