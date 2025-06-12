import pytest
from app import db


def test_init_db(monkeypatch):
    def mock_connect(*args, **kwargs):
        class MockConn:
            def cursor(self):
                return self

            def execute(self, q):
                pass

            def commit(self):
                pass

            def close(self):
                pass

        return MockConn()

    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect)
    db.init_db()


def test_save_interaction(monkeypatch):
    def mock_connect(*args, **kwargs):
        class MockConn:
            def cursor(self):
                return self

            def execute(self, q, args):
                pass

            def commit(self):
                pass

            def close(self):
                pass

        return MockConn()

    monkeypatch.setattr("app.db.psycopg2.connect", mock_connect)
    db.save_interaction("user1", "Hola", "Hola legal")
