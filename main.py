from fastapi import FastAPI,Header
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

@app.get('/')
async def read_root():
    return {"Message":"Hello World"}

@app.get('/greet')
async def name(username:Optional[str]="Prasun",age:int=25):
    return{"Message":f"Hello {username} your age is {age}"}

class Book(BaseModel):
    title:str
    author:str
    year:int

@app.post('/create_book')
async def create_book(book:Book):
    return{"title":book.title,
           "author":book.author,
           "year":book.year
           }
    

@app.get('/get_headers')
async def get_all_request_headers(
    user_agent: Optional[str] = Header(None),
    accept_encoding: Optional[str] = Header(None),
    referer: Optional[str] = Header(None),
    connection: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
    host: Optional[str] = Header(None),
):
    request_headers = {}
    request_headers["User-Agent"] = user_agent
    request_headers["Accept-Encoding"] = accept_encoding
    request_headers["Referer"] = referer
    request_headers["Accept-Language"] = accept_language
    request_headers["Connection"] = connection
    request_headers["Host"] = host

    return request_headers    