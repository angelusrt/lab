# BigQuery Com DBT

Projetinho para aprender a conectar o DBT com o BigQuery.

## Setup

Para iniciar, você precisará de ter o arquivo "service_account_key.json" do GCP:

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install dbt dbt-bigquery
dbt init project
```

