from asyncpg.pool import Pool

from database.v1.pool import get_pool
from database.v1.sql.enjoyed.create import create_table_enjoyed, create_index_on_id


async def main() -> None:
    database_pool: Pool = await get_pool()

    await create_table_enjoyed(database_pool=database_pool)
    await create_index_on_id(database_pool=database_pool)

    await database_pool.close()


if __name__ == "__main__":
    import asyncio

    asyncio.get_event_loop().run_until_complete(main())
