"""
token_utils.py

Módulo utilitario para la creación y validación de tokens JWT.
"""

# pylint: disable=import-error

from datetime import datetime, timedelta
from typing import Optional

import jwt
from fastapi import HTTPException, status

# En producción, obtener desde variable de entorno
SECRET_KEY = "TU_SECRET_KEY_AQUI"
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Genera un token JWT con expiración.

    Args:
        data (dict): Datos a incluir en el token.
        expires_delta (Optional[timedelta]): Tiempo hasta la expiración.

    Returns:
        str: Token JWT generado.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(hours=1))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_access_token(token: str) -> dict:
    """
    Verifica un token JWT.

    Args:
        token (str): Token JWT a verificar.

    Returns:
        dict: Payload decodificado si el token es válido.

    Raises:
        HTTPException: Si el token ha expirado o es inválido.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
