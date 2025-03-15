from fastapi import FastAPI
from src.books.routes import book_router
version="v1"

app=FastAPI(
    title="BOOK API",
    description="A rest api for book management",
    version=version)
app.include_router(book_router,prefix='/api/{version}/books',tags=['books'])