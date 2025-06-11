import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.openai_client import generate_response

def test_generate_response_format(monkeypatch):
    # Simula el contenido que retornaría OpenAI
    class MockMessage:
        content = "Respuesta simulada"

    class MockChoice:
        message = MockMessage()

    class MockCompletions:
        @staticmethod
        def create(*args, **kwargs):
            return type("MockResponse", (), {"choices": [MockChoice()]})()

    class MockChat:
        completions = MockCompletions()

    class MockClient:
        chat = MockChat()

    monkeypatch.setattr("app.openai_client.openai.OpenAI", lambda api_key=None: MockClient())

    response = generate_response("¿Cuál es la ley laboral actual?")
    assert isinstance(response, str)
    assert response == "Respuesta simulada"

