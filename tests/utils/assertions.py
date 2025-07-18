"""
Funciones de aserción reutilizables para pruebas del chatbot legal.
"""


def assert_chat_respuesta_simulada(
    client, token, mensaje="Hola, ¿cuáles son mis derechos laborales?"
):
    """
    [
        ✓ Función auxiliar para verificar el endpoint /chat.
        ✓ Envía un mensaje con token JWT válido simulando una pregunta legal.
        ✓ Utiliza el cliente de pruebas para hacer la petición HTTP.
        ✓ Valida:
            - Que la respuesta tenga código 200 (éxito).
            - Que la respuesta contenga la clave "respuesta".
        ✓ Permite cambiar el mensaje enviado para reuso en distintos tests.
    ]
    """
    response = client.post(
        "/chat",
        headers={"Authorization": f"Bearer {token}"},
        json={"user_id": "test", "mensaje": mensaje},
    )

    assert response.status_code == 200
    assert "respuesta" in response.json()
