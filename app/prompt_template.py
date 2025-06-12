# prompt_templates.py


def prompt_laboral_chile(context: str, pregunta: str) -> str:
    return f"""
    Actúa como un abogado laboral chileno experto en el Código del Trabajo. 
    Basado en la siguiente documentación extraída, responde la consulta con precisión y claridad legal:

    Documentación relevante:
    {context}

    Pregunta legal del usuario:
    {pregunta}

    Respuesta profesional:
    """
