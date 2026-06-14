# Elementary com DBT

Este projetinho tem como propósito o meu estudo da biblioteca Elementary que 
adiciona utilitários de observabilidade ao DBT.

[https://docs.elementary-data.com/data-tests/anomaly-detection-tests/volume-anomalies](Elementary Data Tests)

## Build

Para instalar e executar o dbt com elementary:

```{bash}
python3 -m venv .venv
source .venv/bin/activate

pip install dbt "dbt-duckdb==1.9.1" duckdb elementary-data

dbt deps
dbt run --select elementary

dbt run && dbt test
```

Para visualizar reporte no browser:

```{bash}
edr report
```
