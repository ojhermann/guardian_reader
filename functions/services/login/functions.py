from os import getenv
from typing import Dict

from fastapi.security import OAuth2PasswordRequestForm

from functions.passwords.exceptions import InvalidPassword
from functions.passwords.functions import password_is_ok
from models.login.access_token import AccessToken
from static_data.login import GUARDIAN_JWT_KEY, TOKEN_TYPE
from functions.passwords.user_password_reference import UserPasswordReference


async def generate_token(form_data: OAuth2PasswordRequestForm) -> Dict[str, str]:
    if not password_is_ok(
            form_data.password,
            getenv(UserPasswordReference(form_data.username))):
        raise InvalidPassword()

    return {
        "access_token": AccessToken(username=form_data.username).generate_encoded_jwt(getenv(GUARDIAN_JWT_KEY)),
        "token_type": TOKEN_TYPE
    }
