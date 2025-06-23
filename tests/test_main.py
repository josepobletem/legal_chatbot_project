"""
[✓] Tests de integración para los endpoints principales del chatbot legal.
"""

# pylint: disable=redefined-outer-name
# pylint: disable=import-error
# pylint: disable=unused-import

import pytest

from app.token_utils import create_access_token
from tests.utils.assertions import assert_chat_respuesta_simulada
from tests.utils.common_fixtures import client


@pytest.fixture
def valid_token():
    """
    [
        ✓ Genera un token JWT válido para pruebas.
    ]
    """
    return create_access_token(data={"sub": "test-user"})


def test_chat_token_valido(client, valid_token):
    """
    [
        ✓ POST /chat con token válido.
        ✓ Verifica status 200 y respuesta simulada.
    ]
    """
    assert_chat_respuesta_simulada(client, valid_token)


def test_chat_token_invalido(client):
    """
    [
        ✗ POST /chat con token inválido.
        ✓ Verifica que retorne 401 Unauthorized.
    ]
    """
    response = client.post(
        "/chat",
        headers={"Authorization": "Bearer wrong-token"},
        json={"user_id": "test", "mensaje": "¿Qué es un finiquito?"},
    )
    assert response.status_code == 401
    assert "Token inválido" in response.json()["detail"]
