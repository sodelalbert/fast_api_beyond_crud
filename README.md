# FastAPI Beyond CRUD

Small FastAPI tutorial to get familiar with backend developement.

<https://youtu.be/TO4aQ3ghFOc>

## Installation

## CURL

GET Method Example

```bash
curl -X GET http://127.0.0.1:8000/books | jq
```

POST Method Example

```bash
curl -X POST http://127.0.0.1:8000/books \
 -H "Content-Type: application/json" \
 -d '{"id": 22, "title": "Quo Vadis", "author": "Henryk Sienkiewicz", "year": 2008}' | jq
```

## FastAPI Roters

FastAPI routers help you organize your application by grouping related endpoints into separate modules. This makes your codebase more modular and maintainable.

### Example: Creating and Including a Router

First, create a router in a separate file (e.g., `routers/books.py`):

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
def read_books():
    return [{"id": 1, "title": "1984"}]
```

Then, include the router in your main application (`main.py`):

```python
from fastapi import FastAPI
from routers import books

app = FastAPI()
app.include_router(books.router)
```

### Benefits

- **Separation of concerns:** Keep related routes together.
- **Reusability:** Easily share routers across projects.
- **Scalability:** Simplifies adding new features as your API grows.

For more details, see the [FastAPI documentation on routers](https://fastapi.tiangolo.com/tutorial/bigger-applications/).