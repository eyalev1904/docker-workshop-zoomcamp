variable "aws_region" {
  description = "AWS region to deploy resources in"
  type = string
  default = "eu-north-1"

}

variable "bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "data-engineering-zoomcamp-1568692036"
}


variable "dataset_name" {
  description = "Glue Catalog database name (logical dataset for Athena/Glue)"
  type        = string
  default = "ny_taxi_database"
}

variable "gcp_project_id" {
  description = "GCP project id"
  type        = string
  default     = "dtc-de-course-485613"
}

variable "gcp_project_name" {
  description = "GCP project display name"
  type        = string
  default     = "DTC DE Course"
}

variable "gcp_bq_dataset" {
  description = "BigQuery dataset name"
  type        = string
  default     = "dtc-de-course-485613"
}

variable "gcp_bq_location" {
  description = "BigQuery dataset location"
  type        = string
  default     = "us-central1"
}

variable "gcp_bucket_name" {
  description = "GCS bucket name"
  type        = string
  default     = "de-zoomcamp"
}

variable "gcp_bucket_location" {
  description = "GCS bucket location/region"
  type        = string
  default     = "eu"
}