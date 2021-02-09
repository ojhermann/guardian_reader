from asyncpg.pool import Pool


async def create_table_enjoyed(database_pool: Pool) -> None:
    QUERY: str = """
    CREATE TABLE IF NOT EXISTS enjoyed (
        as_of BIGINT NOT NULL,
        id TEXT NOT NULL,
        PRIMARY KEY (as_of, id)
    );
    """
    async with database_pool.acquire() as connection:
        await connection.execute(QUERY)


async def create_index_on_id(database_pool: Pool) -> None:
    QUERY: str = """
        CREATE INDEX IF NOT EXISTS id_index ON enjoyed (id);
        """
    async with database_pool.acquire() as connection:
        await connection.execute(QUERY)
