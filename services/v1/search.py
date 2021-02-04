from typing import Dict

from fastapi import APIRouter, Depends, Query

from client.models.search.search_response import SearchResponse
from functions.services.login.user_verification.functions import validate_token
from functions.services.search.functions import get_count_of_results, \
    get_results_without_bodies as get_results_without_bodies_fnc, \
    get_results_with_bodies as get_results_with_bodies_fnc
from services.v1._client import guardian_client
from static_data.search import SEARCH

router = APIRouter(
    prefix=f"/{SEARCH}",
    tags=[SEARCH],
    dependencies=[Depends(validate_token)]
)

TAGS_METADATA: Dict[str, str] = {
    "name": f"{SEARCH}",
}


@router.get("/body", response_model=SearchResponse)
async def get_results_with_bodies(
        start_on_page: int = Query(
            default=1,
            description="Number of the page out of the possible pages."
        ),
        results_per_response: int = Query(
            default=1,
            description="Number of Result objects returned per page."
        )
) -> SearchResponse:
    return await get_results_with_bodies_fnc(
        guardian_client=guardian_client,
        start_on_page=start_on_page,
        results_per_response=results_per_response)


@router.get("/count_of_available_results")
async def get_count_of_available_results() -> int:
    return await get_count_of_results(guardian_client)


@router.get("/no_body", response_model=SearchResponse)
async def get_results_without_bodies(
        start_on_page: int = Query(
            default=1,
            description="Number of the page out of the possible pages."
        ),
        results_per_response: int = Query(
            default=5,
            description="Number of Result objects returned per page."
        )
) -> SearchResponse:
    return await get_results_without_bodies_fnc(
        guardian_client=guardian_client,
        start_on_page=start_on_page,
        results_per_response=results_per_response)
