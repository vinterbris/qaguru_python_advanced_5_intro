from http import HTTPStatus

import pytest
import requests

def test_status(app_url):
    response = requests.get(f'{app_url}/status')
    assert response.status_code == HTTPStatus.OK

    body = response.json()
    assert body['database'] is True