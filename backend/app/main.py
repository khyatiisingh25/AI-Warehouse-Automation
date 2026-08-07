from fastapi import FastAPI
from sqlalchemy import text

from app.api.router import api_router
from app.config import settings
from app.database import engine

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Backend API for the AI-Based Warehouse Automation & Digital Twin System",
)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)


@app.get("/")
def root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME} 🚀"
    }


@app.get("/health")
def health_check():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))
    return {
        "status": "healthy",
        "database": "connected"
    }