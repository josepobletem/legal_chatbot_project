"""
[✓] Tests de integración para el endpoint /chat del chatbot legal.
"""

# pylint: disable=redefined-outer-name
# pylint: disable=import-error
# pylint: disable=unused-import

from tests.utils.assertions import assert_chat_respuesta_simulada
from tests.utils.common_fixtures import client


def test_chat(client):
    """
    [
        ✓ POST /chat con token válido.
        ✓ Verifica status 200 y respuesta simulada.
    ]
    """
    assert_chat_respuesta_simulada(client)
