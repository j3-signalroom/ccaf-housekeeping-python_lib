variable "aws_region" {
    description = "The AWS Region."
    type        = string
}

variable "aws_account_id" {
    description = "The AWS Account ID."
    type        = string
}

variable "aws_access_key_id" {
    description = "The AWS Access Key ID."
    type        = string
    default     = ""
}

variable "aws_secret_access_key" {
    description = "The AWS Secret Access Key."
    type        = string
    default     = ""
}

variable "aws_session_token" {
    description = "The AWS Session Token."
    type        = string
    default     = ""
}

variable "catalog_name" {
    description = "The CCAF Catalog Name."
    type        = string
    default     = ""
}

variable "database_name" {
    description = "The CCAF Database Name."
    type        = string
    default     = ""
}

variable "ccaf_secrets_path" {
    description = "The CCAF AWS Secrets Manager secrets path."
    type        = string
}
