import json
import os

from fastapi import FastAPI, status, Response, HTTPException
from fastapi_pagination import Page, add_pagination, paginate

from reqres_microservice.data.user_data import user_token
from reqres_microservice.models.AppStatus import AppStatus
from reqres_microservice.models.User import User
import uvicorn


app = FastAPI()
add_pagination(app)

users: list[User]

@app.get('/api/status', status_code=status.HTTP_200_OK)
def get_status() -> AppStatus:
    return AppStatus(users=bool(users))

@app.post('/api/login')
def post_login():
    return {
        "token": user_token
    }


@app.get('/api/users/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, response: Response) -> User:
    if user_id < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid user id")
    if user_id > len(users):
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users[user_id - 1]


# req: GET /users?page=2&size=10
@app.get('/api/users', response_model=Page[User], status_code=status.HTTP_200_OK)
async def get_users() -> Page[int]:
    return paginate(users)

@app.post('/api/register', status_code=status.HTTP_200_OK)
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

@app.on_event("startup")
def load_users():
    global users

    # Берём директорию, где лежит текущий main.py
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Поднимаемся на один уровень вверх и в data/users.json
    data_path = os.path.join(base_dir, '..', 'reqres_microservice', 'data', 'users.json')

    with open(data_path) as file:
        users = json.load(file)
    for user in users:
        User.model_validate(user)
    print('Users loaded')


if __name__ == "__main__":
    uvicorn.run('app.main:app', host='localhost', port=8000, reload=True)