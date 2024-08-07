from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from db.models.base import Base

engine = create_async_engine(
    "sqlite+aiosqlite:///tasks.db"
)

AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
