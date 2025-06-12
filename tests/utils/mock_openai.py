"""
Mocks reutilizables para simular respuestas del cliente OpenAI en tests.
"""

# pylint: disable=too-few-public-methods


class MockMessage:
    """Simula el contenido del mensaje devuelto por OpenAI."""

    content = "Respuesta simulada"


class MockChoice:
    """Simula una opción de respuesta dentro de 'choices'."""

    message = MockMessage()


class MockCompletions:
    """Simula la creación de una respuesta de completado."""

    @staticmethod
    def create(*_args, **_kwargs):
        """Devuelve una respuesta simulada."""
        return type("MockResponse", (), {"choices": [MockChoice()]})()


class MockChat:
    """Simula el cliente de chat."""

    completions = MockCompletions()


class MockClient:
    """Simula el cliente OpenAI."""

    chat = MockChat()
