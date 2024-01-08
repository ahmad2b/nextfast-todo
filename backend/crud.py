from sqlalchemy.orm import Session
import models, schemas


def create_todo(db: Session, todo: schemas.TodoRequest):
    db_todo = models.ToDo(
        title=todo.title, completed=todo.completed, description=todo.description
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo


def read_todos(db: Session, completed: bool):
    if completed is False:
        return db.query(models.ToDo).all()
    else:
        return db.query(models.ToDo).filter(models.ToDo.completed == completed).all()


def read_todo(db: Session, todo_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()


def update_todo(db: Session, todo_id: int, todo: schemas.TodoRequest):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == todo_id).update(
        {
            models.ToDo.title: todo.title,
            models.ToDo.description: todo.description,
            models.ToDo.completed: todo.completed,
        }
    )
    db.commit()
    db.refresh(db_todo)
    return db_todo


def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(models.ToDo).filter(models.ToDo.id == todo_id).first()
    if db_todo is None:
        return None
    db.query(models.ToDo).filter(models.ToDo.id == todo_id).delete()
    db.commit()
    return True
