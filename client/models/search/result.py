from datetime import datetime

from pydantic import BaseModel, Field

from client.models.search.guardian_fields import GuardianFields


class Result(BaseModel):
    '''
        Subset of the Guardian's response when querying the search endpoint

        https://open-platform.theguardian.com/documentation/search
        '''
    id: str = Field(
        ...,
        description="Unique id."
    )

    type: str = Field(
        ...,
        description="Type of result."
    )

    section_id: str = Field(
        ...,
        description="Section ID.",
        alias="sectionId"
    )

    section_name: str = Field(
        ...,
        description="Section name.",
        alias="sectionName"
    )

    web_publication_date: datetime = Field(
        ...,
        description="Datetime of the publication on the web.",
        alias="webPublicationDate"
    )

    web_title: str = Field(
        ...,
        description="The title displayed on the web.",
        alias="webTitle"
    )

    web_url: str = Field(
        ...,
        description="The URL of the human-readable site.",
        alias="webUrl"
    )

    api_url: str = Field(
        ...,
        description="The URL of the raw content.",
        alias="apiUrl"
    )

    is_hosted: bool = Field(
        ...,
        alias="isHosted"
    )

    pillar_id: str = Field(
        ...,
        alias="pillarId"
    )

    pillar_name: str = Field(
        ...,
        alias="pillarName"
    )

    guardian_fields: GuardianFields = Field(
        None,
        description="Fields returned by the relevant query",
        alias="fields"
    )
