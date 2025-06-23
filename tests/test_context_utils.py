"""
Tests para la función truncate_context en context_utils.py.
"""

from app.utils.context_utils import truncate_context


def dummy_tokenizer(text: str):
    """
    Tokenizer simulado que simplemente divide en palabras (tokens).
    """
    return text.split()


def test_truncate_context_within_limit():
    """
    Verifica que truncate_context no recorte si no se excede max_tokens.
    """
    texts = ["Uno dos tres", "Cuatro cinco", "Seis siete"]
    max_tokens = 10  # hay 7 tokens

    result = truncate_context(texts, dummy_tokenizer, max_tokens)

    assert result == texts  # nada se recorta


def test_truncate_context_exceeds_limit():
    """
    Verifica que truncate_context recorte los textos si exceden max_tokens.
    """
    texts = ["uno dos tres cuatro cinco", "seis siete ocho", "nueve diez once doce"]
    max_tokens = 8  # tokens máximos permitidos

    result = truncate_context(texts, dummy_tokenizer, max_tokens)

    # Solo deberían caber los dos primeros textos
    assert len(result) == 2
    assert "nueve" not in " ".join(result)
