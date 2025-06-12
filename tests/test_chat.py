import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_chat(monkeypatch):
    # 🧠 Mock cliente OpenAI
    class MockMessage:
        content = "Respuesta simulada desde test_chat"

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

    monkeypatch.setattr(
        "app.openai_client.openai.OpenAI", lambda api_key=None: MockClient()
    )

    # 🧱 Mock psycopg2.connect para evitar conexión real
    class MockConnection:
        def cursor(self):
            return self

        def execute(self, *args, **kwargs):
            pass

        def commit(self):
            pass

        def close(self):
            pass

    monkeypatch.setattr(
        "app.db.psycopg2.connect", lambda *args, **kwargs: MockConnection()
    )

    response = client.post(
        "/chat",
        headers={"Authorization": "Bearer secret-token"},
        json={
            "user_id": "test",
            "mensaje": "Hola, ¿cuáles son mis derechos laborales?",
        },
    )

    assert response.status_code == 200
    assert response.json()["respuesta"] == "Respuesta simulada desde test_chat"
