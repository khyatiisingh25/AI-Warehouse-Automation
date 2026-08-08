# Project Setup

## Clone Repository

```bash
git clone https://github.com/khyatiisingh25/AI-Warehouse-Automation.git
```

---

## Open Project

```bash
cd AI-Warehouse-Automation
```

---

## Create Personal Branch

Example:

```bash
git checkout -b feature/backend-ayush
git push -u origin feature/backend-ayush
```

---

## Pull Latest Changes

```bash
git pull origin main
```

---

## Backend Setup

```bash
cd backend

python3.11 -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn app.main:app --reload
```

Swagger:

http://127.0.0.1:8000/docs

---

## Rules

Never push directly to main.

Create Pull Requests.

Commit frequently.

Keep commits meaningful.