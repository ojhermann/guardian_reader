from asyncpg.pool import Pool

QUERY: str = """
DROP TABLE IF EXISTS enjoyed;
"""


async def delete_table_enjoyed(database_pool: Pool) -> None:
    async with database_pool.acquire() as connection:
        await connection.execute(QUERY)
