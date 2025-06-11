from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.openai_client import generate_response
from app.db import init_db, save_interaction
from app.monitor import setup_monitoring
from loguru import logger
import os

app = FastAPI()
security = HTTPBearer()

API_TOKEN = os.getenv("API_TOKEN", "secret-token")

@app.on_event("startup")
async def startup():
    init_db()
    setup_monitoring(app)
    logger.info("App iniciada.")

def authorize(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != API_TOKEN:
        raise HTTPException(status_code=403, detail="Token inválido")

@app.post("/chat")
async def chat(req: Request, credentials: HTTPAuthorizationCredentials = Depends(authorize)):
    data = await req.json()
    user_id = data.get("user_id")
    mensaje = data.get("mensaje")
    respuesta = generate_response(mensaje)
    save_interaction(user_id, mensaje, respuesta)
    return {"respuesta": respuesta}
