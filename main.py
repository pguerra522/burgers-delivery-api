from fastapi import FastAPI
from order_routes import order_router
from auth_routes import auth_router
from fastapi_jwt_auth import AuthJWT
from schemas import Settings
import inspect, re
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel

@AuthJWT.load_config
def get_config():
    return Settings()

app = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)