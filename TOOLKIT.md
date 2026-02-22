# 🛠️ FastAPI Beginner's Toolkit — Master Index

> **Moringa AI Capstone Project**
> *Prompt-Powered Kickstart: Building a Beginner's Toolkit for FastAPI*

---

## 📂 Project Structure

```
fastapi-toolkit/
│
├── main.py              # ⚡ FastAPI application — entry point
├── config.py            # ⚙️  App settings & environment config
├── requirements.txt     # 📦 Python dependencies
├── __init__.py          # 🐍 Package initializer
├── .gitignore           # 🚫 Files excluded from Git
│
├── README.md            # 📖 Setup & run instructions
├── TOOLKIT.md           # 📋 This file — master index
├── AI_PROMPTS.md        # 🧠 AI prompt journal & reflections
└── CHECKLIST.md         # ✅ Submission checklist
```

---

## 📖 File Guide

### `main.py` — The Application
The core FastAPI app. Contains three routes:
| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Returns a welcome message |
| `/items/{item_id}` | GET | Returns item by ID + optional query param |
| `/health` | GET | Health check — confirms API is running |

Run it with:
```bash
uvicorn main:app --reload
```

---

### `config.py` — Configuration
Manages all app settings using Pydantic's `BaseSettings`.
Settings can be overridden via a `.env` file or environment variables.

Key settings:
| Setting | Default | Description |
|---------|---------|-------------|
| `app_name` | FastAPI Beginner's Toolkit | Application title |
| `host` | 127.0.0.1 | Server host |
| `port` | 8000 | Server port |
| `debug` | True | Debug mode |
| `reload` | True | Hot reload (dev only) |

---

### `requirements.txt` — Dependencies
Install all dependencies with:
```bash
pip install -r requirements.txt
```

| Package | Purpose |
|---------|---------|
| `fastapi` | The web framework |
| `uvicorn` | ASGI server to run the app |
| `pydantic` | Data validation via type hints |
| `python-dotenv` | Load `.env` file into environment |
| `httpx` | HTTP client (useful for testing) |

---

### `__init__.py` — Package File
Marks the project as a Python package and stores metadata like version and author.

---

### `.gitignore` — Git Exclusions
Prevents sensitive and unnecessary files from being pushed to GitHub including:
- Virtual environment folders (`venv/`, `env/`)
- `.env` files containing secrets
- Python cache files (`__pycache__/`, `*.pyc`)
- IDE config folders (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)

---

### `AI_PROMPTS.md` — Prompt Journal
Full log of all 7 GenAI prompts used during this project, including:
- The exact prompt submitted
- Summary of the AI's response
- Personal evaluation and star rating
- Overall reflections on using AI as a learning tool

---

### `CHECKLIST.md` — Submission Checklist
A step-by-step checklist covering:
- GitHub repo setup
- File completeness
- Local testing
- PDF toolkit verification
- Final submission steps

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/fastapi-toolkit.git
cd fastapi-toolkit

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
uvicorn main:app --reload

# 5. Open in browser
# http://127.0.0.1:8000/docs
```

---

## 🔗 Useful Links

| Resource | URL |
|----------|-----|
| FastAPI Docs | https://fastapi.tiangolo.com |
| Uvicorn Docs | https://www.uvicorn.org |
| Pydantic Docs | https://docs.pydantic.dev |
| Swagger UI | http://127.0.0.1:8000/docs *(when running locally)* |

---

*Built with ❤️ and a lot of good prompts — Moringa AI Capstone 2026*
