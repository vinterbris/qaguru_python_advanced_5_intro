import dotenv

from app.database import create_db_and_tables

dotenv.load_dotenv()

import json
import os

from fastapi import FastAPI
from fastapi import status as fa_status
from fastapi_pagination import add_pagination

from routers import status, users
from reqres_microservice.data.user_data import user_token
from app.models.User import User
from database import users_db
import uvicorn


app = FastAPI()
add_pagination(app)
app.include_router(status.router)
app.include_router(users.router)

@app.post('/api/login')
def post_login():
    return {
        "token": user_token
    }


@app.post('/api/register', status_code=fa_status.HTTP_200_OK)
def post_user():
    return {
        "id": 4,
        "token": user_token
    }


# @app.delete('/api/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(user_id: int, response: Response):
#     for user in users_list:
#         if user['id'] == user_id:
#             return ''
#     response.status_code = status.HTTP_404_NOT_FOUND
#     return ''

# @app.on_event("startup")
# def load_users():
#     # Берём директорию, где лежит текущий main.py
#     base_dir = os.path.dirname(os.path.abspath(__file__))
#     # Поднимаемся на один уровень вверх и в data/users.json
#     data_path = os.path.join(base_dir, '..', 'reqres_microservice', 'data', 'users.json')
#
#     with open(data_path) as file:
#         users_db.extend(json.load(file))
#     for user in users_db:
#         User.model_validate(user)
#     print('Users loaded')


if __name__ == "__main__":
    create_db_and_tables()
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)