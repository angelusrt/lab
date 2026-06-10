# BigQuery com Airflow

Neste projetinho, eu uso uma camada leve do Airflow 
para fazer conexão (e etl) com o BigQuery.

## Build

Para iniciar o projeto:

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install apache-airflow apache-airflow-providers-google kagglehub pandas
airflow db migrate

export AIRFLOW_HOME=$PWD 

mkdir tmp
```

Depois, conecte-se ao BigQuery:

```{bash}
airflow connections add [nome] \
  --conn-type google_cloud_platform \
  --conn-extra '{
    "extra__google_cloud_platform__key_path": [service_account.json],
    "extra__google_cloud_platform__project": [nome do projeto],
    "extra__google_cloud_platform__scope": "https://www.googleapis.com/auth/bigquery"
  }'
```

Recomendo, depois, ir no aquivo criado pelo Airflow 'airflow.cfg' e alterar: 

```{toml}
load_examples = False
```

E, para executar:

```{bash}
export AIRFLOW_BIGQUERY_TABLE = [nome da tabela no formato 'projeto.dataset.tabela'] 

airflow scheduler
airflow api-server

airflow dags reserialize
airflow dags trigger flow
```
