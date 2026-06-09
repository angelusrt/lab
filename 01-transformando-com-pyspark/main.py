from pyspark.sql import SparkSession
from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window

from pathlib import Path
import kagglehub
import duckdb


def get_data(spark:SparkSession):
    path = Path(kagglehub.dataset_download("olistbr/brazilian-ecommerce"))

    customers_file = path / "olist_customers_dataset.csv"
    geolocation_file = path / "olist_geolocation_dataset.csv"
    orders_file = path / "olist_orders_dataset.csv"

    orders = spark.read.csv(str(orders_file), header=True, inferSchema=True)
    customers = spark.read.csv(str(customers_file), header=True, inferSchema=True)
    geolocation = spark.read.csv(str(geolocation_file), header=True, inferSchema=True)

    return (orders, customers, geolocation)


def get_state_ranked_sells(orders:DataFrame, customers:DataFrame, geolocation:DataFrame):
    # Eliminando "duplicatas" arbitrariamente baseado no código zip
    geolocation = geolocation.dropDuplicates(["geolocation_zip_code_prefix"])

    customers_with_location = customers.join(
        geolocation, 
        on=(customers.customer_zip_code_prefix == geolocation.geolocation_zip_code_prefix)
    )

    orders_with_customers_and_location = orders.join(
        customers_with_location,
        on="customer_id"
    )

    window = (
        Window
        .partitionBy("geolocation_state")
        .orderBy(F.desc("quantidade"))
    )

    orders_with_location = orders_with_customers_and_location[
        ["geolocation_state", "geolocation_city"]
    ]

    orders_count = (
        orders_with_location
        .groupBy(["geolocation_state", "geolocation_city"])
        .count()
        .withColumnRenamed("count", "quantidade")
        .orderBy("quantidade", ascending=False)
    )

    orders_ranked = (
        orders_count
        .withColumn("rank", F.dense_rank().over(window))
        .filter("rank <= 2")
        .drop("rank")
    )

    return orders_ranked


def load_ranked_sells(filename:str):
    with duckdb.connect("database.duckdb") as conn:
        conn.execute("""
            CREATE SCHEMA IF NOT EXISTS finance
        """)

        conn.execute(f"""
            CREATE OR REPLACE TABLE finance.f_orders_ranked_by_state AS
            SELECT * FROM read_parquet('{filename}')
        """)


if __name__ == "__main__":
    spark = (
        SparkSession.builder
        .appName("learning")
        .master("local[*]")
        .getOrCreate()
    )

    orders, customers, geolocation = get_data(spark)

    ranked_sells_by_state = get_state_ranked_sells(
        orders, 
        customers, 
        geolocation
    )

    file_to_save = "data/ranked_sells_by_state.parquet"

    (
        ranked_sells_by_state
        .write
        .mode("overwrite")
        .parquet(file_to_save)
    )

    load_ranked_sells(file_to_save)

