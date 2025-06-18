"""Módulo para inicializar y guardar interacciones en la base de datos PostgreSQL."""

import os

# pylint: disable=import-error
import psycopg2


def init_db():
    """
    Inicializa la base de datos creando la tabla 'historial' si no existe.

    La tabla incluye los campos: id, user_id, mensaje, respuesta y timestamp.
    La conexión se establece usando la variable de entorno DATABASE_URL.
    """
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS historial (
            id SERIAL PRIMARY KEY,
            user_id TEXT,
            mensaje TEXT,
            respuesta TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()
    cur.close()
    conn.close()


def save_interaction(user_id: str, mensaje: str, respuesta: str):
    """
    Guarda una interacción en la tabla 'historial' de la base de datos.

    Args:
        user_id (str): ID del usuario que realizó la consulta.
        mensaje (str): Pregunta realizada por el usuario.
        respuesta (str): Respuesta generada por el chatbot.
    """
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO historial (user_id, mensaje, respuesta) VALUES (%s, %s, %s)",
        (user_id, mensaje, respuesta),
    )
    conn.commit()
    cur.close()
    conn.close()
