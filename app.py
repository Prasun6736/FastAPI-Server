from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()




books = [
    {
        "id": 1,
        "title": "Think Python",
        "author": "Allen B. Downey",
        "publisher": "O'Reilly Media",
        "published_date": "2021-01-01",
        "page_count": 1234,
        "language": "English",
    },
    {
        "id": 2,
        "title": "Django By Example",
        "author": "Antonio Mele",
        "publisher": "Packt Publishing Ltd",
        "published_date": "2022-01-19",
        "page_count": 1023,
        "language": "English",
    },
    {
        "id": 3,
        "title": "The web socket handbook",
        "author": "Alex Diaconu",
        "publisher": "Xinyu Wang",
        "published_date": "2021-01-01",
        "page_count": 3677,
        "language": "English",
    },
    {
        "id": 4,
        "title": "Head first Javascript",
        "author": "Hellen Smith",
        "publisher": "Oreilly Media",
        "published_date": "2021-01-01",
        "page_count": 540,
        "language": "English",
    },
    {
        "id": 5,
        "title": "Algorithms and Data Structures In Python",
        "author": "Kent Lee",
        "publisher": "Springer, Inc",
        "published_date": "2021-01-01",
        "page_count": 9282,
        "language": "English",
    },
    {
        "id": 6,
        "title": "Head First HTML5 Programming",
        "author": "Eric T Freeman",
        "publisher": "O'Reilly Media",
        "published_date": "2011-21-01",
        "page_count": 3006,
        "language": "English",
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date:str 
    page_count: int
    language: str

class UpdateBook(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

@app.get('/books',response_model=List[Book])
async def get_books():
    return books

@app.post('/books',status_code=status.HTTP_201_CREATED)
async def create_book(book_data:Book)->dict:
    new_book=book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{books_id}')
async def get_book(books_id:int)->dict:
    for book in books:
        if book['id']==books_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found')

@app.patch('/books/{book_id}')
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

@app.delete('/books/{book_id}',status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id:int):
    for i in books:
        if i['id']==book_id:
            books.remove(i)

            return {}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Book not found')