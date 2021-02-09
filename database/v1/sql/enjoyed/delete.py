from asyncpg.pool import Pool
from asyncpg.prepared_stmt import PreparedStatement
from asyncpg.protocol.protocol import Record

QUERY: str = """
DELETE 
FROM enjoyed  
WHERE as_of = $1 AND id = $2 
RETURNING *;
"""


async def delete_enjoyed_article(
        database_pool: Pool,
        id: str,
        as_of: int
) -> list[Record]:
    async with database_pool.acquire() as connection:
        prepared_statement: PreparedStatement = await connection.prepare(QUERY)
        return await prepared_statement.fetch(as_of, id)
