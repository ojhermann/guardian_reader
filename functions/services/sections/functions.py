from fastapi import HTTPException, status
from httpx import RequestError

from client.client import GuardianClient
from client.models.sections.section_response import SectionResponse


async def get_sections(guardian_client: GuardianClient) -> SectionResponse:
    try:
        return await guardian_client.get_sections()
    except RequestError:
        # todo add logging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
