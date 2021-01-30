from datetime import datetime, timedelta
from unittest import TestCase

from models.login.access_token import AccessToken

USERNAME: str = "fake_username"
LIFE_TIME_IN_MINUTES: int = 30
ACCESS_TOKEN: AccessToken = AccessToken(username=USERNAME, lifetime_in_minutes=LIFE_TIME_IN_MINUTES)
FAKE_KEY: str = "4e833e9a6033140ff0354df51fcea71e61b6525e9bdfba57aabeab493cd729be"


class TestAccessToken(TestCase):
    def test_sub_works(self) -> None:
        self.assertEqual(USERNAME,
                         ACCESS_TOKEN.sub)

    def test_exp_works(self) -> None:
        self.assertTrue(ACCESS_TOKEN.exp > datetime.utcnow() + timedelta(minutes=29))
        self.assertTrue(ACCESS_TOKEN.exp < datetime.utcnow() + timedelta(minutes=31))

    def test_generate_encoded_jwt_works(self) -> None:
        jwt: str = ACCESS_TOKEN.generate_encoded_jwt(key=FAKE_KEY)
        self.assertTrue(isinstance(jwt, str))
