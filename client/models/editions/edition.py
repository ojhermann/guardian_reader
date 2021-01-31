from pydantic import BaseModel, Field


class Edition(BaseModel):
    '''
    Contains information about an edition of The Guardian

    https://open-platform.theguardian.com/documentation/edition
    '''

    id: str = Field(
        ...,
        description="The unique id for the Edition."
    )

    path: str = Field(
        ...,
        description="The path for the Edition."
    )

    edition: str = Field(
        ...,
        description="str identifier of the Edition."
    )

    web_title: str = Field(
        ...,
        description="Title of the Edition.",
        alias="webTitle"
    )

    web_url: str = Field(
        ...,
        description="Human-readable url of the Edition.",
        alias="webUrl"
    )

    api_url: str = Field(
        ...,
        description="API url of the Edition.",
        alias="apiUrl"
    )
