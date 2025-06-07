from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel


books = [
    {"id": 1, "title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
    {"id": 2, "title": "The Pragmatic Programmer", "author": "Andy Hunt", "year": 1999},
    {"id": 3, "title": "Deep Learning", "author": "Ian Goodfellow", "year": 2016},
    {"id": 4, "title": "Design Patterns", "author": "Erich Gamma", "year": 1994},
]


class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int


class BookUpdateModel(BaseModel):
    title: str
    author: str
    year: int


app = FastAPI()


@app.get("/books", status_code=status.HTTP_200_OK, response_model=list[Book])
async def get_all_books() -> list:
    return books


@app.get("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.post("/books", status_code=status.HTTP_201_CREATED, response_model=Book)
async def create_book(book_data: Book) -> dict:
    """
    # Create a new item in the catalog.

    `book_data` should contain the following fields:

    - **name**: Name of the item.
    - **price**: Price of the item in USD.
    - **description**: A short description (optional).
    """
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book


@app.patch("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def update_book(book_id: int, data: BookUpdateModel) -> dict:
    for book in books:
        if book["id"] == book_id:
            data = data.model_dump()
            book.update(data)
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.put("/books/{book_id}", status_code=status.HTTP_200_OK, response_model=Book)
async def put_book(book_id: int, book_data: Book) -> dict:
    for book in books:
        if book["id"] == book_id:
            book_data = book_data.model_dump()
            books.pop(books.index(book))
            books.append(book_data)
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")


@app.delete("/books/{book_id}", status_code=status.HTTP_200_OK)
async def delete_book(book_id: int) -> dict:
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
