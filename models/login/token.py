from pydantic import BaseModel, Field

from static_data.login import TOKEN_TYPE


class Token(BaseModel):
    '''
    Used when granting access to the services in this repo
    '''
    access_token: str = Field(
        ...,
        description="str representation of an encoded, associated AccessToken"
    )

    token_type: str = Field(
        TOKEN_TYPE,
        description="The type of token"
    )
