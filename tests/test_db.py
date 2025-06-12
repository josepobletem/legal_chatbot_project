"""
Tests para las funciones de base de datos en el módulo db.
"""

from app import db
from tests.utils.mock_db import mock_connect_basic


def test_init_db(monkeypatch):
    """
    Prueba la función init_db con una conexión simulada.
    """
    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect_basic)
    db.init_db()


def test_save_interaction(monkeypatch):
    """
    Prueba la función save_interaction con una conexión simulada.
    """
    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect_basic)
    db.save_interaction("user1", "Hola", "Hola legal")
