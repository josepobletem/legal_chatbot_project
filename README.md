# 🧠 Legal Chatbot con FastAPI, GPT y PostgreSQL

📄 Descripción del Proyecto

Legal Chatbot es una solución conversacional desarrollada con el objetivo de brindar respuestas legales automatizadas, confiables y trazables, integrando capacidades de IA generativa (GPT) con una arquitectura robusta y escalable.

La plataforma permite a los usuarios interactuar mediante lenguaje natural, recibir respuestas fundamentadas y registrar cada conversación en una base de datos. Está diseñada para facilitar la integración en entornos legales, centros de ayuda, departamentos de compliance o automatización de atención al cliente.
✨ Características destacadas

    🧠 Inteligencia Artificial Legal: integración con OpenAI GPT (ChatCompletion) para generar respuestas legales.

    ⚙️ FastAPI Backend: API rápida, escalable y con documentación automática vía Swagger.

    🔐 Autenticación segura: protección de endpoints mediante token Bearer.

    🗄️ Persistencia de datos: conexión a PostgreSQL para almacenar cada interacción.

    📈 Monitoreo con Prometheus: métricas de uso y latencia listas para observabilidad avanzada.

    🐳 Contenerización: listo para desplegar con Docker y Docker Compose.

    ☁️ Infraestructura como código: Terraform disponible para GCP (Cloud Run) y AWS (EC2 + RDS + ECR).

    🚀 CI/CD moderno: integración continua con GitHub Actions y despliegue automatizado con Cloud Build.

💼 Casos de uso

    LegalTech y plataformas de consulta jurídica

    Automatización de soporte legal interno en empresas

    Departamentos de RRHH para resolución de dudas contractuales

    Agencias de cumplimiento normativo o atención ciudadana

---

## 🚀 Tecnologías

- **FastAPI**: framework principal de la API.
- **OpenAI GPT**: backend de generación de texto.
- **PostgreSQL**: persistencia del historial de conversación.
- **Docker + Docker Compose**: para orquestación local.
- **Prometheus**: para monitoreo y métricas.
- **Loguru**: para logging estructurado y alertas.
- **GitHub Actions**: CI/CD automático.
- **pytest**: testing de endpoints.
- **Terraform** (opcional): infraestructura como código.

---

## 🧩 Funcionalidades destacadas

| Módulo                   | Descripción                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `/chat` endpoint         | Recibe preguntas legales, aplica RAG y responde en lenguaje natural.        |
| `prompt_templates.py`    | Prompts legales por especialidad: laboral, tributario, civil, etc.          |
| `retriever.py`           | Recupera contexto legal relevante para cada pregunta.                       |
| `embedder.py`            | Indexa documentos legales y construye FAISS (o Chroma) para RAG.            |
| `auth.py`                | Verifica tokens en headers para proteger endpoints.                         |
| `db.py`                  | Guarda las preguntas/respuestas con timestamp.


## 🧠 Ejemplo de flujo RAG

1. El usuario envía:
   `"¿Qué derechos tengo si me despiden por necesidades de la empresa?"`

2. El sistema busca contexto legal relevante (ej: Art. 161 del Código del Trabajo).

3. Se genera un prompt como:

```text
Actúa como un abogado laboral chileno experto en el Código del Trabajo.
Usa el siguiente contexto legal para responder con precisión:

Artículo 161: Despido por necesidades de la empresa...

Pregunta:
¿Qué derechos tengo si me despiden por necesidades de la empresa?

Respuesta:
...

4. GPT responde de forma especializada y fundamentada.
```

## 📦 Instalación rápida (local)

### Requisitos

- Docker y Docker Compose
- Clave de OpenAI (`OPENAI_API_KEY`)

### Instrucciones

```bash
git clone https://github.com/tu_usuario/legal_chatbot.git
cd legal_chatbot
cp .env.example .env  # Edita con tus credenciales si lo deseas
make install
docker-compose up --build
```

Accede a la API en: [http://localhost:8000/docs](http://localhost:8000/docs)
Prometheus en: [http://localhost:9090](http://localhost:9090)

---

## 🔐 Autenticación

Para consumir el endpoint `/chat`, se requiere un token tipo Bearer:

```http
Authorization: Bearer secret-token
```

Puedes modificarlo con la variable de entorno `API_TOKEN`.

---

## 🧪 Testing

```bash
make test
```

---
## 🔧 Uso desde terminal:

```bash
bash run.sh dev
bash run.sh int
bash run.sh prod
```

## 📈 Monitoreo

El endpoint `/metrics` expone estadísticas de uso para ser scrapeadas por Prometheus.

---

## ☁️ Variables de entorno (.env ejemplo)

```env
OPENAI_API_KEY=tu-clave
DATABASE_URL=postgresql://user:pass@db:5432/chatbot
API_TOKEN=secret-token
```

---

## 📜 Licencia

MIT


## ☁️ Despliegue con Terraform en GCP

1. Completa terraform.tfvars:

```hcl
project_id = "tu-proyecto"
region     = "us-central1"
zone       = "us-central1-a"
```

2. Ejecuta

```bash
terraform init
terraform apply -var-file="terraform.tfvars"
```

Esto creará una instancia con Docker y el bot en ejecución automáticamente.


# 🧪 Instrucciones para usar

## 🌐 Cloud Run + Artifact Registry (Google Cloud)

1. Autentícate en GCP:

```bash
gcloud auth application-default login
gcloud auth configure-docker
```
2. Construye la imagen:

```bash
gcloud builds submit --tag us-central1-docker.pkg.dev/legal_chatbot_project/chatbot/chatbot-image
```

3. Crea el archivo terraform.tfvars:

```hcl
project_id     = "tu-proyecto"
region         = "us-central1"
openai_api_key = "sk-..."
api_token      = "secret-token"
```

4. Inicializa y aplica Terraform:

```bash
cd terraform/cloud_run
terraform init
terraform apply -var-file="terraform.tfvars"
```

## 🟦 EC2 + RDS + ECR (AWS completo)

### 🚀 Despliegue paso a paso

1. Autenticación

```bash
aws configure
```

2. Terraform

```bash
cd terraform/aws_deploy
terraform init
terraform apply -var 'ami_id=ami-xxxxxxxxx' -var 'key_pair_name=mi_llave'
```

3. Build y Push a ECR

```bash
# Login a ECR
aws ecr get-login-password | docker login --username AWS --password-stdin <ecr_repo_url>

# Build & push
docker build -t chatbot .
docker tag chatbot:latest <ecr_repo_url>:latest
docker push <ecr_repo_url>:latest
```

## 📈 Monitoreo y logs

# Dashboards de Grafana para Legal Chatbot Project

Este directorio contiene la configuración necesaria para que Grafana cargue automáticamente datasources y dashboards personalizados al iniciar con Docker Compose.

## Estructura

```
grafana/
└── provisioning/
    ├── datasources/
    │   └── prometheus.yaml
    └── dashboards/
        ├── dashboard.yaml
        └── mi_dashboard.json
```

- **datasources/prometheus.yaml**: Configura Prometheus como fuente de datos.
- **dashboards/dashboard.yaml**: Indica a Grafana dónde buscar dashboards.
- **dashboards/mi_dashboard.json**: Dashboard(s) exportados desde Grafana en formato JSON.

## ¿Cómo agregar un dashboard?

1. Crea o edita un dashboard en la interfaz de Grafana.
2. Exporta el dashboard como JSON.
3. Guarda el archivo exportado en `grafana/provisioning/dashboards/`.

## ¿Cómo funciona?

Al iniciar Grafana con Docker Compose, se cargarán automáticamente:
- El datasource de Prometheus.
- Todos los dashboards JSON ubicados en `grafana/provisioning/dashboards/`.

## Acceso

- Grafana estará disponible en: [http://localhost:3000](http://localhost:3000)
- Usuario/contraseña por defecto: `admin` / `admin`

## Referencias

- [Documentación oficial de provisión de Grafana](https://grafana.com/docs/grafana/latest/administration/provisioning/)


# Integración de Vertex AI en Legal Chatbot Project

Esta integración permite consultar modelos de lenguaje alojados en Vertex AI directamente desde la API del chatbot legal e incluye integración con Google Cloud Monitoring (Stackdriver) y Vertex AI para trazas, métricas y predicciones avanzadas.

## ¿Qué hace esta integración?

- Expone un endpoint `/vertexai-legal-answer` en la API.
- Permite enviar preguntas legales y obtener respuestas generadas por un modelo desplegado en Vertex AI.
- Facilita la conexión segura usando credenciales de Google Cloud.

## Archivos relevantes

- `app/vertex_ai_router.py`: Contiene el router y la lógica para consultar Vertex AI.
- `app/main.py`: Incluye el router de Vertex AI en la aplicación FastAPI.

## Configuración

1. **Credenciales de Google Cloud**
   - Descarga una cuenta de servicio con permisos de Vertex AI.
   - Guarda el archivo JSON en una ruta segura.

2. **Variables de entorno**
   Puedes definir estas variables en tu entorno o en un archivo `.env`:
   ```
   GCP_PROJECT_ID=tu-proyecto
   VERTEX_PROJECT_ID=tu-proyecto
   VERTEX_LOCATION=us-central1
   VERTEX_ENDPOINT_ID=tu-endpoint-id
   VERTEX_CREDENTIALS_PATH=/ruta/a/credenciales.json
   ```

3. **Instala dependencias**
   ```
   pip install google-cloud-aiplatform
   ```
   Si tienes problemas con las versiones de las dependencias, puedes instalar las siguientes dependencias específicas:
   ```
   pip install google-cloud-aiplatform==1.11.0 google-auth==1.24.0 google-auth-oauthlib==0.4.1 google-auth-httplib2==0.0.3 google-api-python-client==1.12.7
   ```
   ```
   pip install google-cloud-aiplatform opentelemetry-sdk opentelemetry-exporter-google-cloud opentelemetry-instrumentation-fastapi
   ```
Para evitar conflictos de versiones, instala las siguientes dependencias específicas:

```
pip install opentelemetry-sdk==0.17b0 opentelemetry-api==0.17b0 opentelemetry-exporter-google-cloud==0.17b0 opentelemetry-instrumentation-fastapi
```
## Uso

Haz una petición POST al endpoint `/vertexai-legal-answer` con el parámetro `question`:

```
POST /vertexai-legal-answer
Content-Type: application/json

{
  "question": "¿Cuál es la ley de propiedad intelectual en mi país?"
}
```

**Respuesta:**
```json
{
  "answer": "Respuesta generada por el modelo de Vertex AI."
}
```
## Notas

- Asegúrate de que tu endpoint de Vertex AI esté desplegado y accesible.
- Puedes adaptar el endpoint para recibir otros parámetros según tu modelo.
- Consulta la [documentación oficial de Vertex AI](https://cloud.google.com/vertex-ai/docs) para más detalles sobre


# Integración de Google Cloud Monitoring y Vertex AI en Legal Chatbot Project

Este proyecto ahora incluye integración con Google Cloud Monitoring (Stackdriver) y Vertex AI para trazas, métricas y predicciones avanzadas.

## Funcionalidades agregadas

1. **Google Cloud Monitoring**:
   - Exporta métricas y trazas de la aplicación a GCP Monitoring y Cloud Trace.
   - Usa OpenTelemetry para instrumentar la aplicación FastAPI.

2. **Vertex AI**:
   - Endpoint `/vertexai-legal-answer` que consulta modelos de lenguaje alojados en Vertex AI.
   - Permite enviar preguntas legales y obtener respuestas generadas por modelos personalizados.

---

## Archivos relevantes

### GCP Monitoring
- `app/gcp_monitoring.py`: Configura la exportación de métricas y trazas a GCP Monitoring.
- `main.py`: Inicializa GCP Monitoring en el evento de startup.

### Vertex AI
- `app/vertex_ai_router.py`: Contiene el router y la lógica para consultar Vertex AI.
- `main.py`: Incluye el router de Vertex AI en la aplicación FastAPI.

---
### Métricas y trazas
- Las métricas y trazas estarán disponibles en la consola de GCP:
  - **Monitoring**: [https://console.cloud.google.com/monitoring](https://console.cloud.google.com/monitoring)
  - **Trace**: [https://console.cloud.google.com/traces](https://console.cloud.google.com/traces)

## Referencias

- [Google Cloud Monitoring](https://cloud.google.com/monitoring/docs)
- [Vertex AI](https://cloud.google.com/vertex-ai/docs)
- [OpenTelemetry](https://opentelemetry.io/docs/)

## 🧠 Créditos

Este proyecto está desarrollado por José Poblete M. y Chatgpt 4o, para profesionales del derecho y tecnología, con foco en acceso justo a la información legal automatizada.
