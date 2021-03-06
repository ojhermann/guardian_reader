from typing import Dict, Optional, Any

import httpx
from os import getenv

from client.models.editions.editions import Editions
from client.models.search.search_response import SearchResponse
from client.models.sections.section_response import SectionResponse
from static_data.api import GUARDIAN_API_KEY


class Endpoints:
    editions: str = "https://content.guardianapis.com/editions"
    search: str = "https://content.guardianapis.com/search"
    sections: str = "https://content.guardianapis.com/sections"
    tags: str = "https://content.guardianapis.com/tags"


TIMEOUT: httpx.Timeout = httpx.Timeout(
    timeout=3.1,
    connect=3.1,
    read=3.1,
    write=3.1,
    pool=3.1
)


class _GuardianClient(httpx.AsyncClient):
    def __init__(self):
        super().__init__(
            timeout=TIMEOUT)
        self._api_key: str = getenv(GUARDIAN_API_KEY)

    def _get_api_key_param(self) -> Dict[str, str]:
        return {"api-key": self._api_key}

    async def _get_response(
            self,
            endpoint: str,
            params: Optional[dict[str, Any]] = None) -> httpx.Response:
        request: httpx.Request = httpx.Request(
            method="GET",
            url=endpoint,
            params=self._get_api_key_param() | params if params else self._get_api_key_param()
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

    async def _get_response_as_object(
            self,
            endpoint: str,
            response_type,
            params: Optional[dict[str, Any]] = None):
        guardian_response: httpx.Response = await self._get_response(endpoint, params)
        return response_type(**(guardian_response.json())['response'])


class GuardianClient(_GuardianClient):
    def __init__(self):
        super().__init__()

    async def get_editions(self) -> Editions:
        return await self._get_response_as_object(
            endpoint=Endpoints.editions,
            response_type=Editions
        )

    async def get_sections(self) -> SectionResponse:
        return await self._get_response_as_object(
            endpoint=Endpoints.sections,
            response_type=SectionResponse
        )

    async def get_results(
            self,
            start_on_page: int,
            results_per_response: int,
            include_body: bool
    ) -> SearchResponse:
        params: dict[str, Any] = {
            "page": start_on_page,
            "page-size": results_per_response,
        }
        if include_body:
            params["show-fields"] = "body"

        return await self._get_response_as_object(
            endpoint=Endpoints.search,
            response_type=SearchResponse,
            params=params
        )
