from locust import task, HttpUser, between
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


class APIUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_posts(self):
        self.client.get("/posts")

    @task
    def get_single_post(self):
        self.client.get("/posts/1")

    @task
    def create_post(self):
        data = {"title": "foo", "body": "bar", "userId": 1}
        self.client.post("/posts", json=data)

    @task
    def update_post(self):
        data = {"id": 1, "title": "foo", "body": "bar", "userId": 1}
        self.client.put("/posts/1", json=data)

    @task
    def delete_post(self):
        self.client.delete("/posts/1")
