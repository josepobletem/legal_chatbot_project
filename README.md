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

    Loguru configurado para logging estructurado

    Puedes extender con Prometheus/Grafana

## 🧠 Créditos

Este proyecto está desarrollado por José Poblete M. y Chatgpt 4o, para profesionales del derecho y tecnología, con foco en acceso justo a la información legal automatizada.
