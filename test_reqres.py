from http import HTTPStatus

import requests

from data.test_data import login

# url = 'https://reqres.in/api'
url = 'http://0.0.0.0:8000/api'
headers = {'x-api-key': 'reqres-free-v1'}


def test_login_successful():
    response = requests.post(f'{url}/login',
                             json=login, headers=headers)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['token'] == 'QpwL5tke4Pnpja7X4'


def test_delete_user_check_empty_response():
    response = requests.delete(f'{url}/users/4', headers=headers)

    assert response.status_code == HTTPStatus.NO_CONTENT

    assert response.text == ''


def test_single_user_not_found_returns_empty_body():
    response = requests.get(f'{url}/users/23', headers=headers)

    assert response.status_code == HTTPStatus.NOT_FOUND

    body = response.json()
    assert body == {}


def test_user_registration_successful():
    response = requests.post(f'{url}/register', headers=headers)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['id'] == 4
    assert body['token'] == 'QpwL5tke4Pnpja7X4'


def test_microservice_get_user_successful():
    response = requests.get(f'{url}/users/2', headers=headers)

    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body == {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
            "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
        }
    }
