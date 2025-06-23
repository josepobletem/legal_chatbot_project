"""
[✓] Tests para el endpoint /auth/refresh-token del chatbot legal.
"""

# pylint: disable=redefined-outer-name
# pylint: disable=import-error

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.routes import auth_routes


@pytest.fixture
def local_auth_client():
    """
    [
        ✓ Crea una app FastAPI con el router de auth.
        ✓ Devuelve un TestClient listo para testing.
    ]
    """
    test_app = FastAPI()
    test_app.include_router(auth_routes.router)
    return TestClient(test_app)


def test_refresh_token_success(local_auth_client):
    """
    [
        ✓ Test de éxito: POST /auth/refresh-token.
        ✓ Verifica código 200.
        ✓ Verifica que el token esté presente en la respuesta.
    ]
    """
    response = local_auth_client.post("/auth/refresh-token")

    assert response.status_code == 200
    json_data = response.json()

    assert "access_token" in json_data
    assert json_data["token_type"] == "bearer"
    assert len(json_data["access_token"]) > 10
