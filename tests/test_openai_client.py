from app.openai_client import generate_response

def test_generate_response_format(monkeypatch):
    class MockOpenAI:
        @staticmethod
        def ChatCompletion_create(*args, **kwargs):
            return {
                "choices": [{"message": {"content": "Respuesta simulada"}}]
            }

    monkeypatch.setattr("app.openai_client.openai.ChatCompletion.create", MockOpenAI.ChatCompletion_create)
    response = generate_response("¿Cuál es la ley laboral actual?")
    assert isinstance(response, str)
    assert response == "Respuesta simulada"
