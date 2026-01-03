# Advanced API Project – Task 1

## Book API Endpoints

### Public Endpoints
- GET /api/books/
- GET /api/books/<id>/

### Authenticated Endpoints
- POST /api/books/create/
- PUT /api/books/<id>/update/
- DELETE /api/books/<id>/delete/

## Permissions
- Read access is public
- Create, update, and delete require authentication

## Technologies Used
- Django
- Django REST Framework
- SQLite

## Features
- Generic class-based views
- Serializer validation
- Nested relationships
- Permission enforcement


## Book API – Advanced Features

### Filtering
Filter books by title, publication year, or author ID:


## Running Unit Tests

All API endpoints are tested for CRUD, filtering, searching, ordering, and permissions.

Run tests using:

```bash
python manage.py test api
