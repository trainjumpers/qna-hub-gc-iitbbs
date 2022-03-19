import pytest
from fastapi import status
from requests import Response
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def client() -> TestClient:
    with TestClient(app=app) as test_client:  # using context manager as we want the startup and shutdown events to run
        yield test_client  # testing happens here


@pytest.fixture(scope="session")
def user(client: TestClient) -> dict:
    response: Response = client.post("/api/users/signup",
                                     json={
                                         "email": "test@iitbbs.ac.in",
                                         "password": "testpassword"
                                     },
                                     headers={"Content-Type": "application/json"})
    assert response.status_code == status.HTTP_201_CREATED
    return response.json()
