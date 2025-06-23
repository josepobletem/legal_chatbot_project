project_id  = "tu-proyecto-gcp"
region      = "us-central1"
env         = "prod"

app_image   = "gcr.io/tu-proyecto-gcp/legal-chatbot:prod"  # imagen específica para prod
cpu         = "1"
memory      = "1024Mi"

db_user     = "chatbot_prod_user"
db_pass     = "super_secret_prod_pass"
db_name     = "chatbot_prod_db"

openai_token = "sk-prod-xxxxx"
api_token    = "prod-secret-token"
