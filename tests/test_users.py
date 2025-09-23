from http import HTTPStatus

import pytest
import requests

from app.models.User import User
from test_reqres_microservice.data.user_data import new_user_1, new_user_2, new_user_0
from tests.conftest import app_url, prepare_test_data


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


def test_create_user(send_reqres, delete_user):
    user = new_user_1
    response = send_reqres.post('/users', json=new_user_1)

    assert response.status_code == HTTPStatus.CREATED

    body = response.json()
    assert body['email'] == user['email']
    assert body['first_name'] == user['first_name']
    assert body['last_name'] == user['last_name']
    assert body['avatar'] == user['avatar']

def test_patch_user(send_reqres, create_user, delete_user):
    user_id = create_user
    user_data = new_user_2
    user_data['email'] = new_user_1['email']
    response = send_reqres.patch(f'/users/{user_id}', json=new_user_2)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['email'] == new_user_2['email']
    assert body['first_name'] == new_user_2['first_name']
    assert body['last_name'] == new_user_2['last_name']
    assert body['avatar'] == new_user_2['avatar']

def test_delete_user(send_reqres, create_user):
    user_id = create_user
    response = send_reqres.delete(f'/users/{user_id}')
    assert response.status_code == HTTPStatus.NO_CONTENT

def test_delete_nonexistent_user(send_reqres):
    response = send_reqres.delete('/users/50000')
    assert response.status_code == HTTPStatus.NOT_FOUND


def test_users(send_reqres):
    response = send_reqres.get('/users?page=1&size=6')
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    for user in body['items']:
        User.model_validate(user)

def test_get_users_no_duplicates(users):
    users_ids = [(user['id']) for user in users]
    assert len(users_ids) == len(set(users_ids))


def test_get_user(send_reqres, prepare_test_data):
    for user_id in (prepare_test_data[0], prepare_test_data[-1]):
        response = send_reqres.get(f'/users/{user_id}')
        assert response.status_code == HTTPStatus.OK

        user = response.json()
        User.model_validate(user)

@pytest.mark.parametrize("user_id", [99999])
def test_get_nonexistent_user(send_reqres, user_id):
    response = send_reqres.get(f'/users/{user_id}')

    assert response.status_code == HTTPStatus.NOT_FOUND

@pytest.mark.parametrize("user_id", [-1, 0, 'sadf'])
def test_user_invalid_data(send_reqres, user_id):
    response = send_reqres.get(f'/users/{user_id}')

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
