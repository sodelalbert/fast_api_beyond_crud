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
