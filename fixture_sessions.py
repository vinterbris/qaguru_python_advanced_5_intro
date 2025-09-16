import pytest

from base_session import BaseSession
from config import Server

@pytest.fixture(scope='session')
def send_reqres(env):
    with BaseSession(base_url=Server(env).reqres) as session:
        yield session
