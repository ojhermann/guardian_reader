from typing import Dict

import httpx
from os import getenv

from client.models.editions.editions import Editions
from static_data.api import GUARDIAN_API_KEY

ENDPOINT_EDITIONS: str = "https://content.guardianapis.com/editions"

TIMEOUT: float = 3.1


class GuardianClient(httpx.AsyncClient):
    def __init__(self):
        super().__init__(
            timeout=httpx.Timeout(TIMEOUT))
        self._api_key: str = getenv(GUARDIAN_API_KEY)

    def _get_api_key_param(self) -> Dict[str, str]:
        return {"api-key": self._api_key}

    async def get_editions(self) -> Editions:
        request: httpx.Request = httpx.Request(
            method="GET",
            url=ENDPOINT_EDITIONS,
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

        return Editions(**(guardian_response.json())['response'])
