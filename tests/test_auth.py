"""
Tests para la función de autorización de tokens en el chatbot legal.
"""

# pylint: disable=import-error

import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from app.main import authorize


def test_invalid_token():
    """
    [
        ✓ Verifica que un token inválido dispare una excepción HTTP 403.
    ]
    """
    invalid_credentials = HTTPAuthorizationCredentials(
        scheme="Bearer", credentials="wrong"
    )

    with pytest.raises(HTTPException) as exc_info:
        authorize(invalid_credentials)

    assert exc_info.value.status_code == 403
