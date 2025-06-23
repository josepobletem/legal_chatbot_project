terraform {
  backend "gcs" {
    bucket  = "terraform-state-legal-chatbot"
    prefix  = "env/prod"
  }
}
