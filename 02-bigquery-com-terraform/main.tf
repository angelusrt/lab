terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.8.0"
    }
  }
}

variable "project_id" { type = string }
variable "region_name" { type = string }
variable "zone_name" { type = string }
variable "bigquery_dataset_name" { type = string }
variable "bigquery_location" { type = string }
variable "bigquery_account_name" { type = string }

provider "google" {
  project = var.project_id
  region = var.region_name
  zone = var.zone_name
}

resource "google_project_service" "bigquery" {
  project = var.project_id
  service = "bigquery.googleapis.com"

  disable_on_destroy = false
}

resource "google_bigquery_dataset" "main_dataset" {
  dataset_id = var.bigquery_dataset_name
  location = var.bigquery_location

  depends_on = [
    google_project_service.bigquery
  ]
}

resource "google_service_account" "bigquery_sa" {
  account_id = var.bigquery_account_name 
  display_name = "BigQuery Service Account"
}

resource "google_project_iam_member" "bigquery_user" {
  project = var.project_id
  role = "roles/bigquery.user"
  member = "serviceAccount:${google_service_account.bigquery_sa.email}"
}
