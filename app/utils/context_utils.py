"""
context_utils.py

Utilidades para truncar el contexto de entrada para modelos LLM.
"""

from typing import Callable, List


def truncate_context(
    texts: List[str], tokenizer: Callable[[str], List[int]], max_tokens: int
) -> List[str]:
    """
    Trunca el conjunto de textos para que su longitud total no supere max_tokens.

    Args:
        texts (List[str]): Lista de textos recuperados (por ejemplo desde RAG).
        tokenizer (Callable): Función que convierte texto a lista de tokens.
        max_tokens (int): Límite máximo de tokens permitidos.

    Returns:
        List[str]: Lista truncada de textos, dentro del límite de tokens.
    """
    total_tokens = 0
    result = []

    for text in texts:
        tokens = tokenizer(text)
        token_count = len(tokens)

        if total_tokens + token_count > max_tokens:
            break

        result.append(text)
        total_tokens += token_count

    return result
