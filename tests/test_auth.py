import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from app.main import authorize


def test_invalid_token():
    invalid = HTTPAuthorizationCredentials(scheme="Bearer", credentials="wrong")
    try:
        authorize(invalid)
    except HTTPException as e:
        assert e.status_code == 403
