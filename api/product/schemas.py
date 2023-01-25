from uuid import uuid4
from pydantic import BaseModel, Field
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


def generate_token():
    return str(uuid4())


class UserInPut(ProductBase):
    name: str = None
    price: int = None


class UserOut(ProductBase):
    id: int
    token: str = Field(default_factory=generate_token)


