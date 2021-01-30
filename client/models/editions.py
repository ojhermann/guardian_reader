from typing import List

from pydantic import BaseModel, Field

from client.models.edition import Edition


class Editions(BaseModel):
    '''
    The Guardian's response when querying for all editions

    https://open-platform.theguardian.com/documentation/edition
    '''

    status: str = Field(
        ...,
        description="Guardian-specific http response code; it will return ok as long as the Guardian API received a well-formed request."
    )

    user_tier: str = Field(
        ...,
        description="Describes the type of rights possessed by the token used in the API call.",
        alias="userTier"
    )

    total: int = Field(
        ...,
        description="The number of Edition objects in the response."
    )

    editions: List[Edition] = Field(
        ...,
        description="A list of all available Edition object.",
        alias="results"
    )
