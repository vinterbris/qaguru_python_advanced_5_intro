from fastapi import APIRouter, HTTPException
from fastapi_pagination import Page, paginate
from starlette import status
from starlette.responses import Response

from app.database import users_db
from app.models.User import User

router = APIRouter(prefix='/api/users')

@router.get('/{user_id}', status_code=status.HTTP_200_OK)
async def get_user(user_id: int, response: Response) -> User:
    if user_id < 1:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Invalid user id")
    if user_id > len(users_db):
        response.status_code = status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return users_db[user_id - 1]


@router.get('/', response_model=Page[User], status_code=status.HTTP_200_OK)
async def get_users() -> Page[int]:
    return paginate(users_db)
