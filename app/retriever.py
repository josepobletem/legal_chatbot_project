"""
retriever.py

Módulo de recuperación de contexto legal para el chatbot.

Simula la búsqueda de fragmentos legales relevantes a partir de una consulta del usuario.
En producción se podría usar FAISS, ChromaDB o PGVector.
"""

import re
from typing import List


def retrieve_context(query: str) -> List[str]:
    """
    Simula la recuperación de contexto legal relevante para la consulta del usuario.

    Parameters
    ----------
    query : str
        Pregunta en lenguaje natural formulada por el usuario.

    Returns
    -------
    List[str]
        Lista de fragmentos de texto legal relacionados con la consulta.
        Lista vacía si no se encuentra contexto.
    """
    fragments = []

    # Normalizamos query en lowercase
    query = query.lower()

    # Despido
    if re.search(r"\bdespido\b", query):
        fragments.append(
            "Artículo 161 del Código del Trabajo: Las necesidades de la empresa son causal de "
            "término de contrato..."
        )

    # Vacaciones (acepta "vacacion", "vacación", "vacaciones", "VACACIONES")
    if re.search(r"\bvacaci[oó]n(?:es)?\b", query):
        fragments.append(
            "Artículo 67 del Código del Trabajo: El feriado anual consiste en 15 días hábiles..."
        )

    # Licencia médica (permite con o sin tilde en medica)
    if re.search(r"\blicencia\s+m[eé]dica\b", query):
        fragments.append(
            "Artículo 202 del Código del Trabajo: Protección del empleo durante licencia médica..."
        )

    return fragments
