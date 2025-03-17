from sqlmodel import create_engine, text
from sqlalchemy.ext.asyncio import AsyncEngine
from src.config import Config
from sqlmodel import SQLModel

engine = AsyncEngine(
    create_engine(
    url=Config.DB_URL,
    echo=True,
)
)
async def db_init():
    async with engine.begin() as conn:
        statement = text("SELECT 'hello';")
        result = await conn.execute(statement)
        print(result.all())

