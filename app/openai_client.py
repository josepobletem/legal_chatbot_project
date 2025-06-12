# app/openai_client.py

import os
import openai
from app.prompt_templates import prompt_laboral_chile
from app.retriever import retrieve_context


def generate_response(user_question: str) -> str:
    # Recuperar contexto legal relevante
    context = retrieve_context(user_question)

    # Generar prompt especializado
    prompt = prompt_laboral_chile(context, user_question)

    # Inicializar cliente OpenAI
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Solicitar respuesta al modelo
    response = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content
