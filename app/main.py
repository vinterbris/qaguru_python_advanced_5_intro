import json

from fastapi import FastAPI, status, Response, HTTPException
from fastapi_pagination import Page, add_pagination, paginate

from data.user_data import user_token, users_list
from models.AppStatus import AppStatus
from models.User import User
import uvicorn

app = FastAPI()

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


@app.delete('/api/users/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, response: Response):
    for user in users_list:
        if user['id'] == user_id:
            return ''
    response.status_code = status.HTTP_404_NOT_FOUND
    return ''

add_pagination(app)

if __name__ == "__main__":
    with open('../data/users.json') as file:
        users = json.load(file)

    for user in users:
        User.model_validate(user)

    print('Users loaded')

    uvicorn.run(app, host='localhost', port=8000)
