"""
[✓] Tests de integración para el endpoint /chat del chatbot legal.
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


def test_chat(client, valid_token):
    """
    [
        ✓ POST /chat con token válido.
        ✓ Verifica status 200 y respuesta simulada.
    ]
    """
    assert_chat_respuesta_simulada(client, valid_token)
