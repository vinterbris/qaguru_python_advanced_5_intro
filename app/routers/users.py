from typing import List

from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, paginate
from starlette import status
from starlette.responses import Response

from app.database import users
from app.models.User import User, UserCreate, UserUpdate

router = APIRouter(prefix='/api/users')


@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, response: Response) -> User:
    if user_id < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid user id")
    user = users.get_user(user_id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.get('/', response_model=Page[User], status_code=status.HTTP_200_OK)
async def get_users() -> List[User]:
    return paginate(users.get_users())


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_user(user: User) -> User:
    UserCreate.model_validate(user.model_dump())
    return users.create_user(user)


@router.patch('/{user_id}', status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: User) -> User:
    if user_id < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Invalid user data')
    UserUpdate.model_validate(user.model_dump())
    return users.update_user(user_id, user)


@router.delete('/{user_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int):
    if user_id < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail='Invalid user data')
    users.delete_user(user_id)
    return {'message': "User deleted"}
