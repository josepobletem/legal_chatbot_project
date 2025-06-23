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

    assert isinstance(context, list)
    assert len(context) > 0
    assert any("Artículo 161" in fragment for fragment in context)


def test_retrieve_context_no_match():
    """
    Verifica que se devuelva una lista vacía cuando no hay coincidencia con palabras clave.

    Returns
    -------
    None
    """
    query = "¿Qué pasa si llego tarde al trabajo?"
    context = retrieve_context(query)

    assert isinstance(context, list)
    assert not context
