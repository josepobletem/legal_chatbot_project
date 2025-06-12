"""
Tests de integración para el endpoint /chat del chatbot legal.
"""

from fastapi.testclient import TestClient

from app.main import app
from tests.utils.mock_db import mock_connect_basic
from tests.utils.mock_openai import MockClient

client = TestClient(app)


def test_chat(monkeypatch):
    """
    Prueba el endpoint /chat utilizando mocks para OpenAI y PostgreSQL.
    """
    monkeypatch.setattr("app.openai_client.openai.OpenAI", lambda api_key=None: MockClient())
    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect_basic)

    response = client.post(
        "/chat",
        headers={"Authorization": "Bearer secret-token"},
        json={
            "user_id": "test",
            "mensaje": "Hola, ¿cuáles son mis derechos laborales?",
        },
    )

    assert response.status_code == 200
    assert response.json()["respuesta"] == "Respuesta simulada"
