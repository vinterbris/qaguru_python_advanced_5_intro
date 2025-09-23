import os

import pytest
import dotenv

pytest_plugins = ['fixture_sessions']

def pytest_addoption(parser):
    parser.addoption('--env', default='dev')

@pytest.fixture(scope='session')
def env(request):
    return request.config.getoption('--env')


@pytest.fixture(scope='session', autouse=True)
def envs():
    dotenv.load_dotenv()


@pytest.fixture(scope='session')
def app_url():
    return os.getenv('APP_API_URL')
