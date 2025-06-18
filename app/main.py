"""Módulo principal que define el servidor FastAPI del chatbot legal."""

import os

# pylint: disable=import-error
from fastapi import Depends, FastAPI, HTTPException, Request, Response
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from loguru import logger
from prometheus_client import generate_latest

# App internals
from app.db import init_db, save_interaction
from app.monitor import setup_monitoring
from app.openai_client import generate_response
from app.vertex_ai_router import router as vertex_ai_router

# Instrumentación opcional
# from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Inicializa la aplicación FastAPI
app = FastAPI()

# FastAPIInstrumentor.instrument_app(app)  # (Descomenta si usas OpenTelemetry)

# Seguridad con token Bearer
security = HTTPBearer()
API_TOKEN = os.getenv("API_TOKEN", "secret-token")


@app.on_event("startup")
async def startup():
    """
    Inicializa base de datos y Prometheus al arrancar la app.
    """
    init_db()
    setup_monitoring(app)
    logger.info("App iniciada correctamente.")


def authorize(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Valida el token de autorización enviado por el cliente.

    Args:
        credentials (HTTPAuthorizationCredentials): Credenciales del encabezado Authorization.

    Raises:
        HTTPException: Si el token no es válido.
    """
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Token inválido")


@app.post("/chat")
async def chat(req: Request, _: HTTPAuthorizationCredentials = Depends(authorize)):
    """
    Endpoint principal del chatbot legal. Recibe una pregunta y retorna una respuesta generada.

    Args:
        req (Request): JSON con user_id y mensaje.

    Returns:
        dict: Contiene la respuesta generada por el modelo.
    """
    data = await req.json()
    user_id = data.get("user_id")
    mensaje = data.get("mensaje")

    respuesta = generate_response(mensaje)
    save_interaction(user_id, mensaje, respuesta)

    return {"respuesta": respuesta}


@app.get("/metrics")
def metrics():
    """
    Endpoint expone métricas Prometheus.

    Returns:
        Response: Métricas en texto plano.
    """
    return Response(generate_latest(), media_type="text/plain")


# Agrega el router de Vertex AI
app.include_router(vertex_ai_router)
