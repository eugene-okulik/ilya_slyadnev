import pytest
import requests
import allure

url = "https://api.restful-api.dev/objects"


@allure.step("Отправка запроса")
def send_request(method, url, data=None):
    with allure.step(f"Sending {method} request to {url}"):
        response = requests.request(method, url, json=data)
        response.raise_for_status()
        return response.json()


@pytest.fixture(scope="session", autouse=True)
def setup_and_teardown():
    with allure.step("Setup and Teardown"):
        print("Start testing")
        yield
        print("Testing completed")


@pytest.fixture(autouse=True)
def before_and_after_test():
    with allure.step("Before and After Test"):
        print("before test")
        yield
        print("after test")


@allure.title("Создание объекта")
@pytest.mark.parametrize("data", [
    {"name": "Apple MacBook Pro 16",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "Dell XPS 15",
     "data": {"year": 2020, "price": 1499.99, "CPU model": "Intel Core i7", "Hard disk size": "512 GB"}},
    {"name": "Lenovo ThinkPad X1",
     "data": {"year": 2021, "price": 1299.99, "CPU model": "AMD Ryzen 7", "Hard disk size": "512 GB"}}
])
def test_create_object(data):
    with allure.step("Create object"):
        response_data = send_request("POST", url, data)

        assert response_data.get("name") == data["name"]
        assert response_data.get("data") == data["data"]
        return response_data.get("id")


@allure.title("Обновление объекта")
@pytest.mark.critical
def test_update_object():
    with allure.step("Update object"):
        object_id = test_create_object({"name": "Apple MacBook Pro 16",
                                        "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                 "Hard disk size": "1 TB"}})
        data = {
            "name": "Apple MacBook Air M3",
            "data": {
                "year": 2024,
                "price": 2849.99,
                "CPU model": "Apple M3",
                "Hard disk size": "1 TB"
            }
        }
        response_data = send_request("PUT", f"{url}/{object_id}", data)

        assert response_data.get("name") == data["name"]
        assert response_data.get("data") == data["data"]


@allure.title("Частичное обновление объекта")
@pytest.mark.medium
def test_partially_update_object():
    with allure.step("Partially update object"):
        object_id = test_create_object({"name": "Apple MacBook Pro 16",
                                        "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                 "Hard disk size": "1 TB"}})
        data = {"name": "Apple MacBook PRO MAX M3"}
        response_data = send_request("PATCH", f"{url}/{object_id}", data)

        assert response_data.get("name") == data["name"]


@allure.title("Удаление объекта")
def test_delete_object():
    with allure.step("Delete object"):
        object_id = test_create_object({"name": "Apple MacBook Pro 16",
                                        "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9",
                                                 "Hard disk size": "1 TB"}})
        response_data = send_request("DELETE", f"{url}/{object_id}")
        assert response_data == {"message": f"Object with id = {object_id} has been deleted."}
