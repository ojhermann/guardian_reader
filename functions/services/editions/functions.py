from typing import List

from fastapi import HTTPException, status
from httpx import RequestError

from client.client import GuardianClient
from client.models.editions.edition import Edition
from client.models.editions.editions import Editions


async def get_editions(guardian_client: GuardianClient) -> List[Edition]:
    try:
        editions: Editions = await guardian_client.get_editions()
        return editions.editions
    except RequestError:
        # todo add logging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
