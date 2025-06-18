"""
[✓] Tests de integración para los endpoints principales del chatbot legal.
"""

# pylint: disable=redefined-outer-name
# pylint: disable=import-error
# pylint: disable=unused-import


from tests.utils.assertions import assert_chat_respuesta_simulada
from tests.utils.common_fixtures import client


def test_chat_token_valido(client):
    """
    [
        ✓ POST /chat con token válido.
        ✓ Verifica status 200 y respuesta simulada.
    ]
    """
    assert_chat_respuesta_simulada(client)


def test_chat_token_invalido(client):
    """
    [
        ✗ POST /chat con token inválido.
        ✓ Verifica que retorne 403.
    ]
    """
    response = client.post(
        "/chat",
        headers={"Authorization": "Bearer wrong-token"},
        json={"user_id": "test", "mensaje": "¿Qué es un finiquito?"},
    )
    assert response.status_code == 403
