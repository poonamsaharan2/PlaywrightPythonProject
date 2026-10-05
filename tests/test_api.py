from urllib import request

import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_get_user(api_request):
    response = api_request.get("https://jsonplaceholder.typicode.com/users/1")

    expect(response).to_be_ok()

    data = response.json()

    assert data["id"] == 1
    assert data['name'] == "Leanne Graham"


def test_create_user(api_request):
    response = api_request.post("https://jsonplaceholder.typicode.com/users",
                            data={
                                "name": "Poonam",
                                "email": "poonam@example.com"
                            }
                            )
    expect(response).to_be_ok()
    assert response.status == 201
    data = response.json()
    assert data["name"] == "Poonam"
    assert data["email"] == "poonam@example.com"
    assert "id" in data

def test_update_user(api_request):
    response = api_request.put("https://jsonplaceholder.typicode.com/users/1",
                           data={
                               "name": "Poonam Updated",
                               "email": "updated@example.com"
                           }
                           )
    expect(response).to_be_ok()
    assert response.status == 200
    data = response.json()
    assert data["name"] == "Poonam Updated"
    assert data["email"] == "updated@example.com"
    assert "id" in data


def test_delete_user(api_request):
    response = api_request.delete("https://jsonplaceholder.typicode.com/users/1")

    expect(response).to_be_ok()
    assert response.status == 200

