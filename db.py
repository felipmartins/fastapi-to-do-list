from sqlmodel import SQLModel, create_engine, Session
import task_model

sqlite_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_name}"

engine = create_engine(sqlite_url, echo=True)

SQLModel.metadata.create_all(engine)

