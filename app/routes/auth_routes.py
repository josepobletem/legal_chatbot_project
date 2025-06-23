"""
auth_routes.py

Router de autenticación para generación de nuevos tokens JWT.
"""

from datetime import timedelta

from fastapi import APIRouter

from app.token_utils import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/refresh-token")
def refresh_token() -> dict:
    """
    Endpoint para obtener un nuevo token JWT con expiración.

    Returns:
        dict: Contiene el access_token y el tipo 'bearer'.
    """
    new_token = create_access_token(
        data={"sub": "user_id"}, expires_delta=timedelta(hours=1)
    )
    return {"access_token": new_token, "token_type": "bearer"}
