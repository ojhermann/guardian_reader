from fastapi import HTTPException, status
from httpx import RequestError

from client.client import GuardianClient
from client.models.search.search_response import SearchResponse


async def get_count_of_results(guardian_client: GuardianClient) -> int:
    try:
        search_response: SearchResponse = await guardian_client.get_results(
            start_on_page=1,
            results_per_response=0,
            include_body=False)
        return search_response.total_results
    except RequestError:
        # todo add logging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


async def get_results_with_bodies(
        guardian_client: GuardianClient,
        start_on_page: int,
        results_per_response: int) -> SearchResponse:
    try:
        return await guardian_client.get_results(
            start_on_page=start_on_page,
            results_per_response=results_per_response,
            include_body=True
        )
    except RequestError:
        # todo add logging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


async def get_results_without_bodies(
        guardian_client: GuardianClient,
        start_on_page: int,
        results_per_response: int) -> SearchResponse:
    try:
        return await guardian_client.get_results(
            start_on_page=start_on_page,
            results_per_response=results_per_response,
            include_body=False
        )
    except RequestError:
        # todo add logging
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
