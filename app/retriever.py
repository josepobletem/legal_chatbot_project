# app/retriever.py


def retrieve_context(query: str) -> str:
    """
    Simula la recuperación de contexto legal relevante para la consulta del usuario.
    En producción, conecta con FAISS, ChromaDB o PGVector.
    """
    if "despido" in query.lower():
        return "Artículo 161 del Código del Trabajo: Las necesidades de la empresa son causal de término de contrato..."
    return "No se encontró contexto legal relevante, responde de forma general."
