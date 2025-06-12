"""
Tests para verificar la recuperación de contexto legal simulado en retriever.py.
"""

from app.retriever import retrieve_context


def test_retrieve_context_with_match():
    """
    Valida que se recupere contexto legal adecuado cuando se detecta una palabra clave relacionada.

    Returns
    -------
    None
    """
    query = "¿Qué dice el Código del Trabajo sobre el despido?"
    context = retrieve_context(query)
    assert "Artículo 161" in context


def test_retrieve_context_no_match():
    """
    Verifica que se devuelva una respuesta genérica cuando no hay coincidencia con palabras clave.

    Returns
    -------
    None
    """
    query = "¿Qué pasa si llego tarde al trabajo?"
    context = retrieve_context(query)
    assert (
        context == "No se encontró contexto legal relevante, responde de forma general."
    )
