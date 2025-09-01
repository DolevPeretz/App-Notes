# 📒 Notes App – Backend (FastAPI + PostgreSQL)

This is the backend for the **Notes App**, built using FastAPI and PostgreSQL. It handles authentication and CRUD operations for notes.

---

## 📁 Project Structure

```
app/
├── api/
│   ├── routes/               # All API route definitions
│   └── deps.py               # Shared dependencies
├── core/
│   └── security.py           # JWT token creation and validation
├── crud/
│   ├── note.py               # CRUD operations for notes
│   └── user.py               # CRUD operations for users
├── db/
│   ├── models/               # SQLAlchemy models (Note, User)
│   └── session.py            # Database session (PostgreSQL)
├── schemas/                  # Pydantic schemas for validation
├── debug.py                  # Utility to create a user for testing
├── main.py                   # FastAPI app definition and router registration
└── middleware.py             # CORS configuration
```

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the app

```bash
uvicorn app.main:app --reload
```

The app will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🛠 Create Test User

There is no registration endpoint. Instead, create a test user by running:

```bash
python app/debug.py
```

This will insert a user into your **PostgreSQL** database with default credentials (defined in `debug.py`).

---

## 🧪 Run Tests

```bash
pytest
```

Tests use `httpx.AsyncClient` to simulate login and perform CRUD operations on notes.

---

## 🧩 API Routes Summary

| Method | Endpoint    | Description             |
| ------ | ----------- | ----------------------- |
| POST   | /auth/login | Login and get JWT token |
| GET    | /notes      | Get all notes for user  |
| POST   | /notes      | Create a new note       |
| PUT    | /notes/{id} | Update a note by ID     |
| DELETE | /notes/{id} | Delete a note by ID     |

> 🔐 All `/notes` routes require Authorization header with a valid `Bearer <JWT>` token.

---

## 🧳 Stack

- **FastAPI** – Web framework
- **PostgreSQL** – Database
- **SQLAlchemy** – ORM
- **Pydantic** – Data validation
- **httpx** – Async HTTP client (used for testing)
- **Pytest** – Test runner

---

## 📌 Notes

- Authentication is done using JWT (see `core/security.py`).
- User data is created only via `debug.py`.
- CORS settings are configured via `middleware.py`.
