
from fastapi import APIRouter
from typing import List
from fastapi.exceptions import HTTPException
from fastapi import status
from src.books.schemas import Book,UpdateBook
from src.books.book import books

book_router=APIRouter()

@book_router.get('/',response_model=List[Book])
async def get_books():
    return books

@book_router.post('/',status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
    new_book=book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/{books_id}')
async def get_book(books_id:int)->dict:
    for book in books:
        if book['id']==books_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found')

@book_router.patch('/{book_id}')
async def update(book_id:int,book:UpdateBook)-> dict:
    for b in books:
        if b['id']==book_id:
            b['title']=book.title
            b['author']=book.author
            b['publisher']=book.publisher
            b['page_count']=book.page_count
            b['language']=book.language
            return b
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found')

@book_router.delete('/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for i in books:
        if i['id']==book_id:
            books.remove(i)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found')