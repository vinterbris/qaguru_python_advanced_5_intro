import os

from sqlmodel import create_engine, SQLModel

engine = create_engine(os.getenv('DATABASE_ENGINE'), pool_size=os.getenv("DATABASE_POOL_SIZE", 10))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
