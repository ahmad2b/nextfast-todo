from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, status
import schemas, crud
from db import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post(
    "", response_model=schemas.TodoResponse, status_code=status.HTTP_201_CREATED
)
def create_todo(todo: schemas.TodoRequest, db: Session = Depends(get_db)):
    db_todo = crud.create_todo(db, todo)
    return db_todo


@router.get("", response_model=List[schemas.TodoResponse])
def read_todos(completed: bool = False, db: Session = Depends(get_db)):
    db_todos = crud.read_todos(db, completed)
    return db_todos


@router.get("/{todo_id}", response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.read_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.put("/{todo_id}", response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo: schemas.TodoRequest, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo


@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return True
