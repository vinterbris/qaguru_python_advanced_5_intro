from http import HTTPStatus

import pytest
import requests

from app.models.User import User
from test_reqres_microservice.data.user_data import new_user_1, new_user_2
from tests.conftest import app_url, fill_test_data


@pytest.fixture()
def users(app_url):
    response = requests.get(f'{app_url}/users')
    assert response.status_code == HTTPStatus.OK
    return response.json()['items']

@pytest.fixture()
def create_user(app_url):
    response = requests.post(f'{app_url}/users', json=new_user_1)
    assert response.status_code == HTTPStatus.CREATED
    return response.json()['id']

@pytest.fixture()
def delete_user(app_url):
    yield

    response = requests.get(f'{app_url}/users')
    assert response.status_code == HTTPStatus.OK
    for user in response.json()['items']:
        if user['email'] == new_user_1['email']:
            response = requests.delete(f'{app_url}/users/{user["id"]}')
            assert response.status_code == HTTPStatus.NO_CONTENT


def test_create_user(app_url, delete_user):
    response = requests.post(f'{app_url}/users', json=new_user_1)

    assert response.status_code == HTTPStatus.CREATED

    body = response.json()
    assert body['email'] == new_user_1['email']
    assert body['first_name'] == new_user_1['first_name']
    assert body['last_name'] == new_user_1['last_name']
    assert body['avatar'] == new_user_1['avatar']

def test_patch_user(app_url, create_user, delete_user):
    user_id = create_user
    user_data = new_user_2
    user_data['email'] = new_user_1['email']
    response = requests.patch(f'{app_url}/users/{user_id}', json=new_user_2)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['email'] == new_user_2['email']
    assert body['first_name'] == new_user_2['first_name']
    assert body['last_name'] == new_user_2['last_name']
    assert body['avatar'] == new_user_2['avatar']

def test_delete_user(app_url, create_user):
    user_id = create_user
    response = requests.delete(f'{app_url}/users/{user_id}')
    assert response.status_code == HTTPStatus.NO_CONTENT

def test_delete_nonexistent_user(app_url):
    response = requests.delete(f'{app_url}/users/1')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_users(app_url):
    response = requests.get(f'{app_url}/users?page=1&size=6')
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    for user in body['items']:
        User.model_validate(user)

def test_users_no_duplicates(users):
    users_ids = [(user['id']) for user in users]
    assert len(users_ids) == len(set(users_ids))


def test_user(app_url, fill_test_data):
    for user_id in (fill_test_data[0], fill_test_data[-1]):
        response = requests.get(f'{app_url}/users/{user_id}')
        assert response.status_code == HTTPStatus.OK

        user = response.json()
        User.model_validate(user)

@pytest.mark.parametrize("user_id", [13])
def test_user_nonexistent(app_url, user_id):
    response = requests.get(f'{app_url}/users/{user_id}')

    assert response.status_code == HTTPStatus.NOT_FOUND

@pytest.mark.parametrize("user_id", [-1, 0, 'sadf'])
def test_user_invalid_data(app_url, user_id):
    response = requests.get(f'{app_url}/users/{user_id}')

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

# def test_login_successful(app_url):
#     response = requests.post(f'{app_url}/login',
#                              json=login)
#
#     assert response.status_code == HTTPStatus.OK
#
#     body = response.json()
#     assert body['token'] == 'QpwL5tke4Pnpja7X4'


# def test_user_registration_successful(app_url):
#     response = requests.post(f'{app_url}/register')
#
#     assert response.status_code == HTTPStatus.OK
#
#     body = response.json()
#     assert body['id'] == 4
#     assert body['token'] == 'QpwL5tke4Pnpja7X4'