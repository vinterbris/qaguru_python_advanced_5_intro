from contextlib import asynccontextmanager

import dotenv

dotenv.load_dotenv()
from app.database.engine import create_db_and_tables
from app.routers import status, users

from fastapi import FastAPI
from fastapi_pagination import add_pagination

import uvicorn

@asynccontextmanager
async def lifespan(_: FastAPI):
    create_db_and_tables()

    yield

app = FastAPI(lifespan=lifespan)
add_pagination(app)
app.include_router(status.router)
app.include_router(users.router)


if __name__ == "__main__":
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)