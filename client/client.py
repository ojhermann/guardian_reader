from typing import Dict

import httpx
from os import getenv

from client.models.editions.editions import Editions
from client.models.sections.section_response import SectionResponse
from static_data.api import GUARDIAN_API_KEY

ENDPOINT_EDITIONS: str = "https://content.guardianapis.com/editions"
ENDPOINT_SECTIONS: str = "https://content.guardianapis.com/sections"

TIMEOUT: float = 3.1


class GuardianClient(httpx.AsyncClient):
    def __init__(self):
        super().__init__(
            timeout=httpx.Timeout(TIMEOUT))
        self._api_key: str = getenv(GUARDIAN_API_KEY)

    def _get_api_key_param(self) -> Dict[str, str]:
        return {"api-key": self._api_key}

    async def _get_response(
            self,
            endpoint: str) -> httpx.Response:
        request: httpx.Request = httpx.Request(
            method="GET",
            url=endpoint,
            params=self._get_api_key_param()
        )

        guardian_response: httpx.Response = await self.send(
            request=request
        )

        if guardian_response.status_code != httpx.codes.OK:
            raise httpx.RequestError(
                message="Something went wrong with your request.",
                request=request
            )

        return guardian_response

    async def _get_response_for_user(
            self,
            endpoint: str,
            response_type):
        guardian_response: httpx.Response = await self._get_response(endpoint)
        return response_type(**(guardian_response.json())['response'])

    async def get_editions(self) -> Editions:
        return await self._get_response_for_user(
            endpoint=ENDPOINT_EDITIONS,
            response_type=Editions
        )

    async def get_sections(self) -> SectionResponse:
        return await self._get_response_for_user(
            endpoint=ENDPOINT_SECTIONS,
            response_type=SectionResponse
        )
