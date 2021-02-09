from asyncpg.pool import Pool
from database.v1.sql.enjoyed.get import get_when_enjoyed as get_when_enjoyed_db


async def get_when_enjoyed(
        database_pool: Pool,
        id: str
) -> list[int]:
    # testing issue: https://magicstack.github.io/asyncpg/current/api/index.html#record-objects
    return [record["as_of"] for record in await get_when_enjoyed_db(database_pool=database_pool, id=id)]
