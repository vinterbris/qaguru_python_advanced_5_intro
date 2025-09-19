from typing import Iterable, Type, List

from fastapi import HTTPException, status
from sqlmodel import Session, select, delete
from .engine import engine
from ..models.User import User


def get_user(user_id: int) -> User | None:
    with Session(engine) as session:
        return session.get(User, user_id)

def get_users() -> List[User]:
    with Session(engine) as session:
        statement = select(User)
        return list(session.exec(statement).all())

def create_user(user: User) -> User:
    user = User(**user.model_dump(mode="json"))
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user) #  обновление модели, чтобы в ней появился id из БД
        return user

def update_user(user_id: int, user: User) -> Type[User]:
    user = User(**user.model_dump(mode="json"))
    with Session(engine) as session:
        db_user = session.get(User, user_id)
        if not db_user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
        user_data = user.model_dump(exclude_unset=True)
        db_user.sqlmodel_update(user_data)
        session.add(db_user)
        session.commit()
        session.refresh(db_user)
        return db_user


def delete_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        session.delete(user)
        session.commit()


def clear_db_users():
    with Session(engine) as session:
        session.exec(delete(User))
        session.commit()
