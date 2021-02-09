import os
from typing import Optional

import asyncpg
from asyncpg.pool import Pool


async def get_pool() -> Pool:
    return await asyncpg.create_pool(
        dsn=os.getenv("DATABASE_URL"),
        ssl="require")


class DatabasePool:
    def __init__(self):
        self._pool: Optional[Pool] = None

    async def get(self) -> Pool:
        if not self._pool:
            self._pool = await get_pool()
        return self._pool

    async def close(self) -> None:
        if self._pool:
            await self._pool.close()
