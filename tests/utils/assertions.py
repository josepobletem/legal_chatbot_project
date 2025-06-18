"""
Funciones de aserción reutilizables para pruebas del chatbot legal.
"""


def assert_chat_respuesta_simulada(
    client, mensaje="Hola, ¿cuáles son mis derechos laborales?"
):
    """
    [
        ✓ Función auxiliar para verificar el endpoint /chat.
        ✓ Envía un mensaje con token válido simulando una pregunta legal.
        ✓ Utiliza el cliente de pruebas para hacer la petición HTTP.
        ✓ Valida:
            - Que la respuesta tenga código 200 (éxito).
            - Que el contenido sea {"respuesta": "Respuesta simulada"}.
        ✓ Permite cambiar el mensaje enviado para reuso en distintos tests.
    ]
    """
    response = client.post(
        "/chat",
        headers={"Authorization": "Bearer secret-token"},
        json={"user_id": "test", "mensaje": mensaje},
    )
    assert response.status_code == 200
    assert response.json() == {"respuesta": "Respuesta simulada"}
