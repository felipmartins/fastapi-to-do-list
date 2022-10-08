from datetime import datetime
from fastapi import FastAPI
from sqlmodel import Session, select
from app.models.db import engine
from app.models.task_model import Task
from app.routes import task_routes


app = FastAPI()

app.include_router(task_routes.router)


@app.get("/", tags=["Home"], status_code=200)
async def home():
    return {
        "message": "You're on root route, please visit /docs to see all routes or /tasks to see all tasks"
    }
