output "cloud_run_url" {
  description = "URL pública del chatbot"
  value       = google_cloud_run_service.chatbot_service.status[0].url
}
