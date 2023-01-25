"""
Create
Read
Update
Delete
"""

from api.product.schemas import UserIn, UserOut, UserInPut
from api.product.helper import Helper


helper = Helper()


def check_token(token):
    if token in helper.cache_by_token:
        pass
    else:
        raise ValueError(f"{token} is incorrect token")

    if len(token) == 5:
        pass
    else:
        raise ValueError("incorrect token")


def create_product(product_in: UserIn) -> UserOut:
    product = UserOut(**product_in.dict(), id=helper.next_id)
    helper.db[product.id] = product

    return product


def get_product_by_id(product_id: int) -> UserOut:
    product = helper.db[product_id]
    return product


def get_products() -> list[UserOut]:
    products = list(helper.db.values())
    return products


def put_product(product_id: int, product_in: UserInPut) -> UserOut:
    product = helper.db[product_id].dict()
    for i, j in product_in.dict().items():
        if i in product and j is not None:
            product[i] = j

    product_out = UserOut(**product)
    helper.db[product_id] = product_out

    return product_out


def delete_product(product_id: int) -> None:
    if product_id in helper.db:
        del helper.db[product_id]