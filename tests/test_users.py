from http import HTTPStatus

import pytest
import requests

from reqres_microservice.data.test_data import login
from reqres_microservice.models.User import User


@pytest.fixture()
def users(app_url):
    response = requests.get(f'{app_url}/users')
    assert response.status_code == HTTPStatus.OK
    return response.json()['items']



def test_users(app_url):
    response = requests.get(f'{app_url}/users?page=1&size=6')
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    for user in body['items']:
        User.model_validate(user)

def test_users_no_duplicates(users):
    users_ids = [(user['id']) for user in users]
    assert len(users_ids) == len(set(users_ids))


@pytest.mark.parametrize("user_id", [1, 6, 12])
def test_user(app_url, user_id):
    response = requests.get(f'{app_url}/users/{user_id}')
    assert response.status_code == HTTPStatus.OK

    user = response.json()
    User.model_validate(user)

@pytest.mark.parametrize("user_id", [13])
def test_user_invalid_data(app_url, user_id):
    response = requests.get(f'{app_url}/users/{user_id}')

    assert response.status_code == HTTPStatus.NOT_FOUND

@pytest.mark.parametrize("user_id", [-1, 0, 'sadf'])
def test_user_invalid_data(app_url, user_id):
    response = requests.get(f'{app_url}/users/{user_id}')

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_login_successful(app_url):
    response = requests.post(f'{app_url}/login',
                             json=login)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['token'] == 'QpwL5tke4Pnpja7X4'


def test_user_registration_successful(app_url):
    response = requests.post(f'{app_url}/register')

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['id'] == 4
    assert body['token'] == 'QpwL5tke4Pnpja7X4'