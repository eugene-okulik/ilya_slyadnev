import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.mark.parametrize("endpoint, expected_status", [
    ("/posts", 200),
    ("/posts/1000", 404)
])
def test_get_requests(endpoint, expected_status):
    response = requests.get(BASE_URL + endpoint)

    assert response.status_code == expected_status


@pytest.mark.parametrize("endpoint, data, expected_status", [
    ("/posts", {"title": "foo", "body": "bar", "userId": 1}, 201),
    ("/posts1", {"title": "foo", "body": "bar", "userId": 1}, 404)
])
def test_post_requests(endpoint, data, expected_status):
    response = requests.post(BASE_URL + endpoint, json=data)

    assert response.status_code == expected_status


@pytest.mark.parametrize("id, data, expected_status", [
    (1, {"id": 1, "title": "foo", "body": "bar", "userId": 1}, 200),
    (1001, {"id": 1, "title": "foo", "body": "bar", "userId": 1}, 500)
])
def test_put_requests(id, data, expected_status):
    response = requests.put(BASE_URL + f"/posts/{id}", json=data)

    assert response.status_code == expected_status


@pytest.mark.parametrize("id, expected_status", [
    (1, 200),
    ("", 404)
])
def test_delete_requests(id, expected_status):
    response = requests.delete(BASE_URL + f"/posts/{id}")

    assert response.status_code == expected_status
