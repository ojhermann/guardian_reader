from datetime import datetime
from typing import Optional

from asyncpg.pool import Pool

from database.v1.functions.enjoyed.delete import delete_enjoyed_article as delete_enjoyed_article_fnc
from database.v1.functions.enjoyed.get import get_when_enjoyed as get_when_enjoyed_fnc
from database.v1.functions.enjoyed.insert import insert_enjoyed_article as insert_enjoyed_article_fnc
from models.enjoyed.enjoyed import Enjoyed


async def delete_enjoyed_article(
        database_pool: Pool,
        as_of: int,
        id: str,
) -> Optional[Enjoyed]:
    return await delete_enjoyed_article_fnc(
        database_pool=database_pool,
        as_of=as_of,
        id=id
    )


async def get_when_enjoyed(
        database_pool: Pool,
        id: str
) -> list[int]:
    return await get_when_enjoyed_fnc(
        database_pool=database_pool,
        id=id
    )


async def insert_enjoyed_article(
        database_pool: Pool,
        id: str,
        as_of: int = int(datetime.utcnow().timestamp())
) -> Optional[Enjoyed]:
    return await insert_enjoyed_article_fnc(
        database_pool=database_pool,
        id=id,
        as_of=as_of)
