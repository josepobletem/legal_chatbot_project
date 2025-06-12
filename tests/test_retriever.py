# tests/test_retriever.py

from app.retriever import retrieve_context


def test_retrieve_context_with_match():
    query = "¿Puedo ser despedido por necesidades de la empresa?"
    context = retrieve_context(query)
    assert "Artículo 161" in context


def test_retrieve_context_without_match():
    query = "Consulta irrelevante"
    context = retrieve_context(query)
    assert "No se encontró" in context
