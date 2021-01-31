from pydantic import BaseModel, Field

from client.models.sections.edition import Edition


class Section(BaseModel):
    '''
    Information about the `Section`

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

    editions: list[Edition] = Field(
        ...,
        description="The list of existing `Edition` objects for this section."
    )
