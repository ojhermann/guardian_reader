from datetime import datetime

from asyncpg.pool import Pool
from asyncpg.prepared_stmt import PreparedStatement
from asyncpg.protocol.protocol import Record

QUERY: str = """
INSERT INTO enjoyed (as_of, id) 
VALUES ($1, $2) 
ON CONFLICT (as_of, id) DO NOTHING
RETURNING *;
"""


async def insert_enjoyed_article(
        database_pool: Pool,
        id: str,
        as_of: int = int(datetime.utcnow().timestamp())
) -> list[Record]:
    async with database_pool.acquire() as connection:
        prepared_statement: PreparedStatement = await connection.prepare(QUERY)
        return await prepared_statement.fetch(as_of, id)
