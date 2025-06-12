"""
Módulo de recuperación de contexto legal para el chatbot.

Simula la búsqueda de fragmentos legales relevantes a partir de una consulta del usuario.
"""

def retrieve_context(query: str) -> str:
    """
    Simula la recuperación de contexto legal relevante para la consulta del usuario.

    Esta función busca palabras clave en la consulta para retornar un fragmento legal
    representativo. En entornos de producción, este método se puede reemplazar por una
    búsqueda semántica real usando motores como FAISS, ChromaDB o PGVector.

    Parameters
    ----------
    query : str
        Pregunta en lenguaje natural formulada por el usuario.

    Returns
    -------
    str
        Fragmento de texto legal relacionado si hay coincidencia, o una respuesta genérica
        si no se encuentra contexto.
    """
    if "despido" in query.lower():
        return (
            "Artículo 161 del Código del Trabajo: Las necesidades de la empresa son causal de "
            "término de contrato..."
        )
    return "No se encontró contexto legal relevante, responde de forma general."
