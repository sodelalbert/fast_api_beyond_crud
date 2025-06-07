from fastapi import FastAPI
from src.books.routes import book_router

version = "v1"

app = FastAPI(
    version=version,
    title="Book Catalog API",
    description="API for managing a book catalog",
    contact={"name": "Book Catalog Team", "email": ""},
)
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
