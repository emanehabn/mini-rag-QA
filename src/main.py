
from fastapi import FastAPI
from routes import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from contextlib import asynccontextmanager

from helpers.config import get_settings


app = FastAPI()

# python 3.10 modification
@asynccontextmanager
async def lifespan():
    settings = get_settings()

    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)

    app.db_client = app.mongo_conn(settings.MONGODB_DATABASE)

    yield

    app.mongo_conn.close()

"""@app.on_event("startup")
async def startup_db_client():
    settings = get_settings()

    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)

    app.db_client = app.mongo_conn(settings.MONGODB_DATABASE)

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongo_conn.close()
"""

app.include_router(base.base_router)
app.include_router(data.data_router)


