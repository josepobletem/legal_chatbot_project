# Ejemplo de recurso mínimo — un output simulado
# Puedes luego poner google_cloud_run_service y google_sql_database_instance aquí

# Por ahora, para que el pipeline no falle:

resource "null_resource" "placeholder" {}

# Aquí es donde después agregarás:
# resource "google_cloud_run_service" "chatbot" { ... }
# resource "google_sql_database_instance" "chatbot_db" { ... }
