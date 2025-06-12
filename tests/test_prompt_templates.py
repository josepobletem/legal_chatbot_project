# tests/test_prompt_templates.py

from app.prompt_templates import prompt_laboral_chile


def test_prompt_laboral_chile():
    context = "Artículo 161: Despido por necesidades de la empresa."
    question = "¿Qué significa esto legalmente?"

    prompt = prompt_laboral_chile(context, question)

    assert "Artículo 161" in prompt
    assert "¿Qué significa esto legalmente?" in prompt
    assert "derecho laboral chileno" in prompt
