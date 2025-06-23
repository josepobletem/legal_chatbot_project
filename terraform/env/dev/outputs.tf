output "cloud_run_url" {
  description = "URL pública del chatbot legal en Cloud Run (dev)"
  value       = module.app_infra.cloud_run_url
}

output "db_instance_connection_name" {
  description = "Connection name de la instancia CloudSQL (dev)"
  value       = module.app_infra.db_instance_connection_name
}

output "project_id" {
  description = "Project ID de GCP (dev)"
  value       = var.project_id
}

output "region" {
  description = "Región de despliegue (dev)"
  value       = var.region
}
