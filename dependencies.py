from db.engine import AsyncSessionLocal


async def get_db():
    db = await AsyncSessionLocal()
    try:
        yield db
    finally:
        db.close()
