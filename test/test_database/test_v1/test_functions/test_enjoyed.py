from datetime import datetime

from aiounittest import AsyncTestCase
from asyncpg.pool import Pool

from database.v1.functions.enjoyed.delete import delete_enjoyed_article
from database.v1.functions.enjoyed.get import get_when_enjoyed
from database.v1.functions.enjoyed.insert import insert_enjoyed_article
from database.v1.pool import get_pool


class TestEnjoyed(AsyncTestCase):
    async def test_everything_is_working(self) -> None:
        pool: Pool = await get_pool()

        await self.it_can_insert_get_and_delete(pool=pool)

        await pool.close()

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
        when_enjoyed: list[int] = await get_when_enjoyed(
            database_pool=pool,
            id=fake_id
        )
        self.assertIsNotNone(when_enjoyed)
        self.assertEqual(1, len(when_enjoyed))
        self.assertEqual(fake_as_of, when_enjoyed[0])

        await delete_enjoyed_article(
            database_pool=pool,
            id=fake_id,
            as_of=fake_as_of
        )
        when_enjoyed = await get_when_enjoyed(
            database_pool=pool,
            id=fake_id
        )
        self.assertIsNotNone(when_enjoyed)
        self.assertEqual(0, len(when_enjoyed))
