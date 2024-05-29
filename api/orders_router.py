from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from models import schemas
from api import crud
from data_base.database import get_db

router = APIRouter(
    prefix="/orders",
    tags=["orders"]
)


@router.post("/orders/", summary="Создать заказ", response_model=schemas.Order)
def create_order(order: schemas.OrderCreate, db: Session = Depends(get_db)):
    return crud.create_order(db=db, order=order)


@router.put("/orders/{order_id}", summary="Обновить заказ", response_model=schemas.Order)
def update_order(order_id: int, order: schemas.OrderUpdate, db: Session = Depends(get_db)):
    db_order = crud.update_order(db=db, order_id=order_id, order=order)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return db_order


@router.delete("/orders/{order_id}", summary="Удалить заказ", response_model=schemas.Order)
def delete_order(order_id: int, db: Session = Depends(get_db)):
    db_order = crud.delete_order(db=db, order_id=order_id)
    if db_order is None:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    return db_order
