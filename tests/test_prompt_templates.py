"""
Tests para verificar la correcta generación del prompt legal en prompt_templates.py.
"""

from app.prompt_templates import prompt_laboral_chile


def test_prompt_laboral_chile():
    """
    Valida que el prompt generado contenga todos los componentes legales esperados.

    Este test asegura que el contexto y la pregunta se incorporan correctamente
    al prompt y que contiene términos claves del dominio legal chileno.

    Returns
    -------
    None
    """
    context = "Artículo 161: Despido por necesidades de la empresa."
    question = "¿Qué significa esto legalmente?"

    prompt = prompt_laboral_chile(context, question)

    assert "Artículo 161" in prompt
    assert "¿Qué significa esto legalmente?" in prompt
    assert "abogado laboral chileno" in prompt
    assert "Código del Trabajo" in prompt
