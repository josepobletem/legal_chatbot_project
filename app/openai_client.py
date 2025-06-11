import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(mensaje: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensaje}]
    )
    return response["choices"][0]["message"]["content"]
