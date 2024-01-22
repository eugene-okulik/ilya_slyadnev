import requests

url = "https://api.restful-api.dev/objects"


def send_request(method, url, data=None):
    try:
        response = requests.request(method, url, json=data)
        response.raise_for_status()
        return response
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        raise


def create_object():
    data = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = send_request("POST", url, data)
    response_data = response.json()
    assert response_data.get("name") == data["name"]
    assert response_data.get("data") == data["data"]
    return response_data.get("id")


def update_object(object_id):
    data = {
        "name": "Apple MacBook Air M3",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "Apple M3",
            "Hard disk size": "1 TB"
        }
    }
    response = send_request("PUT", f"{url}/{object_id}", data)
    response_data = response.json()
    assert response_data.get("name") == data["name"]
    assert response_data.get("data") == data["data"]


def partially_update_object(object_id):
    data = {
        "name": "Apple MacBook PRO MAX M3"
    }
    response = send_request("PATCH", f"{url}/{object_id}", data)
    response_data = response.json()
    assert response_data.get("name") == data["name"]


def delete_object(object_id):
    response = send_request("DELETE", f"{url}/{object_id}")
    response_data = response.json()
    assert response_data == {"message": f"Object with id = {object_id} has been deleted."}


object_id = create_object()
print(f"Создан объект с ID: {object_id}")
update_object(object_id)
print("Успешно обновлен с помощью метода PUT")
partially_update_object(object_id)
print("Успешно обновлен с помощью метода PATCH")
delete_object(object_id)
print("Объект удален")
