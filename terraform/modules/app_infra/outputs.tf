# Outputs simulados (para que terraform plan no explote)

output "cloud_run_url" {
  value = "https://fake-url-for-${var.env}.test"
}

output "db_instance_connection_name" {
  value = "${var.project_id}:${var.region}:chatbot-db-${var.env}"
}
