import json
import os
from http import HTTPStatus

import dotenv
import pytest
import requests

from app.database.users import clear_db_users

from test_reqres_microservice.utils.path import relative_from_root


@pytest.fixture(scope='session', autouse=True)
def envs():
    dotenv.load_dotenv()


@pytest.fixture(scope='session')
def app_url():
    return os.getenv('APP_API_URL')


@pytest.fixture(scope='session', autouse=True)
def fill_test_data(app_url):
    path_to_file = 'test_reqres_microservice/data/users.json'
    # with open(os.path.abspath(path_to_file)) as f:
    with open(relative_from_root(path_to_file)) as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f'{app_url}/users', json=user)
        api_users.append(response.json())

    user_ids = [user['id'] for user in api_users]

    # clear_db_users()

    yield user_ids

    for user_id in user_ids:
        response = requests.delete(f'{app_url}/users/{user_id}')
        assert response.status_code == HTTPStatus.NO_CONTENT


