"""
Módulo de construcción de prompts para consultas legales laborales chilenas.
"""

def prompt_laboral_chile(context: str, pregunta: str) -> str:
    """
    Construye un prompt especializado para consultas de derecho laboral chileno.

    Este prompt será utilizado por un modelo de lenguaje (ej. GPT) y está diseñado
    para simular la respuesta de un abogado laboral chileno, integrando el contexto
    legal recuperado y la pregunta del usuario.

    Parameters
    ----------
    context : str
        Fragmento de texto legal relevante recuperado previamente
        (ej. artículo del Código del Trabajo).

    pregunta : str
        Consulta legal específica formulada por el usuario.

    Returns
    -------
    str
        Prompt formateado listo para enviar al modelo de lenguaje.
    """
    return (
        "Actúa como un abogado laboral chileno experto en el Código del Trabajo. "
        "Basado en la siguiente documentación extraída, responde la consulta con "
        "precisión y claridad legal:\n\n"
        f"Documentación relevante:\n{context}\n\n"
        f"Pregunta legal del usuario:\n{pregunta}\n\n"
        "Respuesta profesional:"
    )
