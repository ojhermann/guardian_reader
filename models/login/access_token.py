from datetime import timedelta, datetime

from jose import jwt
from pydantic import BaseModel, Field

from static_data.login import LIFETIME_IN_MINUTES_DEFAULT, HS256


class AccessToken(BaseModel):
    '''
    Used when granting access to the services in this repo
    '''

    def __init__(self,
                 username: str,
                 lifetime_in_minutes: int = LIFETIME_IN_MINUTES_DEFAULT
                 ) -> None:
        super().__init__(sub=username,
                         exp=datetime.utcnow() + timedelta(minutes=lifetime_in_minutes)
                         )

    sub: str = Field(...,
                     title="Subject",
                     description="https://tools.ietf.org/html/rfc7519#section-4.1.2"
                     )
    exp: datetime = Field(...,
                          title="Expiration Time",
                          description="https://tools.ietf.org/html/rfc7519#section-4.1.4"
                          )

    def generate_encoded_jwt(self, key: str, algorithm=HS256) -> str:
        return jwt.encode(self.dict(), key, algorithm=algorithm)
