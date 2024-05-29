from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import schemas
from api import crud
from data_base.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


@router.post("/users/", summary="Создать пользователя", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Имя пользователя занято")
    return crud.create_user(db=db, user=user)


@router.get("/users/{user_id}", summary="Получить пользователя", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


@router.put("/users/{user_id}", summary="Обновить пользователя", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user


@router.delete("/users/{user_id}", summary="Удалить пользователя", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")
    return db_user
