terraform {
  backend "local" {
    bucket  = "terraform-state-legal-chatbot"
    prefix  = "env/prod"
  }
}
