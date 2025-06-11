variable "project_id" {
  description = "ID del proyecto de GCP"
  type        = string
}

variable "region" {
  description = "Región donde se desplegarán los recursos"
  type        = string
  default     = "us-central1"
}

variable "zone" {
  description = "Zona específica para la instancia"
  type        = string
  default     = "us-central1-a"
}
