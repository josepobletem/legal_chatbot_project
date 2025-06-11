provider "aws" {
  region = var.region
}

# ECR Repository
resource "aws_ecr_repository" "chatbot_repo" {
  name = "chatbot-image"
}

# RDS PostgreSQL
resource "aws_db_instance" "chatbot_db" {
  allocated_storage    = 20
  engine               = "postgres"
  engine_version       = "15.2"
  instance_class       = "db.t3.micro"
  name                 = "chatbot"
  username             = var.db_username
  password             = var.db_password
  skip_final_snapshot  = true
  publicly_accessible  = true
}

# Security Group
resource "aws_security_group" "chatbot_sg" {
  name        = "chatbot_sg"
  description = "Allow HTTP and Postgres"

  ingress {
    from_port   = 8000
    to_port     = 8000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 5432
    to_port     = 5432
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# EC2 Instance
resource "aws_instance" "chatbot_ec2" {
  ami                         = var.ami_id
  instance_type               = "t3.micro"
  key_name                    = var.key_pair_name
  security_groups             = [aws_security_group.chatbot_sg.name]
  user_data                   = file("user_data.sh")
  associate_public_ip_address = true

  tags = {
    Name = "chatbot-server"
  }
}
