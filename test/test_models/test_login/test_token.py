from unittest import TestCase

from models.login.token import Token
from static_data.login import TOKEN_TYPE

ACCESS_TOKEN: str = "this_is_not_really_an_access_token"
TOKEN: Token = Token(
    access_token=ACCESS_TOKEN
)


class TestToken(TestCase):
    def test_it_contains_the_correct_access_token(self) -> None:
        self.assertEqual(ACCESS_TOKEN, TOKEN.access_token)

    def test_it_contains_the_correct_token_type(self) -> None:
        self.assertEqual(TOKEN_TYPE, TOKEN.token_type)
