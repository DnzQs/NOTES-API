from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def create_test_user():

    client.post(
        "/auth/register",
        json={
            "email": "notes@example.com",
            "password": "12345678"
        }
    )

    response = client.post(
        "/auth/login",
        data={
            "username": "notes@example.com",
            "password": "12345678"
        }
    )

    token = response.json()["access_token"]

    return token


def test_create_note():

    token = create_test_user()

    response = client.post(
        "/notes/",
        json={
            "title": "Test note",
            "content": "Test content"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "Test note"


def test_get_notes():

    token = create_test_user()

    client.post(
        "/notes/",
        json={
            "title": "My note",
            "content": "Some content"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    response = client.get(
        "/notes/",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)


def test_create_note_unauthorized():

    response = client.post(
        "/notes/",
        json={
            "title": "Hack",
            "content": "Hack content"
        }
    )

    assert response.status_code == 401


def test_delete_note():

    token = create_test_user()

    create_response = client.post(
        "/notes/",
        json={
            "title": "Delete me",
            "content": "Delete content"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    note_id = create_response.json()["id"]

    response = client.delete(
        f"/notes/{note_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200