import pytest
from clients.api_client import APIClient


@pytest.fixture
def api():
    client = APIClient()
    yield client
    client.close()
