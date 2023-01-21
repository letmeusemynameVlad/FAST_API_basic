from pydantic import BaseModel
from typing import List


class Catalog(BaseModel):
    name: str
    prod: str


class UserBase(BaseModel):
    username: str
    age: int
    address: str = None
    accessed_catalog: List[Catalog] = None


class UserIn(UserBase):
    pass


class UserInPut(UserBase):
    username: str = None
    age: int = None


class UserOut(UserBase):
    id: int

