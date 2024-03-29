from typing import Union
from functools import lru_cache

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.middleware.cors import CORSMiddleware


from routers import todos, auth

import config

app = FastAPI()
app.include_router(todos.router, prefix="/todos")
app.include_router(auth.router, prefix="/auth")

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {exc}")
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@lru_cache()
def get_settings():
    return config.Settings()


@app.get("/")
def read_root(settings: config.Settings = Depends(get_settings)):
    return {"Hello": "World", "app_name": settings.app_name}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
