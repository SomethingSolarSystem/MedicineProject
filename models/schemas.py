from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    registered_on: datetime
    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None


class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    stock: int


class ProductCreate(ProductBase):
    pass


class Product(ProductBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    stock: Optional[int] = None


class OrderBase(BaseModel):
    user_id: int
    total_price: float


class OrderCreate(OrderBase):
    pass


class Order(OrderBase):
    id: int
    created_on: datetime
    user: User
    model_config = ConfigDict(from_attributes=True)


class OrderUpdate(BaseModel):
    user_id: Optional[int] = None
    total_price: Optional[float] = None
