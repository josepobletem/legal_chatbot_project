"""
auth.py

Módulo para autorización de endpoints mediante dependencia HTTP Bearer + JWT.
"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.token_utils import verify_access_token

bearer_scheme = HTTPBearer()


def authorize(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    """
    Verifica autorización de un endpoint usando JWT en el header Authorization.

    Args:
        credentials (HTTPAuthorizationCredentials): Token extraído del header.

    Raises:
        HTTPException: Si el token es inválido o ha expirado.
    """
    token = credentials.credentials
    try:
        verify_access_token(token)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Token inválido: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        ) from e
