from fastapi import FastAPI
from db.main import init_db
from src.books.routes import book_router
from contextlib import asynccontextmanager


version = "v1"


@asynccontextmanager
async def life_span(app: FastAPI):
    """
    Application lifespan context manager.
    This can be used to initialize resources or perform setup tasks.
    """
    print(f"Starting application...")
    await init_db()
    yield
    print(f"Stopping application...")


app = FastAPI(
    version=version,
    title="Book Catalog API",
    description="API for managing a book catalog",
    contact={"name": "Book Catalog Team", "email": "sodelalbert@gmail.com"},
    lifespan=life_span,
)

app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
