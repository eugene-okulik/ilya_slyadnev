import pytest
from test_api_slyadnev.endpoints.request import Request
from test_api_slyadnev.endpoints.endpoints import Methods


@pytest.fixture(scope="module")
def api():
    base_url = "https://api.restful-api.dev"
    return Request(base_url)


@pytest.fixture
def objects_api(api):
    return Methods(api)
