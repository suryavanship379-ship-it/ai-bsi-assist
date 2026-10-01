import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/api/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"


def test_chat_bis(client):
    response = client.post(
        "/api/chat",
        json={
            "message": "What is BIS?",
            "conversationHistory": []
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert "BIS" in data["reply"]


def test_product_detection(client):
    response = client.post(
        "/api/chat",
        json={
            "message": "I want to manufacture stainless steel water bottles",
            "conversationHistory": []
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert len(data["cards"]) > 0


def test_conversation_context(client):
    response = client.post(
        "/api/chat",
        json={
            "message": "What testing do I need?",
            "conversationHistory": [
                {
                    "role": "user",
                    "content": "I want to manufacture stainless steel water bottles"
                }
            ]
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "success"
    assert len(data["cards"]) > 0


def test_empty_message(client):
    response = client.post(
        "/api/chat",
        json={
            "message": "",
            "conversationHistory": []
        }
    )

    assert response.status_code == 400

    data = response.get_json()

    assert data["status"] == "error"