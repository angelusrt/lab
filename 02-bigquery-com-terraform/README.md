# BigQuery Com Terraform 

Esse projetinho contém meu estudo de Terraform.

## Build

É necessário que você instale:

- GCP CLI
- Terraform

[Para instalar o GCP CLI, siga esse link](https://docs.cloud.google.com/sdk/docs/install-sdk?hl=pt-br)

[Para instalar o Terraform, siga esse link](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli)

Conecte com a sua conta GCP:

```{bash}
gcloud auth application-default login
```

É necessário que você defina algumas variáveis em um arquivo '.tfvars':

- project_id
- region_name
- zone_name
- billing_account_id
- notification_email
- bigquery_dataset_name
- bigquery_location
- bigquery_admin_account_name
- bigquery_reader_account_name
- bigquery_airflow_account_name

Para rodar:

```{bash}
terraform init
terraform plan
terraform apply

# Depois
terraform destroy
```
