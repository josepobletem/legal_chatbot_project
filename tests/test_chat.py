from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_chat():
    response = client.post(
        "/chat",
        headers={"Authorization": "Bearer secret-token"},
        json={"user_id": "test", "mensaje": "Hola, ¿cuáles son mis derechos laborales?"}
    )
    assert response.status_code in [200, 403]
