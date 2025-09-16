import dotenv


dotenv.load_dotenv()
from app.database.engine import create_db_and_tables

from fastapi import FastAPI
from fastapi_pagination import add_pagination

from app.routers import status, users
import uvicorn


app = FastAPI()
add_pagination(app)
app.include_router(status.router)
app.include_router(users.router)


if __name__ == "__main__":
    create_db_and_tables()
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)