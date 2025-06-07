"""
Test developed for Fast API application with CRUD operations on in-memory sotored books
"""

import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from src.books.routes import book_router
from src.books.book_data import books

# Setup FastAPI app for testing
app = FastAPI()
app.include_router(book_router, prefix="/books")

client = TestClient(app)


def reset_books():
    books.clear()
    books.extend(
        [
            {
                "id": 1,
                "title": "Clean Code",
                "author": "Robert C. Martin",
                "year": 2008,
            },
            {
                "id": 2,
                "title": "The Pragmatic Programmer",
                "author": "Andy Hunt",
                "year": 1999,
            },
            {
                "id": 3,
                "title": "Deep Learning",
                "author": "Ian Goodfellow",
                "year": 2016,
            },
            {
                "id": 4,
                "title": "Design Patterns",
                "author": "Erich Gamma",
                "year": 1994,
            },
        ]
    )


@pytest.fixture(autouse=True)
def run_around_tests():
    reset_books()
    yield
    reset_books()


def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 4


def test_get_book_success():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Clean Code"


def test_get_book_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404


def test_create_book():
    new_book = {
        "id": 5,
        "title": "Refactoring",
        "author": "Martin Fowler",
        "year": 1999,
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201
    assert response.json()["title"] == "Refactoring"
    assert len(books) == 5


def test_update_book_patch():
    update_data = {"title": "Clean Code 2", "author": "Robert C. Martin", "year": 2010}
    response = client.patch("/books/1", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == "Clean Code 2"


def test_update_book_patch_not_found():
    update_data = {"title": "Nonexistent", "author": "Nobody", "year": 2020}
    response = client.patch("/books/999", json=update_data)
    assert response.status_code == 404


def test_put_book_not_found():
    put_data = {"id": 999, "title": "Ghost Book", "author": "Ghost", "year": 2024}
    response = client.put("/books/999", json=put_data)
    assert response.status_code == 404


def test_delete_book():
    response = client.delete("/books/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted successfully"
    assert len(books) == 3


def test_delete_book_not_found():
    response = client.delete("/books/999")
    assert response.status_code == 404
