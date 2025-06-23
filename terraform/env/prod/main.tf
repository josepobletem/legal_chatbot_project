module "app_infra" {
  source = "../../modules/app_infra"

  project_id    = var.project_id
  region        = var.region
  env           = var.env

  app_image     = var.app_image
  cpu           = var.cpu
  memory        = var.memory

  db_user       = var.db_user
  db_pass       = var.db_pass
  db_name       = var.db_name

  openai_token  = var.openai_token
  api_token     = var.api_token
}
