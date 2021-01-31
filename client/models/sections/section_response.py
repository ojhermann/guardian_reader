from pydantic import BaseModel, Field

from client.models.sections.section import Section


class SectionResponse(BaseModel):
    '''
    The Guardian response from the section API.

    https://open-platform.theguardian.com/documentation/section
    '''
    status: str = Field(
        ...,
        description="The status of the response. It refers to the state of the API. Successful calls will receive an ok even if your query did not return any results."
    )

    user_tier: str = Field(
        ...,
        description="Describes the type of rights possessed by the token used in the API call.",
        alias="userTier"
    )

    section_count: int = Field(
        ...,
        description="The number of sections returned.",
        alias="total"
    )

    sections: list[Section] = Field(
        ...,
        description="A list of `Section` objects",
        alias="results"
    )
