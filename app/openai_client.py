import os
import openai

def generate_response(mensaje: str) -> str:
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": mensaje}]
    )
    return response.choices[0].message.content
