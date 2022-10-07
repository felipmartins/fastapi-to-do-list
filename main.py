from fastapi import FastAPI
from db import engine

app = FastAPI()


@app.get("/", tags=["Home"])
async def home():
    return {"message": "You're on root route, please visit /docs to see all routes or /tasks to see all tasks"}


@app.get("/tasks", tags=["Home"])
async def list_tasks():
    return {"message": "All tasks"}