from typing import List

from fastapi import APIRouter

from api.product import crud
from api.product.schemas import UserIn, UserOut, UserInPut


router_product = APIRouter(prefix="/product", tags=["Product"])


@router_product.post("", response_model=UserOut)
def create_product(product_in: UserIn) -> UserOut:
    return crud.create_product(product_in)


@router_product.get("/{product_id}", response_model=UserOut)
def get_product_by_id(product_id: int, token: str) -> UserOut:
    crud.check_token(token)
    return crud.get_product_by_id(product_id)


@router_product.get("s", response_model=List[UserOut])
def get_products(token: str) -> List[UserOut]:
    crud.check_token(token)
    return crud.get_products()


@router_product.delete("/{product_id}")
def get_product_by_id(product_id: int, token: str) -> None:
    crud.check_token(token)
    return crud.delete_product(product_id)


@router_product.put("/{product_id}")
def put_product(product_id: int, product_in: UserInPut, token: str) -> UserOut:
    crud.check_token(token)
    return crud.put_product(product_id, product_in)
