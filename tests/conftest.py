import json
import os
from http import HTTPStatus

import dotenv
import pytest
import requests

from test_reqres_microservice.utils.path import relative_from_root

dotenv.load_dotenv()
from app.database.users import clear_db_users

@pytest.fixture(scope='session')
def app_url():
    return os.getenv('APP_API_URL')

@pytest.fixture(scope='session', autouse=True)
def prepare_test_data(app_url):
    clear_db_users()

    path_to_file = 'test_reqres_microservice/data/users.json'
    with open(relative_from_root(path_to_file)) as f:
        test_data_users = json.load(f)
    api_users = []
    for user in test_data_users:
        response = requests.post(f'{app_url}/users', json=user)
        api_users.append(response.json())

    user_ids = [user['id'] for user in api_users]

    yield user_ids

    clear_db_users()


