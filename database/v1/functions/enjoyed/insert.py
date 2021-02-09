from datetime import datetime
from typing import Optional

from asyncpg.pool import Pool
from asyncpg.protocol.protocol import Record

from database.v1.sql.enjoyed.insert import insert_enjoyed_article as insert_enjoyed_article_db

from models.enjoyed.enjoyed import Enjoyed


async def insert_enjoyed_article(
        database_pool: Pool,
        id: str,
        as_of: int = int(datetime.utcnow().timestamp())
) -> Optional[Enjoyed]:
    # testing issue: https://magicstack.github.io/asyncpg/current/api/index.html#record-objects
    records: list[Record] = await insert_enjoyed_article_db(
        database_pool=database_pool,
        id=id,
        as_of=as_of)

    if records:
        return Enjoyed(as_of=records[0]["as_of"], id=records[0]["id"])
    else:
        return None
