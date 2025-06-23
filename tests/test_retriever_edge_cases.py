"""
[✓] Tests de edge-case para la función retrieve_context en retriever.py.
"""

from app.retriever import retrieve_context


def test_retrieve_context_empty_query():
    """
    [
        ✓ Verifica que una query vacía retorna lista vacía.
    ]
    """
    query = ""
    context = retrieve_context(query)
    assert not context


def test_retrieve_context_spaces_only():
    """
    [
        ✓ Verifica que una query con solo espacios retorna lista vacía.
    ]
    """
    query = "   "
    context = retrieve_context(query)
    assert not context


def test_retrieve_context_uppercase():
    """
    [
        ✓ Verifica que una query en mayúsculas igual matchea.
    ]
    """
    query = "¿QUÉ DICE EL CÓDIGO SOBRE VACACIONES?"
    context = retrieve_context(query)
    assert any(
        "vacacion" in frag.lower() or "artículo" in frag.lower() for frag in context
    )


def test_retrieve_context_special_characters():
    """
    [
        ✓ Verifica que una query con caracteres especiales no rompe.
    ]
    """
    query = "###$$$ vacaciones @@@!!!"
    context = retrieve_context(query)
    assert isinstance(context, list)


def test_retrieve_context_partial_word():
    """
    [
        ✓ Verifica que "vacacion" (sin tilde ni plural) sí matchea con vacaciones.
    ]
    """
    query = "Quiero saber sobre vacacion"
    context = retrieve_context(query)
    assert any(
        "vacacion" in frag.lower() or "artículo" in frag.lower() for frag in context
    )
