from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from models import schemas
from api import crud
from data_base.database import get_db

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


@router.get("/products/", summary="Получить медицинский продукт", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products


@router.post("/products/", summary="Создать медицинский продукт", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@router.put("/products/{product_id}", summary="Обновить медицинский продукт", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud.update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return db_product


@router.delete("/products/{product_id}", summary="Удалить медицинский продукт", response_model=schemas.Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Продукт не найден")
    return db_product
