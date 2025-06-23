"""
Test de flujo: retrieve_context → truncate_context → generación de prompt.
"""

from app.retriever import retrieve_context
from app.utils.context_utils import truncate_context


def dummy_tokenizer(text: str):
    """
    [
        ✓ Tokenizer simulado.
        ✓ Divide el texto en "tokens" por palabras.
    ]
    """
    return text.split()


def test_rag_flow_with_match():
    """
    [
        ✓ Verifica flujo completo cuando hay contexto relevante.
        ✓ Recupera fragmentos.
        ✓ Trunca correctamente.
        ✓ Genera chunks válidos.
    ]
    """
    query = "¿Qué dice el Código del Trabajo sobre vacaciones?"
    context_chunks = retrieve_context(query)

    print("context_chunks:", context_chunks)

    assert isinstance(context_chunks, list)
    assert len(context_chunks) > 0

    truncated_chunks = truncate_context(context_chunks, dummy_tokenizer, max_tokens=50)

    print("truncated_chunks:", truncated_chunks)

    assert len(truncated_chunks) > 0
    assert any(
        "vacaciones" in frag.lower() or "artículo" in frag.lower()
        for frag in truncated_chunks
    )


def test_rag_flow_no_match():
    """
    [
        ✓ Verifica flujo completo cuando no hay contexto relevante.
        ✓ Contexto vacío.
        ✓ Truncamiento seguro en caso vacío.
    ]
    """
    query = "¿Qué pasa si llego tarde al trabajo?"
    context_chunks = retrieve_context(query)

    # No debería haber contexto
    assert not context_chunks

    truncated_chunks = truncate_context(context_chunks, dummy_tokenizer, max_tokens=10)

    # Truncamiento de lista vacía debería devolver lista vacía
    assert not truncated_chunks
