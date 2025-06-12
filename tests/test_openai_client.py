"""
Tests para la función generate_response en openai_client.py.
Simula la llamada al modelo OpenAI usando monkeypatch.
"""

from app.openai_client import generate_response
from tests.utils.mock_openai import MockClient


def test_generate_response_format(monkeypatch):
    """
    Verifica que generate_response devuelva una string esperada
    al simular la respuesta del cliente OpenAI con monkeypatch.
    """
    monkeypatch.setattr("app.openai_client.openai.OpenAI", lambda api_key=None: MockClient())

    response = generate_response("¿Cuál es la ley laboral actual?")
    assert isinstance(response, str)
    assert response == "Respuesta simulada"
