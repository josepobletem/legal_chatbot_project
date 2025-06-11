output "instance_ip" {
  description = "Public IP of EC2 instance"
  value       = aws_instance.chatbot_ec2.public_ip
}

output "ecr_repo_url" {
  description = "URL del repositorio ECR"
  value       = aws_ecr_repository.chatbot_repo.repository_url
}

output "rds_endpoint" {
  description = "RDS PostgreSQL endpoint"
  value       = aws_db_instance.chatbot_db.endpoint
}
