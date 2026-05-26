from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_register_user():

    response = client.post(
        "/auth/register",
        json={
            "email": "test@example.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "User created successfully"


def test_register_duplicate_email():

    client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "12345678"
        }
    )

    response = client.post(
        "/auth/register",
        json={
            "email": "duplicate@example.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 400


def test_login_user():

    client.post(
        "/auth/register",
        json={
            "email": "login@example.com",
            "password": "12345678"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "login@example.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "access_token" in data


def test_login_wrong_password():

    client.post(
        "/auth/register",
        json={
            "email": "wrongpass@example.com",
            "password": "12345678"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "wrongpass@example.com",
            "password": "wrongpassword"
        }
    )

    assert response.status_code == 401