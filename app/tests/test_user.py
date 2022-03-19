from typing import Dict

from fastapi import status
from fastapi.testclient import TestClient
from requests import Response


def test_signup(user: Dict[str, str]):
    assert user['email'] == 'test@iitbbs.ac.in'


def test_signup_user_with_same_email(client: TestClient, user: Dict[str, str]):
    response: Response = client.post("/api/users/signup",
                                     json={
                                         "email": user["email"],
                                         "password": "password"
                                     },
                                     headers={"Content-Type": "application/json"})

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json()["error"] == f"User with email: {user['email']} already exists"


def test_signup_user_with_invalid_password(client: TestClient, user: Dict[str, str]):
    response: Response = client.post("/api/users/signup",
                                     json={
                                         "email": "somenewuser@iitbbs.ac.in",
                                         "password": "short"
                                     },
                                     headers={"Content-Type": "application/json"})

    assert response.status_code == status.HTTP_400_BAD_REQUEST


def test_login(client: TestClient, user: Dict[str, str]):
    email: str = user["email"]
    password: str = "testpassword"
    response: Response = client.post("/api/users/login",
                                     data=f"username={email}&password={password}",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"})

    assert response.status_code == status.HTTP_200_OK
    response_body: Dict[str, str] = response.json()
    assert "access_token" in response_body
    assert response_body["token_type"] == "bearer"
    return response_body["access_token"]


def test_login_with_incorrect_password(client: TestClient, user: Dict[str, str]):
    response: Response = client.post("/api/users/login",
                                     data=f"username={user['email']}&password=password",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json()["error"] == "Invalid credentials"


def test_login_with_non_existent_user(client: TestClient):
    email: str = "someemail@iitbbs.ac.in"
    response: Response = client.post("/api/users/login",
                                     data=f"username={email}&password=password",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"})

    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json()["error"] == f"User with email: {email} does not exist"


def test_get_user(client: TestClient, user: Dict[str, str]):
    email: str = user["email"]
    password: str = "testpassword"
    response: Response = client.post("/api/users/login",
                                     data=f"username={email}&password={password}",
                                     headers={"Content-Type": "application/x-www-form-urlencoded"})

    assert response.status_code == status.HTTP_200_OK
    response_body: Dict[str, str] = response.json()
    assert "access_token" in response_body
    assert response_body["token_type"] == "bearer"

    token: str = response_body["access_token"]
    headers: Dict[str, str] = {"Authorization": f"Bearer {token}"}

    response: Response = client.get("/api/users", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["email"] == user["email"]
    assert "hashed_password" not in response.json()


def test_get_user_with_no_auth_token(client: TestClient, user: Dict[str, str]):
    response: Response = client.get("/api/users")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED