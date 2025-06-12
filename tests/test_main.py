"""
Tests para verificar el acceso al endpoint de documentación interactiva (/docs).
"""

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_docs_accessible():
    """
    Verifica que el endpoint /docs esté accesible y funcionando correctamente.

    Este test comprueba que la documentación automática de FastAPI
    (basada en Swagger UI) responde con un código HTTP 200.

    Returns
    -------
    None
    """
    response = client.get("/docs")
    assert response.status_code == 200
