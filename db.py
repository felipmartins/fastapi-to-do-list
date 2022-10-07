from sqlmodel import SQLModel, create_engine, Session
from task_model import Task

sqlite_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

def test_add_task():
    with Session(engine) as session:
        task = Task(title='Minha task', description="Minha description")
        session.add(task)
        session.commit()
