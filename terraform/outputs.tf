output "instance_ip" {
  description = "IP pública de la instancia donde corre el chatbot"
  value       = google_compute_instance.chatbot_instance.network_interface[0].access_config[0].nat_ip
}
