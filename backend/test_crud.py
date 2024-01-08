from fastapi.testclient import TestClient
from main import app
import pytest
from models import ToDo

client = TestClient(app)


def test_get_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_todo():
    response = client.get("/todos/33")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)


def test_create_todo():
    response = client.post(
        "/todos/",
        json={
            "title": "test todo",
            "description": "test description",
            "completed": False,
        },
    )
    assert response.status_code == 201
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == "test todo"


def test_update_todo():
    response = client.put(
        "/todos/33",
        json={
            "title": "updated test todo",
            "description": "updated test description",
            "completed": True,
        },
    )
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert response.json()["title"] == "updated test todo"


def test_delete_todo():
    response = client.delete("/todos/33")
    assert response.status_code == 204
    # assert isinstance(response.json(), dict)
    # assert response.json()["message"] == "Todo deleted successfully"
