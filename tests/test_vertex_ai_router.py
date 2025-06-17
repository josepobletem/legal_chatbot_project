"""
[✓] Tests de integración con mocks para el endpoint /vertexai-legal-answer del chatbot legal.
"""

# pylint: disable=redefined-outer-name
# pylint: disable=import-error

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

import app.vertex_ai_router as vertex_module
from app.vertex_ai_router import router as vertexai_router
from tests.utils.mock_db import mock_connect_basic


@pytest.fixture
def client(monkeypatch):
    """
    [
        ✓ Crea una app FastAPI con el router de Vertex AI.
        ✓ Mockea la conexión a PostgreSQL (`psycopg2.connect`).
        ✓ Devuelve un TestClient listo para testing.
    ]
    """
    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect_basic)

    test_app = FastAPI()
    test_app.include_router(vertexai_router)

    return TestClient(test_app)


def test_vertexai_legal_answer_success(client, monkeypatch):
    """
    [
        ✓ Test de éxito: POST /vertexai-legal-answer.
        ✓ Mockea `aiplatform.Endpoint.predict()` para simular respuesta.
        ✓ Mockea `aiplatform.init` y `service_account.Credentials`.
        ✓ Verifica código 200 y contenido esperado.
    ]
    """

    class MockEndpoint:  # pylint: disable=too-few-public-methods
        """Mock para simular método predict del endpoint"""

        def predict(self, instances):  # pylint: disable=unused-argument
            """Mock de respuesta predict"""
            return ["Respuesta simulada de Vertex"]

    class MockAiplatform:  # pylint: disable=too-few-public-methods
        """Mock para la plataforma de AI"""

        @staticmethod
        def init(*args, **kwargs):  # pylint: disable=unused-argument
            """Mock sin implementación de init"""
            return None

        @staticmethod
        def Endpoint(*args, **kwargs):  # pylint: disable=invalid-name, unused-argument
            """Mock estático para Endpoint"""
            return MockEndpoint()

    class MockCredentials:  # pylint: disable=too-few-public-methods
        """Mock para las credenciales de servicio"""

        def __init__(self):
            """Constructor vacío"""
            pass  # pylint: disable=unnecessary-pass

    monkeypatch.setattr(vertex_module, "aiplatform", MockAiplatform)
    monkeypatch.setattr(
        vertex_module.service_account,
        "Credentials",
        type(
            "MockCredClass",
            (),
            {"from_service_account_file": staticmethod(lambda _: MockCredentials())},
        ),
    )

    response = client.post(
        "/vertexai-legal-answer",
        json={"question": "¿Cuál es el sueldo mínimo?"},
    )

    assert response.status_code == 200
    assert response.json()["answer"] == "Respuesta simulada de Vertex"


def test_vertexai_legal_answer_error(client, monkeypatch):
    """
    [
        × Test de error: POST /vertexai-legal-answer.
        × Simula un fallo durante la predicción del modelo.
        × Mockea `aiplatform.Endpoint` para lanzar una excepción.
        × Verifica que el código de respuesta sea 500.
        × Verifica que el mensaje de error esté en el cuerpo.
    ]
    """

    class MockAiplatform:  # pylint: disable=too-few-public-methods
        """Mock que lanza error al instanciar Endpoint"""

        @staticmethod
        def init(*args, **kwargs):  # pylint: disable=unused-argument
            """Mock sin implementación de init"""
            return None

        class Endpoint:  # pylint: disable=too-few-public-methods
            """Mock que lanza excepción al inicializar"""

            def __init__(self, *args, **kwargs):  # pylint: disable=unused-argument
                """Constructor que lanza excepción simulada"""
                raise RuntimeError(
                    "Error simulado en Vertex AI"
                )  # pylint: disable=broad-exception-raised

    class MockCredentials:  # pylint: disable=too-few-public-methods
        """Mock para credenciales de servicio"""

        def __init__(self):
            """Constructor vacío"""
            pass  # pylint: disable=unnecessary-pass

    monkeypatch.setattr(vertex_module, "aiplatform", MockAiplatform)
    monkeypatch.setattr(
        vertex_module.service_account,
        "Credentials",
        type(
            "MockCredClass",
            (),
            {"from_service_account_file": staticmethod(lambda _: MockCredentials())},
        ),
    )

    response = client.post(
        "/vertexai-legal-answer",
        json={"question": "¿Qué es el finiquito?"},
    )

    assert response.status_code == 500
    assert "Error consultando Vertex AI" in response.json()["detail"]
