# 🧠 AI Prompt Journal — FastAPI Beginner's Toolkit

> **Moringa AI Capstone Project**
> This document logs every GenAI prompt used during the learning and building process.
> Prompts were submitted on [ai.moringaschool.com](https://ai.moringaschool.com).

---

## How to Read This Journal

Each entry contains:
- **Prompt** — the exact question asked to the AI
- **Response Summary** — key takeaways from the AI's answer
- **Evaluation** — how helpful it was and how it influenced the project

---

## Prompt 1 — Understanding FastAPI

**Prompt used:**
```
What is FastAPI and how does it differ from Flask and Django REST Framework?
```

**AI Response Summary:**
The AI provided a structured comparison covering speed, async support, automatic documentation, and use-case suitability. It explained that FastAPI is async-first and uses Python type hints for automatic request validation — something Flask does not support natively. Django REST Framework was described as more opinionated and suited for full-stack Django projects.

**Evaluation:**
⭐⭐⭐⭐⭐ — Excellent. The comparison made it easy to justify choosing FastAPI for an API-focused capstone. The async explanation was especially clear for a beginner.

---

## Prompt 2 — Installation & Setup

**Prompt used:**
```
Give me a step-by-step guide to install FastAPI and run my first application on Windows.
```

**AI Response Summary:**
The AI walked through: creating a project folder, setting up a virtual environment, installing FastAPI and uvicorn via pip, writing a minimal `main.py`, and running `uvicorn main:app --reload`. It specifically highlighted the Windows difference in virtual environment activation (`Scripts\activate` vs `bin/activate` on macOS/Linux).

**Evaluation:**
⭐⭐⭐⭐⭐ — Very helpful. Catching the Windows activation path difference early saved debugging time. The step-by-step format matched exactly what was needed for the toolkit guide.

---

## Prompt 3 — Path & Query Parameters

**Prompt used:**
```
Explain how path parameters and query parameters work in FastAPI with a code example.
```

**AI Response Summary:**
The AI produced a working code snippet combining both parameter types in one endpoint. It explained that FastAPI automatically parses, validates, and documents them using Python type hints — making the code self-documenting. It also noted that optional query parameters are declared with a default value of `None`.

**Evaluation:**
⭐⭐⭐⭐⭐ — Very helpful. The annotated code made the concept immediately practical. This directly shaped the `/items/{item_id}` route in `main.py`.

---

## Prompt 4 — Debugging a 422 Error

**Prompt used:**
```
I got a 422 Unprocessable Entity error in FastAPI. What does this mean and how do I fix it?
```

**AI Response Summary:**
The AI explained that 422 errors occur when incoming request data fails Pydantic validation — for example, sending a string where an integer is expected. It showed how to inspect the `detail` field in the JSON error response to identify the offending field and expected type.

**Evaluation:**
⭐⭐⭐⭐ — Helpful. Understanding the error body structure saved significant debugging time. Added this to the Common Issues section of the toolkit.

---

## Prompt 5 — Development vs Production Server

**Prompt used:**
```
What is the difference between uvicorn main:app and uvicorn main:app --reload?
```

**AI Response Summary:**
The AI explained that `--reload` enables automatic hot-reloading when source files change — intended for development only. It recommended using `gunicorn` with `uvicorn` workers for production deployments, noting that `--reload` adds overhead and should never be used in a live environment.

**Evaluation:**
⭐⭐⭐⭐ — Useful context for understanding the development vs production distinction. Helped configure the `settings.reload` flag in `config.py`.

---

## Prompt 6 — Project Config & Settings

**Prompt used:**
```
How do I manage app settings and environment variables cleanly in FastAPI using pydantic?
```

**AI Response Summary:**
The AI introduced `pydantic-settings` and the `BaseSettings` class, showing how to define typed settings that can be overridden by environment variables or a `.env` file. It demonstrated creating a `settings` singleton and importing it across the app.

**Evaluation:**
⭐⭐⭐⭐⭐ — Excellent. This directly produced the `config.py` file in this project. Clean and professional approach that scales well.

---

## Prompt 7 — .gitignore for Python Projects

**Prompt used:**
```
What should I include in a .gitignore file for a Python FastAPI project?
```

**AI Response Summary:**
The AI listed all standard Python artifacts to ignore: `__pycache__`, `.pyc` files, virtual environment folders (`venv/`, `env/`), `.env` files containing secrets, IDE-specific folders (`.vscode/`, `.idea/`), and OS files like `.DS_Store`. It also suggested ignoring test coverage reports.

**Evaluation:**
⭐⭐⭐⭐⭐ — Excellent. This directly produced the `.gitignore` file in this project. Prevented accidental secret exposure.

---

## Overall Reflections

Using GenAI prompts throughout this project significantly accelerated the learning process. Key observations:

- **Specificity matters** — Vague prompts like *"tell me about FastAPI"* returned broad answers. Specific prompts like *"explain path parameters with a code example"* returned actionable, usable output.
- **Iteration works** — When a first response wasn't quite right (e.g., the 422 error prompt), a follow-up prompt with more context produced a much better answer.
- **AI as a pair programmer** — The AI felt like a patient senior developer who never gets tired of explaining things. It was most useful for debugging and boilerplate setup.
- **Verification is important** — Not every AI suggestion worked first try. Testing the code locally and cross-referencing the official FastAPI docs was essential.
