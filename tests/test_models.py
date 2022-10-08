from app.models.task_model import Task
from app.models.db import engine
from sqlmodel import Session, select


def test_task_model():
    new_task = Task(title='test_title', description='test_description')
    assert hasattr(new_task, 'id')
    assert hasattr(new_task, 'create_date')
    assert hasattr(new_task, 'update_date')
    assert hasattr(new_task, 'status')
    assert not hasattr(new_task, 'prazo_de_entrega')


mocked_task = Task(id=100000000000000000, title="string", description= "string")

def test_select_from_task_table():
    with Session(engine) as session:
        tasks = list(session.exec(select(Task)))
        assert type(tasks) == list


def test_task_insertion_to_table():
    with Session(engine) as session:
        before_insertion_tasks = len(list(session.exec(select(Task))))
        session.add(mocked_task)
        session.commit()
        session.refresh(mocked_task)
        after_insertion_tasks = len(list(session.exec(select(Task))))

        assert after_insertion_tasks == before_insertion_tasks + 1


def test_update_task_from_table():
    with Session(engine) as session:
        before_insertion_tasks = len(list(session.exec(select(Task))))
        task = session.exec(select(Task).where(Task.id == 100000000000000000)).one()
        task.title = "edited_test_title"
        task.description = "edited_test_title"
        session.add(task)
        session.commit()
        session.refresh(task)
        after_insertion_tasks = len(list(session.exec(select(Task))))
        
        assert after_insertion_tasks == before_insertion_tasks


def test_delete_task_from_table():
    with Session(engine) as session:
        before_insertion_tasks = len(list(session.exec(select(Task))))
        task = session.exec(select(Task).where(Task.id == 100000000000000000)).one()
        session.delete(task)
        session.commit()
        after_insertion_tasks = len(list(session.exec(select(Task))))
        
        assert after_insertion_tasks == before_insertion_tasks - 1