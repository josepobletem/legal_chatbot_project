"""
Cliente de OpenAI para generar respuestas legales usando un prompt especializado.

Este módulo recupera contexto legal, construye un prompt RAG
y consulta a OpenAI para generar respuestas precisas.
"""

import os
import openai
from app.prompt_templates import prompt_laboral_chile
from app.retriever import retrieve_context


def generate_response(user_question: str) -> str:
    """
    Genera una respuesta legal usando el modelo GPT de OpenAI.

    La función realiza:
    - Recuperación de contexto legal con `retrieve_context`.
    - Construcción del prompt con `prompt_laboral_chile`.
    - Llamada al modelo GPT-3.5-turbo vía OpenAI API.

    Parameters
    ----------
    user_question : str
        Pregunta legal en lenguaje natural proporcionada por el usuario.

    Returns
    -------
    str
        Respuesta generada por el modelo de lenguaje.
    """
    context = retrieve_context(user_question)
    prompt = prompt_laboral_chile(context, user_question)

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
