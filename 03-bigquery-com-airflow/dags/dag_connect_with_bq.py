from pathlib import Path
import kagglehub
import pandas as pd
import os

from airflow.sdk import dag, task
from airflow.providers.google.cloud.hooks.bigquery import BigQueryHook


@dag(dag_id="flow")
def flow():
    file_output = "tmp/customers.parquet"

    @task
    def extract_customers():
        path = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))
        customers = pd.read_csv(path / "olist_customers_dataset.csv")

        customers.to_parquet(file_output)

    @task
    def load_to_bigquery(): 
        df = pd.read_parquet(file_output)

        table_name = os.getenv("AIRFLOW_BIGQUERY_TABLE")
        assert type(table_name) is str
        assert table_name != ""

        hook = BigQueryHook(gcp_conn_id="flows")
        client = hook.get_client()

        job = client.load_table_from_dataframe(df, table_name)
        job.result()

        print(f"result: {job.output_rows}")
        os.remove(file_output)

    extraction = extract_customers() 
    load = load_to_bigquery()

    extraction >> load


flow()
