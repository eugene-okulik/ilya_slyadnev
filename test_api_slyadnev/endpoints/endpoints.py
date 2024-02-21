import requests
import allure


class Methods:
    def __init__(self, api):
        self.api = api

    @allure.step("Создание объекта")
    def create_object(self, data):
        return self.api.send_request("POST", "objects", data)

    @allure.step("Обновление объекта")
    def update_object(self, object_id, data):
        return self.api.send_request("PUT", f"objects/{object_id}", data)

    @allure.step("Частичное обновление объекта")
    def partially_update_object(self, object_id, data):
        return self.api.send_request("PATCH", f"objects/{object_id}", data)

    @allure.step("Удаление объекта")
    def delete_object(self, object_id):
        return self.api.send_request("DELETE", f"objects/{object_id}")
