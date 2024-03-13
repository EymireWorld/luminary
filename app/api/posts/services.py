from sqlalchemy.ext.asyncio import AsyncSession


async def get_posts(session: AsyncSession, offset: int, limit: int):
    pass


async def add_post(session: AsyncSession, data: dict):
    pass


async def get_post(session: AsyncSession, post_id: int):
    pass


async def update_post(session: AsyncSession, post_id: int, data: dict):
    pass


async def remove_post(session: AsyncSession, post_id: int):
    pass
