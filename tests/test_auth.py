"""
Tests para la función de autorización de tokens en el chatbot legal.
"""

# pylint: disable=wrong-import-position

import os
import sys

from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import authorize


def test_invalid_token():
    """
    Prueba que un token inválido arroje una excepción HTTP 403.

    Crea un objeto de credenciales con un token incorrecto
    y valida que la función `authorize` rechace la petición.
    """
    invalid = HTTPAuthorizationCredentials(scheme="Bearer", credentials="wrong")
    try:
        authorize(invalid)
    except HTTPException as e:
        assert e.status_code == 403
