from pydantic import BaseModel
from typing import List


class Dimension(BaseModel):
    length: float
    width: float
    height: float


class ProductBase(BaseModel):
    name: str
    price: int
    tags: List[str] = None
    dimensions: Dimension = None


class UserIn(ProductBase):
    pass


class UserInPut(ProductBase):
    name: str = None
    price: int = None


class UserOut(ProductBase):
    id: int


