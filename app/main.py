"""
main.py

Módulo principal que define el servidor FastAPI del chatbot legal.
"""

# pylint: disable=import-error

from fastapi import Depends, FastAPI, Request, Response
from loguru import logger
from prometheus_client import generate_latest

from app.auth import authorize
from app.db import init_db, save_interaction
from app.monitor import setup_monitoring
from app.openai_client import generate_response
from app.routes import auth_routes, vertex_ai_router

app = FastAPI(
    title="Legal Chatbot API",
    description="API para consultas legales usando Vertex AI + JWT Auth",
    version="1.0.0",
)


@app.on_event("startup")
async def startup():
    """
    Inicializa base de datos y Prometheus al arrancar la app.
    """
    init_db()
    setup_monitoring(app)
    logger.info("App iniciada correctamente.")


@app.post("/chat")
async def chat(req: Request, _: str = Depends(authorize)):
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
    Endpoint que expone métricas Prometheus.

    Returns:
        Response: Métricas en texto plano.
    """
    return Response(generate_latest(), media_type="text/plain")


# Montar routers externos
app.include_router(auth_routes.router)
app.include_router(vertex_ai_router.router)
