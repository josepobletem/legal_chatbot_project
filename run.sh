#!/bin/bash

ENV=$1  # dev, int, prod

if [[ -z "$ENV" ]]; then
  echo "❌ Debes especificar el entorno: dev, int o prod"
  exit 1
fi

echo "🔁 Iniciando Legal Chatbot en entorno '$ENV'..."

COMPOSE_FILE="docker/$ENV/docker-compose.yml"
ENV_FILE="docker/$ENV/.env"

if [[ ! -f "$COMPOSE_FILE" ]]; then
  echo "❌ No se encontró el archivo $COMPOSE_FILE"
  exit 1
fi

if [[ ! -f "$ENV_FILE" ]]; then
  echo "❌ No se encontró el archivo $ENV_FILE"
  exit 1
fi

docker-compose -f "$COMPOSE_FILE" --env-file "$ENV_FILE" down
docker-compose -f "$COMPOSE_FILE" --env-file "$ENV_FILE" up --build
