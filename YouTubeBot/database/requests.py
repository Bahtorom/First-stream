from YouTubeBot.database.models import async_session
from YouTubeBot.database.models import User, Item, Category
from sqlalchemy import select, update, delete
from aiogram.types import Message


async def set_user(tg_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id))
            await session.commit()

async def get_categories():
    async with async_session() as session:
        return await session.scalars(select(Category))

async def get_categories_item(category_id):
    async with async_session() as session:
        return await session.scalars(select(Item).where(Item.category == category_id))

async def get_item(item_id):
    async with async_session() as session:
        return await session.scalar(select(Item).where(Item.id == item_id))