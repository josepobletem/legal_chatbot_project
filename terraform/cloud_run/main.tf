provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_artifact_registry_repository" "chatbot_repo" {
  location      = var.region
  repository_id = "chatbot"
  format        = "DOCKER"
}

resource "google_cloud_run_service" "chatbot_service" {
  name     = "legal-chatbot"
  location = var.region

  template {
    spec {
      containers {
        image = "${var.region}-docker.pkg.dev/${var.project_id}/chatbot/chatbot-image:latest"
        ports {
          container_port = 8000
        }
        env {
          name  = "OPENAI_API_KEY"
          value = var.openai_api_key
        }
        env {
          name  = "API_TOKEN"
          value = var.api_token
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  autogenerate_revision_name = true
}

resource "google_cloud_run_service_iam_member" "public_invoker" {
  service  = google_cloud_run_service.chatbot_service.name
  location = google_cloud_run_service.chatbot_service.location
  role     = "roles/run.invoker"
  member   = "allUsers"
}
