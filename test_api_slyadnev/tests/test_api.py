import pytest

from test_api_slyadnev.endpoints.assertions import Assertion
from test_api_slyadnev.utils.test_data import CREATE_OBJECT_DATA


@pytest.mark.parametrize('data', CREATE_OBJECT_DATA)
def test_create_object(objects_api, data):
    response_data = objects_api.create_object(data)

    Assertion.equal(response_data.get("name"), data["name"], message="Name of the object is not as expected")
    Assertion.equal(response_data.get("data"), data["data"], message="Data of the object is not as expected")

    return response_data.get("id")


@pytest.mark.parametrize('data', CREATE_OBJECT_DATA)
def test_update_object(objects_api, data):
    object_id = test_create_object(objects_api, data)
    payload = {
        "name": "Apple MacBook Air M3",
        "data": {
            "year": 2024,
            "price": 2849.99,
            "CPU model": "Apple M3",
            "Hard disk size": "1 TB"
        }
    }
    response_data = objects_api.update_object(object_id, payload)

    Assertion.equal(response_data.get("name"), payload["name"],
                    message="Name of the object is not updated as expected")
    Assertion.equal(response_data.get("data"), payload["data"],
                    message="Data of the object is not updated as expected")


@pytest.mark.parametrize('data', CREATE_OBJECT_DATA)
def test_partially_update_object(objects_api, data):
    object_id = test_create_object(objects_api, data)
    payload = {"name": "Apple MacBook PRO MAX M3"}
    response_data = objects_api.partially_update_object(object_id, payload)

    Assertion.equal(response_data.get("name"), payload["name"],
                    message="Name of the object is not partially updated as expected")


@pytest.mark.parametrize('data', CREATE_OBJECT_DATA)
def test_delete_object(objects_api, data):
    object_id = test_create_object(objects_api, data)
    response_data = objects_api.delete_object(object_id)

    Assertion.equal(response_data, {"message": f"Object with id = {object_id} has been deleted."},
                    message="Object was not deleted successfully")
