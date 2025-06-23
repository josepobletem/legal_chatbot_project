"""
Cliente de OpenAI para generar respuestas legales usando un prompt especializado.

Este módulo recupera contexto legal, construye un prompt RAG
y consulta a OpenAI para generar respuestas precisas.
"""

import os

# pylint: disable=import-error
import openai
import tiktoken

from app.prompt_templates import prompt_laboral_chile
from app.retriever import retrieve_context
from app.utils.context_utils import truncate_context

# Tokenizer (modelo cl100k_base para GPT-3.5/4)
tokenizer = tiktoken.get_encoding("cl100k_base")


def generate_response(user_question: str) -> str:
    """
    Genera una respuesta legal usando el modelo GPT de OpenAI.

    La función realiza:
    - Recuperación de contexto legal con `retrieve_context`.
    - Truncamiento del contexto a un máximo de tokens.
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
    context_chunks = retrieve_context(user_question)

    # Manejo caso sin resultados
    if not context_chunks:
        fallback_prompt = (
            "No se ha encontrado información relevante en la base legal. "
            "La siguiente respuesta es una generalización basada en el conocimiento del modelo:\n\n"
            f"Pregunta: {user_question}"
        )
        prompt = fallback_prompt
    else:
        # Truncar contexto a máx 3000 tokens
        truncated_chunks = truncate_context(
            context_chunks, tokenizer.encode, max_tokens=3000
        )

        # Construir prompt especializado
        prompt = prompt_laboral_chile(truncated_chunks, user_question)

    # Cliente OpenAI
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
