import psycopg2
import os

def init_db():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS historial (
            id SERIAL PRIMARY KEY,
            user_id TEXT,
            mensaje TEXT,
            respuesta TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def save_interaction(user_id, mensaje, respuesta):
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO historial (user_id, mensaje, respuesta) VALUES (%s, %s, %s)",
        (user_id, mensaje, respuesta)
    )
    conn.commit()
    cur.close()
    conn.close()
