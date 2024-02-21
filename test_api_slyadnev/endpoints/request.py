import requests
import allure


class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    @allure.step("Отправка запроса")
    def send_request(self, method, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        with allure.step(f"Sending {method} request to {url}"):
            response = requests.request(method, url, json=data)
            response.raise_for_status()
            return response.json()