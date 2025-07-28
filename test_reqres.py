import requests

# url = 'https://reqres.in/api'
url = 'http://0.0.0.0:8000/api'
headers = {'x-api-key': 'reqres-free-v1'}


def test_login_successful():
    response = requests.post(f'{url}/login',
                             json={"email": "eve.holt@reqres.in", "password": "cityslicka"}, headers=headers)

    assert response.status_code == 200

    body = response.json()
    assert body['token'] == 'QpwL5tke4Pnpja7X4'



def test_delete_user_check_empty_response():
    response = requests.delete(f'{url}/users/4', headers=headers)

    assert response.status_code == 204

    print(response.text)
    assert response.text == ''


def test_single_user_not_found_returns_empty_body():
    response = requests.get(f'{url}/users/23', headers=headers)

    assert response.status_code == 404

    body = response.json()
    assert body == {}


def test_user_registration_successful():
    response = requests.post(f'{url}/register', headers=headers)

    assert  response.status_code == 200

    body = response.json()
    assert body['id'] == 4
    assert body['token'] == 'QpwL5tke4Pnpja7X4'