from sqlmodel import SQLModel, create_engine, Session
from app.models.task_model import Task

sqlite_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)
