from asyncpg.pool import Pool
from asyncpg.prepared_stmt import PreparedStatement
from asyncpg.protocol.protocol import Record

QUERY: str = """
SELECT as_of  
FROM enjoyed  
WHERE id=$1;
"""


async def get_when_enjoyed(
        database_pool: Pool,
        id: str
) -> list[Record]:
    async with database_pool.acquire() as connection:
        prepared_statement: PreparedStatement = await connection.prepare(QUERY)
        return await prepared_statement.fetch(id)
