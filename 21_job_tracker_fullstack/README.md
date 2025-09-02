# 21_job_tracker_fullstack — FastAPI + Postgres (Docker)

Production-style Job Application Tracker.
- FastAPI API with JWT auth
- Postgres via Docker Compose (or SQLite locally)
- Jobs CRUD (title, company, status, etc.)
- Minimal HTML/JS UI for quick testing

## Run with Docker
1) Copy backend\.env.example to backend\.env and set JWT_SECRET.
2) docker compose up --build
API docs: http://localhost:8000/docs

## Run locally (no Docker)
1) cd backend
2) python -m venv .venv
3) .\.venv\Scripts\activate
4) pip install -r requirements.txt
5) copy .env.example .env
6) uvicorn app.main:app --reload
