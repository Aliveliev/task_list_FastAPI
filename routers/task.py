from fastapi import APIRouter, Depends, Path
from sqlalchemy.orm import Session
from database import get_db

from services import task as TaskService
from dto import task as TaskDTO

router = APIRouter()

@router.get('/', tags=['tasks'])
def get_all_tasks():
   return None

@router.post('/', tags=['tasks'])
async def create(data: TaskDTO.Task = None, db: Session = Depends(get_db)):
   return TaskService.create_task(data, db)

@router.get('/{id}', tags=['tasks'])
async def get(id: int = None, db: Session = Depends(get_db)):
   return TaskService.get_task(id, db)

@router.put('/{id}', tags=['tasks'])
async def update(id: int = None, data: TaskDTO.Task = None, db: Session = Depends(get_db), ):
   return TaskService.update(data, db, id)

@router.delete('/{id}', tags=['tasks'])
def delete(id: int = None, db: Session = Depends(get_db)):
   return TaskService.remove(db, id)

