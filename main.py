from datetime import datetime
from fastapi import FastAPI
from sqlmodel import Session, select
from db import engine
from task_model import Task

app = FastAPI()


@app.get("/", tags=["Home"])
async def home():
    return {"message": "You're on root route, please visit /docs to see all routes or /tasks to see all tasks"}


@app.get("/tasks", tags=["Task"])
async def list_tasks():
    with Session(engine) as session:
        tasks = select(Task)
        return list(session.exec(tasks))


@app.post("/tasks", tags=["Task"], status_code=201)
async def add_new_task(req_task: Task):
    with Session(engine) as session:
        session.add(req_task)
        session.commit()
        session.refresh(req_task)
        return {"created": req_task}


@app.put("/tasks/{id}", tags=["Task"], status_code=200)
async def add_new_task(id: int, req_task: Task):
    with Session(engine) as session:
        query = select(Task).where(Task.id == id)
        task = session.exec(query).one()
        task.title = req_task.title
        task.description = req_task.description
        task.status = req_task.status
        task.update_date = datetime.now()
        session.add(task)
        session.commit()
        session.refresh(task)
        return {"edited": task}