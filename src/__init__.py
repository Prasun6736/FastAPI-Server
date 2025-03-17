from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import db_init
@asynccontextmanager
async def life_span(app:FastAPI):
    print("Server Starting")
    await db_init()
    yield
    print("Server End")

version="v1"

app=FastAPI(
    title="BOOK API",
    description="A rest api for book management",
    version=version,lifespan=life_span)
app.include_router(book_router,prefix='/api/{version}/books',tags=['books'])