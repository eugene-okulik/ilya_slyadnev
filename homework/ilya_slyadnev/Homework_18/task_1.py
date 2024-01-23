import requests
import pytest


# Фикстура для создания нового объекта и возвращения его ID
@pytest.fixture
def object_id():
    response = requests.post("https://api.restful-api.dev/objects", json={
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    })

    assert response.status_code == 200
    return response.json()["id"]


def test_update_object(object_id):
    response = requests.put(f"https://api.restful-api.dev/objects/{object_id}", json={
        "name": "Apple MacBook Air M3",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "Apple M3",
            "Hard disk size": "1 TB"
        }
    })
    assert response.status_code == 200


def test_partially_update_object(object_id):
    response = requests.patch(f"https://api.restful-api.dev/objects/{object_id}", json={
        "name": "Apple MacBook PRO MAX M3"
    })
    assert response.status_code == 200


def test_delete_object(object_id):
    response = requests.delete(f"https://api.restful-api.dev/objects/{object_id}")
    assert response.status_code == 200

    assert response.json() == {"message": f"Object with id = {object_id} has been deleted."}
