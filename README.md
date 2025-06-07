# FastAPI Beyond CRUD

Small FastAPI tutorial to get familiar with backend developement.

<https://youtu.be/TO4aQ3ghFOc>

## Installation & Running server

Project depends on `uv` package manager.

```bash
uv sync
```

Runnign the server

```bash
uv run fastapi dev src/
```

## Debuging FastAPI in VS Code

Debugging of FAST API based application in VS Code can be implemented using `launch.json` file.
You can set breakpoints after starting debug server to, applicaiton with stop it's execution allowing
to see it's state and ispect database contents when program will reach breakpoint.

```json
"configurations": [
    {
      "name": "Python Debugger: FastAPI",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["src:app", "--reload"],
      "jinja": true
    }
  ]
```

## Testing

Test for API endpoints is implemented using `pytest` modeule.

To execute test cases run following command in project root

```bash
uv run pytest
```

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

```python
version = "v1"
app = FastAPI(version=version)
app.include_router(book_router, prefix=f"/api/{version}/books", tags=["books"])
```

## ORM - Object Relation Model

ORM is managing interaciton with database and creation of tables within it. It makes types translation and allows to exectue SQL querys on DB.

There are two most popular ORM implementatation in Python ecosystem as per today.

- SQL Model (Implemented by creator of FastAPI)
- SQL Alchemy

## PostgreSQL

Database is currently setup as Docker Copose container. Intent is to integrate it when project grows to Dockerized environemnt.

```bash
docker-compose up - d
```

### Connect to DB via Docker

```bash
docker exec -it postgres-db psql -U psql_user -d bookly_db
```

### Connect via DBeaver

To connect to the database using DBeaver, you can use the following configuration:

![DBeaver Connection Settings](dbeaver_config.png)
