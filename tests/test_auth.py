"""
[✓] Tests para la función de autorización con JWT en el chatbot legal.
"""

# pylint: disable=import-error

from datetime import timedelta

import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from app.auth import authorize
from app.token_utils import create_access_token


def test_invalid_token():
    """
    [
        ✓ Verifica que un token inválido dispare una excepción HTTP 401.
        ✓ Mensaje esperado en detail.
    ]
    """
    invalid_credentials = HTTPAuthorizationCredentials(
        scheme="Bearer", credentials="wrong-token"
    )

    with pytest.raises(HTTPException) as exc_info:
        authorize(invalid_credentials)

    assert exc_info.value.status_code == 401
    assert "Token inválido" in str(exc_info.value.detail)


def test_valid_token():
    """
    [
        ✓ Verifica que un token JWT válido no dispare excepción.
        ✓ Token con expiración en 5 minutos.
    ]
    """
    token = create_access_token(
        data={"sub": "test-user"}, expires_delta=timedelta(minutes=5)
    )
    valid_credentials = HTTPAuthorizationCredentials(scheme="Bearer", credentials=token)

    # No debería lanzar excepción
    assert authorize(valid_credentials) is None
