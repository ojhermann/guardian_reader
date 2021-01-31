from pydantic import BaseModel, Field


class Edition(BaseModel):
    '''
    `Edition`-specific information about the `Section`

    https://open-platform.theguardian.com/documentation/section
    '''

    id: str = Field(
        ...,
        description="Section id."
    )

    web_title: str = Field(
        ...,
        description="The title displayed on the web.",
        alias="webTitle"
    )

    api_url: str = Field(
        ...,
        description="The URL of the raw content.",
        alias="apiUrl"
    )

    code: str = Field(
        ...,
        description="The code of the section."
    )
