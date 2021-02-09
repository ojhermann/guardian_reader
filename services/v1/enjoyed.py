from typing import Dict, Optional

from fastapi import Depends, APIRouter, Query

from database.v1.pool import DatabasePool
from functions.services.enjoyed.functions import insert_enjoyed_article, get_when_enjoyed as get_when_enjoyed_fnc
from functions.services.login.user_verification.functions import validate_token
from models.enjoyed.enjoyed import Enjoyed
from static_data.enjoyed import ENJOYED

router = APIRouter(
    prefix=f"/{ENJOYED}",
    tags=[ENJOYED],
    dependencies=[Depends(validate_token)]
)

TAGS_METADATA: Dict[str, str] = {
    "name": f"{ENJOYED}",
}

database_pool: DatabasePool = DatabasePool()


@router.on_event("shutdown")
async def shutdown():
    await database_pool.close()


@router.post("/", response_model=Optional[Enjoyed])
async def record_enjoyment(
        guardian_result_id: str = Query(...)
):
    """
    Records the enjoyment of an article with it's `id` and when that happened, as measured by seconds since the epoch
    """
    return await insert_enjoyed_article(
        database_pool=await database_pool.get(),
        id=guardian_result_id
    )


@router.get("/")
async def get_when_enjoyed(
        guardian_result_id: str = Query(...)
) -> list[int]:
    """
    Gets a list of dates, represented as seconds since epoch, of when an article was enjoyed
    """
    return await get_when_enjoyed_fnc(
        database_pool=await database_pool.get(),
        id=guardian_result_id)
