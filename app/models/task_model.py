from enum import Enum
from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime


class Status(str, Enum):
    pending = "pending"
    doing = "doing"
    done = "done"


class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    create_date: datetime = datetime.now()
    update_date: datetime = datetime.now()
    title: str
    description: str
    status: Status = Status.pending
