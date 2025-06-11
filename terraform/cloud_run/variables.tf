variable "project_id" {
  description = "ID del proyecto de GCP"
  type        = string
}

variable "region" {
  description = "Región donde se desplegará Cloud Run"
  type        = string
  default     = "us-central1"
}

variable "openai_api_key" {
  description = "Clave de OpenAI"
  type        = string
}

variable "api_token" {
  description = "Token para proteger el endpoint"
  type        = string
}
