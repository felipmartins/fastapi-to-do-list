from fastapi import FastAPI
from sqlmodel import Session, select
from db import engine
from task_model import Task

app = FastAPI()


@app.get("/", tags=["Home"])
async def home():
    return {"message": "You're on root route, please visit /docs to see all routes or /tasks to see all tasks"}


@app.get("/tasks", tags=["Home"])
async def list_tasks():
    with Session(engine) as session:
        tasks = select(Task)
        return list(session.exec(tasks))