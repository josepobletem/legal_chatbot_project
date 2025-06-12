def retrieve_context(query: str) -> str:
    """
    Recupera el contexto legal más relevante para una consulta dada.

    Esta versión simula una recuperación basada en coincidencias de palabras clave,
    incluyendo variaciones comunes asociadas a despidos laborales.

    Parameters
    ----------
    query : str
        La pregunta del usuario en lenguaje natural.

    Returns
    -------
    str
        Fragmento de texto legal relevante (simulado) o una respuesta genérica si no hay coincidencia.
    """
    query_lower = query.lower()

    palabras_clave = [
        "despido",
        "despedido",
        "despedir",
        "necesidades de la empresa",
        "término del contrato",
    ]

    if any(palabra in query_lower for palabra in palabras_clave):
        return (
            "Artículo 161 del Código del Trabajo: El empleador puede poner término al contrato "
            "de trabajo por necesidades de la empresa, tales como bajas en productividad, "
            "innovaciones tecnológicas o cambios en el mercado."
        )

    return "No se encontró contexto legal relevante, responde de forma general."
