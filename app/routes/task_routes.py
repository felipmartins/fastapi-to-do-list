from fastapi import APIRouter
from app.models.task_model import Task
from app.models.db import engine
from sqlmodel import Session, select
from datetime import datetime

router = APIRouter(prefix="/tasks", tags=["Task"])


@router.get("")
async def list_tasks():
    with Session(engine) as session:
        tasks = select(Task)
        return list(session.exec(tasks))


@router.post("", status_code=201)
async def add_new_task(req_task: Task):
    with Session(engine) as session:
        session.add(req_task)
        session.commit()
        session.refresh(req_task)
        return {"created": req_task}


@router.put("/{id}", status_code=200)
async def edit_task(id: int, req_task: Task):
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


@router.delete("/{id}", status_code=200)
async def delete_task(id: int):
    with Session(engine) as session:
        query = select(Task).where(Task.id == id)
        task = session.exec(query).one()
        session.delete(task)
        session.commit()
        return {"deleted"}
