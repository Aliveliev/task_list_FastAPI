from models.task import Task
from sqlalchemy.orm import Session
from dto import task

from datetime import datetime

def create_task(data: task.Task, db: Session):
    task = Task(name=data.name,
                description=data.description)
    
    try:
        db.add(task)
        db.commit()
        db.refresh(task)

    except Exception as e:
        print(e)

    return task

def get_task(id: int, db: Session):
    return db.query(Task).filter(Task.id==id).first()

def update(data: task.Task, db: Session, id: int):
    task = db.query(Task).filter(Task.id==id).first()
    task.name = data.name
    task.description = data.description

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def remove(db: Session, id: int):
    task = db.query(Task).filter(Task.id==id).delete()
    db.commit()

    return task