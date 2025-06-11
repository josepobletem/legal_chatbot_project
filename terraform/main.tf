provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_compute_instance" "chatbot_instance" {
  name         = "chatbot-instance"
  machine_type = "e2-medium"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {}  # Asigna IP pública automáticamente
  }

  metadata_startup_script = file("startup.sh")
}
