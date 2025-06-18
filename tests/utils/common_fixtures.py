"""
Fixture de cliente HTTP con mocks para pruebas de integración.
"""

# pylint: disable=import-error

import pytest
from fastapi.testclient import TestClient

from app.main import app
from tests.utils.mock_db import mock_connect_basic
from tests.utils.mock_openai import MockClient


@pytest.fixture
def client(monkeypatch):
    """
    [
        ✓ Fixture reutilizable para tests de integración.
        ✓ Mockea `OpenAI` con `MockClient` para evitar llamadas reales.
        ✓ Mockea `psycopg2.connect` para evitar conexión real a PostgreSQL.
        ✓ Devuelve un `TestClient` con la app de FastAPI cargada.
    ]
    """
    monkeypatch.setattr(
        "app.openai_client.openai.OpenAI", lambda api_key=None: MockClient()
    )
    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect_basic)

    return TestClient(app)
