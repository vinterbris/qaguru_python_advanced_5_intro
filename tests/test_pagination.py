from http import HTTPStatus

import pytest
import requests


@pytest.mark.parametrize('size', [1, 6, 12])
def test_amount_of_expected_objects(app_url, size):
    response = requests.get(f'{app_url}/users?page=1&size={size}')
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert size == len(body['items'])


@pytest.mark.parametrize('size, page_count', [(1, 12), (6, 2), (12, 1)])
def test_pages_count(app_url, size, page_count):
    response = requests.get(f'{app_url}/users?page=1&size={size}')
    print(response)
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert page_count == body['pages']


def test_data_on_pages(app_url):
    response_p1 = requests.get(f'{app_url}/users?page=1&size=6')
    response_p2 = requests.get(f'{app_url}/users?page=2&size=6')
    assert response_p1.status_code == HTTPStatus.OK
    assert response_p2.status_code == HTTPStatus.OK

    print(response_p1.json())

    body_p1 = response_p1.json()
    body_p2 = response_p2.json()
    for user in body_p1['items']:
        assert user not in body_p2['items']
