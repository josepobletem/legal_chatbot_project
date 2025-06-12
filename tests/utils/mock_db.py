"""
Mocks reutilizables para pruebas de base de datos PostgreSQL.
"""

def mock_connect_basic(*_args, **_kwargs):
    """
    Función mock que simula una conexión a una base de datos PostgreSQL.

    Returns
    -------
    MockConn : objeto con métodos básicos: cursor, execute, commit, close.
    """
    class MockConn:
        """Simula una conexión básica a la base de datos."""

        def cursor(self):
            """Devuelve el cursor simulado."""
            return self

        def execute(self, *_args, **_kwargs):
            """Simula la ejecución de una consulta SQL."""
            pass # pylint: disable=unnecessary-pass

        def commit(self):
            """Simula el commit de la transacción."""
            pass # pylint: disable=unnecessary-pass

        def close(self):
            """Simula el cierre de la conexión."""
            pass # pylint: disable=unnecessary-pass

    return MockConn()
