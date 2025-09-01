# Notes Frontend (Vite + React + TypeScript)

This is the frontend for the Notes App, built with Vite, React, TypeScript
CSS. It connects to a FastAPI backend and PostgreSQL database for user-authenticated note management.

## 🛠 Tech Stack

- [React](https://react.dev/)
- [TypeScript](https://www.typescriptlang.org/)
- [Vite](https://vitejs.dev/)
- React Router
- Custom Protected Routes
- Token-based Authentication (JWT)

## 📁 Project Structure

```
src/
├── components/          # Reusable UI components (Forms, Notes list, etc.)
├── pages/               # Route-level views (Login, Notes)
├── schemas/             # Zod validation schemas
├── services/            # API service calls (Auth, Notes)
├── utils/               # Utility functions (e.g., token storage)
├── App.tsx              # Main app component
├── main.tsx             # App entry point
```

## ⚙️ Features

- 🔐 Login via email & password
- ✅ Protected routes with automatic redirects
- 📝 Add, edit, delete notes list
- 🌐 Backend integration using RESTful APIs
- 💾 Token storage in localStorage

## 🧪 Running Locally

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

### 📦 Environment Variables

Ensure `.env` file contains the following:

```
VITE_API_BASE_URL=http://localhost:5173/
```

## 📸 UI Screenshots

- **Login Page**: Authenticates users with credentials.
- **Notes Page**: Lists, adds, edits and deletes notes.

## 🗂 Pages

- `/login`: Login page
- `/notes`: Main notes dashboard
