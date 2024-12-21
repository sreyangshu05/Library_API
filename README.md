# Library Management System API

_A simple Flask-based API for managing books and members in a library._

## Table of Contents

- [About the Project](#about-the-project)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)

---

## About the Project

This repository provides a **Library Management System API** built using Flask. The API supports CRUD operations for managing books and members, includes search functionality for books by title or author, and implements token-based authentication with pagination for results.

---

## Features

- CRUD operations for books and members
- Search functionality for books by title or author
- Token-based authentication for secure access
- Pagination for API results
- Built-in unit tests for both books and members

---

## Installation

Follow these steps to set up the project locally:

1. **Run the API**
   ```bash
   git clone https://github.com/sreyangshu05/Library_API.git
   cd Library_API
   python app.py

## Usage:
- The application will run on http://127.0.0.1:5000/.
- Use tools like Postman or curl to interact with the API.

## API Endpoints:
- Header: All endpoints require an Authorization header with a token.

### Books:
- POST /books
- GET /books?page=<page_number>&limit=<items_per_page>
- GET /books/search?q=<query>
- PUT /books/<book_id>
- DELETE /books/<book_id>

### Members:
- POST /members
- GET /members?page=<page_number>&limit=<items_per_page>
- PUT /members/<member_id>
- DELETE /members/<member_id>

## Testing:
- tests/test_books.py: Contains tests for book-related API endpoints.
- tests/test_members.py: Contains tests for member-related API endpoints.
