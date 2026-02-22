# 🚀 Prompt-Powered Kickstart: Beginner's Toolkit for FastAPI

> **Moringa AI Capstone Project** — Built using GenAI-assisted learning.

A minimal, fully working FastAPI application demonstrating core framework features:
- A root `GET /` endpoint
- A dynamic `GET /items/{item_id}` endpoint with path and query parameters
- Auto-generated interactive API docs via Swagger UI

---

## 📋 Requirements

| Requirement | Details |
|-------------|---------|
| Python | 3.8 or higher (3.11 recommended) |
| pip | Comes bundled with Python 3.4+ |
| OS | Windows 10/11, macOS 10.15+, or Linux |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/fastapi-toolkit.git
cd fastapi-toolkit
```

### 2. Create and Activate a Virtual Environment

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

> ✅ Your terminal prompt should now show `(venv)` at the start.

### 3. Install Dependencies

```bash
pip install fastapi uvicorn
```

---

## ▶️ Running the Application

```bash
uvicorn main:app --reload
```

You should see output like:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx]
INFO:     Application startup complete.
```

> The `--reload` flag enables hot-reloading during development. Remove it in production.

---

## 🧪 Testing the API

Once the server is running, open your browser and visit:

| Endpoint | URL | Expected Response |
|----------|-----|-------------------|
| Root | http://127.0.0.1:8000/ | `{"message": "Hello, FastAPI World!"}` |
| Item by ID | http://127.0.0.1:8000/items/5 | `{"item_id": 5, "query": null}` |
| Item + query | http://127.0.0.1:8000/items/5?q=test | `{"item_id": 5, "query": "test"}` |
| **Swagger Docs** | http://127.0.0.1:8000/docs | Interactive API documentation UI |
| ReDoc | http://127.0.0.1:8000/redoc | Alternative documentation UI |

---

## 📁 Project Structure

```
fastapi-toolkit/
├── main.py        # FastAPI application
└── README.md      # This file
```

---

## 🐛 Common Issues

| Error | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'fastapi'` | Run `pip install fastapi uvicorn` and ensure venv is activated |
| `Address already in use` (port 8000) | Use a different port: `uvicorn main:app --reload --port 8001` |
| `uvicorn: command not found` | Try `python -m uvicorn main:app --reload` |
| `422 Unprocessable Entity` | Check that you're passing the correct data types (e.g., integer for `item_id`) |

---

## 📚 References

- [FastAPI Official Docs](https://fastapi.tiangolo.com)
- [Uvicorn Documentation](https://www.uvicorn.org)
- [Pydantic Documentation](https://docs.pydantic.dev)
- [FastAPI Full Course — freeCodeCamp (YouTube)](https://www.youtube.com/watch?v=0sOvCWFmrtA)

---

## 🧠 About This Project

This project was built as part of the **Moringa AI Capstone — Beginner's Toolkit with GenAI**.
Generative AI prompts were used throughout the learning and development process.
See the [Toolkit PDF](./FastAPI_Beginners_Toolkit.pdf) for the full AI Prompt Journal and documentation.

---

*Made with ❤️ and a lot of good prompts.*
