"""
Router para consultas legales usando Vertex AI.
"""

import os

# pylint: disable=import-error
from fastapi import APIRouter, HTTPException
from google.cloud import aiplatform
from google.oauth2 import service_account
from pydantic import BaseModel

router = APIRouter()

# Configuración de entorno
PROJECT_ID = os.getenv("VERTEX_PROJECT_ID", "tu-proyecto")
LOCATION = os.getenv("VERTEX_LOCATION", "us-central1")
ENDPOINT_ID = os.getenv("VERTEX_ENDPOINT_ID", "tu-endpoint-id")
CREDENTIALS_PATH = os.getenv("VERTEX_CREDENTIALS_PATH", "ruta/a/credenciales.json")


class QuestionRequest(BaseModel):
    """
    Modelo de entrada para el endpoint /vertexai-legal-answer.

    Attributes:
        question (str): Pregunta legal enviada por el usuario.
    """

    question: str


@router.post("/vertexai-legal-answer")
def vertexai_legal_answer(req: QuestionRequest):
    """
    Consulta un modelo de Vertex AI para responder preguntas legales.

    Args:
        req (QuestionRequest): Objeto con la pregunta legal.

    Returns:
        dict: Contiene la respuesta generada por el modelo de Vertex AI.

    Raises:
        HTTPException: Error 500 si falla la llamada al modelo.
    """
    try:
        credentials = service_account.Credentials.from_service_account_file(
            CREDENTIALS_PATH
        )
        aiplatform.init(
            project=PROJECT_ID,
            location=LOCATION,
            credentials=credentials,
        )
        endpoint = aiplatform.Endpoint(ENDPOINT_ID)
        response = endpoint.predict(instances=[{"content": req.question}])
        return {"answer": response[0] if response else "Sin respuesta"}
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error consultando Vertex AI: {e}",
        ) from e
