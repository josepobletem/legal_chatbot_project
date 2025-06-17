# Usa una imagen base ligera
FROM python:3.10-slim

# Evita mensajes interactivos
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Establece el directorio de trabajo
WORKDIR /app

# Copia primero los requirements y los instala (mejora la cache)
COPY requirements.txt .

# Instala dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libpq-dev \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Copia el resto del código del proyecto
COPY . .

# Expone el puerto de la app
EXPOSE 8000

# Comando por defecto para iniciar el servidor
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
