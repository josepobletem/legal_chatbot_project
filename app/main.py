"""Módulo principal que define el servidor FastAPI del chatbot legal."""

import os
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from loguru import logger
from app.openai_client import generate_response
from app.db import init_db, save_interaction
from app.monitor import setup_monitoring

app = FastAPI()
security = HTTPBearer()
API_TOKEN = os.getenv("API_TOKEN", "secret-token")


@app.on_event("startup")
async def startup():
    """Inicializa la base de datos y el monitoreo al arrancar la app."""
    init_db()
    setup_monitoring(app)
    logger.info("App iniciada.")


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
    Endpoint para recibir una pregunta legal y responderla usando OpenAI.

    Args:
        req (Request): Objeto de solicitud con JSON que contiene user_id y mensaje.

    Returns:
        dict: Respuesta generada por el modelo.
    """
    data = await req.json()
    user_id = data.get("user_id")
    mensaje = data.get("mensaje")
    respuesta = generate_response(mensaje)
    save_interaction(user_id, mensaje, respuesta)
    return {"respuesta": respuesta}
