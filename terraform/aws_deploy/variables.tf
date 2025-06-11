variable "region" {
  default = "us-east-1"
}

variable "ami_id" {
  description = "Amazon Linux 2 AMI ID (Ubuntu también válido)"
  type        = string
}

variable "key_pair_name" {
  description = "Nombre del key pair para acceso SSH"
  type        = string
}

variable "db_username" {
  default = "user"
}

variable "db_password" {
  default = "pass1234"
}
