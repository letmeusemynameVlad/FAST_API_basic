import json  # builtin modules

from fastapi import FastAPI, Path, Query, Body  # external modules, i.o. which used pip install
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse, RedirectResponse
import uvicorn

from models import UserRequest, UserResponse, Family  # custom modules, our self python files
from api.product.views import router_product


app = FastAPI()
app.include_router(router_product)

"""
    :param user_id: is parameter of url (required-обязательно)
    :param user_type: is parameter of query (required-обязательно)
    :param address: is parameter of query (optional-необязательно)
    :return: simple json
"""

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

