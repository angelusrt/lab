import utils

docs = [
    "Kafka is a distributed event streaming platform used to build real-time data pipelines.",
    "dbt (data build tool) transforms data in your warehouse using SQL and follows a layered schema pattern.",
    "Elementary is a data observability tool built on top of dbt that monitors data quality and anomalies.",
    "Airflow is a workflow orchestration tool used to schedule and monitor data pipelines.",
    "RAG stands for Retrieval-Augmented Generation. It retrieves relevant documents before generating an answer.",
]

template = """
Answer the question based only on the context below.
If the answer is not in the context, say "I don't know".\n
Context:\n{}\n
Question:\n{}
"""

if __name__ == "__main__":
    query = "What is Airflow?"

    utils.init()
    relevant_chunks = utils.retrieve(query, docs)

    print(f"Question:\n{query}\n")

    print("Retrieved chunks:\n")
    for chunk in relevant_chunks:
        print(f"  → {chunk}")

    answer = utils.answer(
        query, 
        relevant_chunks,
        lambda a, b: template.format(a, b)
    )

    print(f"Answer:\n{answer}\n")
