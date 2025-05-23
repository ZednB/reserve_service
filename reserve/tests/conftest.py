import pytest
from fastapi.testclient import TestClient
from reserve.main import app


@pytest.fixture
def client():
    return TestClient(app)
