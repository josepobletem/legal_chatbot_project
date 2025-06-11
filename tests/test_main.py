from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_docs_accessible():
    response = client.get("/docs")
    assert response.status_code == 200
