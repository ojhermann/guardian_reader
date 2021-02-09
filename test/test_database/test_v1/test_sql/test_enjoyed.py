from datetime import datetime

from aiounittest import AsyncTestCase
from asyncpg.pool import Pool
from asyncpg.protocol.protocol import Record

from database.v1.pool import get_pool
from database.v1.sql.enjoyed.delete import delete_enjoyed_article
from database.v1.sql.enjoyed.get import get_when_enjoyed
from database.v1.sql.enjoyed.insert import insert_enjoyed_article


class TestEnjoyed(AsyncTestCase):
    async def test_everything_is_working(self) -> None:
        pool: Pool = await get_pool()

        await self.table_exists(pool=pool)

        await self.it_can_insert_get_and_delete(pool=pool)

        await pool.close()

    async def table_exists(self, pool: Pool) -> None:
        async with pool.acquire() as connection:
            self.assertTrue(await connection.fetch("SELECT 'public.enjoyed'::regclass"))

    async def it_can_insert_get_and_delete(self, pool: Pool) -> None:
        fake_id: str = "fake_id"
        fake_as_of: int = int(datetime(
            year=1980,
            month=1,
            day=1,
            hour=1,
            minute=1,
            second=1,
            microsecond=1,
        ).timestamp())

        await insert_enjoyed_article(
            database_pool=pool,
            id=fake_id,
            as_of=fake_as_of
        )
        result: list[Record] = await get_when_enjoyed(
            database_pool=pool,
            id=fake_id
        )
        self.assertIsNotNone(result)
        self.assertEqual(1, len(result))
        self.assertEqual(fake_as_of, result[0]["as_of"])

        await delete_enjoyed_article(
            database_pool=pool,
            id=fake_id,
            as_of=fake_as_of
        )
        result = await get_when_enjoyed(
            database_pool=pool,
            id=fake_id
        )
        self.assertIsNotNone(result)
        self.assertEqual(0, len(result))
