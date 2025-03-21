from sqlmodel import create_engine, SQLModel
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
        from src.books.models import Book 
        await conn.run_sync(SQLModel.metadata.create_all)
        
##db columns from book model
