variable "prefix" {
  default = "hvwd"
}

variable "project" {
  default = "hawkvisum_website_dockerised"
}

variable "contact" {
  default = "rachamallavarun1995@gmail.com"
}

variable "db_username" {
  description = "Username for the RDS Postgres database"
}

variable "db_password" {
  description = "Password for the RDS Postgres database"
}

variable "bastion_key_name" {
  default = "hawkvisum-website-devops-bastion"
}

variable "ecr_image_api" {
  description = "ECR image for API"
  default     = "586393922090.dkr.ecr.us-east-1.amazonaws.com/hawkvisum_website_dockerised:latest"
}

variable "ecr_image_proxy" {
  description = "ECR image for proxy"
  default     = "586393922090.dkr.ecr.us-east-1.amazonaws.com/hawkvisum_website_dockerised_proxy:latest"
}

variable "django_secret_key" {
  description = "Secret key for Django app"
}