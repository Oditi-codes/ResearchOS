# Backend Notes

> Notes covering backend concepts learned during the ResearchOS project.
>
> Current stack:
> - FastAPI
> - Python

---

# FastAPI

---

## What is FastAPI?

FastAPI is a modern Python framework used for building APIs.

It provides:

- HTTP request handling
- REST API creation
- JSON responses
- Automatic documentation
- Validation

In ResearchOS, FastAPI acts as the backend API layer.

---

# API

---

## What is an API?

API (Application Programming Interface) allows different software components to communicate.

In ResearchOS:
``` md
Next.js Frontend

communicates with

FastAPI Backend
```
through APIs.

---

# REST API

---

## What is REST?

REST (Representational State Transfer) is an architectural style for designing web APIs.

REST APIs use:

- HTTP methods
- URLs
- JSON responses

Example: `GET /`

---

# HTTP

---

## What is HTTP?

HTTP (HyperText Transfer Protocol) is the communication protocol used between clients and servers.

Example:
- Browser
- HTTP Request
- Server
- HTTP Response


---

# HTTP GET Request

---

## What is GET?

GET is an HTTP method used to retrieve data.

Example:

```python
@app.get("/")
```
creates a GET endpoint.

---
# FastAPI Application
---

## Creating FastAPI Application

Example:
```python
app = FastAPI()
```
creates the backend application instance.

Routes and middleware are attached to this object.

---
# Route
---

## What is a Route?

A route maps an HTTP request to a Python function.

Example:
```python
@app.get("/")
def root():
```

Meaning:
```md
GET /

executes

root()
```

---
# JSON Response
---

## What is JSON?

JSON (JavaScript Object Notation) is a lightweight data exchange format.

Example:

Python:
```python
{
 "message":"Hello"
}
```
becomes:

JSON:
```json
{
 "message":"Hello"
}
```
FastAPI automatically converts Python dictionaries into JSON responses.

---
# Sync vs Async Endpoints
---

## Synchronous Endpoint

Example:
```python
@app.get("/")
def root():
```
Executes normally.

Suitable for:
- Simple operations
- CPU calculations

## Asynchronous Endpoint

Example:
```py
@app.get("/")
async def root():
```

Suitable for:
- Database calls
- API calls
- File operations

ResearchOS will use async endpoints for operations involving:
- LLM APIs
- Vector databases
- External services


--- 
# Middleware
---

## What is Middleware?

Middleware is a layer that processes requests and responses before they reach route handlers.

Flow:
```md
Request

↓

Middleware

↓

Route

↓

Response
```

Examples:
- CORS
- Authentication
- Logging
- Rate limiting
--- 
# CORS
---

## What is CORS?

CORS (Cross-Origin Resource Sharing) is a browser security mechanism that controls which origins can access a backend API.

Example:

Frontend: `localhost:3000`
Backend: `localhost:8000`

These are different origins because the ports differ.

## Why do we need CORS?

Browsers block requests between different origins unless the backend explicitly allows them.

FastAPI uses CORS middleware to allow trusted frontend origins.

---
# CORS Configuration

Example:
```py
app.add_middleware(
    CORSMiddleware
)
```
CORS is configured at application level because it affects all routes.

--- 
# Backend Architecture

Current ResearchOS architecture:
```md
Browser

↓

Next.js Frontend

↓

HTTP Request

↓

FastAPI Backend

↓

JSON Response
```
Future:
```md
FastAPI

↓

PostgreSQL

↓

ChromaDB

↓

LLM Services
```
---
# Last Updated
---
Day 02